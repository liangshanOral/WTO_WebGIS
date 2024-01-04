# 用baidumap api得到地区经纬度
import requests
import pandas as pd 

api_key = "jVR9BTsdfsxzTn69kkHQHif2vdwccdEm"

def get_location(api_key,address):
    url = f"http://api.map.baidu.com/geocoding/v3/?ak={api_key}&output=json&address={address}"

    response=requests.get(url)
    data=response.json()

    if data["status"] == 0:
        result = data["result"]
        location = result["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        return latitude, longitude
    else:
        return None

'''

'''
df=pd.read_excel("F:/zyy_wto/data/Commercial_services_export.xlsx")
regions=df['Partner Economy'].unique()
locations=[]
for region in regions:
    print(region)
    coordinates = get_location(api_key, region)
    locations.append(coordinates)

print(locations[:10])