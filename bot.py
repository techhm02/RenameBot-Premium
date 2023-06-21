import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6145510462:AAHXP6-gJsNED1zL-3dxpiPUIAAIIFiC8Dg")

API_ID = int(os.environ.get("API_ID", "27100881"))

API_HASH = os.environ.get("API_HASH", "ba917e1a377fa4ea750d9253bcaf9940")

STRING = os.environ.get("STRING", "BQB4wCQSqEaE7anB_Uq1khFKOYtikl8IOQV8FNyWca4oZ1lP9CAsRT1jIT2J0wOTY_hlPA-0HGwAl-g4hjx9_NbJsj5GLlqY7ekQd6Y95gqYtohw-KfR6z3GGx-8CXbzSwCftJPYoEghvSWUTgLTyPbpyO96xNTQg4o5C3NjsaNnPclYp1fQB2O_jN12srBd6noUjIM6Z4SocsqhJ14xiWOyPsx3iSU6i93jEqsH0uo0qnMfm7p_b5CcHyuhM3xtTUIHZ-BncFYOqR0boZNlbp-Z5BDwwp-GQF9U7RvKNJLSSfQJevhnmw-6FpeVVQ_4gltLM4_lzlB16WeRRT1fzM0Nc2uVuQA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
