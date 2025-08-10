from pydantic import BaseModel
from typing import Optional

class Quote(BaseModel):
    platform: str
    item_key: str
    item_name: str
    buy_price: float
    sell_price: float
    stock_buy: int
    stock_sell: int
    trade_lock: bool = False
    updated_ts: float = 0.0

class DealCandidate(BaseModel):
    item_key: str
    item_name: str
    buy_platform: str
    sell_platform: str
    net_buy: float
    net_sell: float
    profit: float
    margin_pct: float
    stock_buy: int
    stock_sell: int
    notes: Optional[str] = None
