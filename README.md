### A Djangle project for webgis 

2023.12.21

now it only loads some data


### Get Start
```
git clone [https://github.com/liangshanOral/WTO_WebGIS.git](https://github.com/liangshanOral/WTO_WebGIS.git)
```
配置环境
```
pip install -r requirements.txt
```
迁移数据库
```
python manage.py migrate
```
创建一个超级用户，从而可以查看数据
```
python manage.py createsuperuser
```
RUN！
```
python manage.py runserver
```
转到admin就可以查看数据库了

### 数据说明
data comes form WTO [https://stats.wto.org/]

it stores in .data

时间跨度 2022-2015

不同地区 不同类别 不同年份 年进出口量

不同地区 不同年份 季度、月进出口量 （但是有些不全）

不同地区 不同年份 进出口指数


![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3eab747e-7837-4492-809b-0a40c4e38b27/b89cf4eb-ebf5-4f70-abe0-673e062b645c/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3eab747e-7837-4492-809b-0a40c4e38b27/74466429-8871-4a21-9dba-16c0731bc39a/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3eab747e-7837-4492-809b-0a40c4e38b27/310dcaea-5a62-4c67-a8ab-173ad533f7ac/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3eab747e-7837-4492-809b-0a40c4e38b27/4d8ffc54-aa7c-4bf0-ba89-2c2e8c7bbad2/Untitled.png)

