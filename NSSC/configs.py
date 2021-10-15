from etherscan import Etherscan
from web3 import Web3
import os


eth = Etherscan(os.environ['etherscan_api']) 
infura_key = os.environ['infura_key']
web3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{infura_key}"))