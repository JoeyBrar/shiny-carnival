try:
    import requests
    import os
    import re
    import discord
    from discord.ext import commands, tasks
    from bs4 import BeautifulSoup
except Exception as e:
    print(f"{e}")


client = commands.Bot(command_prefix = '.')
['.help', 'type .help'] # For later


# Startup
@client.event
async def on_ready():
    change_status.start()
    print('Bot is online.\n')

@tasks.loop(seconds=10)
async def switch():
    for i in range(['.help', 'type .help']):
        await client.status_change(activity=discord.Game(i))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('pass in all required arguments pls')

# Dictionary command:



# ------------------------------------------------------------------------------------
# Dont commit or push with actual token
# Token: Not decided yet
# Replace with 'test' after use
client.run('test') 