import discord
import pickle

model = pickle.load(open('Final_Model.pkl', 'rb'))
cv = pickle.load(open('cv_transfrom.pkl', 'rb'))

client = discord.Client()


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
        await message.delete()
        await message.channel.send('Message was Offensive, hence deleted!')


client.run('OTA4NjI3MjU0Mzg3NTY4Njcw.YY4fEg.2hPZkvmZ-hi5IrirqOYOIGl2gF4')
