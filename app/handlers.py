from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


router = Router()



@router.message(Command("start"))
async def bot_start(message: Message):
    try:
        file_id = message.voice.file_id
        await message.answer(f"{file_id}")
    except Exception as e:
        await message.answer(f"Что то пошло не так: {e}")