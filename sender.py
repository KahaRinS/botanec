from Token import TOKEN
import vk_api
from vk_api import VkUpload
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


image = 'D:/Proga/2022/Botanec/botanec/photos/Danek.jpg'

session = vk_api.VkApi(
    token=TOKEN
)

upload = VkUpload(session)

global vk
vk = session.get_api()
longpoll = VkBotLongPoll(session, 212634817)


def sender(id, text):
    session.method('messages.send', {
        'chat_id': id, 'message': text, 'random_id': get_random_id()})


def sender_photo(id, text):
    attachments = []
    upload_image = upload.photo_messages(photos=image)[0]
    attachments.append('photo{}_{}'.format(
        upload_image['owner_id'], upload_image['id']))
    session.method('messages.send', {
        'chat_id': id, 'message': text, 'random_id': get_random_id(), 'attachment': ','.join(attachments)})
