import discord
from discord import embeds
from discord import message
from discord.ext import commands
from NSSC.contract.contract import NSSC
from .utils import errorEmbed,embedGenerator,set_prefixes
import random



class settings(commands.Cog,description="Chnage Prefix , Manage Bot and Many More"):
    def __init__(self, client):
        self.client = client
       


    @commands.command(name="prefix",brief='prefix [new_prefix]\n [*]Change Prefix For Server') # Your command decorator.
    @commands.has_permissions(manage_channels=True) 
    async def call(self, ctx): # ctx is a representation of the 
        args = ctx.message.content.split(" ")
        if len(args) < 2:
            await ctx.send(embed=errorEmbed("Invalid Command, Please Review It >contract [address] [funcname] [args]"))
            return
        new_prefix = args[1]
        guild_id = ctx.guild.id
        set_prefixes(guild_id,new_prefix)
        embed= embedGenerator(title="Contract Function Lookup",description="Calling Function")
        embed.add_field(name="New Prefix",value=f"`{new_prefix}`",inline=True)
        embed.add_field(name="Guild ID",value=f"`{guild_id}`",inline=True)
        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""
        if "is not found" in (str(error)):
            return
        embed=errorEmbed(error)
        
        await ctx.send(embed=embed)

    
   



def setup(client):# Must have a setup function
    client.add_cog(settings(client)) # Add the class to the cog.

