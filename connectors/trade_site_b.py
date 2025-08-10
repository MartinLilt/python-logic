import time
from core.models import Quote

async def fetch_quotes():
    ts = time.time()
    return [
        # На B продаём дороже, чем покупаем на A
        Quote(platform="B", item_key="immortal_sword", item_name="Immortal Sword",
              buy_price=10.90, sell_price=11.50, stock_buy=5, stock_sell=5, updated_ts=ts),

        # Arcana тут не так интересна (чтобы показать разные варианты)
        Quote(platform="B", item_key="arcana_ember", item_name="Arcana Ember Spirit",
              buy_price=106.0, sell_price=108.0, stock_buy=1, stock_sell=2, updated_ts=ts),

        # Rare Gem тут как приёмник — выгодно продавать сюда из C
        Quote(platform="B", item_key="rare_gem", item_name="Rare Gem",
              buy_price=7.60, sell_price=7.90, stock_buy=8, stock_sell=8, updated_ts=ts),
    ]
