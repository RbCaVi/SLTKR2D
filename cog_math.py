from pyfunc.assetload import blockinfos, idtoblock as quickidtable,locale
import matplotlib.pyplot as plt
import numpy
import nextcord
import random
import math
import re
from PIL import Image
from nextcord.ext import commands
from pyfunc.lang import lprint
from pyfunc.commanddec import CogCommand
from eval_expr import evaluate,NUM


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @CogCommand("eval")
    async def evalu(self, ctx:commands.Context, *, formulae="3 * ( 1 + 2 )"):
        result=evaluate(formulae)
        #if result[0]!=NUM:
        #    raise Exception('didn\'t output a number')
        await ctx.send(f"{formulae} = {result[1]}")
    
    @CogCommand("plot")
    async def plot(self, ctx:commands.Context, slope:int=3, yinter:int=3, min_:int=-20, max_:int=20):
        xaxis = numpy.arange(min_, max_, 0.1)
        yaxis = []
        for x in xaxis:
            yaxis += [slope*x+yinter]
        plt.plot(xaxis, yaxis)
        showy = f"{slope}x"
        if yinter != 0: showy += ["+",""][yinter<0] + str(yinter)
        plt.savefig("cache/plot.png")
        plt.grid()
        
        await ctx.send(file=nextcord.File("cache/plot.png", filename=f"{showy}.png"))
        plt.close()
    
    # Copied from my old code, should run N (2≤N≤10^9) within 1 sec
    @CogCommand("prime")
    async def prime(self, ctx:commands.Context, n:int=12):
        if n < 0: raise Exception('Negetive Value')
        r = n
        i = 2
        c = {}
        def inc(num):
            lprint(num, end=" ")
            try: c[str(num)]
            except: c[str(num)] = 0
            c[str(num)] += 1
        def handleexpo(expo) -> str:
            cvexp = ''.join(list("⁰¹²³⁴⁵⁶⁷⁸⁹")[int(digit)] for digit in str(expo))
            if cvexp == "¹": return ""
            else: return cvexp
        while i*i<=n:
            if n % i == 0:
                n //= i
                inc(i)
            else:
                i += 1
        inc(n)
            
        await ctx.send(f"{r} = {' * '.join([f'{base}{handleexpo(expo)}' for base, expo in c.items()])}")
        
    # Near Same tested as !prime 
    @CogCommand("factor")
    async def factor(self, ctx:commands.Context, n:int=12):
        r = n
        m = int(math.sqrt(n))
        factor = []
        for i in range(1, m + 1):
            if n % i == 0:
                factor.append(str(i))
        if m * m == n:
            m -= 1
        for i in range(m, 0, -1):
            if n % i == 0:
                factor.append(str(n // i))
        await ctx.send(f"{r} has {len(factor)} factors: \n{', '.join(factor)}")
        
def setup(bot):
	bot.add_cog(Math(bot))