import datetime
import keyboard
from aiogram import types
from create import dp
import random as rnd
import logFile
total_candie = 100


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    logFile.createNewLogFile(f'game start: {message.from_user.first_name}')
    await message.answer(f'{message.from_user.first_name} привет тебе!!!  Этот бот для игры в 🍬🍬🍬! Давай играть!'
                         f'Ознакомься с /rules_of_the_game'
                         , reply_markup=keyboard.kb_after_start)


@dp.message_handler(commands=['set'])
async def mes_start(message: types.Message):
    global total_candie
    count = message.text.split()[1]
    total_candie = int(count)
    await message.answer(f'Стартовое количество 🍬: {total_candie}')
    logFile.addInfoInLog(f' count candies = {total_candie}')
    await message.answer('Забирай!, набери нужное количество...', reply_markup=keyboard.kb_neutral)
@dp.message_handler(commands=['rules_of_the_game'])
async def mes_help(message: types.Message):
    await message.answer('🔴 Через команду "/set " задается стартовое '
                         'количество 🍬🍬🍬 \n'
                         '🔴 Дальше мы с тобой поочереди забираем 🍬🍬🍬(но не более 28 за раз!!!!)\n'
                         '🔴Выигрывает тот, кто забирает последним!!! 🏎', reply_markup=keyboard.kb_set)

@dp.message_handler()
async def mes_candies(message: types.Message):
    global total_candie
    bot_candies = rnd.randint(0, 28)
    if message.text.isdigit():
        if int(message.text) <= 28:
            total_candie -= int(message.text)
            await message.answer(f'👉Ты забрал {message.text} 🍬, осталось {total_candie} конфет.')
            if total_candie == 0:
                await message.answer(f'👉👉👉Ты 🏆🥇! Что бы сыграть еще, задай заново стартовое количество конфет!')
                logFile.addInfoInLog(' winner'+ '\n')
            else:
                if total_candie > 56:
                    total_candie -= bot_candies
                    await message.answer(f'🤖  забрал {bot_candies} 🍬, осталось {total_candie} 🍬.')
                elif total_candie <=56 and total_candie > 28:
                    bot_candies = (29 - total_candie) * (-1)
                    total_candie -= bot_candies
                    await message.answer(f'🤖  забрал {bot_candies} 🍬, осталось {total_candie} 🍬.')
                elif total_candie <= 28:
                    bot_candies = total_candie
                    total_candie -= bot_candies
                    logFile.addInfoInLog(' lost' + '\n')
                    await message.answer(f'🤖  забрал {bot_candies} 🍬, осталось {total_candie} 🍬\n'
                                         f'🤖  🏆🏆🏆!!!'
                                         f'Если хочешь еще, нажми старт', reply_markup=keyboard.kb_start)


                elif total_candie == 29:
                    bot_candies = 1
                    total_candie -= bot_candies
                    await message.answer(f'🤖  забрал {bot_candies} 🍬, осталось {total_candie} 🍬.')
        else:
            await message.answer('‼️Не больше 28!')


