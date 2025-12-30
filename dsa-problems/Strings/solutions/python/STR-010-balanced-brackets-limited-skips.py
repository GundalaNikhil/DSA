def can_balance_with_skips(s: str, k: int) -> bool:
    balance = 0
    skips_used = 0

    for char in s:
        if char == '(':
            balance += 1
        else:  # char == ')'
            balance -= 1
            if balance < 0:
                # Need to skip this ')'
                skips_used += 1
                balance = 0

    # Remaining balance are unmatched '(' - need skips for them
    total_skips_needed = skips_used + balance
    return total_skips_needed <= k


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
