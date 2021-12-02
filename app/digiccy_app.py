import logging
from app import create_app_api
from app.utils.code_msg import CommonJsonRet
from app.digiccy_log import init_log

init_log()

app, api = create_app_api()

@app.errorhandler(404)
def page_not_not_found(error):
    return CommonJsonRet(code=404,
                         msg="404 Not Found . there is not this api",
                         data="").to_json_str()

@api.errorhandler
def default_error_handler(exception):
    # 异常栈写入
    logging.error(exception)
    return CommonJsonRet(code=500,
                         msg=exception.message,
                         data="server exception capture").to_json()

if __name__ == '__main__':
    print("app=", app)
    app.run(host='0.0.0.0', port=58480)
