# leaderboard
import asyncio
import discord
from discord.ext import commands, tasks
from util import logger
from api import steamAPI

class leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(leaderboard(bot))