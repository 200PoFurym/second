from telebot import types
def phone_bt():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone = types.KeyboardButton("Поделитесь контактом", request_contact=True)
    kb.add(phone)
    return kb
def main_menu_kb():
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

def all_products(actual_products):
    kb = types.InlineKeyboardMarkup(row_width=2)
    back = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back")
    cart = types.InlineKeyboardButton(text="Корзина", callback_data="user_cart")
    products = [types.InlineKeyboardButton(text=i[1], callback_data=i[0]) for i in actual_products]
    kb.add(*products)
    kb.row(cart)
    kb.row(back)
    return kb


def exact_product(current_ammount=1, plus_or_minus=""):
    kb = types.InlineKeyboardMarkup(row_width=3)
    # постоянные кнопки
    back = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")
    accept = types.InlineKeyboardButton(text="Добавить в корзигу", callback_data="to_cart")
    minus = types.InlineKeyboardButton(text="➖", callback_data="minus")
    plus = types.InlineKeyboardButton(text="➕", callback_data="plus")
    count = types.InlineKeyboardButton(text=f"{current_ammount}", callback_data="none")
    # динамичная кнопка
    if plus_or_minus == "plus":
        new_ammount = current_ammount + 1
        count = types.InlineKeyboardButton(text=f"{new_ammount}", callback_data="none")
    elif plus_or_minus == "minus":
        if current_ammount > 1:
            new_ammount = current_ammount - 1
            count = types.InlineKeyboardButton(text=f"{new_ammount}", callback_data="none")
    kb.add(minus, count, plus)
    kb.row(accept)
    kb.row(back)
    return kb


def get_cart_kb(cart):
    kb = types.InlineKeyboardMarkup(row_width=1)
    clear = types.InlineKeyboardButton(text="Очистить корзину", callback_data="clear_cart")
    back = types.InlineKeyboardButton(text="Назад", callback_data="main_menu")
    order = types.InlineKeyboardButton(text="оформить заказ", callback_data="order")
    products = [types.InlineKeyboardButton(text=f"{i[0]}", callback_data=f"{i[0]}")for i in cart]
    kb.add(clear, back, order)
    kb.add(*products)
    return kb
