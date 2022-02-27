import datetime

import pytz
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "NOT FOR PUBLIC USE. ASK ME IF THE TOKEN IS NEEDED"
START_MESSAGE = "Hi! I am a simple greeting bot. My commands:\n/sayhello\n/saygood\nTake pleasure!"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(START_MESSAGE)


def say_hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello!")


def say_good(update: Update, context: CallbackContext) -> None:
    current_hour = datetime.datetime.now(pytz.timezone("Europe/Moscow")).time().hour

    if current_hour > 12:
        morning_or_evening = "evening"
    else:
        morning_or_evening = "morning"

    update.message.reply_text(f"Good {morning_or_evening}!")


def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("sayhello", say_hello))
    dispatcher.add_handler(CommandHandler("saygood", say_good))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
