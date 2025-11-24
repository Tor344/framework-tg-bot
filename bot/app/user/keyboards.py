from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

user_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="user",callback_data='user_inline_keyboard')]])

user_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text="user",callback_data='user_keyboard')]])