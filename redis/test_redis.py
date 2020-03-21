import redis
from redis_pool import POOL

conn = redis.Redis(connection_pool=POOL)
conn.set('a', 123)
print(conn.get('a'))