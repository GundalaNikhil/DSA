import sys
sys.path.insert(0, 'solutions/python')

from DP_006_strict_jump_lis_bounded import longest_bounded_diff_subsequence

# Test from hidden: n=50000, a=[0,1,2...49999], d=0, g=5
# Expected: 50000
result = longest_bounded_diff_subsequence(list(range(50000)), 0, 5)
print(f'Result: {result}, Expected: 50000')

# Simpler test: [0,1,2,3,4], d=0, g=5 - should be 5 (all)
result2 = longest_bounded_diff_subsequence([0, 1, 2, 3, 4], 0, 5)
print(f'Small test: {result2}, Expected: 5')
