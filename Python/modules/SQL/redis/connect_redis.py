import redis

# host = "127.0.0.1"
# port = 6379
# db = 8
# password = "123456qa"

host = ""
port = 6379
db = 8
password = "123456qa"


pool = redis.ConnectionPool(host=host, port=port, decode_response=True)
redis_connect = redis.Redis(connection_pool=pool)

name = "test1"
value = 1234
ex = 10  # 过期时间，秒
px = 10  # 过期时间，毫秒
nx = True  # 为True时，只有name 不存在时，添加
xx = True  # 为True时，只有name 存在时，添加


redis_connect.set(name=name, value=value, ex=ex)

ret_info = redis_connect.get(data_key)

