import nextcord
import random
from PIL import Image
from nextcord.ext import commands
from assetload import blockinfos, idtoblock as quickidtable
# 0~101, win = 103
# 10 day
# each day 8 chance
# cd 2 hr
# each chance = 0.97%, each day = 7.77%, whole time = 77.7%
class Fest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.cooldown(1, 7200, commands.BucketType.user)
    @commands.command(name="lunar-new-year", description="Refer to the announcement.", aliases=[])
    async def __lny(self, ctx):
        RNG = random.randint(0, 102)
        print(ctx.author, RNG)
        if RNG != 102:
            key = quickidtable[RNG]
            key = "air" if key=="NIC" else key
            embed = nextcord.Embed()
            img = Image.open("assets/block_zoo.png")
            icox, icoy = blockinfos[key]["iconcoord"]
            img = img.crop((16*icox, 16*icoy, 16*(icox+1), 16*(icoy+1))).resize((128, 128), Image.NEAREST)
            img.save("sed.png")
            embed.title = "Mission Failed, We'll get them next time."
            embed.description = f"Here's a {key.replace("_", " ")} to calm you :)"
            embed.set_image(url="attachment://sed.png")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(file=nextcord.File("sed.png", filename="sed.png"), embed=embed)
            return
        else: #HOLY
            print(ctx.author)
            embed = nextcord.Embed()
            embed.title = "Legit?"
            embed.set_image(url="attachment://t.png")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(file=nextcord.File("assets/fest_lny/b.png", filename="t.png"), embed=embed)

    @commands.Cog.listener()
    async def on_command_error(cog, ctx, error):
        print(error)
        if isinstance(error, commands.CommandOnCooldown):
            print("ERR", cog)
            await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)}s.')
def setup(bot):
	bot.add_cog(Fest(bot))