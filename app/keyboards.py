from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class MainKeyboard:
    TO_FEED = "Перейти к Вокс Ленте"
    TO_CREATE = "Записать свой Вокс"


main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MainKeyboard.TO_FEED),
     KeyboardButton(text=MainKeyboard.TO_CREATE),
    ]
],
resize_keyboard=True,
input_field_placeholder="Выберите действие")