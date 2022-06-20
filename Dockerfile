FROM       hub.windinfo.cn/python/python3.8base:dm8
MAINTAINER  songpengfei@goldwind.com.cn

WORKDIR	    /outer_shortdata
COPY        requirements.txt  .
USER      0

RUN        pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple  &&\
           pip3  install -r requirements.txt   -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
COPY   .  /outer_shortdata/

ENTRYPOINT  [ "python", "enterpoint.py" ]

