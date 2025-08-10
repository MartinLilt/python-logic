import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", "0"))
BASE_CURRENCY = os.getenv("BASE_CURRENCY", "EUR")

PLATFORMS = {
    "A": {"buy_fee": 0.03, "sell_fee": 0.03},
    "B": {"buy_fee": 0.04, "sell_fee": 0.02},
    "C": {"buy_fee": 0.05, "sell_fee": 0.03},
}

RISK = {
    "min_margin_pct": 6.0,
    "min_profit_abs": 0.40,
    "slippage_buffer_pct": 1.0,
    "freshness_sec": 120,
}
