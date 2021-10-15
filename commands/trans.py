from os import name
import discord
from discord import embeds
from discord.ext import commands
from NSSC.trans.trans import Trans
from .utils import embedGenerator, get_addr, get_addr_by_prefix, get_prefixes, loadingEmbed,validate_address
import random
import asyncio



class TransC(commands.Cog,description="Commands Related to Transactions"):
    def __init__(self, client):
        self.client = client
        self.trans = Trans()


    @commands.command(name="balance",brief='balance [address]\n [*]Checks balance of given ETH Address', description='Get ETH Bal and USD Worth of Wallet') # Your command decorator.
    async def balance(self, ctx,address): # ctx is a representation of the 
        embed = embedGenerator(title="Balance Lookup",description="Lookup Balance of any ETH Addr")
        user_id = ctx.message.author.id
        long_adr = get_addr_by_prefix(str(user_id),address)
        if long_adr:
            address = long_adr
        address= validate_address(address)
        #LOADING
        embed=loadingEmbed("Checking Balance Of Address","Please Be Patient")
        embed.add_field(name="Address",value=f"`{address}`")
        
        embed.add_field(name="Balance",value=f"`Fetching....`")
        embed.add_field(name="Worth",value=f"`Fetching....`")

        inital_msg = await ctx.send(embed=embed)
        
        embed=embedGenerator(title="Balance Lookup",description="Lookup Balance of any ETH Addr")
        embed.add_field(name="Address",value=f"`{address}`")
        data = self.trans.balanceOf(address)
        embed.add_field(name="Balance",value=f"`{data['strbal']}`")
        embed.add_field(name="Worth",value=f"`{data['worth']} USD`")
        await inital_msg.edit(embed=embed)

def setup(client):# Must have a setup function
    client.add_cog(TransC(client)) # Add the class to the cog.