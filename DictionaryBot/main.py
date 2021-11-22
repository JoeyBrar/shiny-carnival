try:
    from discord.ext import commands, tasks
    import define
    import discord
except Exception as e:
    print(f"{e}")

client = commands.Bot(command_prefix = 'thicc ')
x = ['thicc help', 'type thicc help']

# Startup
@client.event
async def on_ready():
    switch.start()
    print('Bot is online.\n')

@tasks.loop(seconds=10)
async def switch():
    for i in range(len(x)):
        await client.change_presence(activity=discord.Game(i))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('pass in all required arguments pls')

@client.command(help="- Don't know a word? Look it up here using the say command! Usage: thicc help (word)")
async def say(ctx, *, question):
    for index, i in enumerate(define.define_word(question)):
        try:
            await ctx.send((f"**Type #{index+1}** {i[0]} \n**Meaning(s) #{index+1}:** {' '.join(i)}"))
        except:
            print('check ur spelling')

# ------------------------------------------------------------------------------------
# Don't commit or push with actual token
# DM me for token
# Replace with 'test' after use
client.run('test')
