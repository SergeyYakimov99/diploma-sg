from django.core.management.base import BaseCommand
from django.db.models import Q

from bot.models import TgUser
from bot.tg.client import TgClient
from bot.tg.dc import Message
from goals.models import Goal


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

    def handle_message(self, msg: Message):
        tg_user, created = TgUser.objects.get_or_create(
            tg_user_id=msg.msg_from.id,
            tg_chat_id=msg.chat.id
        )
        if created:
            tg_user.generate_verification_code()
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text=f"Подтвердите свой аккаунт, введите код: {tg_user.verification_code} на сайте."
            )
        elif msg.text == '/goals':
            # goals = Goal.objects.select_related("user", "category__board").filter(
            #     Q(category__board__participants__user_id=tg_user.user.id) & ~Q(status=Goal.Status.archived)
            # )
            goals = Goal.objects.filter(
                category__board__participants__user=tg_user.user).exclude(status=Goal.Status.archived)
            goals_list = '\n'.join([goal.title for goal in goals])
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text=f'Список целей: \n{goals_list}'
            )
        else:
            self.tg_client.send_message(
                chat_id=msg.chat.id,
                text=f"Неизвестная команда"
            )

    def handle(self, *args, **options):
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                if hasattr(item, 'message'):
                    self.handle_message(item.message)


