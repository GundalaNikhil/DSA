from typing import List

def max_profit(prices: List[int], fee: int) -> int:
    n = len(prices)
    NEG = -4 * 10**18
    buyable = 0
    hold = NEG
    unlock = [NEG] * (n + 8)
    ans = 0
    for i, p in enumerate(prices):
        if unlock[i] != NEG:
            buyable = max(buyable, unlock[i])
        prev_hold = hold
        hold = max(hold, buyable - p)
        if prev_hold != NEG:
            sell_profit = prev_hold + p - fee
            ans = max(ans, sell_profit)
            next_monday = i - (i % 7) + 7
            if next_monday < len(unlock):
                unlock[next_monday] = max(unlock[next_monday], sell_profit)
    if hold != NEG:
        ans = max(ans, hold + prices[-1] - fee)
    ans = max(ans, buyable)
    for val in unlock[n:]:
        ans = max(ans, val)
    return ans


def main():
    n, fee = map(int, input().split())
    prices = list(map(int, input().split()))
    print(max_profit(prices, fee))

if __name__ == "__main__":
    main()
