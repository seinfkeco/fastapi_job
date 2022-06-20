# -*- coding: utf-8 -*-
__auther__ = '35942'


import uvicorn

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from settings import TZ

Schedule = AsyncIOScheduler({
    'jobstores':{
        'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    },
    'job_defaults': {
        'coalesce': False,
        'max_instances': 3
    },
    'timezone': TZ}
)

Schedule.start()


if __name__ == "__main__":

    uvicorn.run(
        app='app:app',
        host="0.0.0.0",
        port=8010,
        reload=False,
        debug=True
    )
