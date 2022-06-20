# -*- coding: utf-8 -*-
__auther__ = '35942'


import os
import pytz

# 业务库
MONGO_SALT_URL = os.getenv('MONGO_SALT_URL','')

# 基础库
MONGO_SALT_META_URL = os.getenv('MONGO_SALT_META_URL','')

# 日志等级
LOG_LEVEL = os.getenv("LOG_LEVEL", 'DEBUG')

# 时区
TZ = pytz.timezone('Asia/Shanghai')