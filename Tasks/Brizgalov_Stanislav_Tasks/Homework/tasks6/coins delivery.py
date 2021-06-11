from decimal import Decimal


def coins_delivery(user_money, cost):
    coins = {'2': "2 руб", '1': "1 руб", '0.50': "50 коп", '0.20': "20 коп", '0.10': "10 коп", '0.05': "5 коп",
             '0.02': "2 коп", '0.01': "1 коп"}
    delivery = Decimal(user_money) - Decimal(cost)
    counts_dict = {}
    for coin, name in coins.items():
        quantity_coin = delivery // Decimal(coin)
        if quantity_coin:
            counts_dict[name] = str(quantity_coin)
            delivery -= quantity_coin * Decimal(coin)
            if not delivery:
                break
    return counts_dict


print(coins_delivery('10.89', '3.20'))
