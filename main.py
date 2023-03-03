from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,Bot
import os
import requests
from bs4 import BeautifulSoup as BS


TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
       ['Ob Havo']
       
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )


Toshkent = requests.get('https://sinoptik.ua/погода-ташкент')
html_Toshkent = BS(Toshkent.content, 'html.parser')
Samarqand=requests.get('https://sinoptik.ua/погода-самарканд')
html_Samarqand=BS(Samarqand.content,'html.parser')
Fargona=requests.get('https://sinoptik.ua/погода-фергана')
html_Fargona=BS(Fargona.content,'html.parser')
Buxoro=requests.get('https://sinoptik.ua/погода-бухара')
html_Buxoro=BS(Buxoro.content,'html.parser')
Jizzax=requests.get('https://sinoptik.ua/погода-джизак')
html_Jizzax=BS(Jizzax.content,'html.parser')
Qarshi=requests.get('https://sinoptik.ua/погода-карши')
html_Qarshi=BS(Qarshi.content,'html.parser')
Andijon=requests.get('https://sinoptik.ua/погода-андижан')
html_Andijon=BS(Andijon.content,'html.parser')
Xiva=requests.get('https://sinoptik.ua/погода-Хива')
html_Xiva=BS(Xiva.content,'html.parser')
Denov=requests.get('https://sinoptik.ua/погода-Денов')
html_Denov=BS(Denov.content,'html.parser')
Termiz=requests.get('https://sinoptik.ua/погода-термез')
html_Termiz=BS(Termiz.content,'html.parser')
Nukus=requests.get('https://sinoptik.ua/погода-Нукус')
html_Nukus=BS(Nukus.content,'html.parser')
Urganch=requests.get('https://sinoptik.ua/погода-ургенч')
html_Urganch=BS(Urganch.content,'html.parser')
Navoiy=requests.get('https://sinoptik.ua/погода-навои')
html_Navoiy=BS(Navoiy.content,'html.parser')
Namangan=requests.get('https://sinoptik.ua/погода-Наманган')
html_Namangan=BS(Namangan.content,'html.parser')
Guliston=requests.get('https://sinoptik.ua/погода-гулистан')
html_Guliston=BS(Guliston.content,'html.parser')
Zarafshon=requests.get('https://sinoptik.ua/погода-навои')
html_Zarafshon=BS(Zarafshon.content,'html.parser')
for el in html_Toshkent.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Toshkent_min = min[4:]
    Toshkent_max = max[5:]
    print(Toshkent_min, Toshkent_max)
for el in html_Fargona.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Fargona_min = min[4:]
    Fargona_max = max[5:]
for el in html_Buxoro.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Buxoro_min = min[4:]
    Buxoro_max = max[5:]
   # print(Samarqand_min, Samarqand_max)
for el in html_Jizzax.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Jizzax_min = min[4:]
    Jizzax_max = max[5:]
   
for el in html_Qarshi.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Qarshi_min = min[4:]
    Qarshi_max = max[5:]
   # print(Samarqand_min, Samarqand_max)
for el in html_Nukus.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Nukus_min = min[4:]
    Nukus_max = max[5:]
   # print(Samarqand_min, Samarqand_max)
for el in html_Termiz.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Termiz_min = min[4:]
    Termiz_max = max[5:]
   # print(Samarqand_min, Samarqand_max)
for el in html_Xiva.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Xiva_min = min[4:]
    Xiva_max = max[5:]
  #  print(Samarqand_min, Samarqand_max)
for el in html_Andijon.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Andijon_min = min[4:]
    Andijon_max = max[5:]
  #  print(Samarqand_min, Samarqand_max)
for el in html_Namangan.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Namangan_min = min[4:]
    Namangan_max = max[5:]
   # print(Samarqand_min, Samarqand_max)
for el in html_Guliston.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Guliston_min = min[4:]
    Guliston_max = max[5:]
    #print(Samarqand_min, Samarqand_max)
for el in html_Zarafshon.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Zarafshon_min = min[4:]
    Zarafshon_max = max[5:]
   # print(Samarqand_min, Samarqand_max)
for el in html_Navoiy.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Navoiy_min = min[4:]
    Navoiy_max = max[5:]
    #print(Samarqand_min, Samarqand_max)
for el in html_Denov.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Denov_min = min[4:]
    Denov_max = max[5:]
    #print(Samarqand_min, Samarqand_max)
for el in html_Urganch.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Urganch_min = min[4:]
    Urganch_max = max[5:]
  #  print(Samarqand_min, Samarqand_max)
for el in html_Samarqand.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    Samarqand_min = min[4:]
    Samarqand_max = max[5:]
  #  print(Samarqand_min, Samarqand_max)

def city():
    return [
        [InlineKeyboardButton("Toshkent", callback_data=f"01"),(InlineKeyboardButton("Andijon", callback_data=f"09"))],
        [InlineKeyboardButton("Fargʻona", callback_data=f"02"),(InlineKeyboardButton("Namangan", callback_data=f"10"))],
        [InlineKeyboardButton("Buxoro", callback_data=f"03"),(InlineKeyboardButton("Guliston", callback_data=f"11"))],
        [InlineKeyboardButton("Jizzax", callback_data=f"04"),(InlineKeyboardButton("Zarafshon", callback_data=f"12"))],
        [InlineKeyboardButton("Qarshi", callback_data=f"05"),(InlineKeyboardButton("Navoiy", callback_data=f"13"))],
        [InlineKeyboardButton("Nukus", callback_data=f"06"),(InlineKeyboardButton("Samarqand", callback_data=f"14"))],
        [InlineKeyboardButton("Termiz", callback_data=f"07"),(InlineKeyboardButton("Denov", callback_data=f"15"))],
        [InlineKeyboardButton("Xiva", callback_data=f"08"),(InlineKeyboardButton("Urganch", callback_data=f"16"))],
   
             
    ]


def back():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")

    if data[0] == "01":
        query.message.edit_text(f"Bugun Toshkent shaxrida havo o`zgarib turadi\nmin {Toshkent_min}\nmax "
                                f"{Toshkent_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    if data[0] == "02":
        query.message.edit_text(f"Bugun Fargona shaxrida havo o`zgarib turadi\nmin {Fargona_min}\nmax "
                                f"{Fargona_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "03":
            query.message.edit_text(f"Bugun Buxoro shaxrida havo o`zgarib turadi\nmin {Buxoro_min}\nmax "
                                f"{Buxoro_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "04":
        query.message.edit_text(f"Bugun Jizzax shaxrida havo o`zgarib turadi\nmin {Jizzax_min}\nmax "
                                f"{Jizzax_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "05":
        query.message.edit_text(f"Bugun Qarshi shaxrida havo o`zgarib turadi\nmin {Qarshi_min}\nmax "
                                f"{Qarshi_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "06":
        query.message.edit_text(f"Bugun Nukus shaxrida havo o`zgarib turadi\nmin {Nukus_min}\nmax "
                                f"{Nukus_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "07":
        query.message.edit_text(f"Bugun Termiz shaxrida havo o`zgarib turadi\nmin {Termiz_min}\nmax "
                                f"{Termiz_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "08":
        query.message.edit_text(f"Bugun Xiva shaxrida havo o`zgarib turadi\nmin {Xiva_min}\nmax "
                                f"{Xiva_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "09":
        query.message.edit_text(f"Bugun Andijon shaxrida havo o`zgarib turadi\nmin {Andijon_min}\nmax "
                                f"{Andijon_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "10":
        query.message.edit_text(f"Bugun Namangan shaxrida havo o`zgarib turadi\nmin {Namangan_min}\nmax "
                                f"{Namangan_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "11":
        query.message.edit_text(f"Bugun Guliston shaxrida havo o`zgarib turadi\nmin {Guliston_min}\nmax "
                                f"{Guliston_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "12":
        query.message.edit_text(f"Bugun Zarafshon shaxrida havo o`zgarib turadi\nmin {Zarafshon_min}\nmax "
                                f"{Zarafshon_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "13":
        query.message.edit_text(f"Bugun Navoiy shaxrida havo o`zgarib turadi\nmin {Navoiy_min}\nmax "
                                f"{Navoiy_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "14":
        query.message.edit_text(f"Bugun Samraqanda shaxrida havo o`zgarib turadi\nmin {Samarqand_min}\nmax "
                                f"{Samarqand_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "15":
        query.message.edit_text(f"Bugun Denov shaxrida havo o`zgarib turadi\nmin {Denov_min}\nmax "
                                f"{Denov_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
    if data[0] == "16":
        query.message.edit_text(f"Bugun Urganch shaxrida havo o`zgarib turadi\nmin {Urganch_min}\nmax "
                                f"{Urganch_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
   
    elif data[0] == 'back1':
        query.message.edit_text(
            f"Bu yerdan Shahar yoki viloyatni tanla 👇",
            reply_markup=InlineKeyboardMarkup(city()))


def havo(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Salom {user.first_name} 🖐🏼\nBu yerdan Shahar yoki viloyatni tanla 👇""",
                              reply_markup=InlineKeyboardMarkup(city()))
"""
updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))

updater.dispatcher.add_handler(MessageHandler(Filters.text('♻️ Orqaga'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Ob Havo'),havo))

updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))

updater.start_polling()
updater.idle()
"""