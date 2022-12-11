from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from menuBot.function import *


bot = Bot(token='5931424673:AAHvDu8YrD0zNlu8uGhwa87RekXrFhESuvM')
updater = Updater(token='5931424673:AAHvDu8YrD0zNlu8uGhwa87RekXrFhESuvM')
dispatcher = updater.dispatcher

# Token key from the bot

start_handler = CommandHandler('start', start)
receiving_data_handler = MessageHandler(Filters.text & (~Filters.command), receiving_data)
mes_data_handler = CommandHandler('end', cancel)


conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={start_calc: [receiving_data_handler]},
                                   fallbacks=[mes_data_handler])


dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()