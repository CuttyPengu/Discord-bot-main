

         
import hcskr

from discord.ext import commands
from discord.utils import get
import pytz
import datetime
import discord
import asyncio

from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import nest_asyncio
nest_asyncio.apply()

client = discord.Client()

bot = commands.Bot(command_prefix='!')



token = "ODI4NTAzNzY0NDA2MzcwMzE1.YGqiQg.VWKEcRdq11aC2O1BprR5IpP-8Sg"







@client.event
async def on_ready():
    print(client.user.name)
    print("Bot complete")
    game = discord.Game("!도움말")
    await client.change_presence (status=discord.Status.online, activity=game)






@client.event
async def on_message(message):
    if message.content.startswith('!자가진단 하자 '):
          message.content = message.content.replace("!자가진단 하자 ","")
          messagesplit = message.content.split(",")
          await message.delete()   
         
          
          name = (messagesplit[0])
          birth = (messagesplit[1])
          region = (messagesplit[2])
          school = (messagesplit[3])
          level = (messagesplit[4])
          password = (messagesplit[5])
          data = hcskr.selfcheck(name,birth,region,school,level,password)    
                                  
          await message.channel.send(data['message'])


          
          
          

@client.event
async def on_message(message):
    if message.content == ('!도움말'):
        embed = discord.Embed(title="자가진단하는법!", description="명령어",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name="명령어", value="!자가진단 하자 이름,생년월일,지역,학교이름,학교종류,비밀번호(숫자4자리)", inline=False)
        embed.add_field(name="예시", value="!자가진단 하자 조펭구,070223,서울,냉방중,중학교,비밀번호(숫자4자리)", inline=False)
        embed.add_field(name="주의사항", value="개인정보를 정확하게 입력해주세요 (개인정보 입력시 띄어쓰기 없음)", inline=True)
        embed.set_footer(text="Bot Made by. Pengu9783#2952")
        await message.channel.send(embed=embed)


     
    
    
   





     
    
    
   
















client.run(token)