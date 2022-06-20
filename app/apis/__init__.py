# -*- coding: utf-8 -*-
__auther__ = '35942'

from fastapi import APIRouter

api_router = APIRouter()

from app.apis.powers import shortdata
from app.apis.powers import gateway_api
from app.apis.sceduler import job


api_router.include_router(shortdata.router, prefix="/power")
api_router.include_router(gateway_api.router, prefix="/power")
api_router.include_router(job.router, prefix="/job")