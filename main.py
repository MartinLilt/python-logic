import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

from config import BOT_TOKEN, ADMIN_CHAT_ID, PLATFORMS, RISK, BASE_CURRENCY
from core.arbitrage import pairwise_deals
from core.formatting import as_table
from core.models import Quote

from connectors.trade_site_a import fetch_quotes as fetch_a
from connectors.trade_site_b import fetch_quotes as fetch_b
from connectors.trade_site_c import fetch_quotes as fetch_c

load_dotenv()

async def collect_all():
    qa, qb, qc = await asyncio.gather(fetch_a(), fetch_b(), fetch_c())
    quotes = qa + qb + qc

    by_item = {}
    for q in quotes:
        by_item.setdefault(q.item_key, {})[q.platform] = q
    return by_item

def rows_from_deals(deals):
    headers = ["Item", "Buy@X", "In", "StockX", "Sell@Y", "Out", "StockY", "Profit", "Margin%"]
    rows = []
    for d in deals:
        rows.append([
            d.item_name, d.buy_platform, f"{d.net_buy:.2f}",
            d.stock_buy, d.sell_platform, f"{d.net_sell:.2f}",
            d.stock_sell, f"{d.profit:.2f}", f"{d.margin_pct:.2f}",
        ])
    return headers, rows

async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот‑аналитик для арбитража между 3 трейд‑площадками.\n"
        "Команды:\n"
        "• /whoami — показать твой chat_id\n"
        "• /arbitrage — найти текущие связки (мок‑данные)\n"
        f"Базовая валюта: {BASE_CURRENCY}"
    )

async def cmd_whoami(message: Message):
    await message.answer(f"Твой chat_id: {message.chat.id}")

async def cmd_arbitrage(message: Message):
    by_item = await collect_all()
    deals = pairwise_deals(by_item, PLATFORMS, RISK)

    if not deals:
        await message.answer("❌ Нет подходящих сделок по заданным фильтрам.")
        return

    for d in deals[:10]:  # показываем топ-10
        text = (
            f"🎯 <b>{d.item_name}</b>\n"
            f"📥 Покупка: <b>{d.buy_platform}</b> — {d.net_buy:.2f} {BASE_CURRENCY} "
            f"(остаток: {d.stock_buy})\n"
            f"📤 Продажа: <b>{d.sell_platform}</b> — {d.net_sell:.2f} {BASE_CURRENCY} "
            f"(принимают: {d.stock_sell})\n"
            f"💰 Прибыль: <b>+{d.profit:.2f} {BASE_CURRENCY}</b>   "
            f"📈 Маржа: <b>+{d.margin_pct:.2f}%</b>"
        )
        await message.answer(text, parse_mode="HTML")

async def main():
    token = BOT_TOKEN or os.getenv("BOT_TOKEN", "")
    if not token:
        raise RuntimeError("Не найден BOT_TOKEN в .env")

    bot = Bot(token)
    dp = Dispatcher()
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_whoami, Command("whoami"))
    dp.message.register(cmd_arbitrage, Command("arbitrage"))

    print("Бот запущен. Нажми Ctrl+C для остановки.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
