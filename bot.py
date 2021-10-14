import discord
from discord.ext import commands
from commands.utils import embedGenerator,get_prefixes
from dotenv import load_dotenv
import os 
load_dotenv()
from pretty_help import DefaultMenu, PrettyHelp
menu = DefaultMenu(page_left="⬅️", page_right="➡️", active_time=5)

# Custom ending note
ending_note = "The ending note from {ctx.bot.user.name}\nFor command {help.clean_prefix}{help.invoked_with}"

activity = discord.Game(name=">help")

bot = commands.Bot(command_prefix= get_prefixes, description="Not So Smart Contract is Not So Smart Contract Bot.",activity=activity, status=discord.Status.dnd)



cog_files = ['commands.contract','commands.settings']

for cog_file in cog_files: 
    bot.load_extension(cog_file) 
    print("%s has loaded." % cog_file) 


bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note)

bot.run(os.environ['discord_token'])