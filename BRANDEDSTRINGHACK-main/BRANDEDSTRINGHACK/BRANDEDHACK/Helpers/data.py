from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 


PM_TEXT = """
** 𝗛𝗘𝗬{},**
𝐈 𝐀𝐌 **{}** 𝗔 𝗕𝗢𝗧 𝗧𝗢 𝗛𝗔𝗖𝗞 𝗨𝗦𝗘𝗥 𝗔𝗖𝗖𝗢𝗨𝗡𝗧.

ɪ sᴜᴘᴘᴏʀᴛ ʙᴏᴛʜ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ
ᴄʟɪᴄᴋ ᴏɴ ʜᴀᴄᴋ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴡʜᴀᴛ I ᴄᴀɴ ᴅᴏ.
"""

HACK_TEXT = """
"A" :~ [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴏᴡɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs]

"B" :~ [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʟɪᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, ᴜsʀɴᴀᴍᴇ... ᴇᴛᴄ]

"C" :~ [ʙᴀɴ ᴀ ɢʀᴏᴜᴘ {ɢɪᴠᴇ ᴍᴇ SᴛʀɪɴɢSᴇssɪᴏɴ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ɪ ᴡɪʟʟ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛʜᴇʀᴇ}]

"D" :~ [ᴋɴᴏᴡ ᴜsᴇʀ ʟᴀsᴛ ᴏᴛᴘ {𝟷sᴛ ᴜsᴇ ᴏᴘᴛɪᴏɴ B ᴛᴀᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ʟᴏɢɪɴ ᴛʜᴇʀᴇ Aᴄᴄᴏᴜɴᴛ ᴛʜᴇɴ ᴜsᴇ ᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴏᴛᴘ}]

"E" :~ [Jᴏɪɴ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ ᴠɪᴀ SᴛʀɪɴɢSᴇssɪᴏɴ]

"F" :~ [Lᴇᴀᴠᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ ᴠɪᴀ SᴛʀɪɴɢSᴇssɪᴏɴ]

"G" :~ [Dᴇʟᴇᴛᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ]

"H" :~ [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴛᴡᴏ sᴛᴇᴘ ɪs ᴇɴᴇᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ]

"I" :~ [ᴛᴇʀᴍɪɴᴀᴛᴇ Aʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs ᴇxᴄᴇᴘᴛ Yᴏᴜʀ SᴛʀɪɴɢSᴇssɪᴏɴ]

"J" :~ [ᴅᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ]

"K" :~ [ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

"L" :~ [ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴀᴅᴍɪɴs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]
"""
info = """
 ❥︎ ɴᴀᴍᴇ : {}
 ❥︎ ɪᴅ : {}
 ❥︎ ᴘʜᴏɴᴇ ɴᴏ : +{}
 ❥︎ ᴜsᴇʀɴᴀᴍᴇ : @{}
"""

PM_BUTTON = IKM([[IKB("•─╼⃝𖠁 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗛𝗔𝗖𝗞 𖠁⃝╾─•", callback_data="hack_btn")]])



HACK_MODS = IKM([
    [
        IKB("A", callback_data="A"),
        IKB("B", callback_data ="B"),
        IKB("C", callback_data="C"),
        IKB("D", callback_data="D"),
        IKB("E", callback_data="E"),          
    ],
    [
        IKB("F", callback_data="F"),
        IKB("G", callback_data ="G"),
        IKB("H", callback_data="H"),
        IKB("I", callback_data="I"),
                   
    ],
    [
        IKB("J", callback_data="J"),
        IKB("K", callback_data="K"),
        IKB("L", callback_data ="L"),                           
    ],
    ],    
    )



LOG_TEXT = """
     ● ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ●

 ❥︎ ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴀɴʏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴜsɪɴɢ 
 ❥︎ ᴛʜᴇɪʀ ᴘʏʀᴏɢʀᴀᴍ ᴏʀ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ.
 ❥︎ ᴏᴡɴᴇʀ : 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗞𝗜𝗡𝗚
"""
