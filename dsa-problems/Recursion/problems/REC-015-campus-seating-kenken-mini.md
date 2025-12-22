---
problem_id: REC_CAMPUS_SEATING_KENKEN_MINI__1579
display_id: REC-015
slug: campus-seating-kenken-mini
title: "Campus Seating KenKen Mini"
difficulty: Medium
difficulty_score: 59
topics:
  - Recursion
  - Backtracking
  - Constraint Satisfaction
tags:
  - recursion
  - backtracking
  - kenken
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-015: Campus Seating KenKen Mini
## Problem Statement
Solve a 4x4 KenKen-like puzzle. Fill digits 1 to 4 so that each row and column contains no repeated digits. Cages are provided with a target value and operation that must be satisfied by the digits in that cage.
Return any valid solution grid, or `NONE` if impossible.
![Problem Illustration](../images/REC-015/problem-illustration.png)
## Input Format
- First line: integer `c` (number of cages)
- Next `c` lines: `target op len r1 c1 r2 c2 ...`
  - `op` is one of `+`, `-`, `*`, `/`, or `=`
  - `len` is the number of cells in the cage
  - coordinates are zero-based
## Output Format
- If solvable, output 4 lines each with 4 integers
- Otherwise output `NONE`
## Constraints
- Grid size is fixed at 4x4
- `1 <= c <= 16`
- All cage cells are within the grid
## Example
**Input:**
```
16
1 = 1 0 0
2 = 1 0 1
3 = 1 0 2
4 = 1 0 3
3 = 1 1 0
4 = 1 1 1
1 = 1 1 2
2 = 1 1 3
2 = 1 2 0
1 = 1 2 1
4 = 1 2 2
3 = 1 2 3
4 = 1 3 0
3 = 1 3 1
2 = 1 3 2
1 = 1 3 3
```
**Output:**
```
1 2 3 4
3 4 1 2
2 1 4 3
4 3 2 1
```
**Explanation:**
Each row and column is a permutation of 1..4, and every single-cell cage matches its target.
![Example Visualization](../images/REC-015/example-1.png)
## Notes
- For `+` and `*`, order does not matter
- For `-` and `/`, use absolute difference or quotient between two values
- Use backtracking with row/column constraints
- Any valid solution is acceptable
## Related Topics
Backtracking, Constraint Satisfaction, Recursion
---
## Solution Template
### Java
```java
import java.util.*;
class Solution {
    public int[][] solveKenKen(List<int[]> cages) {
        // Your implementation here
        return new int[0][0];
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        List<int[]> cages = new ArrayList<>();
        for (int i = 0; i < c; i++) {
            int target = sc.nextInt();
            String op = sc.next();
            int len = sc.nextInt();
            int[] data = new int[3 + 2 * len];
            data[0] = target;
            data[1] = op.charAt(0);
            data[2] = len;
            for (int j = 0; j < len; j++) {
                data[3 + 2 * j] = sc.nextInt();
                data[4 + 2 * j] = sc.nextInt();
            }
            cages.add(data);
        }
        Solution solution = new Solution();
        int[][] result = solution.solveKenKen(cages);
        if (result.length == 0) {
            System.out.println("NONE");
        } else {
            for (int i = 0; i < 4; i++) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < 4; j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(result[i][j]);
                }
                System.out.println(sb.toString());
            }
        }
        sc.close();
    }
}
```
### Python
```python
def solve_kenken(cages: list[list[int]]) -> list[list[int]]:
    # Your implementation here
    return []
def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    c = int(next(it))
    cages = []
    for _ in range(c):
        target = int(next(it))
        op = next(it)
        length = int(next(it))
        coords = []
        for _ in range(length):
            r = int(next(it))
            c2 = int(next(it))
            coords.extend([r, c2])
        cages.append([target, ord(op), length] + coords)
    result = solve_kenken(cages)
    if not result:
        print("NONE")
    else:
        for row in result:
            print(" ".join(str(x) for x in row))
if __name__ == "__main__":
    main()
```
### C++
```cpp
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> solveKenKen(const vector<vector<int>>& cages) {
        // Your implementation here
        return {};
    }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int c;
    if (!(cin >> c)) return 0;
    vector<vector<int>> cages;
    for (int i = 0; i < c; i++) {
        int target, len;
        char op;
        cin >> target >> op >> len;
        vector<int> data(3 + 2 * len);
        data[0] = target;
        data[1] = op;
        data[2] = len;
        for (int j = 0; j < len; j++) {
            cin >> data[3 + 2 * j] >> data[4 + 2 * j];
        }
        cages.push_back(data);
    }
    Solution solution;
    vector<vector<int>> result = solution.solveKenKen(cages);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (j) cout << ' ';
                cout << result[i][j];
            }
            cout << "\n";
        }
    }
    return 0;
}
```
### JavaScript
```javascript
const readline = require("readline");
class Solution {
  solveKenKen(cages) {
    // Your implementation here
    return [];
  }
}
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const c = parseInt(data[idx++], 10);
  const cages = [];
  for (let i = 0; i < c; i++) {
    const target = parseInt(data[idx++], 10);
    const op = data[idx++];
    const len = parseInt(data[idx++], 10);
    const entry = [target, op.charCodeAt(0), len];
    for (let j = 0; j < len; j++) {
      const r = parseInt(data[idx++], 10);
      const c2 = parseInt(data[idx++], 10);
      entry.push(r, c2);
    }
    cages.push(entry);
  }
  const solution = new Solution();
  const result = solution.solveKenKen(cages);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.map((row) => row.join(" ")).join("\n"));
  }
});
```
