import logging
import uuid

from aiogram import Router, F, Bot
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart

from src.config import Config
from src.filters.private_chat_filter import PrivateFilter
from src.keyboards.default.menu_keyboards import menu_keyboards
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
        msg = f"""#yigitlarga

Uylan do'stim!

Inson hayotini eng ahamyatli voqealaridan biri bu oila qurish.

Uzoq kutilgan (rosti men ham intiqib kutgan) kun nasib 26-iyul 21.00 da yopiq telegram kanalda yigitlar uchun alohida uylanish mavzusida suhbat qilib bermoqchiman.

Unda Ustozlardan , kitoblardan va yaqinlarimizdan o'rgangan amaliy bilimlarni bermoqchiman.

Quyida suhbatda ko'riladigan ayrim masalalar 

Puli bor sog'lom yigit oila quishga tayyormasmi?

Qanday tayyorlanalidi o'zi? 

Menga mos qiz O'zbekistonda bormi?

Qaysida xayr bor ilmli ko'cha qizidami yoki ilmsiz uy qizida?

. ......

Boshqa yan ko'plab muhim masalalarga milliy qadriyatlarimizdan kelib chiqib to'xtalib o'tamiz.

Bu suhbat uchun maxsus tayyorlanyabman va nasib siz kutgandan ko'pini aytamiz.

Suhbatga qo'shilish uchun botga kiring


@hasantuyliyev_bot
@hasantuyliyev_bot
@hasantuyliyev_bot
@hasantuyliyev_bot"""
        await message.answer_photo(caption=msg, reply_markup=menu_keyboards, photo="AgACAgIAAxkDAAIJYmiDT92_ksbCIe8G9xGUqJqcDd47AAJ38TEbFPgYSFrksBR7dmX8AQADAgADeQADNgQ")
        # photo = await message.answer_photo(caption=msg, photo=FSInputFile("uploads/start_img.jpg"))
        # print(photo.photo[-1].file_id)
    except Exception as ex:
        logging.error(ex)


@start_router.callback_query(PrivateFilter(), F.data == "check_subs")
async def check_subs(call: CallbackQuery, bot: Bot, config: Config):
    await call.answer()
    result = str()
    for channel in config.misc.channel_ids:
        status = await subscription.check(bot, user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✔ <b>{channel.title}</b> kanaliga obuna bo'lgansiz! \n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌️<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a> \n\n")

    await call.message.answer(result, disable_web_page_preview=True)
