from django.core.management.base import BaseCommand
from bot.models import TgUser
from bot.tg.client import TgClient
from bot.tg.dc import Message


class Command(BaseCommand):
    help = 'Runs telegram bot'
    tg_client = TgClient("5871475478:AAEIrz8pK8Ep7KUhI23AKAvkRIZAqcYjsAc")

    def handle_unverified_user(self, msg: Message, tg_user: TgUser):
        code = '123'
        tg_user.verification_code = code
        tg_user.save()
        self.tg_client.send_message(
            chat_id=msg.chat.id,
            text=f' {code}'
        )

    def handle_user(self, msg: Message):
        tg_user = TgUser.objects.filter(tg_user_id=msg.msg_from.id)
        if not tg_user:
            self.tg_client.send_message(chat_id=msg.chat.id, text='Привет!')
        else:
            self.tg_client.send_message(chat_id=msg.chat.id, text='Уже был!')

    def handle(self, *args, **options):
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
#                self.handle_user(item.message)
                print(item.message)
