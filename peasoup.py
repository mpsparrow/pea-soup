'''
Bot Name: pea soup
Creator: Matthew (mattthetechguy)
Version: 0.1
Date Created: April 15, 2020
'''
import asyncio
import discord
import cogLoader
from discord.ext import commands, tasks
from util import configParse, logger
from cogs import leaderboard
from api import ipLocation, steamAPI

bot = commands.Bot(command_prefix=configParse.defaultPrefix())

# runs on startup
@bot.event
async def on_ready():
    logger.log("Loading...")
    cogLoader.load(bot)
    logger.log("Started!")
    logger.log("Starting background tasks...")
    leaderboardUpdate.start()
    logger.log("Background tasks started!")

# simple ping command
@bot.command(name='ping', description='pings bot', usage='ping')
async def ping(ctx):
    await ctx.send("pong!")

@tasks.loop(seconds=30.0)
async def leaderboardUpdate():
    logger.log("Leaderboard updater task")
    servers = steamAPI.getServers()
    logger.log(servers)
    '''
    channel = self.bot.get_channel(700501891150381106)
    for i in servers:
        logger.log("1")
        '''

# starts bot
bot.run(configParse.token())