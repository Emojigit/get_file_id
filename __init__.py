# -*- coding: utf-8 -*-

__author__ = "Emoji"
__version__ = "1.0.0"
__url__ = "https://github.com/Emojigit/catworm"
__description__ = "Get file ID"
__dname__ = "get_file_id"

from telethon import events, utils
def setup(bot):
    @bot.on(events.NewMessage(pattern='/fileid'))
    async def catworm(event):
        replymsg = await event.get_reply_message()
        if replymsg and replymsg.document != None:
            id = replymsg.file.id
            await replymsg.reply("`{}`".format(id))
            raise events.StopPropagation
        await event.respond("Please reply to a valid file.")
        raise events.StopPropagation
