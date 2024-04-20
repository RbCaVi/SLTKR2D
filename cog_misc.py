import nextcord
from nextcord.ext import commands
from pyfunc.commanddec import CogCommand, InteractionCogCommand_Local
from pathlib import Path
import os
import time


class Misc(commands.Cog):
    def __init__(self, bot, branch):
        self.bot = bot
        self.branch = branch
        
    @CogCommand("branch")
    async def branch(self, ctx:commands.Context):
        await ctx.send(f"Current branch is {self.branch}")
        
    @InteractionCogCommand_Local("timestamp")
    async def timestamp(self, 
                     interaction: nextcord.Interaction, 
                     offsetsecond: int = nextcord.SlashOption(required=False, default=0),
                     formating = nextcord.SlashOption(name="formating", required=False, choices=[
                        "Default",
                        "List All",
                        "Short Time",
                        "Long Time",
                        "Short Date",
                        "Long Date",
                        "Short Date/Time",
                        "Long Date/Time",
                        "Relative Time"
                    ], default="Default")):
        formatings = {
                        "Default": "",
                        "Short Time": ":t",
                        "Long Time": ":T",
                        "Short Date": ":d",
                        "Long Date": ":D",
                        "Short Date/Time": ":f",
                        "Long Date/Time": ":F",
                        "Relative Time": ":R"
                    }
        currenttime = int(time.time())-offsetsecond
        if formating == "List All":
            await interaction.response.send_message(
                "\n".join([
                    f"{key} | <t:{currenttime}{item}>" for key, item in formatings.items()
                ])) 
        else:
            await interaction.response.send_message(f"{formating} | <t:{currenttime}{formatings[formating]}>") 
                
    

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

    bot.add_cog(Misc(bot,branch))