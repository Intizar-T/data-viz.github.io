##### ---------------------------- Description ---------------------------- #####
# ---- All the data of a given user can be filtered and cleaned easily ----- #
# ---- We can select our own desired attributes in addition to the 4 ----- #
##### --------------------------------------------------------------------- #####

##### ---------------------------- File structure ---------------------------- #####
# project_folder
#   |
#   |--code_folder
#   |   |
#   |   |--process.py
#   |   |--app.py
#   |  
#   |--data_folder
#   |   |
#   |   |--user_info.csv
#   |   |--P0701.zip
#   |   |--P0702.zip
#   |--PreprocessedData
#   |   |
#   |   |--skin gsr hrv
#       |   |
#       |   |-- PreprocessedP0701.csv
#       |   |-- PreprocessedP0702.csv
#       |
#       |--physical activity
#           |
#           |-- PreprocessedP0701.csv
#           |-- PreprocessedP0702.csv
#
##### --------------------------------------------------------------------- #####

from numpy.lib.utils import deprecate_with_doc
import pandas as pd
import numpy as np
import zipfile, os, re
import pathlib
import csv


class preprocess():
    def __init__(self):
        self.project_path = pathlib.Path.cwd().parent
        self.data_list = os.listdir(os.path.join(self.project_path, 'data'))[2:-2]
        ## Make sure this is written in alphabetic order
        ## Pick any attribute with its features
        self.our_attributes = {
            #'Accelerometer': ['X', 'Y', 'Z'],
            'Gsr': ['Resistance'],
            'PhysicalActivityEventEntity': ['confidence'],
            'RRInterval': ['Interval'],
            'SkinTemperature': ['Temperature']
        }
    
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
                if (700 <= int(row[0]) < 800):
                    UID = 'P0' + row[0]
                else:
                    UID = 'P' + row[0]

                if user_UID == UID:
                    infos['Openness'] = row[1]
                    infos['Conscientiousness'] = row[2]
                    infos['Neuroticism'] = row[3]
                    infos['Extraversion'] = row[4]
                    infos['Agreeableness'] = row[5]
                    infos['Age'] = row[6]
                    infos['Gender'] = row[7]
                    break
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
                if attr in list(self.our_attributes.keys()):
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

    
    ## ------ This function filters outliers data attr becomes "Resistance" for Gsr, "Interval" for RRInterval ...
    def filter_outlier(self, df, col_names, range, cleaned, SD=True):
        # Change timestamp to ms and use it as index
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', drop=True, inplace=True)

        if cleaned:
            if SD:
                for col in col_names:
                    df['outlier ' + col] = self.find_anomalies_SD(df[col], range)
            else:
                for col in col_names:
                    df['outlier ' + col] = self.find_anomalies_IQ(df[col], range)
            
            # Detect outliers and remove them
            for col in col_names:
                df = df[df['outlier ' + col] == False]
            
            df = df.drop(['outlier ' + name for name in col_names], axis = 1)
        
        return df


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

    ## ------ This function labels the range ------ ##
    def label_range(self, df, attr):
        min_val = df[attr].min()
        max_val = df[attr].max()
        label=[]
        for x in df[attr]:
            if x >= 0 and x<= 0.8 * max_val:
                label.append("Good")
            elif x > 0.8 * max_val:
                label.append("Very Good")
            elif x<=0 and x>= 0.8 * min_val:
                label.append("Poor")
            else:
                label.append("Very Poor")
        return label

    ## ------ This function is used to calculate the percentage of poor points ------ ##
    def percentage_poor(self, df):
        temp_df = df.groupby('label').count().sort_index()
        return temp_df
    

    ## ------ cleanse the data and merge dataframes of each attribute ------ ##
    def clean_merge_data(self, df_list, attr_list, cleaned):
        count_attr = [attr_list.count(attr) for attr in list(self.our_attributes.keys())]
        indices = [sum(count_attr[:x]) for x in range(0, len(count_attr) + 1)]
        attr_df = {}
        i = 0

        for key, value in self.our_attributes.items():
            df_list_attr = [self.filter_outlier(df_x, value, range=3, cleaned=cleaned, SD=True) for df_x in df_list[indices[i]:indices[i+1]]]
            df_attr = pd.concat(df_list_attr)
            attr_df[key] = self.timestamp_categorise(df_attr)
            i += 1
        
        return attr_df
    

    ## ------ A container function ------ ##
    def wrapper_function(self, user_UID, cleaned=True, preprocessed=True):
        list_of_users_UID = self.users()
        if user_UID not in list_of_users_UID:
            print("Not a Proper UID")
            return [pd.DataFrame() for x in range(3)]

        if preprocessed == True:
            aggregate_skin_gsr_hrv = pd.read_csv(os.path.join(self.project_path, 'PreprocessedData', 'skin gsr hrv', "Preprocessed" + user_UID))
            physical_activity = pd.read_csv(os.path.join(self.project_path, 'PreprocessedData', 'physical activity', "Preprocessed" + user_UID))

        else:  
            dataframe_list, attribute_list = self.extract_user_data(user_UID)
            dict_attr_df = self.clean_merge_data(dataframe_list, attribute_list, cleaned)            # A dictionary of all the attributes we chose and their dataframe
            
            physical_activity = dict_attr_df['PhysicalActivityEventEntity']
            
            aggregate_skin_gsr = pd.concat([dict_attr_df['SkinTemperature'], dict_attr_df['Gsr']], axis=1, sort=False)
            aggregate_skin_gsr = self.remove_nan(aggregate_skin_gsr)
            aggregate_skin_gsr['Gsr_calculated'] = (-1) * 38.3279 * aggregate_skin_gsr['Temperature'] + 2769.4713
            aggregate_skin_gsr['Gsr_difference'] = aggregate_skin_gsr['Gsr_calculated'] - aggregate_skin_gsr['Resistance']

            aggregate_skin_gsr_hrv = pd.concat([aggregate_skin_gsr, dict_attr_df['RRInterval']], axis=1, sort=False)
            aggregate_skin_gsr_hrv = self.remove_nan(aggregate_skin_gsr_hrv)
        
        aggregate_skin_gsr_hrv['label'] = self.label_range(aggregate_skin_gsr_hrv, 'Gsr_difference')
        percent_poor_df = self.percentage_poor(aggregate_skin_gsr_hrv)
        
        return aggregate_skin_gsr_hrv, physical_activity, percent_poor_df