import discord
from bot_logic import gen_pass
from coin import flip_coin
import coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642") 
    elif message.content.startswith('pass'):
        password = gen_pass(12)
        await message.channel.send(password) 
    elif message.content.startswith('coin'):
        result = flip_coin()
        await message.channel.send(result) 
    else:
        await message.channel.send(message.content)
    


client.run("MTI2ODM2ODEyMDEyNTU5MTU3NA.GXtO98.Xom5aNxjdWG56qjHwlePqucwCNizOTnfRWBEso")