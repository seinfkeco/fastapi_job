# -*- coding: utf-8 -*-
__auther__ = '35942'

from datetime import datetime

from fastapi import APIRouter, Body
from enterpoint import Schedule
from apscheduler.triggers.cron import CronTrigger

from app.utils.func_utils import resp_fail, resp_ok, cron_task
from app.apis.sceduler.task import curl_gateway_url

router = APIRouter()


# 获取全部任务信息
@router.get("/all", summary="获取任务列表", tags=["schedule"])
def get_api_data():
    schedules = []
    for job in Schedule.get_jobs():
        schedules.append(
            {"job_id": job.id, "func_name": job.func_ref, "func_args": job.args, "cron_model": str(job.trigger),
             "next_run": str(job.next_run_time)}
        )
    return resp_ok(data=schedules)


# cron 更灵活的定时任务 可以使用crontab表达式
@router.post("/cron/schedule/", summary="开启定时:crontab表达式", tags=["schedule"])
async def add_cron_job(
        job_id: str = Body(..., title="任务id", embed=True),
        crontab: str = Body('*/5 * * * *', title="crontab 表达式"),
        run_time: str = Body(..., title="第一次运行时间", description="当前时间点之后", embed=True)
):
    res = Schedule.get_job(job_id=job_id)
    if res:
        return resp_fail(msg=f"{job_id} job already exists")
    schedule_job = Schedule.add_job(curl_gateway_url,
                                    CronTrigger.from_crontab(crontab),
                                    args=(job_id,),
                                    id=job_id,  # job ID
                                    next_run_time=datetime.strptime(run_time, '%Y-%m-%d %H:%M:%S')
                                    )
    return resp_ok(data={"job_id": schedule_job.id})


# 通过id 删除任务
@router.post("/del", summary="移除任务", tags=["schedule"])
async def remove_schedule(
        job_id: str = Body(..., title="任务id", embed=True)
):
    res = Schedule.get_job(job_id=job_id)
    if not res:
        return resp_fail(msg=f"not found job {job_id}")
    Schedule.remove_job(job_id)
    return resp_ok()