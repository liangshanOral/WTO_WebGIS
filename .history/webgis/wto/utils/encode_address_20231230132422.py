# 用baidumap api得到地区经纬度
import requests
import pandas as pd 

def get_location(api_key,addrss):
    

df=pd.read_excel("F:/zyy_wto/data/Commercial_services_export.xlsx")
regions=df['Partner Economy'].unique()
for region in regions:
