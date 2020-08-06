import discord
from discord.ext import commands

token = ("NTg3NTYzMjk3NjUwMjQ1NjU4.XP4Y9g.hU0I2XSCMGiV9A2jnwi0oUp97bw")

client = commands.Bot(command_prefix = ".")
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot logged in!")
    await client.change_presence(activity=discord.Game("Baumstamm"))


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Baum Bot", description="Alle Commands für den Bot", color=0x00ff00)
    embed.add_field(name=".ping", value="Pings the bot")
    embed.add_field(name=".clear", value="Clears some or all messages in a channel")
    await ctx.send(embed = embed)


@client.command()
async def ping(ctx):
    await ctx.send(f"Bot Ping: {round(client.latency * 1000)}ms")


@client.command()
async def clear(ctx, amount=None):
    if amount == None:
        await ctx.channel.purge()
    else: 
        await ctx.channel.purge(limit=int(amount) + 1)


#@client.event
#async def on_message(message):
    #if message.content.find("!help") != -1:
        #embed = discord.Embed(title="Baum Bot", description="Alle Commands für den Bot")
        #embed.add_field(name="!test", value="Pingt den Bot")
        #await message.channel.send(content=None, embed=embed)

    #elif message.content.find("!test") != -1:
        #await message.channel.send("Bot funktioniert!")


@client.event
async def on_member_join(member):
    channel = client.get_channel(560509329086611476)
    guild=member.guild
    message = f"{member.mention} ist nun ein Baum!"
    await channel.send(message)
    await member.edit(nick=f"Baum🌳🌲{member.name}", reason="Prefix edit")
    baumrole = get(member.guild.roles, name="Baum")
    await member.add_role(baumrole)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(560509329086611476)
    guild=member.guild
    message = f"{member.mention} ist kein Baum mehr"
    await channel.send(message)

client.run(token)
