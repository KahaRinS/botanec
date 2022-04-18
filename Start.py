import traceback
from main import Main
from sender import longpoll, VkBotEventType
import threading

if __name__ == '__main__':
    while True:
        try:
            for event in longpoll.listen():
                try:
                    if event.type == VkBotEventType.MESSAGE_NEW:
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
