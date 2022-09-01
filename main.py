from pygismeteo import Gismeteo
import telebot
import sqlite3

bot = telebot.TeleBot("5594186231:AAFxJWorbJxeHCZFwGXZVAdOVa_Yt9Wd26c") #Токен бота
conn = sqlite3.connect('SEPTEMBERTESTBOT.db', check_same_thread=False)
cursor = conn.cursor() #Подключение таблицы sqlite3

def db_table_val(username: str, city: str):
	cursor.execute('INSERT INTO username (username, city) VALUES (?,?)', (username,city))
	conn.commit() #Чтение таблицы

gismeteo = Gismeteo() #функция gismeteo


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, назови свой город:")
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    search_results = gismeteo.search.by_query( message.text )
    city_id = search_results[0].id
    current = gismeteo.current.by_id(city_id) #api gismeteo
    answer = "В твоем городе/селе" + " " + str(current.temperature.air.c) + " градусов по Цельсию." #ответ
    bot.reply_to(message, answer)
    username = message.from_user.username
    city = message.text #сохранение данных в таблицу sqlite3
    db_table_val(username=username, city=city)


bot.infinity_polling()
