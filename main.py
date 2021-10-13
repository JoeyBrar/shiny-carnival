try:
    import requests
    import os
    import re
    import discord
    from discord.ext import commands, tasks
except Exception as e:
    print(f"{e}")
