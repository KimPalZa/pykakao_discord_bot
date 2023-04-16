from PyKakao import KoGPT
from PyKakao import Karlo
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
TOKEN = '디코토큰'
kakoapi = '카카오 REST API KEY'
GPT = KoGPT(kakoapi)
karlo = Karlo(kakoapi)
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

@bot.command()
async def 질문(message,*,vars):
    print(vars)
    max_tokens = 128
    result = GPT.generate(vars, max_tokens, temperature=0.2)
    print(result)
    await message.channel.send(result['generations'][0]['text'])
    
@bot.command()
async def 이미지(message,*,vars):
    img_dict = karlo.text_to_image(vars, 1)
    img_str = img_dict.get("images")[0].get('image')
    img = karlo.string_to_image(base64_string = img_str, mode = 'RGBA')
    img.save("./original.png")
    file = discord.File("original.png")
    await message.channel.send(file=file)
    
bot.run(TOKEN)
