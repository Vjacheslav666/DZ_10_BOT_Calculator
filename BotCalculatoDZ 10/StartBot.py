from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from menuBot.function import *


bot = Bot(token='Token key from the bot')
updater = Updater(token='Token key from the bot')
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
receiving_data_handler = MessageHandler(Filters.text & (~Filters.command), receiving_data)
mes_data_handler = CommandHandler('end', cancel)


conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={start_calc: [receiving_data_handler]},
                                   fallbacks=[mes_data_handler])


dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()