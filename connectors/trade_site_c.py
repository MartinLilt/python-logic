import time
from core.models import Quote

async def fetch_quotes():
    ts = time.time()
    return [
        # Чуть дешевле A, но главным будет маршрут A -> B
        Quote(platform="C", item_key="immortal_sword", item_name="Immortal Sword",
              buy_price=10.10, sell_price=10.70, stock_buy=3, stock_sell=6, updated_ts=ts),

        # Здесь выгодно продавать Arcana, если покупать на A
        Quote(platform="C", item_key="arcana_ember", item_name="Arcana Ember Spirit",
              buy_price=105.0, sell_price=112.0, stock_buy=2, stock_sell=2, updated_ts=ts),

        # Тут выгодно покупать Rare Gem и нести на B
        Quote(platform="C", item_key="rare_gem", item_name="Rare Gem",
              buy_price=6.20, sell_price=6.60, stock_buy=6, stock_sell=6, updated_ts=ts),
    ]
