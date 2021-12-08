import json
import logging
import time

import app



def settle():
    """settle"""
    try:
        length = app.bsc_wallet.getPoolLength()
        if length != 0 :
            for index in length:
                result0 = app.bsc_wallet.checkoutSettle(index)
                if result0:
                    result1, strHash = app.bsc_wallet.settle(index)
                    if result1:
                        # Avoid sending transactions too fast
                        time.sleep(10)
    except Exception as e:
        logging.error("settle error:{}".format(str(e)))


def finish():
    """finish"""
    try:
        length = app.bsc_wallet.getPoolLength()
        if length != 0:
            for index in length:
                result0 = app.bsc_wallet.checkoutFinish(index)
                if result0:
                    result1, strHash = app.bsc_wallet.finish(index)
                    if result1:
                        # Avoid sending transactions too fast
                        time.sleep(5)
    except Exception as e:
        logging.error("finish error:{}".format(str(e)))



def liquidate():
    """liquidation"""
    try:
        length = app.bsc_wallet.getPoolLength()
        if length != 0:
            for index in length:
                result0 = app.bsc_wallet.checkoutLiquidation(index)
                if result0:
                    result1, strHash = app.bsc_wallet.liquidate(index)
                    if result1:
                        # Avoid sending transactions too fast
                        time.sleep(5)
    except Exception as e:
        logging.error("finish error:{}".format(str(e)))
