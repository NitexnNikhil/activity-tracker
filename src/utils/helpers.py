from utils.redis_db import redis

def get_date_key(user, selected_date):

    return (
        f"user:{user}:habits:{selected_date}"
    )

def save_habit(
    user,
    selected_date,
    habit,
    value
):

    key = get_date_key(
        user,
        selected_date
    )

    redis.hset(
        key,
        values={
            habit: str(value)
        }
    )

def get_habits(
    user,
    selected_date
):

    key = get_date_key(
        user,
        selected_date
    )

    data = redis.hgetall(key)

    if not data:
        return {}

    return data