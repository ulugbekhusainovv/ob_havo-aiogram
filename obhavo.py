from aiogram import types, Dispatcher, Bot, executor
from weatherapi import obhavo
token = "6675064296:AAHCBW0Kxb6q3J3FdaygWY8Hixv-IaAWWbk"

bot = Bot(token=token)
dispatcher = Dispatcher(bot=bot)

@dispatcher.message_handler(commands="start")
async def start(msg: types.Message):
    chatId = msg.from_user.id
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    userName = msg.from_user.username
    await bot.send_message(chat_id=chatId, text=f"Salom {first_name} botimizga hush kelibsiz bu bot sizga shahringizdagi ob-havo haqida ma'lumot beradi")

@dispatcher.message_handler(content_types="text")
async def message(msg:types.Message):
    chatId = msg.from_user.id
    first_name = msg.from_user.first_name
    # last_name = msg.from_user.last_name
    # userName = msg.from_user.username
    shahar = msg.text
    data = obhavo(shahar=shahar)
    if data == 'Error':
        await msg.answer("Ma'lumot topilmadi")
    else:
        await msg.answer(data)
            # await bot.send_message(chat_id=chatId, text=f"Salom {first_name} botga shaxar nomini kiriting")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher)