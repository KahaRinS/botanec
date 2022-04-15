import traceback
import time
from datetime import datetime
from MessageText import MessageText
from sender import sender,longpoll,vk,VkBotEventType,sender_photo
from vk_api import VkUpload

now = datetime.now().strftime('%H')


def Main(id,text):
	try:
		msg = MessageText(text)
		msg.Lower()
		msg.DeleteSymbols()
		#id = event.chat_id
		if msg.msg == 'ботанек':
			if int(now)<12:
				sender(id, 'Добрый вечер')
			else:
				sender(id, 'Доброе утро')
		elif msg.msg == 'ботанек отправь фото самого пиздатого чела':
			sender_photo(id, 'Держи')
		elif msg.msg == 'ботанек яйка':
			sender(id, 'Пакуль не працуе')
		elif msg.msg == 'ботанек цикл один':
			for i in range(0, 5):
				sender(id, '1')
				time.sleep(1)
		elif msg.msg == 'ботанек цикл два':
			for i in range(0, 5):
				sender(id, '2')
				time.sleep(1)
		elif msg.msg == 'ботанек цикл три':
			for i in range(0, 5):
				sender(id, '3')
				time.sleep(1)
		return 1
	except:
		print(traceback.print_exc())
		print ('Сосни хуйца, всё сломалось')
		return 0	
