from menuBot.controller import *
from menuBot.log import *
from telegram.ext import ConversationHandler

start_calc = 0

menu_text = ("Я бот-калькулятор!\n"
            "При решении примера считаю, что числа в примере положительные\n\n"
            "Понимаю знаки: /, *, +, -\n\n"
            "Знаю приоритет действий. Могу работать со скобками.\n\n"
            "Команда /end отключит меня.")

menu_text2 = ("Отвечаю на задачи подобных примеров:\n\n"
            "число+число\n"
            "число-число\n"
            "число*число\n"
            "число/число\n"
            "( число+число )*число\n"
            "( число-число )*число\n")

def start(update, context):
    context.bot.send_message(update.effective_chat.id, menu_text)
    context.bot.send_message(update.effective_chat.id, menu_text2)
    get_id_user(update.effective_chat.id)
    return start_calc

def receiving_data(update, context):
    data = update.message.text
    get_input_data(data)  
    list_data = parseable_data(data) 
    result = solution_equation(list_data)  
    get_result(result) 
    save_log()  
    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'До встречи!')
    return ConversationHandler.END
