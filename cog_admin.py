import glob
import os
import nextcord
from nextcord.ext import commands
from lang import evl
from commanddec import CogCommand

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @CogCommand("viewcog")
    async def viewcog(self,ctx):
        embed = nextcord.Embed()
        embed.description = ""
        for cog_name in glob.glob("cog_*.py"):
            print([dir(o) for i, o in self.bot.cogs.items()])
            print([o.__cog_name__ for i, o in self.bot.cogs.items()])
            embed.description += f"| {cog_name[:-3]} \n"
        await ctx.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @CogCommand("loadcog")
    async def loadcog(self,ctx, tar):
        try:
            self.bot.load_extension("cog_"+tar)
            await ctx.send("LOADED "+"cog_"+tar+".py")
        except commands.errors.ExtensionAlreadyLoaded:
            await ctx.send("cog_"+tar+".py is already loaded.")
        except commands.errors.ExtensionNotFound:
            await ctx.send("cog_"+tar+".py not found.")
            
    @commands.has_permissions(administrator=True)
    @CogCommand("unloadcog")
    async def unloadcog(self,ctx, tar):
        try:
            if tar == "cog_admin":
                await ctx.send("You can't unload cog_admin!") # prevent softlock
                return
            self.bot.unload_extension("cog_"+tar)
            await ctx.send("UNLOADED "+"cog_"+tar+".py")
        except commands.errors.ExtensionAlreadyLoaded:
            await ctx.send("cog_"+tar+".py is already unloaded.")
        except commands.errors.ExtensionNotFound:
            await ctx.send("cog_"+tar+".py not found.")
            
    @commands.has_permissions(administrator=True)
    @CogCommand("reloadcog")
    async def reloadcog(self,ctx, tar):
        try:
            self.bot.unload_extension("cog_"+tar)
            self.bot.load_extension("cog_"+tar)
            await ctx.send("RELOADED "+"cog_"+tar+".py")
        except commands.errors.ExtensionNotFound:
            await ctx.send("cog_"+tar+".py not found.")    
    
    @commands.has_permissions(administrator=True)
    @CogCommand("deletelog")
    async def delog(self, ctx):
        for cachef in glob.glob("cache/log/cache-??-??-????.txt"):
            os.remove(cachef)
        await ctx.send("Done.")

            
    
def setup(bot):
	bot.add_cog(Admin(bot))