import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
import config
from main import get_info_from_file
from datetime import datetime
from aiogram import html



logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Понедельник")],
        [types.KeyboardButton(text="Вторник")],
        [types.KeyboardButton(text="Среда")],
        [types.KeyboardButton(text="Четверг")],
        [types.KeyboardButton(text="Пятница")],
        [types.KeyboardButton(text="Суббота")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                         input_field_placeholder='Выбери день недели')
    await message.answer("На какой день недели хочешь узнать расписание?", reply_markup=keyboard)


@dp.message(F.text.lower())
async def with_puree(message: types.Message):
    print(F.text.lower())
    time_now = datetime.now().strftime('%H:%M')
    added_text = html.underline(f"Создано в {time_now}")
    day_week = html.bold(message.text)
    await message.answer(f'{day_week}\n{get_info_from_file(message.text.lower())}\n\n{added_text}', parse_mode="HTML")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
