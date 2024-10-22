from aiogram.enums.chat_type import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message


class PrivateFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE
