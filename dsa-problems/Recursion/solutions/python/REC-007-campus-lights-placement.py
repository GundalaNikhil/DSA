def place_lights(n: int, k: int, d: int) -> list[list[int]]:
    """
    Find all valid placements of k lights on positions 0 to n-1.
    Any two lights must be at least d positions apart.
    """
    if k == 0:
        return [[]]

    result = []

    def backtrack(start_pos, lights_placed, current_placement):
        # Base case: we've placed all k lights
        if lights_placed == k:
            result.append(current_placement[:])
            return

        # Pruning: not enough remaining positions to place remaining lights
        remaining_lights = k - lights_placed
        remaining_positions = n - start_pos
        if remaining_positions < remaining_lights:
            return

        # Try placing a light at each remaining position
        for pos in range(start_pos, n):
            # Check if we can place a light at this position
            # It must be at least d positions away from the last placed light
            if not current_placement or pos - current_placement[-1] >= d:
                current_placement.append(pos)
                backtrack(pos + 1, lights_placed + 1, current_placement)
                current_placement.pop()

    backtrack(0, 0, [])
    return result

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, k, d = map(int, data[:3])
    result = place_lights(n, k, d)
    if not result:
        print("NONE")
    else:
        for combo in result:
            print(" ".join(str(x) for x in combo))

if __name__ == "__main__":
    main()
