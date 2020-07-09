# loads cogs
import os
from util import logger

def load(bot):
    for cog in os.listdir('./cogs'):
        if cog.endswith('.py'):
            try:
                bot.load_extension(f'cogs.{cog[:-3]}')
                logger.log(f"{cog} --> LOADED")
            except Exception as e:
                logger.log(f"{cog} --> FAILED")
                logger.log(e)