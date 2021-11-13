import discord
from discord.ext.commands import has_permissions
import pickle
import random
from discord.utils import get
import re

model = pickle.load(open('Final_Model.pkl', 'rb'))
cv = pickle.load(open('cv_transfrom.pkl', 'rb'))

titles = ['This is a warning!', 'Watch your language!', 'Be careful what you speak', 'Be cool!', 'Watch it!']

client = discord.Client()

limitVote = 5


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
            if COUNT == 2:
                user = ""
                descp = embed['description']
                x = re.search(r"\<([0-9@]+)\>", descp)
                await message.channel.send("<" + x.group(1) + ">")


@has_permissions(kick_members=True)
async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kick')


client.run('enter bot token')
