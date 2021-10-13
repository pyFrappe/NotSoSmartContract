import NSSC
from NSSC.contract import contract
NSSC = contract.NSSC()

abi = NSSC.get_abi("0x1a92f7381b9f03921564a437210bb9396471050c")
read_functions = NSSC.write_functions(abi)
print(NSSC.call_functions(address="0x1a92f7381b9f03921564a437210bb9396471050c",funcname="balanceOf",args=["0x4265de963cdd60629d03FEE2cd3285e6d5ff6015"]))