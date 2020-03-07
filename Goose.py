# Goose bot, Archivist for the Library of Zebulax
import os
import discord
import asyncio
import random
from dotenv import load_dotenv
from CatchPhrases import catchPhrases
from GoosePlays import goosePlaying
from GooseQuotes import gooseQuotes
from GooseAnswers import gooseAnswers
from GooseDoubt import gooseDoubt
from GoosePayRespects import goosePayRespects
#from libraryPoints import get_name
#from libraryPoints import award_points
#from libraryPoints import revoke_points

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    game = discord.Game(goosePlaying())
    await client.change_presence(status = discord.Status.online, activity = game);

@client.event
async def on_message(message):
    message_upper = (message.content).upper()
    if message.author == client.user:
        return 

    #WIP
    '''
    if 'LIBRARY POINTS' in message_upper:
        if any(a in message_upper for a in players):        #got it!
            print(a)
        member = message.author
        #print(member.name)
        #await message.channel.send(f' {member.name} has a few library points ')
        get_name(member.name)
    '''
    
    if message_upper.startswith('BDE'):
        bde_item = message.content
        bde_response = "HONK! HONK HONK HOOONK! Translation: *%s is %d%% Big Dick Energy.*" %(bde_item[4:], random.randint(0, 100))
        await message.channel.send(bde_response)
        
    if message_upper.endswith('?') and any(x in message_upper for x in catchPhrases):
        answer = random.choice(gooseAnswers)
        await message.channel.send(answer)

    elif any(x in message_upper for x in catchPhrases):
        response = random.choice(gooseQuotes)
        await message.channel.send(response)
       

    elif 'F' == message_upper:
        f_response = random.choice(goosePayRespects)
        await message.channel.send(f_response)

    elif 'X' == message_upper:
        x_response = random.choice(gooseDoubt)
        await message.channel.send(x_response)
        
    elif message.content == 'raise-exception':
        raise discord.DiscordException
        
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game(goosePlaying())
        await client.change_presence(status = discord.Status.online, activity = game);
        await asyncio.sleep(14400) #4 hours
        
client.loop.create_task(my_background_task())

client.run(token)
