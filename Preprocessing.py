from ast import Index
import pandas as pd
import numpy as np
from functools import reduce
import plotly.graph_objects as go
from statsmodels.formula.api import ols
import plotly.express as px

P0701=pd.read_csv('HRV_GSR_Temperature/P0701TempGSRHRV.csv')
P0702=pd.read_csv('HRV_GSR_Temperature/P0702TempGSRHRV.csv')
P0703=pd.read_csv('HRV_GSR_Temperature/P0703TempGSRHRV.csv')
P0704=pd.read_csv('HRV_GSR_Temperature/P0704TempGSRHRV.csv')
P0705=pd.read_csv('HRV_GSR_Temperature/P0705TempGSRHRV.csv')
P0706=pd.read_csv('HRV_GSR_Temperature/P0706TempGSRHRV.csv')
P0707=pd.read_csv('HRV_GSR_Temperature/P0707TempGSRHRV.csv')
P0708=pd.read_csv('HRV_GSR_Temperature/P0708TempGSRHRV.csv')
P0709=pd.read_csv('HRV_GSR_Temperature/P0709TempGSRHRV.csv')
P0710=pd.read_csv('HRV_GSR_Temperature/P0710TempGSRHRV.csv')
P0711=pd.read_csv('HRV_GSR_Temperature/P0711TempGSRHRV.csv')
P0712=pd.read_csv('HRV_GSR_Temperature/P0712TempGSRHRV.csv')
P0713=pd.read_csv('HRV_GSR_Temperature/P0713TempGSRHRV.csv')
P0714=pd.read_csv('HRV_GSR_Temperature/P0714TempGSRHRV.csv')
P0715=pd.read_csv('HRV_GSR_Temperature/P0715TempGSRHRV.csv')
P0716=pd.read_csv('HRV_GSR_Temperature/P0716TempGSRHRV.csv')
P0717=pd.read_csv('HRV_GSR_Temperature/P0717TempGSRHRV.csv')
P0718=pd.read_csv('HRV_GSR_Temperature/P0718TempGSRHRV.csv')
P0719=pd.read_csv('HRV_GSR_Temperature/P0719TempGSRHRV.csv')
P0721=pd.read_csv('HRV_GSR_Temperature/P0721TempGSRHRV.csv')
P0722=pd.read_csv('HRV_GSR_Temperature/P0722TempGSRHRV.csv')
P0723=pd.read_csv('HRV_GSR_Temperature/P0723TempGSRHRV.csv')
P0725=pd.read_csv('HRV_GSR_Temperature/P0725TempGSRHRV.csv')
P0726=pd.read_csv('HRV_GSR_Temperature/P0726TempGSRHRV.csv')
P0727=pd.read_csv('HRV_GSR_Temperature/P0727TempGSRHRV.csv')
P0728=pd.read_csv('HRV_GSR_Temperature/P0728TempGSRHRV.csv')
P0729=pd.read_csv('HRV_GSR_Temperature/P0729TempGSRHRV.csv')
P1501=pd.read_csv('HRV_GSR_Temperature/P1501TempGSRHRV.csv')
P1502=pd.read_csv('HRV_GSR_Temperature/P1502TempGSRHRV.csv')
P1503=pd.read_csv('HRV_GSR_Temperature/P1503TempGSRHRV.csv')
P1504=pd.read_csv('HRV_GSR_Temperature/P1504TempGSRHRV.csv')
P1505=pd.read_csv('HRV_GSR_Temperature/P1505TempGSRHRV.csv')
P1506=pd.read_csv('HRV_GSR_Temperature/P1506TempGSRHRV.csv')
P1507=pd.read_csv('HRV_GSR_Temperature/P1507TempGSRHRV.csv')
P1508=pd.read_csv('HRV_GSR_Temperature/P1508TempGSRHRV.csv')
P1509=pd.read_csv('HRV_GSR_Temperature/P1509TempGSRHRV.csv')
P1510=pd.read_csv('HRV_GSR_Temperature/P1510TempGSRHRV.csv')
P1511=pd.read_csv('HRV_GSR_Temperature/P1511TempGSRHRV.csv')
P1514=pd.read_csv('HRV_GSR_Temperature/P1514TempGSRHRV.csv')
P1515=pd.read_csv('HRV_GSR_Temperature/P1515TempGSRHRV.csv')
P1516=pd.read_csv('HRV_GSR_Temperature/P1516TempGSRHRV.csv')
P1517=pd.read_csv('HRV_GSR_Temperature/P1517TempGSRHRV.csv')
P1518=pd.read_csv('HRV_GSR_Temperature/P1518TempGSRHRV.csv')
P1519=pd.read_csv('HRV_GSR_Temperature/P1519TempGSRHRV.csv')
P1520=pd.read_csv('HRV_GSR_Temperature/P1520TempGSRHRV.csv')
P1521=pd.read_csv('HRV_GSR_Temperature/P1521TempGSRHRV.csv')
P1522=pd.read_csv('HRV_GSR_Temperature/P1522TempGSRHRV.csv')
P1523=pd.read_csv('HRV_GSR_Temperature/P1523TempGSRHRV.csv')
P1525=pd.read_csv('HRV_GSR_Temperature/P1525TempGSRHRV.csv')
P1526=pd.read_csv('HRV_GSR_Temperature/P1526TempGSRHRV.csv')
P1527=pd.read_csv('HRV_GSR_Temperature/P1527TempGSRHRV.csv')
P1541=pd.read_csv('HRV_GSR_Temperature/P1541TempGSRHRV.csv')
P3001=pd.read_csv('HRV_GSR_Temperature/P3001TempGSRHRV.csv')
P3002=pd.read_csv('HRV_GSR_Temperature/P3002TempGSRHRV.csv')
P3003=pd.read_csv('HRV_GSR_Temperature/P3003TempGSRHRV.csv')
P3005=pd.read_csv('HRV_GSR_Temperature/P3005TempGSRHRV.csv')
P3007=pd.read_csv('HRV_GSR_Temperature/P3007TempGSRHRV.csv')
P3008=pd.read_csv('HRV_GSR_Temperature/P3008TempGSRHRV.csv')
P3009=pd.read_csv('HRV_GSR_Temperature/P3009TempGSRHRV.csv')
P3010=pd.read_csv('HRV_GSR_Temperature/P3010TempGSRHRV.csv')
P3011=pd.read_csv('HRV_GSR_Temperature/P3011TempGSRHRV.csv')
P3012=pd.read_csv('HRV_GSR_Temperature/P3012TempGSRHRV.csv')
P3013=pd.read_csv('HRV_GSR_Temperature/P3013TempGSRHRV.csv')
P3014=pd.read_csv('HRV_GSR_Temperature/P3014TempGSRHRV.csv')    
P3015=pd.read_csv('HRV_GSR_Temperature/P3015TempGSRHRV.csv')
P3016=pd.read_csv('HRV_GSR_Temperature/P3016TempGSRHRV.csv')
P3017=pd.read_csv('HRV_GSR_Temperature/P3017TempGSRHRV.csv')
P3018=pd.read_csv('HRV_GSR_Temperature/P3018TempGSRHRV.csv')
P3019=pd.read_csv('HRV_GSR_Temperature/P3019TempGSRHRV.csv')
P3021=pd.read_csv('HRV_GSR_Temperature/P3021TempGSRHRV.csv')
P3022=pd.read_csv('HRV_GSR_Temperature/P3022TempGSRHRV.csv')
P3023=pd.read_csv('HRV_GSR_Temperature/P3023TempGSRHRV.csv')
P3024=pd.read_csv('HRV_GSR_Temperature/P3024TempGSRHRV.csv')
P3025=pd.read_csv('HRV_GSR_Temperature/P3025TempGSRHRV.csv')
P3027=pd.read_csv('HRV_GSR_Temperature/P3027TempGSRHRV.csv')
P3028=pd.read_csv('HRV_GSR_Temperature/P3028TempGSRHRV.csv')
P3029=pd.read_csv('HRV_GSR_Temperature/P3029TempGSRHRV.csv')
P3030=pd.read_csv('HRV_GSR_Temperature/P3030TempGSRHRV.csv')
P3041=pd.read_csv('HRV_GSR_Temperature/P3041TempGSRHRV.csv')

P0701.set_index('timestamp', drop=True,append=False, inplace=True)
P0702.set_index('timestamp', drop=True, inplace=True, append=False)
P0703.set_index('timestamp', drop=True, inplace=True,append=False)
P0704.set_index('timestamp', drop=True, inplace=True,append=False)
P0705.set_index('timestamp', drop=True, inplace=True,append=False)
P0706.set_index('timestamp', drop=True, inplace=True,append=False)
P0707.set_index('timestamp', drop=True, inplace=True,append=False)
P0708.set_index('timestamp', drop=True, inplace=True,append=False)
P0709.set_index('timestamp', drop=True, inplace=True,append=False)
P0710.set_index('timestamp', drop=True, inplace=True,append=False)
P0711.set_index('timestamp', drop=True, inplace=True,append=False)
P0712.set_index('timestamp', drop=True, inplace=True,append=False)
P0713.set_index('timestamp', drop=True, inplace=True,append=False)
P0714.set_index('timestamp', drop=True, inplace=True,append=False)
P0715.set_index('timestamp', drop=True, inplace=True,append=False)
P0716.set_index('timestamp', drop=True, inplace=True,append=False)
P0717.set_index('timestamp', drop=True, inplace=True,append=False)
P0718.set_index('timestamp', drop=True, inplace=True,append=False)
P0719.set_index('timestamp', drop=True, inplace=True,append=False)
P0721.set_index('timestamp', drop=True, inplace=True,append=False)
P0722.set_index('timestamp', drop=True, inplace=True,append=False)
P0723.set_index('timestamp', drop=True, inplace=True,append=False)
P0725.set_index('timestamp', drop=True, inplace=True,append=False)
P0726.set_index('timestamp', drop=True, inplace=True,append=False)
P0727.set_index('timestamp', drop=True, inplace=True,append=False)
P0728.set_index('timestamp', drop=True, inplace=True,append=False)
P0729.set_index('timestamp', drop=True, inplace=True,append=False)
P1501.set_index('timestamp', drop=True, inplace=True,append=False)
P1502.set_index('timestamp', drop=True, inplace=True,append=False)
P1503.set_index('timestamp', drop=True, inplace=True,append=False)
P1504.set_index('timestamp', drop=True, inplace=True,append=False)
P1505.set_index('timestamp', drop=True, inplace=True,append=False)
P1506.set_index('timestamp', drop=True, inplace=True,append=False)
P1507.set_index('timestamp', drop=True, inplace=True,append=False)
P1508.set_index('timestamp', drop=True, inplace=True,append=False)
P1509.set_index('timestamp', drop=True, inplace=True,append=False)
P1510.set_index('timestamp', drop=True, inplace=True,append=False)
P1511.set_index('timestamp', drop=True, inplace=True,append=False)
P1514.set_index('timestamp', drop=True, inplace=True,append=False)
P1515.set_index('timestamp', drop=True, inplace=True,append=False)
P1516.set_index('timestamp', drop=True, inplace=True,append=False)
P1517.set_index('timestamp', drop=True, inplace=True,append=False)
P1518.set_index('timestamp', drop=True, inplace=True,append=False)
P1519.set_index('timestamp', drop=True, inplace=True,append=False)
P1520.set_index('timestamp', drop=True, inplace=True,append=False)
P1521.set_index('timestamp', drop=True, inplace=True,append=False)
P1522.set_index('timestamp', drop=True, inplace=True,append=False)
P1523.set_index('timestamp', drop=True, inplace=True,append=False)
P1525.set_index('timestamp', drop=True, inplace=True,append=False)
P1526.set_index('timestamp', drop=True, inplace=True,append=False)
P1527.set_index('timestamp', drop=True, inplace=True,append=False)
P1541.set_index('timestamp', drop=True, inplace=True,append=False)

P3001.set_index('timestamp', drop=True, inplace=True,append=False)
P3002.set_index('timestamp', drop=True, inplace=True,append=False)
P3003.set_index('timestamp', drop=True, inplace=True,append=False)
P3005.set_index('timestamp', drop=True, inplace=True,append=False)
P3007.set_index('timestamp', drop=True, inplace=True,append=False)
P3008.set_index('timestamp', drop=True, inplace=True,append=False)
P3009.set_index('timestamp', drop=True, inplace=True,append=False)
P3010.set_index('timestamp', drop=True, inplace=True,append=False)
P3011.set_index('timestamp', drop=True, inplace=True,append=False)
P3012.set_index('timestamp', drop=True, inplace=True,append=False)
P3013.set_index('timestamp', drop=True, inplace=True,append=False)
P3014.set_index('timestamp', drop=True, inplace=True,append=False)
P3015.set_index('timestamp', drop=True, inplace=True,append=False)
P3016.set_index('timestamp', drop=True, inplace=True,append=False)
P3017.set_index('timestamp', drop=True, inplace=True,append=False)
P3018.set_index('timestamp', drop=True, inplace=True,append=False)
P3019.set_index('timestamp', drop=True, inplace=True,append=False)
P3021.set_index('timestamp', drop=True, inplace=True,append=False)
P3022.set_index('timestamp', drop=True, inplace=True,append=False)
P3023.set_index('timestamp', drop=True, inplace=True,append=False)
P3024.set_index('timestamp', drop=True, inplace=True,append=False)
P3025.set_index('timestamp', drop=True, inplace=True,append=False)
P3027.set_index('timestamp', drop=True, inplace=True,append=False)
P3028.set_index('timestamp', drop=True, inplace=True,append=False)
P3029.set_index('timestamp', drop=True, inplace=True,append=False)
P3030.set_index('timestamp', drop=True, inplace=True,append=False)
P3041.set_index('timestamp', drop=True, inplace=True,append=False)


dfs=np.array([P0701,P0702,P0703,P0704,P0705,P0706,P0707,P0708,P0709,P0710,P0711,P0712,P0713,P0714,P0715,P0716,P0717,P0718,
P0719,P0721,P0722,P0723,P0725,P0726,P0727,P0728,P0729,P1501,P1502,P1503,P1504,P1505,P1506,P1507,P1508,P1509,P1510,P1511,P1514,
P1515,P1516,P1517,P1518,P1519,P1520,P1521,P1522,P1523,P1525,P1526,P1527,P1541,P3001,P3002,P3003,P3005,P3007,P3008,P3009,P3010,P3011,P3012,
P3013,P3014,P3015,P3016,P3017,P3018,P3019,P3021,P3022,P3023,P3024,P3025,P3027,P3028,P3029,P3030, P3041])
dfnames=np.array(['P0701','P0702','P0703','P0704','P0705','P0706','P0707','P0708','P0709','P0710','P0711','P0712','P0713','P0714','P0715','P0716','P0717','P0718',
'P0719','P0721','P0722','P0723','P0725','P0726','P0727','P0728','P0729','P1501','P1502','P1503','P1504','P1505','P1506','P1507','P1508','P1509','P1510','P1511','P1514',
'P1515','P1516','P1517','P1518','P1519','P1520','P1521','P1522','P1523','P1525','P1526','P1527','P1541','P3001','P3002','P3003','P3005','P3007','P3008','P3009','P3010','P3011','P3012',
'P3013','P3014','P3015','P3016','P3017','P3018','P3019','P3021','P3022','P3023','P3024','P3025','P3027','P3028','P3029','P3030','P3041'])

for df in dfs:
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
#combinedDf=dfs[0].join(dfs[1:], on=['Resistance', 'Interval', 'Temperature'])
#combinedDf=reduce(lambda left, right:pd.merge(left, right, how='outer', on=['timestamp']), dfs)
#combinedDf.to_csv('CombineNew.csv')
combinedDf=pd.concat(dfs)
combinedDf.sort_index(ascending=False)
combinedDf['Timestamp']=pd.to_datetime(combinedDf.index, unit='ms')
combinedDf['OldTimestamp']=combinedDf.index
combinedDf.set_index('Timestamp', drop=True, inplace=True, append=False)
#combinedDf.drop(['Unnamed: 0'], axis=1, inplace=True)
#combinedDf.to_csv('CombineTimeNew.csv')
#combinedDf.to_csv('CombineConcat.csv')

filterResistance1=combinedDf.Resistance>10
filterResistance2=combinedDf.Resistance<10000

combinedDf1=combinedDf.loc[filterResistance1 & filterResistance2]

tempQ1=combinedDf1.Temperature.quantile(0.25)
tempQ2=combinedDf1.Temperature.quantile(0.5)
tempQ3=combinedDf1.Temperature.quantile(0.75)
tempIQR=tempQ3-tempQ1

filterTemperature1=combinedDf1.Temperature>(tempQ1-tempIQR)
filterTemperature2=combinedDf1.Temperature<(tempQ3+tempIQR)

combinedDf2=combinedDf1.loc[filterTemperature1 & filterTemperature2]

#figInterval=px.box(combinedDf2, y="Interval")
#figInterval.show()

HRVQ1=combinedDf2.Interval.quantile(0.25)
HRVQ2=combinedDf2.Interval.quantile(0.5)
HRVQ3=combinedDf2.Interval.quantile(0.75)
HRVIQR=HRVQ3-HRVQ1

filterHRV1=combinedDf2.Interval>(HRVQ1-HRVIQR)
filterHRV2=combinedDf2.Interval<(HRVQ3+HRVIQR)
combinedDf3=combinedDf2.loc[filterHRV1 & filterHRV2]

#combinedDf3['Resistance']=pd.to_numeric(combinedDf3.Resistance)
#combinedDf3['Temperature']=pd.to_numeric(combinedDf3.Temperature)
#combinedDf3['Interval']=pd.to_numeric(combinedDf3.Interval)
combinedDf3=combinedDf3.astype({'Resistance':int, 'Temperature':float, 'Interval':float})

fit=ols('Resistance ~ Temperature', data=combinedDf3).fit()
print(fit.params.Intercept) #2769.4712902962815
print(fit.params.Temperature) #-38.327905604176586
fit.summary()

combinedDf3['CalculatedResistance']=(fit.params.Temperature*combinedDf3['Temperature']+fit.params.Intercept)
combinedDf3['GSRDifference']=combinedDf3.CalculatedResistance-combinedDf3.Resistance
combinedDf3.to_csv("finalPreprocessed.csv")
#combinedDf3.style.format({'CalculatedResistance':'{:.4f}', 'GSRDifference':'{:.4f}'},precision=4)
#combinedDf3.to_csv('Regression.csv')
#combinedDf3.to_csv('RegressionRound.csv')
#fig=go.Figure()
#fig.add_trace(go.Scatter(x=combinedDf2.Temperature, y=combinedDf2.Resistance, mode='markers'))
#fig.update_layout(
#    xaxis=dict(
#        rangeslider=dict(
#            visible=True)
#        ),
#    title='Temperature vs GSR',
#    width=900
#    )
#print(combinedDf2['Interval'].unique())
#print(combinedDf2['Interval'].value_counts())
#print(combinedDf3['Interval'].unique())

#fig.add_trace(go.Scatter(x=combinedDf3['GSRDifference'], y=combinedDf3['Interval'], mode='markers'))
#fig.show()
index=0
for df in dfs:
    filterResistanceIndividual1=df['Resistance']>10
    filterResistanceIndividual2=df['Resistance']<10000
    filterInterval1=df['Interval']>(HRVQ1-HRVIQR)
    filterInterval2=df['Interval']<(HRVQ3+HRVIQR)
    filterTemperature1=df['Temperature']>(tempQ1-tempIQR)
    filterTemperature2=df['Temperature']<(tempQ3+tempIQR)
    tempDf1=df.loc[filterResistanceIndividual1 & filterResistanceIndividual2]
    tempDf2=tempDf1.loc[filterInterval1 & filterInterval2]
    finalDf=tempDf1.loc[filterTemperature1 & filterTemperature2]
    #dfIndex=dfs.index(df)
    dfIndex=index
    dfname=dfnames[dfIndex]
    nameString=f'Preprocessed{dfname}.csv'
    finalDf.to_csv(nameString)
    index=index+1

P0701P=pd.read_csv('PhysicalActivity/P0701PhysicalActivity.csv')
P0702P=pd.read_csv('PhysicalActivity/P0702PhysicalActivity.csv')
P0703P=pd.read_csv('PhysicalActivity/P0703PhysicalActivity.csv')
P0704P=pd.read_csv('PhysicalActivity/P0704PhysicalActivity.csv')
P0705P=pd.read_csv('PhysicalActivity/P0705PhysicalActivity.csv')
P0706P=pd.read_csv('PhysicalActivity/P0706PhysicalActivity.csv')
P0707P=pd.read_csv('PhysicalActivity/P0707PhysicalActivity.csv')
P0708P=pd.read_csv('PhysicalActivity/P0708PhysicalActivity.csv')
P0709P=pd.read_csv('PhysicalActivity/P0709PhysicalActivity.csv')
P0710P=pd.read_csv('PhysicalActivity/P0710PhysicalActivity.csv')
P0711P=pd.read_csv('PhysicalActivity/P0711PhysicalActivity.csv')
P0712P=pd.read_csv('PhysicalActivity/P0712PhysicalActivity.csv')
P0713P=pd.read_csv('PhysicalActivity/P0713PhysicalActivity.csv')
P0714P=pd.read_csv('PhysicalActivity/P0714PhysicalActivity.csv')
P0715P=pd.read_csv('PhysicalActivity/P0715PhysicalActivity.csv')
P0716P=pd.read_csv('PhysicalActivity/P0716PhysicalActivity.csv')
P0717P=pd.read_csv('PhysicalActivity/P0717PhysicalActivity.csv')
P0718P=pd.read_csv('PhysicalActivity/P0718PhysicalActivity.csv')
P0719P=pd.read_csv('PhysicalActivity/P0719PhysicalActivity.csv')
P0721P=pd.read_csv('PhysicalActivity/P0721PhysicalActivity.csv')
P0722P=pd.read_csv('PhysicalActivity/P0722PhysicalActivity.csv')
P0723P=pd.read_csv('PhysicalActivity/P0723PhysicalActivity.csv')
P0725P=pd.read_csv('PhysicalActivity/P0725PhysicalActivity.csv')
P0726P=pd.read_csv('PhysicalActivity/P0726PhysicalActivity.csv')
P0727P=pd.read_csv('PhysicalActivity/P0727PhysicalActivity.csv')
P0728P=pd.read_csv('PhysicalActivity/P0728PhysicalActivity.csv')
P0729P=pd.read_csv('PhysicalActivity/P0719PhysicalActivity.csv')
P1501P=pd.read_csv('PhysicalActivity/P1501PhysicalActivity.csv')
P1502P=pd.read_csv('PhysicalActivity/P1502PhysicalActivity.csv')
P1503P=pd.read_csv('PhysicalActivity/P1503PhysicalActivity.csv')
P1504P=pd.read_csv('PhysicalActivity/P1504PhysicalActivity.csv')
P1505P=pd.read_csv('PhysicalActivity/P1505PhysicalActivity.csv')
P1506P=pd.read_csv('PhysicalActivity/P1506PhysicalActivity.csv')
P1507P=pd.read_csv('PhysicalActivity/P1507PhysicalActivity.csv')
P1508P=pd.read_csv('PhysicalActivity/P1508PhysicalActivity.csv')
P1509P=pd.read_csv('PhysicalActivity/P1509PhysicalActivity.csv')
P1510P=pd.read_csv('PhysicalActivity/P1510PhysicalActivity.csv')
P1511P=pd.read_csv('PhysicalActivity/P1511PhysicalActivity.csv')
P1514P=pd.read_csv('PhysicalActivity/P1514PhysicalActivity.csv')
P1515P=pd.read_csv('PhysicalActivity/P1515PhysicalActivity.csv')
P1516P=pd.read_csv('PhysicalActivity/P1516PhysicalActivity.csv')
P1517P=pd.read_csv('PhysicalActivity/P1517PhysicalActivity.csv')
P1518P=pd.read_csv('PhysicalActivity/P1518PhysicalActivity.csv')
P1519P=pd.read_csv('PhysicalActivity/P1519PhysicalActivity.csv')
P1520P=pd.read_csv('PhysicalActivity/P1520PhysicalActivity.csv')
P1521P=pd.read_csv('PhysicalActivity/P1521PhysicalActivity.csv')
P1522P=pd.read_csv('PhysicalActivity/P1522PhysicalActivity.csv')
P1523P=pd.read_csv('PhysicalActivity/P1523PhysicalActivity.csv')
P1525P=pd.read_csv('PhysicalActivity/P1525PhysicalActivity.csv')
P1526P=pd.read_csv('PhysicalActivity/P1526PhysicalActivity.csv')
P1527P=pd.read_csv('PhysicalActivity/P1527PhysicalActivity.csv')
P1541P=pd.read_csv('PhysicalActivity/P1541PhysicalActivity.csv')
P3001P=pd.read_csv('PhysicalActivity/P3001PhysicalActivity.csv')
P3002P=pd.read_csv('PhysicalActivity/P3002PhysicalActivity.csv')
P3003P=pd.read_csv('PhysicalActivity/P3003PhysicalActivity.csv')
P3005P=pd.read_csv('PhysicalActivity/P3005PhysicalActivity.csv')
P3007P=pd.read_csv('PhysicalActivity/P3007PhysicalActivity.csv')
P3008P=pd.read_csv('PhysicalActivity/P3008PhysicalActivity.csv')
P3009P=pd.read_csv('PhysicalActivity/P3009PhysicalActivity.csv')
P3010P=pd.read_csv('PhysicalActivity/P3010PhysicalActivity.csv')
P3011P=pd.read_csv('PhysicalActivity/P3011PhysicalActivity.csv')
P3012P=pd.read_csv('PhysicalActivity/P3012PhysicalActivity.csv')
P3013P=pd.read_csv('PhysicalActivity/P3013PhysicalActivity.csv')
P3014P=pd.read_csv('PhysicalActivity/P3014PhysicalActivity.csv')
P3015P=pd.read_csv('PhysicalActivity/P3015PhysicalActivity.csv')
P3016P=pd.read_csv('PhysicalActivity/P3016PhysicalActivity.csv')
P3017P=pd.read_csv('PhysicalActivity/P3017PhysicalActivity.csv')
P3018P=pd.read_csv('PhysicalActivity/P3018PhysicalActivity.csv')
P3019P=pd.read_csv('PhysicalActivity/P3019PhysicalActivity.csv')
P3021P=pd.read_csv('PhysicalActivity/P3021PhysicalActivity.csv')
P3022P=pd.read_csv('PhysicalActivity/P3022PhysicalActivity.csv')
P3023P=pd.read_csv('PhysicalActivity/P3023PhysicalActivity.csv')
P3024P=pd.read_csv('PhysicalActivity/P3024PhysicalActivity.csv')
P3025P=pd.read_csv('PhysicalActivity/P3025PhysicalActivity.csv')
P3027P=pd.read_csv('PhysicalActivity/P3027PhysicalActivity.csv')
P3028P=pd.read_csv('PhysicalActivity/P3028PhysicalActivity.csv')
P3029P=pd.read_csv('PhysicalActivity/P3029PhysicalActivity.csv')
P3030P=pd.read_csv('PhysicalActivity/P3030PhysicalActivity.csv')
P3041P=pd.read_csv('PhysicalActivity/P3041PhysicalActivity.csv')

pdfs=np.array([P0701P,P0702P,P0703P,P0704P,P0705P,P0706P,P0707P,P0708P,P0709P,P0710P,P0711P,P0712P,P0713P,P0714P,P0715P,P0716P,P0717P,P0718P,
P0719P,P0721P,P0722P,P0723P,P0725P,P0726P,P0727P,P0728P,P0729P,P1501P,P1502P,P1503P,P1504P,P1505P,P1506P,P1507P,P1508P,P1509P,P1510P,P1511P,P1514P,
P1515P,P1516P,P1517P,P1518P,P1519P,P1520P,P1521P,P1522P,P1523P,P1525P,P1526P,P1527P,P1541P,P3001P,P3002P,P3003P,P3005P,P3007P,P3008P,P3009P,P3010P,P3011P,P3012P,
P3013P,P3014P,P3015P,P3016P,P3017P,P3018P,P3019P,P3021P,P3022P,P3023P,P3024P,P3025P,P3027P,P3028P,P3029P,P3030P,P3041P])
pdfnames=np.array(['P0701P','P0702P','P0703P','P0704P','P0705P','P0706P','P0707P','P0708P','P0709P','P0710P','P0711P','P0712P','P0713P','P0714P','P0715P','P0716P','P0717P','P0718P',
'P0719P','P0721P','P0722P','P0723P','P0725P','P0726P','P0727P','P0728P','P0729P','P1501P','P1502P','P1503P','P1504P','P1505P','P1506P','P1507P','P1508P','P1509P','P1510P','P1511P','P1514P',
'P1515P','P1516P','P1517P','P1518P','P1519P','P1520P','P1521P','P1522P','P1523P','P1525P','P1526P','P1527P','P1541P','P3001P','P3002P','P3003P','P3005P','P3007P','P3008P','P3009P','P3010P','P3011P','P3012P',
'P3013P','P3014P','P3015P','P3016P','P3017P','P3018P','P3019P','P3021P','P3022P','P3023P','P3024P','P3025P','P3027P','P3028P','P3029P','P3030P','P3041P'])

index=0
for pdf in pdfs:
    pdf.drop(['Unnamed: 0'], axis=1, inplace=True)
    pdf=pdf.round({'timestamp':-2})
    pdf['Timestamp']=pd.to_datetime(pdf.timestamp, unit='ms')
    pdf['OldTimestamp']=pdf.index
    pdf.set_index('Timestamp', drop=True, inplace=True, append=False)
    pdf=pdf.astype({'confidence':float})

    Pfilter=pdf['confidence']>=0.5
    temppdf=pdf.loc[Pfilter]
    
    tempList=[]
    for idx,row in temppdf.iterrows():
        if row['type']=="STILL":
            #row['ActivityScore']=0
            tempList.append(0)
        elif row['type']=='ON_FOOT':
            #row['ActivityScore']=0.1
            tempList.append(0.1)
        elif row['type']=='WALKING':
            tempList.append(0.5)
            #row['ActivityScore']=0.5
        elif row['type']=='RUNNING' or row['type']=='ON_BICYCLE':
            tempList.append(0.8)
            #row['ActivityScore']=0.8
        else:
            tempList.append(np.nan)
            #row['ActivityScore']=np.nan
    temppdf['ActivityScore']=tempList
    
    pdfname=pdfnames[index]
    pnameString=f'Preprocessed{pdfname}P.csv'
    temppdf.to_csv(pnameString)
    index=index+1
#PcombinedDf=pd.concat(pdfs)
#PcombinedDf.sort_index(ascending=False)
#PcombinedDf['Timestamp']=pd.to_datetime(PcombinedDf.index, unit='ms')
#PcombinedDf['OldTimestamp']=PcombinedDf.index
#PcombinedDf.set_index('Timestamp', drop=True, inplace=True, append=False)

#PcombinedDf.to_csv('CombinedActivity.csv')
print("Done")