import json
import logging
import time

import app



def settle():
    """settle"""
    try:
        length = app.bsc_wallet.getPoolLength()
        if length != 0 :
            for index in range(length):
                poolState = app.bsc_wallet.getPoolState(index)
                print(poolState)
                if poolState == 0:
                    # 0 = match
                    result0 = app.bsc_wallet.checkoutSettle(index)
                    if result0:
                        result1, strHash = app.bsc_wallet.settle(index)
                        if result1:
                            logging.error("settle save hash:{}".format(str(strHash)))
                            # Avoid sending transactions too fast
                            time.sleep(10)
    except Exception as e:
        logging.error("settle error:{}".format(str(e)))


def finish():
    """finish"""
    try:
        length = app.bsc_wallet.getPoolLength()
        if length != 0:
            for index in range(length):
                poolState = app.bsc_wallet.getPoolState(index)
                if poolState == 1:
                    # 1 = execetion
                    result0 = app.bsc_wallet.checkoutFinish(index)
                    if result0:
                        result1, strHash = app.bsc_wallet.finish(index)
                        if result1:
                            logging.error("finish save hash:{}".format(str(strHash)))
                            # Avoid sending transactions too fast
                            time.sleep(10)
    except Exception as e:
        logging.error("finish error:{}".format(str(e)))



def liquidate():
    """liquidation"""
    try:
        length = app.bsc_wallet.getPoolLength()
        if length != 0:
            for index in range(length):
                poolState = app.bsc_wallet.getPoolState(index)
                print(poolState)
                if poolState == 1:
                    # 1 = execetion
                    result0 = app.bsc_wallet.checkoutLiquidation(index)
                    if result0:
                        result1, strHash = app.bsc_wallet.liquidate(index)
                        if result1:
                            logging.error("liquidate save hash:{}".format(str(strHash)))
                            # Avoid sending transactions too fast
                            time.sleep(10)
    except Exception as e:
        logging.error("liquidate error:{}".format(str(e)))
