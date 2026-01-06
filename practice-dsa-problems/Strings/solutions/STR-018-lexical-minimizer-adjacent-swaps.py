import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    k = int(input_data[1])
    n = len(s)
    char_indices = [[] for _ in range(26)]
    for i, char in enumerate(s):
        char_indices[ord(char) - ord("a")].append(i)
        
    for i in range(26):
        char_indices[i].reverse()
        
    bit = [0] * (n + 1)
    
    def update(idx, val):
        idx += 1
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)
            
    def query(idx):
        idx += 1
        res = 0
        while idx > 0:
            res += bit[idx]
            idx -= idx & (-idx)
        return res
        
    result = []
    for i in range(n):
        found = False
        for c in range(26):
            if not char_indices[c]:
                continue
            pos = char_indices[c][-1]
            
            # Count elements removed before `pos`
            removed_count = query(pos) # Range query sum of marked bits in [0, pos]?
            # `pos` is original index.
            # Actual index = pos - removed_count.
            # Wait, BIT tracks REMOVED elements (1 if removed).
            # Cost to move `pos` to front (current `i`) is `(pos - removed_count) - i`?
            # No.
            # We want to pick `pos` and move it to `i`.
            # Cost is number of swaps = distance.
            # Current logical position in the remaning array.
            # Array effectively shrinks? Or we fill `result[i]`.
            # If we pick element at original `pos`, its current index is `pos - query(pos - 1)`.
            # Wait, `query(p)` returns how many removed in [0...p].
            # So shifts = query(pos).
            # Current index = pos - query(pos).
            # But we are filling result index `i`.
            # We don't swapping to `i`. We just pick it.
            # Constraint is "k adjacent swaps".
            # Distance = (current_index) - 0? (If moving to front of remaining).
            # Current Index RELATIVE to remaining elements?
            # If we conceptually remove elements to result, the remaining shift left.
            # The cost to bring `pos` to front is exactly `pos - query(pos)`.
            # Assuming we only removed elements to the left?
            # Or removed elements anywhere?
            # The problem looks like: Construct lexicographically smallest string using at most K swaps.
            # Standard strategy: For each position `i` (0 to n-1), find smallest char in reachable range.
            # Reachable means `distance <= k`.
            # Distance of element at original `pos` is `pos - query(pos)`. (Since `query` counts removed).
            # Yes.
            
            current_pos = pos - query(pos)
            # Or query(pos-1)? `pos` is 0-indexed. query(x) usually 1-indexed sum [1..x+1]?
            # My update/query uses 1-based indexing for bit.
            # update(idx, 1) -> updates index idx+1.
            # query(idx) -> sums bit[1...idx+1]. Covers original indices 0...idx.
            # So count removed in [0...pos-1] is query(pos-1).
            # Then current_pos = pos - query(pos-1).
            
            dist = pos - query(pos - 1) # Cost to move to front
            # But wait, logic suggests cost is relative to 0?
            # The loop `for i in range(n)` fills result.
            # `dist` calculated is absolute position in remaining array (0-based).
            # Since we want to move to index 0 of remaining, cost is indeed `dist`.
            
            if dist <= k:
                k -= dist
                result.append(chr(ord("a") + c))
                char_indices[c].pop()
                update(pos, 1) # Mark pos as removed
                break
                
    print("".join(result))


if __name__ == "__main__":
    solve()
