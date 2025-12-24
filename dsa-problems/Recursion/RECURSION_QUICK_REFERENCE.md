# 🎯 RECURSION TEST CASES - QUICK REFERENCE

**Topic:** Recursion  
**Problems:** 16  
**Test Cases:** 607  
**Status:** ✅ Complete

---

## 📋 Problem List

| ID      | Problem                      | Cases | Difficulty | Algorithm                 |
| ------- | ---------------------------- | ----- | ---------- | ------------------------- |
| REC-001 | Dorm Room Paths              | 38    | Easy       | Grid DP / Combinatorics   |
| REC-002 | Lab ID Permutations No Twins | 38    | Easy       | Backtracking + Pruning    |
| REC-003 | Campus Ticket Packs          | 38    | Easy       | Coin Change DP            |
| REC-004 | Exam Seating Backtrack       | 38    | Medium     | N-Queens                  |
| REC-005 | Robot Route Turns            | 38    | Medium     | DP with State             |
| REC-006 | Subset Sum Exact Count       | 38    | Medium     | Backtracking              |
| REC-007 | Campus Lights Placement      | 38    | Medium     | Combinations + Constraint |
| REC-008 | Alternating Vowel Consonant  | 38    | Medium     | Backtracking              |
| REC-009 | Expression Target One Flip   | 38    | Medium     | Brute Force               |
| REC-010 | Restore Matrix Upper Bounds  | 38    | Medium     | Greedy                    |
| REC-011 | Campus Course Ordering       | 38    | Medium     | Topological Sort          |
| REC-012 | Knight Tour Blocked          | 38    | Hard       | Backtracking              |
| REC-013 | Palindrome Partition Min     | 38    | Medium     | DP + Backtracking         |
| REC-014 | Target Sum Limited Negations | 38    | Medium     | Bit Masking               |
| REC-015 | Campus Seating KenKen        | 38    | Hard       | CSP                       |
| REC-016 | Lexicographic Gray Code      | 37    | Medium     | Recursive Construction    |

---

## 🔑 Key Formulas & Algorithms

### Grid Paths (REC-001)

```
paths(r, c) = C(r+c-2, r-1) = (r+c-2)! / ((r-1)! * (c-1)!)
```

### Coin Change Count (REC-003)

```python
dp[0] = 1
for coin in coins:
    for i in range(coin, target+1):
        dp[i] += dp[i - coin]
```

### N-Queens Count (REC-004)

Known sequence (OEIS A000170):

- n=1: 1, n=2: 0, n=3: 0, n=4: 2
- n=5: 10, n=6: 4, n=7: 40, n=8: 92
- n=9: 352, n=10: 724, n=11: 2680, n=12: 14200

### Gray Code (REC-016)

```
G(n) = ['0' + g for g in G(n-1)] + ['1' + g for g in reversed(G(n-1))]
```

---

## 📊 Test Distribution

| Category  | Count   | Percentage |
| --------- | ------- | ---------- |
| Samples   | 48      | 7.9%       |
| Public    | 77      | 12.7%      |
| Hidden    | 482     | 79.4%      |
| **Total** | **607** | **100%**   |

---

## 🎯 Coverage Highlights

### Edge Cases

- ✅ Empty/minimal inputs (n=1, empty arrays)
- ✅ Maximum constraints (25×25 grids, n=14 N-Queens)
- ✅ Impossible cases (NONE, IMPOSSIBLE outputs)
- ✅ Duplicate handling

### Algorithm Types

- ✅ Simple Recursion (2 problems)
- ✅ Backtracking (7 problems)
- ✅ Dynamic Programming (4 problems)
- ✅ Greedy Algorithms (1 problem)
- ✅ Graph Algorithms (1 problem)
- ✅ Combinatorial Generation (1 problem)

---

## 🚀 Quick Start

### Generate Test Cases

```bash
cd /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems
python3 generate_recursion_testcases_part1.py  # REC-001 to REC-006
python3 generate_recursion_testcases_part2.py  # REC-007 to REC-016
```

### Verify Format

```bash
cd Recursion/testcases
for f in REC-*.yaml; do
    echo "$f: $(grep -c '^- input:' $f) cases"
done
```

### Count Total

```bash
find Recursion/testcases -name "*.yaml" -exec grep -c "^- input:" {} + | \
    awk '{sum+=$1} END {print "Total:", sum}'
```

---

## 📁 File Locations

```
dsa-problems/Recursion/
├── testcases/
│   ├── REC-001-dorm-room-paths.yaml
│   ├── REC-002-lab-id-permutations-no-twins.yaml
│   ├── ... (14 more files)
│   └── REC-016-lexicographic-gray-code.yaml
├── problems/
│   └── (16 problem markdown files)
├── editorials/
│   └── (16 editorial markdown files)
└── RECURSION_TEST_GENERATION_COMPLETE.md
```

---

## 💡 Common Patterns

### Backtracking Template

```python
def backtrack(path, remaining):
    if termination_condition:
        results.append(path[:])
        return

    for candidate in generate_candidates(remaining):
        if is_valid(candidate, path):
            path.append(candidate)
            backtrack(path, update_remaining(remaining))
            path.pop()
```

### Memoization Pattern

```python
memo = {}
def dp(state):
    if state in memo:
        return memo[state]

    if base_case(state):
        return base_value

    result = compute(state)
    memo[state] = result
    return result
```

---

## 🎓 Educational Value

### Difficulty Progression

- **Easy (3 problems)**: Basic recursion, simple DP
- **Medium (12 problems)**: Backtracking with constraints
- **Hard (1 problem)**: Complex constraint satisfaction

### Skills Developed

- Recursive thinking
- State space exploration
- Pruning techniques
- Constraint satisfaction
- Combinatorial generation

---

## ✅ Quality Metrics

- **Format**: 100% YAML compliance (`|-` syntax)
- **Coverage**: All edge cases included
- **Correctness**: Reference solutions verified
- **Distribution**: ~8% samples, ~13% public, ~79% hidden
- **Status**: Production ready

---

**Last Updated:** December 24, 2025  
**Generated By:** Automated Test Case Generation System
