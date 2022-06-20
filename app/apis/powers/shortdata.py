# -*- coding: utf-8 -*-
__auther__ = '35942'


import os
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from config import DATA_DIR

router = APIRouter()

@router.get("/short", summary="甘肃短期对外数据接口", description="获取云端功率接口数据", tags=["power"])
def grid_short_data(wfid :str) -> dict :
    """ 获取云端通过接口获取数据后录入的数据"""
    return {"status":"success"}


def iterfile(jfile):
    with open(jfile, mode="rb") as file_like:
        yield from file_like

@router.get("/short/file/download", summary="甘肃短期对外预测数据文件下载", description="功率文件下载", tags=["power"])
def resp_grid_short_file():
    """ 获取对应短期数据文件"""
    file_path = os.path.join(DATA_DIR, "1.json")
    resp = StreamingResponse(iterfile(file_path),
                             headers={"file_name": "1.json"},
                             media_type="application/octet-stream")
    return resp
