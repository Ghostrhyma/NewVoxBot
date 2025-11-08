from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class MainKeyboard:
    TO_FEED = "Перейти к Vox-Ленте"
    TO_CREATE = "Записать свой Vox"


class FeedKeyboard:
    LIKE = "👍"
    DISLIKE = "👎"
    COMMENT = "💬"
    TO_CREATE = MainKeyboard.TO_CREATE


main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MainKeyboard.TO_FEED),
     KeyboardButton(text=MainKeyboard.TO_CREATE),
    ]
],
resize_keyboard=True,
input_field_placeholder="Выберите действие")


feed_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=FeedKeyboard.LIKE),
     KeyboardButton(text=FeedKeyboard.DISLIKE),
     KeyboardButton(text=FeedKeyboard.COMMENT),
     KeyboardButton(text=FeedKeyboard.TO_CREATE),
    ]
],
resize_keyboard=True,
input_field_placeholder="Выберите действие")