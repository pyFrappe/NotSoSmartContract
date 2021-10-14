from logging import raiseExceptions
import requests
import os
from dotenv import load_dotenv
from etherscan import Etherscan
import json
from web3 import Web3
from functools import lru_cache


load_dotenv()

class NSSC:
    def __init__(self) -> None:
        self.eth = Etherscan(os.environ['etherscan_api']) 
        self.infura_key = os.environ['infura_key']
        self.web3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{self.infura_key}"))
        self.rinkeby = ''
        pass
    
    @lru_cache(maxsize=None)
    def get_abi(self,address):
        data= self.eth.get_contract_abi(address)
       
        return json.loads(data)
    
    def validate_address(self,addr):
        return (Web3.toChecksumAddress(addr))
    
    def read_functions(self,abi):
        read_functions =[]
        for functions in abi:
            if functions["type"] =="function" and functions["stateMutability"] == "view":
                read_functions.append(functions)
        return read_functions
    
    def write_functions(self,abi):
        write_functions =[]
        for functions in abi:
            if functions["type"] =="function" and functions["stateMutability"] != "view":
                write_functions.append(functions)
        return write_functions
    
    def get_function_details(self,abi,funcname):
        to_return = None
        for functions in abi:
            if functions["type"] =="function" and functions["name"] == funcname:
                to_return=functions
                break
        if to_return == None:
            raise Exception("Function Doesnt Exist")
        return to_return
    
    def actual_address(self,address):
        try:
            return (Web3.toChecksumAddress(address))
        except Exception:
            raise Exception("Unable to Verify Address")

    def call_functions(self,address,funcname,args=[]):
        self.address = address

        abi = self.get_abi(self.address)
        
        func_details = self.get_function_details(abi,funcname)
        if func_details["stateMutability"] != "view":
            raise Exception("Cannot Execute Write Functions")

        if len(func_details["inputs"]) != len(args):
            raise Exception("Invalid Number of Arguments")

        self.contract  = self.web3.eth.contract(address=self.address, abi=abi)
        if not args:
            string = f"self.contract.functions.{funcname}().call()"
        else:
            string =f"self.contract.functions.{funcname}('{','.join(args)}').call()"
        return eval(string)

    def owner(self,address):
        self.address =(Web3.toChecksumAddress(address))
        abi = self.get_abi(self.address)
        self.contract  = self.web3.eth.contract(address=self.address, abi=abi)
        return self.contract.functions.owner().call()
        



    