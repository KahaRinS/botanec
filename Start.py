import traceback
from main import Main
from sender import longpoll, VkBotEventType, vk
import threading
from sql import Search, Insert

if __name__ == '__main__':
    while True:
        try:
            for event in longpoll.listen():
                try:
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        if Search(event.object.message['from_id']) == None:
                            user = vk.users.get(
                                user_id=event.object.message['from_id'])
                            first_name = user[0]['first_name']
                            second_name = user[0]['last_name']
                            user_id = event.object.message['from_id']
                            Insert(first_name, second_name, user_id)
                        # print(user[0]['first_name'] +
                        #       " " + user[0]['last_name'])
                        x = threading.Thread(target=Main, args=(
                            event.chat_id, event.message.text))
                        x.start()
                except:
                    print('Сосни хуйца, всё сломалось')
                    print(traceback.print_exc())
                    break
        except:
            print('Сосни хуйца, всё сломалось')
            print(traceback.print_exc())
            break
