from random import randint
import discord
import time
import find
from typing import List
import biography
import random
from biography import Quotes,rules,FloHelp

badwords = ['fudge','poop','poopy','crap','frick','darn','damn','stupid','butt','pee']



async def findint(input):
    max = [int(i) for i in input.split() if i.isdigit()]
    return str(max)

class SimpleHandler:
    def __init__(self, trigger, response):
        self.trigger = trigger
        self.response = response
    async def handle_message(self, message):
        if message.content == self.trigger:
            words = message.content.split()
            await message.channel.send(self.response)
            return
        words = message.content.split()
        if words[0] == self.trigger:
            await message.channel.send(self.response)
            return
        if words[0] in self.trigger:
            await message.channel.send(self.response)
            return

class ArgumentHandler:
    def __init__(self, trigger, response):
        self.trigger = trigger
        self.response = response
    async def handle_message(self, message):
        if self.trigger == '!addquote':
            words = message.content.split("'")
            await self.response(words)
            return
        if message.content == self.trigger:
            words = message.content
            await self.response(words)
            return
        words = message.content.split()
        if words[0] == self.trigger:
            await self.response(words)
            return
            

class MyClient(discord.Client):
    members: List[discord.Member] = []
    is_counting = False
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

        # get all of the members in the guild
        g: discord.Guild = client.get_guild(755816945902682293)
        async for member in g.fetch_members(limit=150):
            print(member.name)
            self.members.append(member)
        print(len(g.members))

    async def on_message(self, message: discord.Message):
        print(message.content)

        async def count(words):
            self.is_counting = True
            max = int(words[1])
            number = 1
            while number <= max:
                if not self.is_counting:
                    return
                await message.channel.send(number)
                number = number + 1
                time.sleep(1)
            return

        async def welcome(words):
            member_name = words[1]
            for member in self.members:
                if member.display_name.startswith(member_name):
                    await message.channel.send(f'Welcome, {member.mention}. May your stay here be memorable.')
        
        async def punch(words):
            member_name = words[1]
            print(message.author)
            for member in self.members:
                if member.display_name.startswith(member_name):
                    await message.channel.send(f'{message.author.mention} punches {member.mention}....thwack!!')

        async def kiss(words):
            member_name = words[1]
            print(message.author)
            for member in self.members:
                if member.display_name.startswith(member_name):
                    await message.channel.send(f'{message.author.mention} kisses {member.mention} ....awww')

        async def kill(words):
            program = words[1]
            if program == 'count':
                self.is_counting = False
            if program == 'spam':
                self.is_spamming = False

        async def spam(words):
            self.is_spamming = True
            subject = words[1]
            while self.is_spamming == True:
                if not self.is_spamming:
                    return
                await message.channel.send(subject)
                # time.sleep(.5)
            return

        async def randomquote(words):
            await message.channel.send(f'{message.author.mention} "{random.choice(Quotes)}"')

        async def addquote(words):
            print(len(words))
            if len(words) >= 2:
                Quotes.append(words[1])
                await message.channel.send(f'"{Quotes[1]}" added to quotes!')

        handlers = [
        
        #### Simple Handlers

            SimpleHandler('!hotchocolate', f'{message.author.mention} Take this warm mug of hot chocolate, right off the stove.'),
            SimpleHandler('!hello', f'Hello {message.author.mention}'),        
            SimpleHandler('!tea', f'Here {message.author.mention}, have a cup of hot, steamy tea.'),
            SimpleHandler('!pizza', f'{message.author.mention} One large cheese, coming right up!'),
            SimpleHandler('pog', f'pog'),
            SimpleHandler('f', f'f in the chat'),
            SimpleHandler('!rules',f'{rules}'),
            SimpleHandler('somebody once told me','the world was gonna roll me'),
            SimpleHandler(":(",f'{message.author.mention} why you sad? why you mad?'),
            SimpleHandler('poopy butt','have some tp, Adam'),
            SimpleHandler('big nerd','no u'),
            SimpleHandler(['thanks','Thanks','thx','thank you','Thank you'],'You are very welcome!'),
            SimpleHandler(['bye','Bye','goodbye','seeya','Goodbye'],f'{message.author.mention} See you later!!'),
            SimpleHandler(['goodnight','Goodnight'],"Goodnight, sleep tight, and don't let the tech-bugs byte!"),
            SimpleHandler('!allquotes',f'{Quotes}'),
            SimpleHandler('!randomnumber',f'{random.randint(1,10)}'),
            SimpleHandler(['FloHelp','!help','/help'], f'{FloHelp}'),
            SimpleHandler('bot','im not your bot, elise.'),

        ### Interactive Handlers

            ArgumentHandler('!count', count),
            ArgumentHandler('!spam', spam),
            ArgumentHandler('!welcome', welcome),
            ArgumentHandler('!punch', punch),
            ArgumentHandler('!kiss',kiss),
            ArgumentHandler('/kill', kill),
            ArgumentHandler('!randomquote', randomquote),
            ArgumentHandler('!addquote', addquote)


        ]

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        for handler in handlers:
            await handler.handle_message(message)

        x = message.author
        for b in badwords:
            if message.content.find(b) >= 0:
                await message.channel.send(f'{x.mention} Watch your Profanity')
        return False

client = MyClient()
client.run('Super Real Key')
