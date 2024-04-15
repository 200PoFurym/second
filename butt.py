from telebot import types

def help():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pom = types.KeyboardButton("Помощь")
    kb.add(pom)
    return kb