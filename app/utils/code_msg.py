# encoding=utf8

import json
import collections


class CodeMsg:
    CM = collections.namedtuple('CM', ['code', 'msg'])
    SUCCESS = CM(200, '成功')


def create_response(ret_cm, data=None, msg=None):
    if ret_cm.code == CodeMsg.SUCCESS.code:
        ret = CommonJsonRet(code=ret_cm.code,
                            msg=ret_cm.msg if msg is None else msg,
                            data=data)
    else:
        ret = CommonJsonRet(code=ret_cm.code,
                            msg=ret_cm.msg if msg is None else msg,
                            data=data)
    return ret.to_json()


class CommonJsonRet():
    """服务统一返回接口格式"""
    def __init__(self, code, msg, data):
        self.code = code
        self.message = msg
        self.data = data

    def to_json_str(self):
        return json.dumps(self.__dict__)

    def to_json(self):
        return self.__dict__
