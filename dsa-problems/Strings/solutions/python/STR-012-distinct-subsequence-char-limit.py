def count_distinct_subsequences_with_limit(s: str, max_freq: int, MOD: int) -> int:
    from collections import defaultdict

    # State: tuple of frequencies for each character
    # Use dict to map state -> count
    dp = defaultdict(int)
    dp[tuple([0] * 26)] = 1  # Empty subsequence

    for char in s:
        char_idx = ord(char) - ord('a')
        new_dp = defaultdict(int)

        for state, count in dp.items():
            # Option 1: Don't include current character
            new_dp[state] = (new_dp[state] + count) % MOD

            # Option 2: Include current character (if allowed)
            if state[char_idx] < max_freq:
                new_state = list(state)
                new_state[char_idx] += 1
                new_state = tuple(new_state)
                new_dp[new_state] = (new_dp[new_state] + count) % MOD

        dp = new_dp

    # Sum all states
    total = sum(dp.values()) % MOD
    return total


def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    parts = input_data.split()
    if len(parts) >= 3:
        s = parts[0]
        try:
            max_freq = int(parts[1])
            MOD = int(parts[2])
            print(count_distinct_subsequences_with_limit(s, max_freq, MOD))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
