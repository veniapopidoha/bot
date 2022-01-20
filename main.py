import telebot
owner = 666697836
from telebot import types
token='1521374248:AAH_KjkeC-9r6NW0tdLXGoo1gOfo8iNxSkA'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Я готовий вислухати вас...')

@bot.message_handler(content_types=["text"])
def handle_text(message):
        
  if(message.chat.id == owner):
    bot.send_message(message.chat.id, 'Ви є власником) Я працюю на всі 600') 
  else:
    bot.forward_message(owner, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, message.from_user.first_name + ', Ваше запитання вже в роботі, очікуйте відповіді:)')
  


bot.infinity_polling()
