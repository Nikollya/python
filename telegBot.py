import telebot

bot = telebot.TeleBot("1025260843:AAGIF7mJhfQDRaAPcogpZpPV0MxZRux40qA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	if message.text=="/start":
		act=True
	elif message.text=="Привет":
		bot.send_message(message.chat.id, message.text)
	elif message.text=="как дела" or message.text=="Как дела":
		bot.send_message(message.chat.id, "Норм")
	else:
		bot.send_message(message.chat.id, "Неверная команда!")
bot.polling(none_stop = True )
