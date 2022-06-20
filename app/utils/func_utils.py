# -*- coding: utf-8 -*-
__auther__ = '35942'


import os
import time
import json
import traceback
from typing import Union
from functools import wraps

import requests

from config import DATA_DIR, LOG_DIR

def resp_ok(*, code=True, msg="ok", data: Union[list, dict, str] = None) -> dict:
    return {"code": code, "msg": msg, "data": data}


def resp_fail(*, code=False, msg="fail", data: Union[list, dict, str] = None):
    return {"code": code, "msg": msg, "data": data}

def dir_mk(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path, exist_ok=True)
        except Exception as ex:
            print(ex.args)

def req_url(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        data = json.loads(resp.content)
        return data
    else:
        return {}

def setup_filedir():
    dir_mk(DATA_DIR)
    dir_mk(LOG_DIR)

async def cron_task(al: str) -> None:
    print(time.strftime("%Y-%m-%d, %H:%M:%S"))

def catch_eror(func):
    @wraps(func)
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as err:
            traceback.print_exc()
            return resp_fail(msg="查询失败", data={"error": err})
    return inner



