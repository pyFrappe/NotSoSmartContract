from os import name, path
import discord
from discord import embeds
from discord.ext import commands
from NSSC.contract.contract import NSSC
from .utils import data_type_fixer, del_addr, errorEmbed,embedGenerator, get_addr, get_addr_by_prefix, get_prefixes, loadingEmbed, set_addr, validate_address
import random
import asyncio
from ast import literal_eval
colors =["AQUA","DARK_AQUA","GREEN","DARK_GREEN","BLUE","DARK_BLUE","PURPLE","DARK_PURPLE","LUMINOUS_VIVID_PINK","DARK_VIVID_PINK","GOLD","DARK_GOLD","ORANGE","DARK_ORANGE","RED","DARK_RED","GREY","DARK_GREY","DARKER_GREY","LIGHT_GREY","NAVY","DARK_NAVY","YELLOW"]



class contracts(commands.Cog,description="Commands Related to Contract Interation"):
    def __init__(self, client):
        self.client = client
        self.nssc = NSSC()


    @commands.command(name="call",brief='contract [address] [function] [args]\n [*]Calls Read Functions from Smart Contract', description='Yuck this is a placeholder') # Your command decorator.
    async def call(self, ctx,address,func_name,*args): # ctx is a representation of the 
        user_id = ctx.message.author.id
        long_adr = get_addr_by_prefix(str(user_id),address)
        if long_adr:

            address = long_adr
        
        args = data_type_fixer(list(args))
        address= validate_address(address)
        #LOADING EMBED
        loading_embed = loadingEmbed("Contract Calling Function","Communicating with contract")
        loading_embed.add_field(name="Address",value=f"`{address}`",inline=True)
        loading_embed.add_field(name="Function",value=f"`{func_name}`",inline=True)
        loading_embed.add_field(name="Args",value=f"`{str(args)}`",inline=True)
        loading_embed.add_field(name="OUTPUT",value=f"`Processing...`",inline=True)
        initial_message=await ctx.send(embed=loading_embed)
        data=self.nssc.call_functions(address=address,funcname=func_name,args=args)
        
        #ACTUAL EMBED
        embed= embedGenerator(title="Contract Function Lookup",description="Calling Function")
        embed.set_author(name="Status : Completed",icon_url="https://w7.pngwing.com/pngs/120/161/png-transparent-white-and-green-check-logo-check-mark-emoji-computer-icons-emoticon-tick-angle-text-rectangle.png")
        embed.add_field(name="Address",value=f"`{address}`",inline=True)
        embed.add_field(name="Function",value=f"`{func_name}`",inline=True)
        embed.add_field(name="Args",value=f"`{str(args)}`",inline=True)
        embed.add_field(name="OUTPUT",value=f"`{data}`",inline=True)
        await initial_message.edit(embed=embed)
    
    @commands.command(name="save",brief='save [address] [short_prefix]\n[*]Save Long Eth Address As Short Prefix') # Your command decorator.
    async def save(self, ctx,Address,Short_Prefix): 
        listx=ctx.message.content.split(" ")
        addr= validate_address(Address)
        short_prefix = Short_Prefix
        user_id = ctx.message.author.id
        set_addr(str(user_id),long_prefix=addr,short_prefix=short_prefix)
        embed= embedGenerator(title="Contract Function Lookup",description="Calling Function")
        embed.add_field(name="Long Prefix",value=f"`{addr}`",inline=True)
        embed.add_field(name="Short Prefix",value=f"`{short_prefix}`",inline=True)
        await ctx.send(embed=embed)
    
    @commands.command(name="saved",brief='See your saved addresses.') # Your command decorator.
    async def saved(self, ctx): 
        user_id = ctx.message.author.id
        saved_prefixes = get_addr(str(user_id))
        print(saved_prefixes)
        embed= embedGenerator(title="Saved Addresses",description="List of all the addresses")
        if saved_prefixes:
            for count,prefixes in enumerate(saved_prefixes):
                embed.add_field(name=f"`[{count}]` {saved_prefixes[prefixes]} : `{prefixes}`",value=f"\u200b")
        else:
            embed.add_field(name="No Addresses Saved",value=f"`Save Some Addreses By Using save [long_address] [short term]`")
        await ctx.send(embed=embed)
    
    @commands.command(name="del",brief='Delete your saved addresses.') # Your command decorator.
    async def delete(self, ctx,address): 
        commands = ctx.message.content.split(" ")
        user_id = ctx.message.author.id
        long_adr = get_addr_by_prefix(str(user_id),address)
        if long_adr:
            address = long_adr
        embed= embedGenerator(title="Delete Saved Addresses",description="Delete Addresses")
        de = del_addr(str(user_id),address)
        if de ==None:
            embed.add_field(name="Error",value="The Address is Not Yet Saved On Your Profile")
            await ctx.send(embed=embed)
            return
        embed.add_field(name="Deleted",value=f"Deleted Address `{address}`")
        await ctx.send(embed=embed)

        


    @commands.command(name="owner",brief='owner [address]\n[*]Returns Owner Of An Address') # Your command decorator.
    async def owner(self, ctx,address): 
        user_id = ctx.message.author.id
        long_adr = get_addr_by_prefix(str(user_id),address)

        if long_adr:

            address = long_adr
        address = validate_address(address)
        #LOADING EMBED
        loading_embed = loadingEmbed("Contract Calling Function","Communicating with contract")
        loading_embed.add_field(name="Address",value=f"`{address}`",inline=True)
        loading_embed.add_field(name="Function",value=f"`owner`",inline=True)
        loading_embed.add_field(name="Args",value=f"`[]`",inline=True)
        loading_embed.add_field(name="OUTPUT",value=f"`Fetching...`",inline=True)
        initial_message=await ctx.send(embed=loading_embed)
        data=self.nssc.owner(address)
        embed= embedGenerator(title="Contract Function Lookup",description="Calling Function")
        embed.add_field(name="Address",value=f"`{address}`",inline=True)
        embed.add_field(name="Function",value=f"`owner`",inline=True)
        embed.add_field(name="Args",value=f"`{[]}`",inline=True)
        embed.add_field(name="OUTPUT",value=f"`{data}`",inline=True)
        await initial_message.edit(embed=embed)
    


def setup(client):# Must have a setup function
    client.add_cog(contracts(client)) # Add the class to the cog.

