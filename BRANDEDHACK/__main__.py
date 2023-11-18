import asyncio
import importlib

from pyrogram import idle
from BRANDEDHACK import LOG
from BRANDEDHACK.modules import ALL_MODULES


async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("BRANDEDHACK.modules." + all_module)
    LOG.print("[bold yellow]𝗛𝗔𝗖𝗞 𝗕𝗜𝗧 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗡𝗢𝗪 𝗙𝗨𝗖𝗞 𝗔𝗟𝗟 𝗧𝗚 𝗜𝗗")
    await idle() 
    LOG.print("[bold red]𝗖𝗔𝗡𝗖𝗟𝗘 𝗔𝗟𝗟 𝗧𝗔𝗦𝗞🤐..........")



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
