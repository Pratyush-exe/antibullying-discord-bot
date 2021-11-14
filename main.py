import discord
import pickle
import random
from discord.utils import get
import re

model = pickle.load(open('Final_Model.pkl', 'rb'))
cv = pickle.load(open('cv_transfrom.pkl', 'rb'))

titles = ['This is a warning!', 'Watch your language!', 'Be careful what you speak', 'Be cool!', 'Watch it!']

client = discord.Client()

limitVote = 3


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    vect = cv.transform([message.content]).toarray()
    res = model.predict(vect)
    if res[0] == 1:
        embed = discord.Embed(title=random.choice(titles),
                              description=f"<@{message.author.id}> this message was offensive hence it is being "
                                          f"deleted\n\n React on the 🚫 to ban <@{message.author.id}>\n (total {limitVote} "
                                          f"votes required)",
                              color=discord.Color.red())
        await message.delete()
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction('🚫')


@client.event
async def on_raw_reaction_add(ctx):
    if ctx.channel_id == ctx.channel_id:
        if ctx.emoji.name == '🚫':
            channel = client.get_channel(ctx.channel_id)
            message = await channel.fetch_message(ctx.message_id)
            reaction = get(message.reactions, emoji=ctx.emoji.name)
            COUNT = reaction.count
            embed = message.embeds[0].to_dict()
            if COUNT >= limitVote:
                descp = embed['description']
                x = re.search(r"\<([0-9@]+)\>", descp)
                embed = discord.Embed(title="Ban",
                                      description="Admin (@everyone) Ban <" + x.group(1) + ">",
                                      color=discord.Color.dark_red())
                await message.channel.send(embed=embed)

client.run('OTA4NjI3MjU0Mzg3NTY4Njcw.YY4fEg.9wEK0V0NgAgFUaKH66TSl1So2wo')
