import pandas as pd
import numpy as np

dfnames=np.array(['P0701','P0702','P0703','P0704','P0705','P0706','P0707','P0708','P0709','P0710','P0711','P0712','P0713','P0714','P0715','P0716','P0717','P0718',
'P0719','P0721','P0722','P0723','P0725','P0726','P0727','P0728','P0729','P1501','P1502','P1503','P1504','P1505','P1506','P1507','P1508','P1509','P1510','P1511','P1514',
'P1515','P1516','P1517','P1518','P1519','P1520','P1521','P1522','P1523','P1525','P1526','P1527','P1541','P3001','P3002','P3003','P3005','P3007','P3008','P3009','P3010','P3011','P3012',
'P3013','P3014','P3015','P3016','P3017','P3018','P3019','P3021','P3022','P3023','P3024','P3025','P3027','P3028','P3029','P3030','P3041'])

for name in dfnames:
    tempname=f'Preprocessed{name}'
    dfname1=f'./PreprocessedData/skin gsr hrv/{tempname}.csv'
    dfname2=f'./PreprocessedData/physical activity/{tempname}PP.csv'
    HRVGSRTempDf=pd.read_csv(dfname1)
    PhysicalActivityDf=pd.read_csv(dfname2)
    resultDf=pd.merge(HRVGSRTempDf, PhysicalActivityDf)
    print(resultDf)
    resultname=f'Merged{name}.csv'
    resultDf.to_csv(resultname)
print("Done")