def picker(prices):
    rest_of_prices = prices.copy()
    largest_profit = 0
    first_index = 0
    second_index= 0
    for price in prices:
        rest_of_prices.remove(price)
        for comp_price in rest_of_prices:
            if comp_price - price > largest_profit:
                largest_profit= comp_price - price
                first_index= prices.index(price)
                second_index = prices.index(comp_price)

    return [first_index,second_index]
