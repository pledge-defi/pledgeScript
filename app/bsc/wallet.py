

import logging
import os

from eth_account import Account
from web3 import Web3
from web3._utils.encoding import to_hex
from web3.middleware import geth_poa_middleware
from app.abi.pledgeContractAbi import pledgeAbi


class BscWallet(object):
    """Bep20 wallet node"""

    PLEDGE_CONTRACT_ADDRESS = os.environ.get('PLEDGE_CONTRACT_ADDRESS','0xe4E98E56B855cf3D1D9693FBAaC3A5e6fDCB53f5')
    PLEDGE_CONTRACT_ABI = pledgeAbi
    # network id
    CHAIN_ID = int(os.environ.get("BEP20_CHAIN_ID", 97))  # 56
    # Manage account address
    FINANCE_ADDRESS = "0x0ff66Eb23C511ABd86fC676CE025Ca12caB2d5d4"
    FINANCE_ADDRESS_SERECT = ""

    # GAS LIMIT
    GAS_LIMIT = int(os.environ.get('BEP20_GAS_LIMIT', 200000))
    GAS_PRICE_LIMIT = int(os.environ.get('BEP20_GAS_PRICE_LIMIT', 50000000000))

    def gas_price(self):
        """gas Price"""
        return self.w3.eth.gasPrice

    def init_app(self, app):
        """node init"""
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
        """the node is linked"""
        return self.w3.isConnected()

    def is_syncing(self):
        """Is the node in sync"""
        return self.w3.eth.syncing

    def get_nonce(self, address):
        """Get account nonce value"""
        nonce = self.w3.eth.getTransactionCount(address, 'pending')
        return nonce

    def getPoolLength(self):
        """get pool lenght"""
        length = self.token_contract.functions.poolLength().call()
        return length

    def checkoutSettle(self, index):
        """checkut settle"""
        length = self.getPoolLength()
        if index <= length:
            result = self.token_contract.functions.checkoutSettle(index).call()
            return result
        else:
            return False

    def settle(self, index):
        """checkout match"""
        account = Account.privateKeyToAccount(self.FINANCE_ADDRESS_SERECT)
        address = account.address
        nonce = self.w3.eth.getTransactionCount(address, 'pending')
        gasLimit = int(self.GAS_LIMIT)
        gasPrice = int(self.GAS_PRICE_LIMIT)
        payload = {
            'value': 0,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
            'from': address,
        }
        try:
            unicorn_txn = self.token_contract.functions.settle(index).buildTransaction(payload)
            signed = account.signTransaction(unicorn_txn)
            tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
            return True, to_hex(tx_hash)
        except Exception as e:
            logging.error("settle is fail:{}".format(e))
            return False, ''

    def checkoutFinish(self, index):
        """checkout finish"""
        legth = self.getPoolLength()
        if index <= legth:
            result = self.token_contract.functions.checkoutFinish(index).call()
            return result
        else:
            return False

    def finish(self, index):
        """checkout finish"""
        account = Account.privateKeyToAccount(self.FINANCE_ADDRESS_SERECT)
        address = account.address
        nonce = self.w3.eth.getTransactionCount(address, 'pending')
        gasLimit = int(self.GAS_LIMIT)
        gasPrice = int(self.GAS_PRICE_LIMIT)
        payload = {
            'value': 0,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
            'from': address,
        }
        try:
            unicorn_txn = self.token_contract.functions.finish(index).buildTransaction(payload)
            signed = account.signTransaction(unicorn_txn)
            tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
            return True, to_hex(tx_hash)
        except Exception as e:
            logging.error("finish is fail:{}".format(e))
            return False, ''

    def checkoutLiquidation(self, index):
        """checkout liquidation"""
        leght = self.getPoolLength()
        if index <= leght:
            result = self.token_contract.functions.checkoutLiquidate(index).call()
            return result
        else:
            return False

    def liquidate(self, index):
        """liquidation"""
        account = Account.privateKeyToAccount(self.FINANCE_ADDRESS_SERECT)
        address = account.address
        nonce = self.w3.eth.getTransactionCount(address, 'pending')
        gasLimit = int(self.GAS_LIMIT)
        gasPrice = int(self.GAS_PRICE_LIMIT)
        payload = {
            'value': 0,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
            'from': address,
        }
        try:
            unicorn_txn = self.token_contract.functions.liquidate(index).buildTransaction(payload)
            signed = account.signTransaction(unicorn_txn)
            tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction)
            return True, to_hex(tx_hash)
        except Exception as e:
            logging.error("checkoutLiquidate is fail:{}".format(e))
            return False, ''


if __name__ == '__main__':
    pass

