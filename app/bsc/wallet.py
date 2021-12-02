

import logging
import os

from eth_account import Account
from web3 import Web3
from web3._utils.encoding import to_hex
from web3.middleware import geth_poa_middleware
from app.abi.pledgeContractAbi import pledgeAbi


class BscWallet(object):
    """BEP20钱包节点"""

    PLEDGE_CONTRACT_ADDRESS = os.environ.get('PLEDGE_CONTRACT_ADDRESS','')
    PLEDGE_CONTRACT_ABI = pledgeAbi
    # 网络ID
    CHAIN_ID = int(os.environ.get("BEP20_CHAIN_ID", 97))  # 56
    # 管理账户地址
    FINANCE_ADDRESS = "0x0ff66Eb23C511ABd86fC676CE025Ca12caB2d5d4"
    FINANCE_ADDRESS_SERECT = ""

    # GAS LIMIT
    GAS_LIMIT = int(os.environ.get('BEP20_GAS_LIMIT', 200000))
    GAS_PRICE_LIMIT = int(os.environ.get('BEP20_GAS_PRICE_LIMIT', 50000000000))

    def gas_price(self):
        """返回gasPrice价格"""
        return self.w3.eth.gasPrice

    def init_app(self, app):
        """初始化节点"""
        self.wallet_url = app.config.get('BEP20_NODE')
        self.w3 = Web3(Web3.HTTPProvider(self.wallet_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        if not self.w3.isConnected():
            logging.error('Connect BEP20 wallet node fial')
        try:
            self.token_contract = self.w3.eth.contract(address=self.PLEDGE_CONTRACT_ADDRESS,
                                                   abi=self.PLEDGE_CONTRACT_ABI)
        except Exception as e:
            logging.error("get pledge contract error:{}".format(str(e)))

    def is_connected(self):
        """节点是否链接"""
        return self.w3.isConnected()

    def is_syncing(self):
        """节点是否在同步中"""
        return self.w3.eth.syncing

    def get_nonce(self, address):
        """获取账户nonce值"""
        nonce = self.w3.eth.getTransactionCount(address, 'pending')
        return nonce

    def settle(self, private, gasPrice, gasLimit):
        """检查借贷双方，是否满足匹配条件"""
        account = Account.privateKeyToAccount(private)
        address = account.address
        nonce = self.w3.eth.getTransactionCount(address, 'pending')
        gasLimit = int(gasLimit)
        gasPrice = int(gasPrice)
        payload = {
            'value': 0,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
            'from': address,
        }

        try:
            unicorn_txn = self.token_contract.functions.settle().buildTransaction(payload)
            signed = account.signTransaction(unicorn_txn)
            tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
            return True, to_hex(tx_hash)
        except Exception as e:
            logging.error("settle is fail:{}".format(e))
            return False, ''

    def finish(self,private, gasPrice, gasLimit):
        """借贷双方执行期到期，到期以后兑进行兑换还债务"""
        account = Account.privateKeyToAccount(private)
        address = account.address
        nonce = self.w3.eth.getTransactionCount(address, 'pending')
        gasLimit = int(gasLimit)
        gasPrice = int(gasPrice)
        payload = {
            'value': 0,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
            'from': address,
        }
        try:
            unicorn_txn = self.token_contract.functions.finish().buildTransaction(payload)
            signed = account.signTransaction(unicorn_txn)
            tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
            return True, to_hex(tx_hash)
        except Exception as e:
            logging.error("finish is fail:{}".format(e))
            return False, ''

    def checkoutLiquidate(self, private, gasPrice, gasLimit):
        """清算操作"""
        account = Account.privateKeyToAccount(private)
        address = account.address
        nonce = self.w3.eth.getTransactionCount(address, 'pending')
        gasLimit = int(gasLimit)
        gasPrice = int(gasPrice)
        payload = {
            'value': 0,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
            'from': address,
        }
        try:
            unicorn_txn = self.token_contract.functions.checkoutLiquidate().buildTransaction(payload)
            signed = account.signTransaction(unicorn_txn)
            tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
            return True, to_hex(tx_hash)
        except Exception as e:
            logging.error("checkoutLiquidate is fail:{}".format(e))
            return False, ''


if __name__ == '__main__':
    pass

