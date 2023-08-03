import discord
import os


intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # this runs when the account is logged into
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # this runs code every time a message is sent
    # await message.channel.send("A message was just sent here!")
    # the ID for the channel you want to use (I swapped it for testing): 1128136575776198676 #can we change it ? what? the id

    if message.content.startswith("/status"):
        otherChannel = discord.utils.get(message.guild.channels, id=1128136575776198676)
        print(otherChannel)
        print(type(otherChannel))
        lastMessage = ""
        async for searchMessage in otherChannel.history(limit=1):
            lastMessage = searchMessage.content

        await message.channel.send(f"The server is {lastMessage}")


client.run('MTEyOTg4MzE2ODUzOTk0MzAyMg.Gwu47y.fvdhOGH646xkpsU61W0JFyKLYLbixNp6o8TlP4')
