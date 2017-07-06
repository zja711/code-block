from redis import Redis,StrictRedis,ConnectionPool
from config import REDIS_CONFIG
redis_pool = ConnectionPool(**REDIS_CONFIG)
REDIS = Redis(connection_pool=redis_pool)





