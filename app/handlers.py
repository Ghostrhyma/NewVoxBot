from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb
import app.func_json as fjson

router = Router()

class GetVoice(StatesGroup):
    file_id = State()


@router.message(Command("start"))
async def bot_start(message: Message):
    await message.answer(text="Добро пожаловать в NewVox", reply_markup=kb.main_keyboard)


@router.message(F.text == kb.MainKeyboard.TO_FEED)
async def go_to_feed(message: Message):
    await message.answer("Вы перешли в Vox-Ленту", reply_markup=kb.vox_feed_keyboard)


@router.message(F.text == kb.MainKeyboard.TO_CREATE)
async def create_new_vox(message: Message, state: FSMContext):
    await state.set_state(GetVoice.file_id)
    await message.answer("Запишите голосовое сообщение до 2 минут\nСообщения дольше 2х минут приниматься не будут",
                        reply_markup=kb.to_feed_from_create)


@router.message(GetVoice.file_id)
async def get_voice(message: Message, state: FSMContext):
    try:
        if message.voice.duration > 120:
            await message.answer("Вы превысили допустимую длину сообщения\n" \
            "Попробуйте еще раз")
        else:
            await state.update_data(file_id=message.voice.file_id)
            id_data = await state.get_data()
            fl_id = id_data["file_id"]

            full_name = message.from_user.full_name
            username = message.from_user.username

            voice_caption = f"{full_name}\n{username}"

            vox = {
                "file_id": fl_id,
                "caption": voice_caption,
                "username": username
            }

            await fjson.add_to_json("app/voxes.json", vox)
            await message.answer("Вы создали новый Vox!", reply_markup=kb.main_keyboard)
            await state.clear()
    except AttributeError:
        await message.answer("Это не голосовое сообщение\n" \
        "Попробуйте еще раз")


@router.message(F.text == kb.VoxFeedKeyBoard.NEXT_VOX)
async def next_vox(message: Message):
    voxes = await fjson.read_from_json("app/voxes.json")
    await message.answer_voice(voice=voxes[0]["file_id"], caption=voxes[0]["caption"], reply_markup=kb.feed_keyboard)