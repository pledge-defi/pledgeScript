# encoding=utf8
import os


class Config(object):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SCHEDULER_EXECUTORS = {
        'default': {
           'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
           'max_workers': '60'},
        'processpool': {
           'type': 'processpool',
           'max_workers': '5'}
        }
    JOBS = [
        # settle
        {
            'id': 'base.get_latest_block.job',
            'func': 'app.bsc.tasks:settle',
            'args': (),
            'trigger': 'interval',
            'seconds': 10,
            'replace_existing': True,
            'coalesce': True,
            'misfire_grace_time': 1,
        },
        # finish
        {
            'id': 'base.get_latest_block.job',
            'func': 'app.bsc.tasks:finish',
            'args': (),
            'trigger': 'interval',
            'seconds': 20,
            'replace_existing': True,
            'coalesce': True,
            'misfire_grace_time': 1,
        },
        # liquidate
        {
            'id': 'base.get_latest_block.job',
            'func': 'app.bsc.tasks:liquidate',
            'args': (),
            'trigger': 'interval',
            'seconds': 30,
            'replace_existing': True,
            'coalesce': True,
            'misfire_grace_time': 1,
        },

    ]


class Development(Config):

    DEBUG = False
    BEP20_NODE = os.environ.get("BEP20_NODE", "https://data-seed-prebsc-1-s1.binance.org:8545")

class Test(Config):

    DEBUG = False
    BEP20_NODE = os.environ.get("BEP20_NODE", "https://data-seed-prebsc-1-s1.binance.org:8545")

class Production(Config):

    DEBUG = True
    BEP20_NODE = os.environ.get("BEP20_NODE", "https://bsc-dataseed.binance.org")



