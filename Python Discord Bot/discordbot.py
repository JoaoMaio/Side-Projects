# Primeira coisa a fazer: instalar o discord.py
# pip install discord.py

# Segunda coisa a fazer: instalar dotenv
# pip install python-dotenv

import os
import discord
from discord.ext import commands
import random
from discord import Intents
from dotenv import load_dotenv
from help import SupremeHelpCommand


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # Pegar o token do arquivo .env
GUILD = os.getenv('DISCORD_GUILD')

intents = Intents.all()  # Criar uma instância de Intents
intents.members = True  # Habilitar a flag de membros
intents.reactions = True  # Habilitar a flag de reações
intents.messages = True  # Habilitar a flag de mensagens

bot = commands.Bot(command_prefix='!', intents=intents)
bot.help_command = SupremeHelpCommand()
############################################################################################################

#region Bot Events

@bot.event
async def on_ready():
    print(bot.user, "Conectou-se ao Discord!")

    for guild in bot.guilds:
        if guild.name == GUILD:
            members = []

            for member in guild.members:
                members.append(member.name)

            print(f'Membros do servidor:\n - {members}')

@bot.event
async def on_member_join(member):
    # Get the "general" channel (you can change this to any channel name)
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'Welcome to the server, {member.mention}!')

@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandOnCooldown):
        await ctx.send(f"You are rate limitted. Please, try again in {exception.retry_after} seconds")

#endregion

#region Commands
@bot.command(name='99', 
            help='Responds with a random quote from Brooklyn 99', 
            aliases=['nine_nine'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def nine_nine(ctx):
    print(ctx.author, "Pediu uma frase do Brooklyn 99")
    
    try:
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            'Cool. Cool cool cool cool cool cool cool, no doubt no doubt no doubt no doubt.',
            'Noice. Smort.',
            'Toight. Toight like a toiger.',
            'Sarge, with all due respect, I am gonna completely ignore everything you just said.',
        ]
    
        response = random.choice(brooklyn_99_quotes)
        await ctx.send(response)
    
    except commands.CommandOnCooldown as e:
        # If the command is on cooldown, this block will run
        await ctx.send(f'You are on cooldown. Try again in {e.retry_after:.2f} seconds.')


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    print(ctx.author, "Pediu para rolar dados")

    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='clear', help='Clears a specified number of messages from the chat.')
async def clear(ctx, amount: int = None):
    print(ctx.author, "Pediu para limpar mensagens")

    # Check if the amount is provided
    if amount is None:
        await ctx.send("Please specify the number of messages to delete. Usage: `!clear <number>`")
        return

    # Check if the amount is valid
    if amount < 1:
        await ctx.send("Please specify a number greater than 0.")
        return

    # Purge the messages
    deleted = await ctx.channel.purge(limit=amount)
    
    # Send a message to confirm deletion and delete it after 5 seconds
    confirmation_message = await ctx.send(f'Foram eliminadas {len(deleted)} mensagens.')
    await confirmation_message.delete(delay=5)

#endregion

@bot.command(name='gato')
async def random_cat(ctx):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    await ctx.send(data[0]['url'])

@bot.command(name='foto')
async def send_random_image(ctx):
    lista_imagens = os.listdir("./photos")
    # Seleciona uma imagem aleatória
    imagem = random.choice(lista_imagens)
    # Envia a imagem para o chat
    await ctx.send(file=discord.File(f"./photos/{imagem}"))

@bot.command(name='avatar', help='Enviar o avatar de um membro')
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar.url)

@bot.command(name='random', help='Gera um número aleatório entre dois valores.')
async def random_number(ctx, start: int, end: int):
    if start >= end:
        await ctx.send('Invalid range. Make sure start is less than end.')
    else:
        number = random.randint(start, end)
        await ctx.send(f'Your random number between {start} and {end} is: {number}')

bot.run(TOKEN)