# -*- coding: utf-8 -*-
__auther__ = '35942'


import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MEDIA_PATH = BASE_DIR/'media'

DATA_DIR = os.path.join(BASE_DIR, "data")

LOG_DIR = os.path.join(BASE_DIR, 'logs')
