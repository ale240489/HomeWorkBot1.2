from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_after_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_set = ReplyKeyboardMarkup(resize_keyboard=True)
kb_neutral = ReplyKeyboardMarkup(resize_keyboard=True)

btnStart = KeyboardButton('/start')
btnAfterStart = KeyboardButton('/rules_of_the_game')

btnNeutral = KeyboardButton('🎰')

btnSet_100 = KeyboardButton('/set 100')
btnSet_1000 = KeyboardButton('/set 1000')
btnSet_200 = KeyboardButton('/set 200')
btnSet_50 = KeyboardButton('/set 50')

kb_start.add(btnStart)
kb_after_start.add(btnAfterStart)
kb_set.add(btnSet_100, btnSet_200, btnSet_50, btnSet_1000)
kb_neutral.add(btnNeutral)
