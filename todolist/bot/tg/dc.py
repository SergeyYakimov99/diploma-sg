from dataclasses import field, dataclass
from typing import List

import marshmallow_dataclass
from marshmallow import EXCLUDE


@dataclass
class MessageFrom:
    id: int
    is_bot: bool
    first_name: str | None
    last_name: str | None
    username: str | None

    class Meta:
        unknown = EXCLUDE


@dataclass
# class MessageChat:
class Chat:
    id: int
    first_name: str | None
    last_name: str | None
    title: str | None
    type: str
    username: str | None

    class Meta:
        unknown = EXCLUDE


@dataclass
class Message:
    message_id: int
    msg_from: MessageFrom = field(metadata={'data_key': 'from'})
    chat: Chat
    date: int
    text: str | None

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateObj:
    update_id: int
    message: Message

    class Meta:
        unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateObj]

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message

    class Meta:
        unknown = EXCLUDE


GET_UPDATES_SCHEMA = marshmallow_dataclass.class_schema(GetUpdatesResponse)()
SEND_MESSAGE_RESPONSE = marshmallow_dataclass.class_schema(SendMessageResponse)()
