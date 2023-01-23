from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\n 'Sharof Rashidov' nomidagi Samarqand davlat universitetining elektron kutubxona botiga xush kelibsiz\n\n Boshlash uchun quyidagi bo'limlardan birini tanlang",reply_markup=menu)
    
