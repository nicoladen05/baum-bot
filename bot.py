import discord

token = ("NTg3NTYzMjk3NjUwMjQ1NjU4.XP4Y9g.hU0I2XSCMGiV9A2jnwi0oUp97bw")

client = discord.Client()

@client.event
async def on_ready():
    print("Bot logged in!")
    await client.change_presence(activity=discord.Game("Baumstamm"))


@client.event
async def on_message(message):
    if message.content.find("!help") != -1:
        embed = discord.Embed(title="Baum Bot", description="Alle Commands für den Bot")
        embed.add_field(name="!test", value="Pingt den Bot")
        await message.channel.send(content=None, embed=embed)

    elif message.content.find("!test") != -1:
        await message.channel.send("Bot funktioniert!")


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
