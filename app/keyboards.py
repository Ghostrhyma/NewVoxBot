from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


class MainKeyboard:
    TO_FEED = "Перейти к Vox-Ленте"
    TO_CREATE = "Записать свой Vox"


class VoxFeedKeyBoard:
    NEXT_VOX = "Мне нужен новый Vox!"
    TO_CREATE = MainKeyboard.TO_CREATE


class FeedKeyboard:
    LIKE = "👍"
    DISLIKE = "👎"
    COMMENT = "💬"

vox_feed_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=VoxFeedKeyBoard.NEXT_VOX),
     KeyboardButton(text=VoxFeedKeyBoard.TO_CREATE),
    ]
],
resize_keyboard=True,
input_field_placeholder="Выберите действие")

to_feed_from_create = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MainKeyboard.TO_FEED)]
])


main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MainKeyboard.TO_FEED),
     KeyboardButton(text=MainKeyboard.TO_CREATE),
    ]
],
resize_keyboard=True,
input_field_placeholder="Выберите действие")


feed_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=FeedKeyboard.LIKE, callback_data="like"),
     InlineKeyboardButton(text=FeedKeyboard.DISLIKE, callback_data="dislike"),
     InlineKeyboardButton(text=FeedKeyboard.COMMENT, callback_data="comment"),
    ]
],
resize_keyboard=True,
input_field_placeholder="Выберите действие")