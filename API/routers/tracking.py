# lib
import config
import task
from celery.result import AsyncResult
from database.mysql_connector import get_all_jobs
from entities import TaskOut
from fastapi import APIRouter, HTTPException
from redis import Redis
from redis.lock import Lock as RedisLock

# entities
redis_instance = Redis.from_url(task.redis_url)
router = APIRouter(prefix="/tracking")


@router.get("/")
def tracking():
    result = get_all_jobs()
    print(result)
    return result


def _to_task_out(r: AsyncResult) -> TaskOut:
    return TaskOut(id=r.task_id, status=r.status)
