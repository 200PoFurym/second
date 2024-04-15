import telebot
from telebot import types
from currency_converter import CurrencyConverter
cur = CurrencyConverter
bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def first(message):
    bot.send_message(message.chat.id, f"<i>Здравствуйтеб введите сумму: </i>", parse_mode='html')
    bot.register_next_step_handler(message, summ)
 def summ(message):
     global money
     money = message.text.strip()
     but = types.KeyboardButton("Нажмите для выбора пары")
     par1 = types.KeyboardButton("USD/SUM", callback_data='usd/sum')
     par2 = types.KeyboardButton("EUR/SUM", callback_data='eur/sum')
     but.add(par1, par2)
bot.infinity_polling()





