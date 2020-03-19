import pymysql
from pymongo import MongoClient

"""
mogo
spring.data.mongodb.database = sunxing_im
spring.data.mongodb.host = 192.168.100.70
spring.data.mongodb.port = 27017
spring.data.mongodb.repositories.enabled = true
spring.data.mongodb.username = im
spring.data.mongodb.password = sunxing321	
"""

from pymongo import MongoClient

host = '192.168.100.70'
client = MongoClient(host, 27017)

#连接mydb数据库,账号密码认证
mydb = client["sunxing_im"]
mydb.authenticate("im", "sunxing321")
mycol = mydb["messages_info"]

for x in mycol.find():
    print(x)
