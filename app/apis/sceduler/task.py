# -*- coding: utf-8 -*-
__auther__ = '35942'


import os
import time
import json

from config import DATA_DIR
from app.utils.func_utils import req_url
from app.utils.log_utils import logger

async def curl_gateway_url(al: str) -> None:
    url = "https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json"
    resp_data = req_url(url)
    dtime_stamp = time.strftime("%Y%m%d_%H%M%S")
    file_name = dtime_stamp + ".json"
    file_name = os.path.join(DATA_DIR, file_name)
    logger.info('write_file=【%s】 success '%file_name)
    with open(file_name, "w") as jfp:
        jfp.write(json.dumps(resp_data))



