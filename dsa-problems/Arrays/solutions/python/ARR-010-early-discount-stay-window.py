import sys
from collections import deque

def max_profit_with_constraints(prices: list[int], dMin: int, dMax: int, C: int) -> int:
    n = len(prices)
    dq = deque() # Stores indices
    max_profit = 0

    # Iterate through every possible SELL day j
    for j in range(dMin, n):
        # The buy date that just became valid is (j - dMin)
        buy_candidate = j - dMin

        # Maintain monotonic increasing deque
        while dq and prices[dq[-1]] >= prices[buy_candidate]:
            dq.pop()
        dq.append(buy_candidate)

        # Remove expired indices (window looking back size dMax)
        # Valid buy range is [j - dMax, j - dMin]
        # So index i is valid if i >= j - dMax.
        # Remove i if i < j - dMax.
        if dq[0] < j - dMax:
            dq.popleft()

        # Calculate profit
        min_buy_price = prices[dq[0]]
        sell_price = min(prices[j], C)
        max_profit = max(max_profit, sell_price - min_buy_price)

    return max_profit

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    dMin, dMax, C = map(int, input().split())

    result = max_profit_with_constraints(prices, dMin, dMax, C)
    print(result)

if __name__ == "__main__":
    main()

