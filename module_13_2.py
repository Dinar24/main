from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '7719533784:AAFBtC4GKqJ_S_HupPO4V0b10fzEax3EfOA'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply('Привет! Я Бот, помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message: types.Message):
    await message.reply('Введите команду /start, чтоюы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)