
import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, CallbackQueryHandler, Filters




from main import(inline_handlerlar,back,city,start,havo)

add = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)


@app.route('/webhook', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return 'GET'

    elif request.method == 'POST':
        data = request.get_json(force=True)

        db:Dispatcher = Dispatcher(bot, None , workers=0)

        update:Update = Update.de_json(data, bot)
        db.add_handler(CommandHandler('start',start))

        db.add_handler(MessageHandler(Filters.text('♻️ Orqaga'),start))
        db.add_handler(MessageHandler(Filters.text('Ob Havo'),havo))

        db.add_handler(CallbackQueryHandler(inline_handlerlar))

        db.process_update(update)
    return "Assalomu alaykum"


#if __name__ == '__main__':
    
 # app.run() 
bot=Bot(TOKEN)

#print(bot.set_webhook('https://obhavotatusf.pythonanywhere.com/webhook'))
#print(bot.delete_webhook())
#print(bot.get_webhook_info())

