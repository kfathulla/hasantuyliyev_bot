import logging
import uuid

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from src.config import Config
from src.filters.private_chat_filter import PrivateFilter
from src.keyboards.default.menu_keyboards import menu_keyboards
from src.loader import services
from src.models.users import User, UserFilter
from src.utils.misc import subscription

start_router = Router()


@start_router.message(PrivateFilter(), CommandStart())
async def user_start(message: Message, bot: Bot, config: Config):
    try:
        user = User()
        user.first_name = message.from_user.first_name
        user.last_name = message.from_user.last_name
        user.username = message.from_user.username or uuid.uuid4().__str__()
        user.telegram_id = message.from_user.id

        # user = await services.user_service.add_or_update_user(user)
        #
        # users = await services.user_service.get_all_users(user_filter=UserFilter(updated_datetime_from=None,
        #                                                                          updated_datetime_to=None))

        msg = """Assalomu alaykum. Ushbu bot orqali siz habaringizni Hasan Tuyliyevga yuborishingiz mumkin bo'ladi. 
            \nTaklif va murojatlarni yo'llashingiz mumkin.    
            \nBizni va o'zingizni vaqtingizni qadrlagan holda yozing.
            \nIltimos odob saqlang!"""
        await message.answer(text=msg, reply_markup=menu_keyboards)

        # msg = f"{user.__dict__} bazaga qo'shildi.\nBazada {users.total_count} ta foydalanuvchi bor."
        # for admin in config.tg_bot.admin_ids:
        #     await bot.send_message(chat_id=admin, text=msg)
    except Exception as ex:
        logging.error(ex)


@start_router.message(PrivateFilter(), F.text == "check_subs")
async def check_subs(call: CallbackQuery, bot: Bot, config: Config):
    await call.answer()
    result = str()
    for channel in config.misc.channel_ids:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✔ <b>{channel.title}</b> kanaliga obuna bo'lgansiz! \n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌️<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a> \n\n")

    await call.message.answer(result, disable_web_page_preview=True)
