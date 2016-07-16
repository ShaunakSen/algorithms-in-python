def coin_change_rec(target, coins):
    min_coins = target

    if target in coins:
        return 1
    else:
        for coin in coins:
            if coin <= target:
                num_coins = 1 + coin_change_rec(target - coin, coins)
            if num_coins < min_coins:
                min_coins = num_coins
        return min_coins


def coin_change_dynamic(target, coins, known_results):
    min_coins = target
    if target in coins:
        known_results[target] = 1
        return 1
    elif known_results[target] > 0:
        return known_results[target]

    else:
        for coin in coins:
            if coin <= target:
                num_coins = 1 + coin_change_dynamic(target - coin, coins, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins
        return min_coins


print coin_change_rec(10, [1, 5])

target = 74
coins = [1, 5, 10, 25]
known_results = [0] * (target+1)
print coin_change_dynamic(target, coins, known_results)
