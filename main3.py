import telebot
import dzbutton as dzbt
from geopy.geocoders import Nominatim
import dbmybot as db
bot = telebot.TeleBot("6699141263:AAHkNIJPG68YKWbAQQmWr9Vd2w72-f0mnEE")

geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0")
# db.add_product(pr_name="Чизбургер", pr_quantity=10, pr_price=30000, pr_des="Лучший", pr_photo="https://burgerkings.ru/image/cache/catalog/photo/598999973-chizburger-600x600.jpg")
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    checker = db.check_user(user_id)
    if checker == False:
        bot.send_message(user_id, "Добро пожаловать в бот KFC!\n"
                              "Пройдите короткую регистрацию.\n\n"
                              "Введите свое имя: ")
        print(message.text)
        bot.register_next_step_handler(message, get_name)
    elif checker == True:
        bot.send_message(user_id,"Выберите действие", reply_markup=dzbt.main_menu_dzbt())
def get_name(message):
    user_id = message.from_user.id
    name = message.text
    bot.send_message(user_id, "Поделитесь своими контактными данными", reply_markup=dzbt.phone_dzbt())
    bot.register_next_step_handler(message, get_phone_number, name)
    print(message.contact)
def get_phone_number(message, name):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        print(phone_number)
        bot.send_message(user_id, "Регистрация завершена."
                                  "Выберите действие", reply_markup=dzbt.main_menu_dzbt())
        db.add_user(user_id=user_id, name=name, phone_number=phone_number)
    else:
        bot.send_message(user_id, "Отправте контакт через кнопку")
        bot.register_next_step_handler(message, get_phone_number, name)
def get_location(message):
    user_id = message.from_user.id
    if message.location:
        longitude = message.location.longitude
        latitude = message.location.latitude
        adress = geolocator.reverse((latitude, longitude))
        bot.send_message(user_id, f"Ваш адрес{adress}")
        bot.send_message(message)
        bot.register_next_step_handler(message)
        print(adress)
        print(message.location)
    else:
        bot.send_message(user_id, "Отправте локацию через кнопку")
        bot.register_next_step_handler(message, get_location)

bot.infinity_polling()