import redis
# 普通连接
conn = redis.Redis(host='127.0.0.1', port=6379)
conn.set('name', 'lusyou')
print(conn.get('name'))

