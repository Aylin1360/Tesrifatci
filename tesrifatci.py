import discord
from discord.ext import commands
import config

client = commands.Bot(command_prefix = '_')

@client.event
async def on_ready():
    print('Selam! Teşrifatçı geldi, biletleri kesiyorum.')

@client.command(aliases=['vizyonda'])
async def vizyon(ctx):
    await ctx.send('Hello')

import random
@client.command()
async def hakan(ctx, *, questions):
    responses = ['Benimle uğraşma Hakan!',
                  'Ne var Hakan?',  
                  'Yine noldu Hakan?',
                  'Hakan, botun mu var burda çağırıp duruyorsun?',
                  'Hakan, git Alple uğraş.',
                  'Dükkanı kapattık Hakan.',
                  'Mesajını bırak Hakan, mesai saatleri içerisinde döneriz.']
    await ctx.send(random.choice(responses))

client.run(config.KEY)