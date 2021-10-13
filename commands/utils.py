import re
import discord
from discord import embeds
import random
import json
import os

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


def get_prefixes(client,message):
    if os.path.isfile('prefixes.json'):
        with open('prefixes.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
            prefixes = json.load(f) #load the json as prefixes
        return prefixes[str(message.guild.id)] #recieve the prefix for the guild id given
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
        if address in list(datas):
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
        
        
