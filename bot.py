import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = ">", case_insensitive = True)

@client.event
async def on_ready():
  print('Entramos como {0.user}' .format(client))

@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author}')

@client.command()
async def dado(ctx, numero):
  variavel = random.randint(1,int(numero))
  await ctx.send(f'O número que saiu no dado é {variavel}')

@client.command()
async def enviarembed(ctx):
  embed = discord.Embed(
    title = 'Título',
    description = 'Descrição',
    colour = 11598249
  )

  embed.set_author(name='Autor', icon_url='https://www.tibiawiki.com.br/images/e/e2/Adamant_Shield.gif')

  embed.set_thumbnail(url='https://www.tibiawiki.com.br/images/b/bb/Ancient_Tiara.gif')

  embed.set_image(url='https://image.api.playstation.com/vulcan/img/rnd/202010/0911/bZBvuQ98T04JvJCR7lJFYssZ.jpg')

  embed.set_footer(text='Esse é o footer')

  embed.add_field(name='Nome do Field', value='Valor do Field', inline=False)
  embed.add_field(name='Nome do Field', value='Valor do Field', inline=True)
  embed.add_field(name='Nome do Field', value='Valor do Field', inline=True)

  await ctx.send(embed = embed)





client.run('token') 
