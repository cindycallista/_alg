def greedy_coin_change(amount, coins):
    coins = sorted(coins, reverse=True)
    result = []

    for c in coins:
        while amount >= c:
            amount -= c
            result.append(c)

    return result

if __name__ == "__main__":
    coins = greedy_coin_change(87, [50, 20, 10, 5, 1])
    print("Coins used:", coins)
