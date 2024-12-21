import discord
from discord.ext import commands
from model import get_class
import os,random 
import requests
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print(f"te haz logueado como {bot.user}")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            file_name = attachments.filename
            file_url = attachments.url
            await attachments.save(f"./{attachments.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5",labels_path="./labels.txt", image_path= f'./{attachments.filename}'))
    else:
        await ctx.send("No haz subido una imagen")

bot.run("MTI1MTM0MTYwMjU0NzQzMzUzMw.GNI9Pb.SMLEDXeKmqeSCEdRDdrpFsAZsJp-Loj2F-jffI")