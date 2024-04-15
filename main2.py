import telebot
import butt
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Добро пожаловать!", reply_markup=butt.help)
