from telebot import types
def phone_dzbt():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone = types.KeyboardButton("Поделитесь контактом", request_contact=True)
    kb.add(phone)
    return kb
def main_menu_dzbt():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    products = types.KeyboardButton("🍽Начать заказ")
    cart = types.KeyboardButton("Корзина")
    feedback = types.KeyboardButton("Отзыв")
    settings = types.KeyboardButton("Настройки")
    kb.add(products, cart, feedback, settings)
    return kb
def location():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    location = types.KeyboardButton("Отправте локацию", request_location=True)
    kb.add(location)
    return kb