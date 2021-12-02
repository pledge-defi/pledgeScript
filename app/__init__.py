import logging
import atexit
import fcntl
from flask import Flask
from flask_apscheduler import APScheduler
from flask_environments import Environments
from flask_restplus import Api
import os





SERVICE_NAME = 'script'
APP_URL_PREFIX = '/v1/api/script'

from app.bsc.wallet import BscWallet

bsc_wallet = BscWallet()




def create_app_api():
    """构成项目所需要的服务实例"""

    app = Flask(SERVICE_NAME)
    flask_env = os.environ.get('FLASK_ENV', "Development")

    # APP所需配置
    config_env = Environments(app, default_env=flask_env)
    config_env.from_object('config')

    bsc_wallet.init_app(app)

    # 初始化api对象
    api = Api(version="v1.0.0", title=SERVICE_NAME, prefix=APP_URL_PREFIX)
    api.init_app(app, add_specs=False)


    f = open("scheduler.lock", "wb")
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        scheduler = APScheduler()
        scheduler.api_enabled = True
        scheduler.init_app(app)
        scheduler.start()
    except Exception as e:
        logging.info(f"script is error {str(e)}")
        pass

    def unlock():
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()

    atexit.register(unlock)
    return app, api



