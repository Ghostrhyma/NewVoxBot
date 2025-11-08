from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb

router = Router()

class GetVoice(StatesGroup):
    file_id = State()

@router.message(Command("start"))
async def bot_start(message: Message):
    await message.answer(text="Добро пожаловать в NewVox", reply_markup=kb.main_keyboard)


@router.message(F.text == kb.MainKeyboard.TO_FEED)
async def go_to_feed(message: Message):
    await message.answer("Заглушка для Вокс Ленты")


@router.message(F.text == kb.MainKeyboard.TO_CREATE)
async def create_new_vox(message: Message, state: FSMContext):
    await state.set_state(GetVoice.file_id)
    await message.answer("Запишите голосовое сообщение до 30 секунд")


@router.message(GetVoice.file_id)
async def get_voice(message: Message, state: FSMContext):
    try:
        if message.voice.duration > 30:
            await message.answer("Вы превысили допустимую длину сообщения")
        else:
            await state.update_data(file_id=message.voice.file_id)
            id_data = await state.get_data()
            fl_id = id_data["file_id"]

            await message.answer(f"ID гс - {fl_id}")
            await state.clear()
    except Exception as e:
        await message.answer(f"Вылезла ошибка: {e}")