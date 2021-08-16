import time
import json
from django.utils.deprecation import MiddlewareMixin
import urllib.parse
# 获取日志logger
import logging

logger = logging.getLogger(__name__)


class LogMiddle(MiddlewareMixin):
    # 日志处理中间件
    def process_request(self, request):
        # 存放请求过来时的时间
        request.init_time = time.time()
        logger.error(f'request in at {request.init_time}')
        return None

    def process_response(self, request, response):
        try:
            end_time = time.time()
            logger.error(f'request end at {end_time}')
            logger.error(f"{request.path} 耗时 {end_time - request.init_time}")
        except:
            logger.critical('系统错误')
        return response
