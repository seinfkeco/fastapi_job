# -*- coding: utf-8 -*-
__auther__ = '35942'


from fastapi import APIRouter
from app.utils.func_utils import resp_ok, req_url
from app.utils.log_utils import logger


router = APIRouter()

@router.get("/curl", summary="甘肃网关获取数据接口", description="甘肃网关获取数据接口", tags=["power"])
async def get_gateway_api_shortdata():
    """请求网关接口返回数据"""
    url = "https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json"
    logger.info('curl api success')
    return resp_ok(data=req_url(url))
