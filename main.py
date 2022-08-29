from pygismeteo import Gismeteo
import telebot

bot = telebot.TeleBot("5594186231:AAFxJWorbJxeHCZFwGXZVAdOVa_Yt9Wd26c")
gismeteo = Gismeteo()
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, назови свой город:")
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    search_results = gismeteo.search.by_query( message.text )
    city_id = search_results[0].id
    current = gismeteo.current.by_id(city_id)
    answer = "В " + "Твоем городе/селе" + " " + str(current.temperature.air.c) + "\n"
    bot.reply_to(message, answer)
bot.infinity_polling()
