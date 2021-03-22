import os
import logging
from asyncio import run_coroutine_threadsafe, get_event_loop, new_event_loop, sleep
from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher
from time import strftime, gmtime
from datetime import datetime
cc = datetime.today()
dd = cc.strftime('%d-%m-%Y_%H_%M')
papks = 'out'
name = "62163783649"




if not os.path.exists(papks):
    os.mkdir(papks)

os.system(f"ffmpeg.exe -i https://s1.moidom-stream.ru/s/public/0000000103.m3u8 neyroset/{papks}/{dd}.jpg")
os.system(f'python neyroset/scripts3/label_image.py --image neyroset/{papks}/{dd}.jpg')


bot = Bot(token='1255862313:AAFWPZqLgPlHH-SXkfji79nLshUjp_SqwDk')
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    print(message.chat.id)
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="узнать о состоянии Онежского озера ")
    keyboard.add(button_1)
   # button_2 = "когда встал лёд"
   # keyboard.add(button_2)
    await message.answer("я вас слушаю, хозяин", reply_markup=keyboard)
    #user_id = message.from_user.id


def otvet(file):
        f_read = open(file, "r")
        return f_read.readlines()[-1]

@dp.message_handler(text=['узнать о состоянии Онежского озера'])
async def process_help_command(message: types.Message):
    await message.reply(otvet("test.txt"))


#@dp.message_handler(text=['когда встал лёд'])
#async def process_help_command(message: types.Message):
 #   await message.reply("df")

async def otpravka(sleep1, sl2):
    while True:
        na_time = strftime('%M/%S', gmtime())
        print(na_time)
        if na_time == '59/59':
            print('час')
            await bot.send_message(1203720181, otvet("test.txt"))
        await sleep(sleep1)


if __name__ == "__main__":
    run_coroutine_threadsafe(otpravka(1, 1), get_event_loop())
    executor.start_polling(dp, skip_updates=True)