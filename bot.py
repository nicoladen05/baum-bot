import discord

token = ("NTg3NTYzMjk3NjUwMjQ1NjU4.XP4Y9g.KV81IPuwzCIVLxSICNdpQ-6fdTw")

client = discord.Client()

@client.event
async def on_ready():
    print("Bot logged in!")
    await client.change_presence(activity=discord.Game("Baum"))

@client.event
async def on_message(message):
    if message.content.find("!test") != -1:
        await message.channel.send("Bot funktioniert!")
    if message.content.find("!help") != -1:
        embed = discord.Embed(title="Baum Bot", description="Hilfe für die Commands")
        embed.add_field(name="!test", value="Pingt den Bot")
        await message.channel.send(content=None, embed=embed)

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "neue-bäume":
            await channel.send_message(f"""{member.mention} ist nun ein Baum!""")

client.run(token)