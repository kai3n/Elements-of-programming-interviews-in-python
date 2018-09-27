def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), float('-inf')

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit_sell_today, max_profit)
        min_price_so_far = min(price, min_price_so_far)
    return max_profit