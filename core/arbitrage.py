from .models import Quote, DealCandidate

def pairwise_deals(item_quotes: dict, fees: dict, risk: dict):
    """
    item_quotes: dict[str, dict[str, Quote]]
    пример: {"immortal_sword": {"A": Quote(...), "B": Quote(...), "C": Quote(...)}}
    """
    candidates = []
    sl = risk.get("slippage_buffer_pct", 0) / 100.0
    min_profit = risk.get("min_profit_abs", 0)
    min_margin = risk.get("min_margin_pct", 0)

    for key, per_platform in item_quotes.items():
        platforms = list(per_platform.keys())
        for i in range(len(platforms)):
            for j in range(len(platforms)):
                if i == j:
                    continue
                X, Y = platforms[i], platforms[j]
                qx, qy = per_platform[X], per_platform[Y]

                # базовые проверки
                if qx.stock_buy <= 0 or qy.stock_sell <= 0 or qx.trade_lock or qy.trade_lock:
                    continue

                buy_fee  = fees[X]["buy_fee"]
                sell_fee = fees[Y]["sell_fee"]

                net_buy  = (qx.buy_price  * (1 + buy_fee))  * (1 + sl)
                net_sell = (qy.sell_price * (1 - sell_fee)) * (1 - sl)

                profit = net_sell - net_buy
                margin = (profit / net_buy) * 100 if net_buy > 0 else -999

                if profit >= min_profit and margin >= min_margin:
                    candidates.append(DealCandidate(
                        item_key=key, item_name=qx.item_name,
                        buy_platform=X, sell_platform=Y,
                        net_buy=round(net_buy, 2), net_sell=round(net_sell, 2),
                        profit=round(profit, 2), margin_pct=round(margin, 2),
                        stock_buy=qx.stock_buy, stock_sell=qy.stock_sell
                    ))

    candidates.sort(key=lambda d: (d.profit, d.margin_pct), reverse=True)
    return candidates[:20]
