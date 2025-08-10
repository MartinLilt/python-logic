import time
from core.models import Quote

async def fetch_quotes():
    ts = time.time()
    return [
        # Покупаем на A дёшево, продаём на B дороже
        Quote(platform="A", item_key="immortal_sword", item_name="Immortal Sword",
              buy_price=10.00, sell_price=10.80, stock_buy=5, stock_sell=10, updated_ts=ts),

        # Этот предмет выгоднее купить на A и продать на C
        Quote(platform="A", item_key="arcana_ember", item_name="Arcana Ember Spirit",
              buy_price=100.00, sell_price=104.00, stock_buy=2, stock_sell=3, updated_ts=ts),

        # Нейтральный для примера
        Quote(platform="A", item_key="rare_gem", item_name="Rare Gem",
              buy_price=6.50, sell_price=6.80, stock_buy=10, stock_sell=10, updated_ts=ts),
    ]
