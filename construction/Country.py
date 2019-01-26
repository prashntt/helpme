import requests
import json
import psycopg2 as pg
connection=pg.connect(user='postgres',
  host='localhost',
  database='django_project',
  password='Administrator',
  port='5432')
"""
cursor1 = connection.cursor()
Trunc_Query='TRUNCATE TABLE CONSTRUCTION_NATION;'
cursor1.execute(Trunc_Query)
print cursor1.query
connection.commit()

response=requests.get('http://services.groupkt.com/country/get/all')
JsonResponse=response.json()
CountryList=JsonResponse['RestResponse']['result']
for i in CountryList:
    country=(i['name'].encode('utf-8'),i['alpha2_code'].encode('utf-8'),i['alpha3_code'].encode('utf-8'))
    cursor2 = connection.cursor()
    Insert_Query='''INSERT INTO CONSTRUCTION_NATION ("Name",alpha2_code,alpha3_code) VALUES {};'''.format(country)
    cursor2.execute(Insert_Query)
    print cursor2.query
    connection.commit()
"""
response=requests.get('http://services.groupkt.com/country/get/all')
JsonResponse=response.json()
CountryList=JsonResponse['RestResponse']['result']
for i in CountryList:
    try:
    	country=(i['name'].encode('utf-8').replace("'",""),i['alpha2_code'].encode('utf-8').replace("'",""),i['alpha3_code'].encode('utf-8').replace("'",""))
    except:
    	continue
    cursor2 = connection.cursor()
    Select_Query="""SELECT COUNT(*) FROM CONSTRUCTION_NATION WHERE "Name"='{}';""".format(country[0])
    cursor2.execute(Select_Query)
    count=cursor2.fetchone()[0]
    print count
    if count == 0:
    	Insert_Query="""INSERT INTO CONSTRUCTION_NATION ("Name",alpha2_code,alpha3_code) VALUES {};""".format(country)
    	cursor2.execute(Insert_Query)
    	print cursor2.query
    	connection.commit()
    else:
    	Update_Query="""UPDATE CONSTRUCTION_NATION SET "Name" = '{name}',alpha2_code='{alpha2_code}',alpha3_code='{alpha3_code}' WHERE "Name"='{name}';""".format(name=country[0],alpha2_code=country[1],alpha3_code=country[2])
    	cursor2.execute(Update_Query)
    	print cursor2.query
    	connection.commit()