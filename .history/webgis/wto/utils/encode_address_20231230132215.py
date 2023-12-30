# 用baidumap api得到地区经纬度

import pandas as pd 

df=pd.read_excel("F:/zyy_wto/data/Commercial_services_export.xlsx")
regions=df['Partner Economy'].unique()
for region in regions:
    