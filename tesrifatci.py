import discord
from discord.ext import commands

from tmdbv3api import TMDb
from tmdbv3api import Movie

import asyncio
from aio_timers import Timer

import config

client = commands.Bot(command_prefix = '%')
tmdb = TMDb()

tmdb.api_key = "61a0cf5912e4a1d5368cf9b4871e0b46" #config.API_KEY
tmdb.language = 'en'
tmdb.debug = True

movie = Movie()

@client.event
async def on_ready():
    print('Selam! Teşrifatçı geldi, biletleri kesiyorum.')


@client.command
async def help(ctx):  
    await ctx.send("Vizyonu belirlemek için %vizyon \nGösterim saati için %gösterim {time} \nFilm arası için %ara {time} \nHakan %hakan {caption}")

@client.command(aliases=['vizyonda'])
async def vizyon(ctx, *, film):
    search = movie.search(film)
    result = ""
    for res in search:
        result += "Bugün Vizyonda: " + res.title + "\n" + str(res.release_date) + "\n" + res.overview + "\n" + str(res.vote_average) 
        break
    await ctx.send(result)
    await ctx.send("İyi Seyirler!")
  

@client.command()
async def gösterim(ctx, time: int):
    await ctx.send(f"{ctx.guild.default_role} Filmimiz Cinefakirium'da başlamak üzeredir: " + str(time) + " dk!")
    def check(message):
        return message.channel == ctx.channel and message.author == ctx.author and message.content.lower() == "cancel"
    try:
        m = await client.wait_for("message", check=check, timeout=time*60)
        await ctx.send("Countdown cancelled")
    except asyncio.TimeoutError:
        await ctx.send(f"{ctx.guild.default_role} Filmimiz Cinefakirium'da gösterimde!")

@client.command()
async def ara(ctx, time: int):
    await ctx.send(f"{ctx.guild.default_role} Film arası! " + str(time) + " dk!")
    def check(message):
        return message.channel == ctx.channel and message.author == ctx.author and message.content.lower() == "cancel"
    try:
        m = await client.wait_for("message", check=check, timeout=time*60)
        await ctx.send("Countdown cancelled")
    except asyncio.TimeoutError:
        await ctx.send(f"{ctx.guild.default_role} Filmimiz Cinefakirium'da devam ediyor!")


import random
@client.command()
async def hakan(ctx, *, questions):
    responses = ['Benimle uğraşma Hakan!',
                  'Ne var Hakan?',  
                  'Yine noldu Hakan?',
                  'Hakan, botun mu var burda çağırıp duruyorsun!',
                  'Hakan, git Alple uğraş.',
                  'Dükkanı kapattık Hakan.',
                  'Mesajını bırak Hakan, mesai saatleri içerisinde döneriz.']
    await ctx.send(random.choice(responses))

#client.run(config.KEY)
client.run("NzkyNzY0MDgwNjQ4NjE3OTg0.X-idFQ.nQHJsA_gF3dutsq_3CAD3Ygzxr0")


