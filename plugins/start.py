from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/sanilaassistant_bot")],
        [InlineKeyboardButton("Source Code🚥", url="https://github.com/sanila2007/Youtube-Downloader-Bot")]
        
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nYou can download any youtube video using this bot. To download simply send the link of the video that you want to download😋\n\n✨️Developer: Sanila Ranatunga\n\n✨️Feedback : @sanilaassistant_bot"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
