from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random 
from datetime import datetime 

token = "d6b376af78459ca2c9ea4c94cce06efa64548653799a6ceb9c5df4c0c74244680f70c627ecce7042692af"

vk_session = vk_api.VkApi(token= token)

session_api = vk_session.get_api()
longpoll = vk_api.longpoll.VkLongPoll(vk_session)
longpoll = VkLongPoll(vk_session)

while True:
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(),"%H:%M:%S")))
			print('Текст сообщения: ' + str(event.text))
			print(event.user_id)

			response = event.text.lower()

			if event.from_user and not (event.from_me):
				if response == 'привет':
					vk_session.method("messages.send", {'user_id':event.user_id, 'message':'Привет, друг!', 'random_id':0})
