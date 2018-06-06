# timezone-bot

import discord
from discord.ext import commands

from datetime import datetime
from pytz import timezone

description = '''A bot to be used for converting a time in UTC to zones used by other members of the discord.

Usage requires the format like this - 2009-05-05 22:28 '''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def timeNow(): #formerly printCurrentTime
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"

    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    await bot.say (now_utc.strftime(fmt) + " (UTC)")

    # Convert to Europe/London time zone
    now_london = now_utc.astimezone(timezone('Europe/London'))
    await bot.say (now_london.strftime(fmt) + " (London)")

    # Convert to Europe/Berlin time zone
    now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
    await bot.say (now_berlin.strftime(fmt) + " (Berlin)")

    # Convert to CET time zone
    now_cet = now_utc.astimezone(timezone('CET'))
    await bot.say (now_cet.strftime(fmt) + " (CET)")

    # Convert to Israel time zone
    now_israel = now_utc.astimezone(timezone('Israel'))
    await bot.say (now_israel.strftime(fmt) + " (Israel)")

    # Convert to Canada/Eastern time zone
    now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
    await bot.say (now_canada_east.strftime(fmt) + " (Canada/Eastern)")

    # Convert to US/Central time zone
    now_central = now_utc.astimezone(timezone('US/Central'))
    await bot.say (now_central.strftime(fmt) + " (US/Central)")

    # Convert to US/Pacific time zone
    now_pacific = now_utc.astimezone(timezone('US/Pacific'))
    await bot.say (now_pacific.strftime(fmt) + " (US/Pacific)")


@bot.command()
async def convertTime(date_str): #formerly printFutureTime #this will only work with a UTC time, so work this out in advance
    #date_str = "2009-05-05+22:28"
    datetime_obj = datetime.strptime(date_str, "%Y-%m-%d+%H:%M")

    fmt = "%Y-%m-%d %H:%M %Z%z"

    # Current time in UTC
    now_utc = datetime_obj.replace(tzinfo=timezone('UTC'))
    await bot.say (now_utc.strftime(fmt) + " (UTC)")

    # Convert to Europe/London time zone
    now_london = now_utc.astimezone(timezone('Europe/London'))
    await bot.say (now_london.strftime(fmt) + " (London)")

    # Convert to Europe/Berlin time zone
    now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
    await bot.say (now_berlin.strftime(fmt) + " (Berlin)")

    # Convert to CET time zone
    now_cet = now_utc.astimezone(timezone('CET'))
    await bot.say (now_cet.strftime(fmt) + " (CET)")

    # Convert to Israel time zone
    now_israel = now_utc.astimezone(timezone('Israel'))
    await bot.say (now_israel.strftime(fmt) + " (Israel)")

    # Convert to Canada/Eastern time zone
    now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
    await bot.say (now_canada_east.strftime(fmt) + " (Canada/Eastern)")

    # Convert to US/Central time zone
    now_central = now_utc.astimezone(timezone('US/Central'))
    await bot.say (now_central.strftime(fmt) + " (US/Central)")

    # Convert to US/Pacific time zone
    now_pacific = now_utc.astimezone(timezone('US/Pacific'))
    await bot.say (now_pacific.strftime(fmt) + " (US/Pacific)")

bot.run('token-goes-here')



##from pytz import all_timezones ##this prints out all available time zones
##
##print (len(all_timezones))
##for zone in all_timezones:
##    print (zone)


# Europe/London
# CET
# Israel
# Canada/Eastern 
# US/Central 
