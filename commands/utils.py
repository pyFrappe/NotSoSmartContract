import re
import discord
from discord import embeds
import random
import json
import os
from web3 import Web3
from ast import literal_eval

footer ={
    "text":"Powered By NSSC | https://discord.gg/ZqAjfm5Zeb "
}



def errorEmbed(error):
    randcolor = random.randint(0, 0xffffff)
    embed= discord.Embed(title="Command Error",description="Error Occured While Executing Command",colour=randcolor)
    embed.add_field(name="Error Message",value=f"`{str(error)}`")
    embed.set_footer(text=footer["text"])
    return embed

def embedGenerator(title,description):
    randcolor = random.randint(0, 0xffffff)
    embed= discord.Embed(title=title,description=description,colour=randcolor)
    embed.set_footer(text=footer["text"])
    return embed

def loadingEmbed(title,description):
    randcolor = random.randint(0, 0xffffff)
    embed= embedGenerator(title=title,description=description)
    embed.set_author(name="Status :Updating",icon_url="https://www.costcoauto.com/save/images/ajax-loading.gif")
    return embed

def validate_address(addr):
    try:
        return (Web3.toChecksumAddress(addr))
    except Exception:
        raise Exception("Invalid Address !")

def get_prefixes(client,message):
    if os.path.isfile('prefixes.json'):
        with open('prefixes.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
            prefixes = json.load(f) #load the json as prefixes
        try:
            return prefixes[str(message.guild.id)] #recieve the prefix for the guild id given
        except AttributeError:
            return ">"
    with open("prefixes.json",'w')as f:
        json.dump({"897093479887405056":">"},f,indent=4)


def set_prefixes(guild_id,prefix):
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild_id)] = prefix#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater


def get_addr(user_id):
    if os.path.isfile('addr.json'):
        with open('addr.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
            addresses = json.load(f) #load the json as prefixes
        if user_id in addresses:
            return addresses[user_id]
    return None

def set_addr(user_id,long_prefix,short_prefix):
    addresses ={}
    if os.path.isfile('addr.json'):
        
        addresses = json.load(open('addr.json')) #load the json as prefixes
    
    if (user_id) in list(addresses):
        
        
        addresses[user_id][long_prefix]=short_prefix
    else:
        addresses[user_id] = {long_prefix:short_prefix}
    with open('addr.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(addresses, f, indent=4) #the indent is to make everything look a bit neater
    return None

def del_addr(user_id,address):
    datas = get_addr(user_id)
    existing_data = json.load(open('addr.json')) #load the json as prefixes
    
    if datas:
        print(list(datas),address)
        if address in list(datas.keys()):
            print("FOUND")
            datas.pop(address, None)
            existing_data[user_id] = datas
            with open('addr.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
                json.dump(existing_data, f, indent=4) #the indent is to make everything look a bit neater
            return True
    

    return None

def get_addr_by_prefix(client_id,addr):
    saved_prefixes = get_addr(client_id)
    saved_prefix_values = []
    if saved_prefixes != None:
        saved_prefix_values = list(saved_prefixes.values())
    if addr in saved_prefix_values:
        addr_index=saved_prefix_values.index(addr)
        address= list(saved_prefixes)[addr_index]
        return address
    return None
        
        

def data_type_fixer(args):
    argu=[]
    for arg in list(args):
        if len(arg) !=42:
            argu.append(literal_eval(arg))
        else:
            argu.append(arg)
    return argu

