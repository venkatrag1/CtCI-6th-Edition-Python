import sys

def num_coins(den, val):
    # for each coin
    #   num_coins(den, val) +=  min(1+ num_coins(den, val - den[i]),
    cache = [sys.maxint] * (val + 1)
    cache[0] = 0

    for coin in den:
        for v in range(coin, val+1):
            num_ways = cache[v-coin]
            if num_ways < sys.maxint:
                cache[v] = min(cache[v], num_ways + 1)
    return cache[val]


if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    V = 11
    print("Minimum coins required is %d" %(num_coins(coins, V)))




