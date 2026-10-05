import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

TOKEN = "SIZNING_TOKENINGIZNI_SHU_YERGA_YOZING"
ADMIN_ID = "5064262839"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# (Barcha anketa funksiyalari va handlerlar o'zgarishsiz qoladi...)

async def main():
    print("Yangi bot ishga tushdi va ishlashga tayyor!")
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
