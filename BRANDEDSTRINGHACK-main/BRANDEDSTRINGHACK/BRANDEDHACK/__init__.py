import os
import asyncio
import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from BRANDEDHACK.Helpers.data import LOG_TEXT
from pyromod import listen 

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
START_PIC = Config.START_PIC



if not START_PIC:
    START_PIC = "https://te.legra.ph/file/e1b4148d7a4cd8b0832d9.jpg"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    


async def BRANDEDHACK():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗞𝗜𝗡𝗚")
    LOG.print("[bold yellow]𝗬𝗢𝗨𝗥 𝗕𝗢𝗧 𝗦𝗧𝗔𝗥𝗧.............")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(BRANDEDHACK())    
