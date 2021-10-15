from logging import raiseExceptions
import requests
import os
from dotenv import load_dotenv
from etherscan import Etherscan
import json
from web3 import Web3
from functools import lru_cache
from ..configs import *

load_dotenv()

class Trans:
    def __init__(self) -> None:
        self.eth = eth
        self.infura_key =infura_key
        self.web3 = web3
        self.rinkeby = ''
        pass

    def balanceOf(self,address):
        wei= self.web3.eth.getBalance(address)
        humanbal = float(self.web3.fromWei(wei,'ether'))
        strbal = str(humanbal)[:6] + " ETH"
        rates = (self.get_rates())
        worth = str(humanbal*float(rates["ethusd"]))[:6]
        return {"eth":humanbal,"worth":worth,"strbal":strbal}
    
    def get_rates(self):
        return eth.get_eth_last_price()

