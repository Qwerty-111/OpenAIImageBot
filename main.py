import requests
from aiogram import Bot, Dispatcher, executor, types

import openai
from PIL import Image
import io

# Устанавливаем токен для Telegram-бота
bot = Bot(token='6117480297:AAHuOcXYTpynU_Emib7k6p5x0yU7sBbgmo4')

dp = Dispatcher(bot=bot)

# Устанавливаем ключ API для DALL-E 2
openai.api_key = "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"


# Обработчик команды /generate
@dp.message_handler(commands=['generate'])
async def generate_image(message: types.Message):
    # Получаем описание изображения из команды пользователя
    description = message.text.lower()

    # Генерируем изображение на основе описания с помощью DALL-E 2
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="512x512"
    )
    print(response)

    # Получаем ссылку на сгенерированное изображение
    image_url = response['data'][0]['url']

    # Загружаем изображение из ссылки
    image = Image.open(io.BytesIO(requests.get(image_url).content))

    # Отправляем изображение пользователю через Telegram-бота
    await message.reply_photo(photo=image)



if __name__ == '__main__':
    executor.start_polling(dp)