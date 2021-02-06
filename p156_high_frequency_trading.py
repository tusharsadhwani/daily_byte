"""
You are given the list of prices of a particular stock. Each element in
the array represents the price of the stock at a given second throughout
the current day. Return the maximum profit you can make trading this
stock.

Note: You may only ever buy and sell a single share of the stock, but
you may make multiple transactions (i.e. buys and sells).

Ex: Given the following prices...

prices = [8, 3, 2, 4, 6, 4, 5], return 5.
"""


from typing import Optional


def max_profit(prices: list[int]) -> int:
    """Returns the maximum profit you can make trading given stock"""
    bought_price: Optional[int] = None
    total_profit = 0

    for index, price in enumerate(prices):
        if bought_price is None:
            if index + 1 == len(prices):
                # last value, no need to do anything
                break

            next_price = prices[index + 1]
            if next_price > price:
                bought_price = price

            continue

        if index + 1 == len(prices):
            # last value, sell it on a high
            total_profit += price - bought_price
            break

        next_price = prices[index + 1]
        if next_price < price:
            # at a peak, sell
            total_profit += price - bought_price
            bought_price = None

    return total_profit


def main() -> None:
    """Main function"""
    prices = [8, 3, 2, 4, 6, 4, 5]
    print(max_profit(prices))


if __name__ == '__main__':
    main()
