# Server promotion commands
import discord
from discord.ext import commands
from util import ftpConnect
from api import steamAPI

def searchDelete(filename: str, steamid: str):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            if (str(steamid) not in line.strip("\n")) and (line.strip("\n") != ""):
                f.write(line)

def roleString(steamid: int):
    name = steamAPI.getName(steamid)
    string = f"{name}={steamid}"
    return string

# 0 = none, 1 = mod, 2 = admin
def roleRemove(steamid: int, perms: int):
    x = ftpConnect.ftpConnect("ftp.nc1.eu")
    x.connect()
    x.login("username", "password")
    x.path("BW06224/Blackwake")
    x.downloadFile("Admin.txt")
    searchDelete("Admin.txt", steamid)
    if perms == 2:
        x.editFile("Admin.txt", roleString(steamid))
    x.uploadFile("Admin.txt")
    x.deleteFile("Admin.txt")
    x.downloadFile("Mod.txt")
    searchDelete("Mod.txt", steamid)
    if perms == 1:
        x.editFile("Mod.txt", roleString(steamid))
    x.uploadFile("Mod.txt")
    x.deleteFile("Mod.txt")
    x.kill()

class Promote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # promote (group)
    @commands.group(name="promote", description="Promote and demote steam users on Blackwake server.", usage="p <subcommand> <steamid>", aliases=['p'])
    @commands.cooldown(1, 5, commands.BucketType.default)
    async def promote(self, ctx):
        pass

    # definition (subcommand)
    @promote.command(name="admin", description="Admin privileges in Blackwake.", usage="p a <steamid>", aliases=['a'])
    async def admin(self, ctx, steamid: int):
        try:
            await ctx.message.add_reaction("<a:loading:700208681685352479>")
            roleRemove(steamid, 2)
            await ctx.message.remove_reaction("<a:loading:700208681685352479>", self.bot.user)
            await ctx.message.add_reaction("✅")
        except:
            await ctx.message.remove_reaction("<a:loading:700208681685352479>", self.bot.user)
            await ctx.message.add_reaction("❌")

    # definition (subcommand)
    @promote.command(name="mod", description="Mod privileges in Blackwake.", usage="p m <steamid>", aliases=['m'])
    async def mod(self, ctx, steamid: int):
        try:
            await ctx.message.add_reaction("<a:loading:700208681685352479>")
            roleRemove(steamid, 1)
            await ctx.message.remove_reaction("<a:loading:700208681685352479>", self.bot.user)
            await ctx.message.add_reaction("✅")
        except:
            await ctx.message.remove_reaction("<a:loading:700208681685352479>", self.bot.user)
            await ctx.message.add_reaction("❌")

    # definition (subcommand)
    @promote.command(name="normal", description="Normal privileges in Blackwake.", usage="p n <steamid>", aliases=['n'])
    async def normal(self, ctx, steamid: int):
        try:
            await ctx.message.add_reaction("<a:loading:700208681685352479>")
            roleRemove(steamid, 0)
            await ctx.message.remove_reaction("<a:loading:700208681685352479>", self.bot.user)
            await ctx.message.add_reaction("✅")
        except:
            await ctx.message.remove_reaction("<a:loading:700208681685352479>", self.bot.user)
            await ctx.message.add_reaction("❌")

def setup(bot):
    bot.add_cog(Promote(bot))