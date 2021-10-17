from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Owner", url="https://t.me/SanilaRanatunga")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/SanilaRanatunga")],
         [InlineKeyboardButton("Torrent Download bot of me😎😋", url="https://t.me/torrentdownloader88_bot")],
        [InlineKeyboardButton("Song Download bot of me😎😋", url="https://t.me/songdownload597_bot")],
        [InlineKeyboardButton("Powerful Chat Bot of me😎😋", url="https://t.me/useful_powerful_chat_bot")]
        
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nYou can download any youtube video using this bot. To download simply send the link of the video that you want to download😋(A bot by @SanilaRanatunga)"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
