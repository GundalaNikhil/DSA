
def pile_split_game(n: int) -> str:
    if n == 0:
        return "Second"
    
    g = [0] * (n + 1)
    
    for i in range(3, n + 1):
        reachable = set()
        # Split into j and i-j.
        # j goes from 1 up to (i-1)//2
        for j in range(1, (i - 1) // 2 + 1):
            reachable.add(g[j] ^ g[i - j])
        
        mex = 0
        while mex in reachable:
            mex += 1
        g[i] = mex
        
    return "First" if g[n] > 0 else "Second"

test_cases = [
    (3, "First"),
    (4, "Second"),
    (1, "Second"),
    (2, "Second"),
    (5, "First"),
    (6, "First"),
    (7, "Second"),
    (8, "First"),
    (9, "First"),
    (10, "Second"),
    (11, "First"),
    (12, "First"),
    (13, "First"),
    (14, "First"),
    (15, "Second"),
    (16, "First"),
    (17, "First"),
    (18, "First"),
    (19, "First"),
    (20, "Second"),
    (21, "First"),
    (22, "Second"),
    (23, "First"),
    (24, "First"),
    (25, "Second"),
    (26, "First"),
    (27, "First"),
    (28, "First"),
    (29, "First"),
    (30, "First"),
    (50, "First"),
    (100, "First"),
    (128, "First"),
    (256, "First"),
    (500, "Second"),
    (1000, "First"),
    (1999, "First"),
    (2000, "First"),
    (123, "First"),
    (456, "First"),
    (789, "First"),
    (999, "First"),
    (1024, "First"),
    (1500, "First"),
    (1777, "First")
]

failed = False
for n, expected in test_cases:
    got = pile_split_game(n)
    if got != expected:
        print(f"Failed: n={n}, Expected={expected}, Got={got}")
        failed = True

if not failed:
    print("All GMT-001 tests passed!")
