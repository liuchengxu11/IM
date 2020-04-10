import redis
from Config.Config import DB_redis_host,DB_redis_port,DB_redis_pwd
import json
import re

"""
spring.redis.host = 192.168.100.70
spring.redis.port = 6379
spring.redis.password = Sunxing321

"""


class Db_redis():
    __pool = None

    def __init__(self,db_seg=0):
        self.host = DB_redis_host
        self.pwd = DB_redis_pwd
        self.port = DB_redis_port
        self.__pool = redis.ConnectionPool(host=self.host, port=self.port, password=self.pwd, db=db_seg)

    # 保存数据
    # expire：过期时间，单位秒

    def set(self, key, value, expire=None):
        redi = redis.Redis(connection_pool=self.__pool)
        redi.set(key, value, ex=expire)

    # 获取数据
    def get(self, key):
        ri= redis.Redis(connection_pool=self.__pool)
        value = ri.get(key)
        if value is None:
            print("_________{}__________无数据".format(key))
            return None
        value = value.decode("UTF-8")
        value1=re.sub(r"\\\\\\","",value)
        value11=json.loads(value1)
        print("_________{}__________有数据".format(key))
        return value11

    # 删除数据
    def dele(self, key):
        redi = redis.Redis(connection_pool=self.__pool)
        if redi.delete(key):
            print("{}___缓存数据删除成功".format(key))


# def select_db(self, date, date1):
#     redis_service = "im"
#     demo = Db_redis(redis_service)
#     demo.initialization_db()


# if __name__ == "__main__":
#     pool = redis.ConnectionPool(host='192.168.100.70', port=6379,password="Sunxing321")
#     r = redis.Redis(connection_pool=pool)
#     r.set('333', '6666')
#     print(r.get('333').decode('utf8'))
