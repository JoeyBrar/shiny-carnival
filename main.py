try:
    import requests
    import os
    import re
    import discord
    from discord.ext import commands, tasks
    from bs4 import BeautifulSoup
except Exception as e:
    print(f"{e}")
