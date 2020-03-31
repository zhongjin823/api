import requests
from common.log import Log

log = Log()


class RequestMethod:
    @staticmethod
    def do_request(url, method, data):
        method = method.lower()
        try:
            if method == "get":
                res = requests.get(url, params=data)
            elif method == "post":
                res = requests.post(url, data=data)
            return res
        except Exception:
            log.error('发送失败', exc_info=True)
