from aiogram.types import \
    ReplyKeyboardMarkup, KeyboardButton

menu_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✉️ Xabar yuborish")
        ],
        # [
        #     KeyboardButton(text="Donat 🍩"),
        #     # KeyboardButton(text="Reklama boʻyicha 🤝")
        # ],
        # [
        #     KeyboardButton(text="test")
        # ]
    ],
    resize_keyboard=True
)
