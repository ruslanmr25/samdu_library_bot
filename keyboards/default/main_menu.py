from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu=ReplyKeyboardMarkup(
     resize_keyboard=True,
     keyboard=[
          [KeyboardButton("🗂Kategoriyalar")],
          [KeyboardButton("🔎 Izlash"),KeyboardButton("📚Tasodifiy kitob")]
     ]
     
     
)