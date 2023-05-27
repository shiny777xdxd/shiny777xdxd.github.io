from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

import configur

bot = Bot("5642410908:AAHmeZndLEJc7Z3F6BabomVGSt7zsc2wqtI")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton("Хаккинг"))
    markup.add(types.KeyboardButton("Деанон"))
    markup.add(types.KeyboardButton("Каталог", web_app=WebAppInfo(url="https://shiny777xdxd.github.io/sneak.html")))
    await message.answer("Наша команда подготовила для тебя множество услуг\товаров, так что выбирай и покупай! \n\nКоманда для поддержки - /support ", reply_markup=markup)


@dp.message_handler(commands=["pay_hak"])
async def payhak(message: types.message):
    await bot.send_invoice(message.chat.id, 'Приватка "Хаккинг"', 'Покупка приватки по хаккингу', 'invoice', configur.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Покупка приватки', 1000 * 100)])


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def pay(message: types.message):
    await message.answer(f'Вот ссылка на приватку:')


@dp.message_handler(content_types=["web_app_data"])
async def web_app(message: types.message):
    await message.answer(message.web_app_data.data)




executor.start_polling(dp)

