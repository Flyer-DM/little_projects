import os
import requests
import soundfile as sf
import speech_recognition as sr
from aiogram import Bot
from aiogram.types import ContentType, Message
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


with open('token.txt', 'r') as token_file:
    token = token_file.read()

bot = Bot(token=token)
dp = Dispatcher(bot)
r = sr.Recognizer()


@dp.message_handler(content_types=[ContentType.TEXT])
async def text_message(message: Message):
    text = await message.text
    with open('answer.txt', 'w') as answer:
        answer.write(text)


@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message(message: Message):
    voice = await message.voice.get_file()
    path = voice.file_path
    oga_audio = os.getcwd() + '\\' + os.path.basename(path)
    wav_audio = oga_audio.replace('.oga', '.wav', 1)
    doc = requests.get(f'https://api.telegram.org/file/bot{token}/{path}')
    with open(f'{oga_audio}', 'wb') as f:
        f.write(doc.content)
    data, samplerate = sf.read(oga_audio)
    sf.write(wav_audio, data, samplerate)
    audio = sr.AudioFile(wav_audio)
    with audio as source:
        audio = r.record(source)
        try:
            await message.answer("Обработка сообщения...")
            text = r.recognize_google(audio, language='ru_RU')
            await message.answer("Сообщение:")
            await message.answer(str(text))
        except sr.UnknownValueError as e:
            await message.answer("Не удалось распознать сообщение.")
    os.remove(oga_audio)
    os.remove(wav_audio)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

