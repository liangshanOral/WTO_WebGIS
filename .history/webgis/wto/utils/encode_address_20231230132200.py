# 用baidumap api得到地区经纬度

import pandas as pd 

df=pd.read_excel("")
regions=df['Partner Economy'].unique()
for region in regions:
    