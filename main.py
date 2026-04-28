import asyncio
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, types

# Берем токен из настроек Render
TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_time_to_summer():
    now = datetime.now()
    year = now.year
    if now.month >= 6:
        year += 1
    summer_start = datetime(year, 6, 1, 0, 0, 0)
    diff = summer_start - now
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"До лета осталось: {days} дн., {hours} ч. и {minutes} мин. ☀️"

@dp.message()
async def summer_countdown(message: types.Message):
    if not message.text:
        return
    text = message.text.lower()
    # Проверка на разные варианты написания
    if ("лет" in text) and any(word in text for word in ["сколько", "скильки", "когда", "када", "осталось", "асталась"]):
        await message.reply(get_time_to_summer())

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
