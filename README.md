### A Djangle project for webgis 

2023.12.21
now it only load some data

data comes form WTO [https://stats.wto.org/] 
it stores in .data

### Get Start
```
bash
git clone https://github.com/liangshanOral/WTO_WebGIS.git
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


