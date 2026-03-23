import redis

try:
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    r.ping()
    REDIS_AVAILABLE = True
except:
    REDIS_AVAILABLE = False


def set_cache(key, value):
    if REDIS_AVAILABLE:
        try:
            r.set(key, value)
        except:
            pass


def get_cache(key):
    if REDIS_AVAILABLE:
        try:
            return r.get(key)
        except:
            return None
    return None