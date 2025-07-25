from aiogram.types import \
    ReplyKeyboardMarkup, KeyboardButton

menu_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✉️ Hasan Tuyliyevga murojaat")
        ],
        [
            KeyboardButton(text="🤵 Uylan do'stim! Masterklass"),
        ]
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
