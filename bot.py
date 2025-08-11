import telegram
import asyncio
import subprocess
from telegram import BotCommand
from telegram.ext import CommandHandler, Updater

# YOU NEED TO RECODE THIS SCRIPT IF YOU WANNA MAKE IT USABLE IN A SCREENSHARE, THIS ONE WON'T BYPASS ANYTHING SINCE IT WAS MADE JUST FOR ME TO TEST THE CONCEPT.

YourToken = 'yourtoken' # Put your bot token, and your chat ID here. (Tip: Use ENV)
YourChatID = 'chatid'
bot = telegram.Bot(token=YourToken)

async def SendMSGOntoTelegram(YourChatID, text): # This is for message forwarding.
    if len(text) <= 4096: # We need to bypass the Telegram message-restriction.
        await bot.send_message(YourChatID=YourChatID, text=text)
    else:
        parts = [text[i:i+4096] for i in range(0, len(text), 4096)]
        for part in parts:
            await bot.send_message(YourChatID=YourChatID, text=part)
            await asyncio.sleep(1)

async def CMDExecution(update, context): # Main function.
    YourChatID = update.message.YourChatID
    if len(context.args) >= 1:
        command = ' '.join(context.args)
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            output = result.stdout + result.stderr
            await SendMSGOntoTelegram(YourChatID, output or "Well we can't track the output, assuming telegram's API issue.") # Just for sure.
        except subprocess.TimeoutExpired:
            await SendMSGOntoTelegram(YourChatID, "Timed out.")
        except Exception as e:
            await SendMSGOntoTelegram(YourChatID, str(e))
    else:
        await SendMSGOntoTelegram(YourChatID, "Usage: /cmd <command>")

async def main():
    await bot.set_my_commands([BotCommand("cmd", "Send inputs to your PC")])
    await bot.send_message(YourChatID=YourChatID, text="[vu] Everything's set! You can send your first command through DM privately, not here :)")
    updater = Updater(YourToken, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("cmd", CMDExecution))
    updater.start_polling()
    await updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    asyncio.run(main())
