# 用baidumap api得到地区经纬度
import requests
import pandas as pd 

api_key = "35f4e1e501594a5abd3a5b8cc4f80008"

'''
# baidu 达不到预期效果
def get_location(api_key,address):
    url = f"http://api.map.baidu.com/geocoding/v3/?ak={api_key}&output=json&address={address}"

    response=requests.get(url)
    data=response.json()
    print(data)
    if data["status"] == 0:
        result = data["result"]
        location = result["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        return latitude, longitude
    else:
        return None
'''

#用
df=pd.read_excel("F:/zyy_wto/data/Commercial_services_export.xlsx")
regions=df['Partner Economy'].unique()
locations=[]
for region in regions:
    coordinates = get_location(api_key, region)
    locations.append(coordinates)

print(locations[:10])
# 统计为 None 的个数
none_count = sum(coord is None for coord in locations)
print(none_count)
