import logging

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from src.config import Config
from src.filters.private_chat_filter import PrivateFilter
from src.keyboards.default.cancel import cancel_button
from src.keyboards.default.menu_keyboards import menu_keyboards
from states.message_state import MessageFormState

message_router = Router()


@message_router.message(PrivateFilter(), F.text == "✉️ Xabar yuborish")
async def message_handler(message: Message, state: FSMContext, bot: Bot):
    try:
        await state.set_state(MessageFormState.AnonymousMessage)
        text = ("Iltimos murojaat yoki taklifingizni imkon qadar qisqa va tushunarliroq qilib yozing."
                "\n\nIltimos murojaat yoki taklifingizni bitta xabarda yozib qoldiring.")
        await message.answer(text=text, reply_markup=cancel_button)
        # photo = await message.answer_photo(photo=InputFile("uploads/images/img.png"))
        # print(photo.photo[-1].file_id)
    except Exception as ex:
        logging.error(ex)


@message_router.message(PrivateFilter(), F.text == "🚫 Bekor qilish", MessageFormState.AnonymousMessage)
async def cancel_message_form(message: Message, state: FSMContext):
    try:
        await state.clear()
        await message.answer(text="Pastdan oʻzingizga kerakli boʻlimni tanlang", reply_markup=menu_keyboards)
    except Exception as ex:
        logging.error(ex)


@message_router.message(PrivateFilter(), MessageFormState.AnonymousMessage)
async def enter_message(message: Message, state: FSMContext, bot: Bot, config: Config):
    await state.clear()
    # user = await services.user_service.get_user_by_telegram_id(telegram_id=message.from_user.id)
    # if user is None or user.id == 0:
    #     user = User()
    #     user.username = message.from_user.username
    #     user.first_name = message.from_user.first_name
    #     user.last_name = message.from_user.last_name
    #     user.telegram_id = message.from_user.id
    #     user = await services.user_service.add_user(user=user)

    # for admin in config.ADMINS:
    #     await message.bot.send_message(chat_id=admin, text=f"{message.from_user.full_name}({(message.from_user.id)}) "
    #                                                        f"dan yangi murojat: ")
    #     await message.bot.send_message(chat_id=admin, text=message.html_text, parse_mode="HTML")
    group_msg = await message.forward(chat_id=config.misc.group_id)
    murojaat = await group_msg.reply(f"Yangi xabar: {message.message_id}"
                          f"\nuser_id: {message.from_user.id}"
                          f"\n{message.from_user.full_name} ( {message.from_user.url} ) (@{message.from_user.username})"
                          f"ning murojati:")


    await message.answer(f"Murojatingiz qabul qilindi.", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"Pastdan oʻzingizga kerakli boʻlimni tanlang", reply_markup=menu_keyboards)
