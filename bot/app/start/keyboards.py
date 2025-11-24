from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="start",callback_data='start_inline_keyboard')]])

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text="start",callback_data='start_keyboard')]])