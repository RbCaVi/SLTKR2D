from nextcord.ext import commands
from pyfunc.commanddec import CogCommand
from pathlib import Path
import subprocess
import sys

class Branch(commands.Cog):
    def __init__(self, bot, branch:str):
        self.bot = bot
        self.branch = branch
        self.subs=[]
        
    @CogCommand("branch")
    async def branch(self, ctx:commands.Context):
        self.subs.append(subprocess.Popen([sys.executable,'main.py']))
        await ctx.send(f"Current branch is {self.branch}")
        
    @CogCommand("delbranch")
    async def delbranch(self, ctx:commands.Context):
        for sub in self.subs:
            sub.kill()
            break # at most 1
        await ctx.send(f"Current branch is {self.branch}")
        
def setup(bot):
    # https://stackoverflow.com/a/62724213
    head_dir = Path(".") / ".git" / "HEAD"
    with head_dir.open("r", encoding="utf-8") as f: content = f.read().splitlines()

    for line in content:
        if line[0:4] == "ref:":
            branch=line.partition("refs/heads/")[2]
            break

    # https://stackoverflow.com/a/77686288
    #process = subprocess.Popen(["git", "branch", "--show-current"], stdout=subprocess.PIPE)
    #branch_name, branch_error = process.communicate()

    bot.add_cog(Branch(bot,branch))