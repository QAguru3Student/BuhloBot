import telebot
from telebot import types




bot = telebot.TeleBot('6611487363:AAHeBhJnCAD4RbsscPSzsbP37snNcg0joZo')





@bot.message_handler(commands=['start']) #стартовая команда
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Доставка бухла")
    markup.add(btn1)
    bot.send_message(message.from_user.id, f"👋 Привет {message.from_user.first_name}", reply_markup=markup)
    bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    #Русский язык
    if message.text == '🇷🇺 Доставка бухла':
        bot.send_message(message.from_user.id, f"{message.from_user.first_name}, cегодня доставка бухла не работает. Пиздуй в магазин!", parse_mode='html')
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')





bot.polling(none_stop=True) #обязательная для работы бота часть