from utils.redis_db import redis

def save_habit(user, habit, value):

    key = f"user:{user}:habits"

    redis.hset(
        key,
        habit,
        value
    )

def get_habits(user):

    key = f"user:{user}:habits"

    data = redis.hgetall(key)

    if data is None:
        return {}

    return data