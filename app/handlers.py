from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


router = Router()

class GetVoice(StatesGroup):
    file_id = State()

@router.message(Command("start"))
async def bot_start(message: Message, state: FSMContext):
    await state.set_state(GetVoice.file_id)
    await message.answer("Запишите голосовое сообщение до 30 секунд")
    # try:
    #     file_id = message.voice.file_id
    #     await message.answer(f"{file_id}")
    # except Exception as e:
    #     await message.answer(f"Что то пошло не так: {e}")


@router.message(GetVoice.file_id)
async def get_voice(message: Message, state: FSMContext):
    try:
        if message.voice.duration > 30:
            await message.answer("Вы превысили допустимую длину сообщения")
        else:
            await state.update_data(file_id=message.voice.file_id)
            id_data = state.get_data()
            fl_id = id_data["file_id"]

            await message.answer(f"ID гс - {fl_id}")
            await state.clear()
    except Exception as e:
        await message.answer(f"Вылезла ошибка: {e}")