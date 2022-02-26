# -*- coding: utf-8 -*-
import telebot
owner = -1001501167582
from telebot import types
token='5100248003:AAGBhr-bp70CLhYq6c3yG2Mo0u-PXZqgNcM'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Я готовий вислухати вас...')

@bot.message_handler(content_types=["text"])
def handle_text(message):
        
  if(message.chat.id == owner):
    bot.send_message(message.chat.id, 'Ви є власником)')
  else:
    bot.forward_message(owner, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, message.from_user.first_name + ', Ваше запитання вже в роботі, очікуйте відповіді:)')
  


bot.infinity_polling()
