##### ---------------------------- Description ---------------------------- #####
# ---- All the data of a given user can be filtered and cleaned easily ----- #
# ---- We can select our own desired attributes in addition to the 4 ----- #
##### --------------------------------------------------------------------- #####

##### ---------------------------- File structure ---------------------------- #####
# project_folder
#   |
#    code_folder
#   |   |
#   |    process.py
#   |    app.py
#    data_folder
#       |
#        user_info.csv
#        P0701.zip
#        P0702.zip
##### --------------------------------------------------------------------- #####

import pandas as pd
import numpy as np
import zipfile, os, re
import pathlib
import csv


class preprocess():
    def __init__(self):
        self.project_path = pathlib.Path.cwd().parent
        self.data_list = os.listdir(os.path.join(self.project_path, 'data'))[2:-2]
        self.our_attributes = ['Gsr', 'PhysicalActivityEventEntity', 'RRInterval', 'SkinTemperature']
    
    ## ------ This function provides a list of all available users ------ ##
    def users(self):
        list_of_users_UID = []
        for user in self.data_list:
            id = re.sub(r'.zip', "", user)
            list_of_users_UID.append(id)
        return list_of_users_UID

    ## ------ This function extract the user's info from the given user_info.csv file ------ ##
    def extract_user_info(self, user_UID):
        infos = {}
        info_path = os.path.join(self.project_path, 'data', 'user_info.csv')
        with open(info_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                UID = 'P' + row[0]
                if user_UID == UID:
                    infos['Openness'] = row[1]
                    infos['Conscientiousness'] = row[2]
                    infos['Neuroticism'] = row[3]
                    infos['Extraversion'] = row[4]
                    infos['Agreeableness'] = row[5]
                    infos['Age'] = row[6]
                    infos['Gender'] = row[7]
        return infos
    
    ## ----- This function specifically preprocesses a selected users data ------ ##
    def extract_user_data(self, user_UID):
        frames = []         ## A list to append each dataframe
        attributes = []     ## A list to append the attibute the dataframes' correspond to
        user_path = os.path.join(self.project_path, 'data', user_UID + '.zip')
        
        with zipfile.ZipFile(user_path) as zip_file:
            all_data = zip_file.namelist()         ## get the filename of all the files within that users file
            all_data_attributes = [x.split("-")[0] for x in all_data]
            
            for index, attr in enumerate(all_data_attributes):
                if attr in self.our_attributes:
                    source = zip_file.open(all_data[index])
                    frames.append(pd.read_csv(source))
                    attributes.append(attr)
        return frames, attributes           ## return two list holding dataframe and the corresponding attribute from self.our_attributes
    
    
    ## ------ Find outliers from a dataframe ------ ##
    def remove_nan(self, df):
        df = df.dropna()
        return df

    
    ## ----- For a 1-D data / np-array ------ ##
    def find_anomalies_SD(self, data, std_range = 3):
        #define a list to accumlate anomalies
        anomalies = []
        
        # Set upper and lower limit to 3 * standard deviation
        data_mean, data_std = np.mean(data), np.std(data)
        anomaly_cut_off = data_std * std_range
        lower_limit, upper_limit  = data_mean - anomaly_cut_off, data_mean + anomaly_cut_off

        # Generate outliers
        for outlier in data:
            anomaly = False
            if outlier > upper_limit or outlier < lower_limit:
                anomaly = True
            anomalies.append(anomaly)
            
        anomalies_arr = np.array(anomalies)
        return anomalies_arr

    
    ## ----- For a 1-D data / np-array ------ ##
    def find_anomalies_IQ(self, data, outlier_cutoff = 1.5):
        #define a list to accumlate anomalies
        anomalies = []
        
        # calculate interquartile range
        q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
        iqr = q75 - q25
        
        # calculate the outlier cutoff
        cut_off = iqr * outlier_cutoff
        lower_limit, upper_limit = q25 - cut_off, q75 + cut_off

        # Generate outliers
        for outlier in data:
            anomaly = False
            if outlier > upper_limit or outlier < lower_limit:
                anomaly = True
            anomalies.append(anomaly)
            
        anomalies_arr = np.array(anomalies)
        return anomalies_arr

    
    ## ------ This function filters outlier data attr becomes "Resistance" for Gsr, "Interval" for RRInterval, "Temperature" for Skin Temp. and "confidence" for Physical Activ.
    def filter_outlier(self, df, data, range, SD=True):
        # Change timestamp to ms and use it as index
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', drop=True, inplace=True)
        
        # Detect outliers and remove them
        if SD == True:
            df['outlier'] = self.find_anomalies_SD(data, range)
        else:
            df['outlier'] = self.find_anomalies_IQ(data, range)
        
        df.drop(df[df['outlier'] == True].index, inplace=True)
        df.drop(['outlier'], axis = 1, inplace = True) 
        
        return df

    
    ## ------ cleanse the data and merge dataframes of each attribute ------ ##
    def clean_merge_data(self, df_list, attr_list):
        count_attr = [attr_list.count(attr) for attr in self.our_attributes]
        indices = [sum(count_attr[:x]) for x in range(1, len(count_attr))]
        
        ## clean and create dataframe for each attribute --> to be stacked horizontally 
        df_list1 = [self.filter_outlier(df_x, df_x['Resistance'], range=3, SD=True) for df_x in df_list[:indices[0]]]
        #df_list1 = [df_x for df_x in df_list[:indices[0]]]
        df1 = pd.concat(df_list1)                   ## Merge all Gsr csv 
        
        df_list2 = [self.filter_outlier(df_x, df_x['confidence'], range=3, SD=True) for df_x in df_list[indices[0]:indices[1]]]
        #df_list2 = [df_x for df_x in df_list[indices[0]:indices[1]]]
        df2 = pd.concat(df_list2)                   ## Merge all PhysicalActivityTransitionEntity csv
        
        df_list3 = [self.filter_outlier(df_x, df_x['Interval'], range=3, SD=True) for df_x in df_list[indices[1]:indices[2]]]
        #df_list3 = [df_x for df_x in df_list[indices[1]:indices[2]]]
        df3 = pd.concat(df_list3)                   ## Merge all RRInterval csv
        
        df_list4 = [self.filter_outlier(df_x, df_x['Temperature'], range=3, SD=True) for df_x in df_list[indices[2]:]]
        #df_list4 = [df_x for df_x in df_list[indices[2]:]] 
        df4 = pd.concat(df_list4)                   ## Merge all SkinTemperature csv 

        return df1, df2, df3, df4
    

    ## ------ This function resamples the data ------ ##
    def timestamp_categorise(self, df, interval="300L", method="first"):
        # You can use other parameters such as 1 millisecond ('1L'), 1 second ('1S'), 1 minute('1T'), 1 hour('1H'), 1 day('1D'), 1 week('1W') and so on.
        
        # If there are multuple rows for same timestamp, we will leave first row among the multiple rows
        df = df.groupby(['timestamp']).first() 
        
        if method == 'first':
            df.resample(interval).first()
        elif method == 'last':
            df.resample(interval).last()
        elif method == 'min':
            df.resample(interval).min()
        elif method == 'max':
            df.resample(interval).max()
        elif method == 'mean':
            df.resample(interval).mean()
        
        return df


    ## ------ A container function ------ ##
    def wrapper_function(self, user_UID):
        list_of_users_UID = self.users()
        if user_UID not in list_of_users_UID:
            print("Non-existing user!")
            return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

        dataframe_list, attribute_list = self.extract_user_data(user_UID)
        df_gsr, df_phy, df_hrv, df_skin = self.clean_merge_data(dataframe_list, attribute_list)
        
        df_gsr, df_phy, df_hrv, df_skin = self.timestamp_categorise(df_gsr), self.timestamp_categorise(df_phy), self.timestamp_categorise(df_hrv), self.timestamp_categorise(df_skin) 
        df_gsr, df_phy, df_hrv, df_skin = self.remove_nan(df_gsr), self.remove_nan(df_phy), self.remove_nan(df_hrv), self.remove_nan(df_skin)

        aggregate_skin_gsr = pd.concat([df_skin, df_gsr], axis=1, sort=False)
        aggregate_skin_gsr = self.remove_nan(aggregate_skin_gsr)

        aggregate_gsr_hrv = pd.concat([df_gsr, df_hrv], axis=1, sort=False)
        aggregate_gsr_hrv = self.remove_nan(aggregate_gsr_hrv)

        return aggregate_skin_gsr, aggregate_gsr_hrv, df_phy