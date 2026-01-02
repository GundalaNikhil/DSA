---
problem_id: STK_CONVEYOR_WEIGHTED_DEDUPLICATION__5318
display_id: STK-003
slug: conveyor-weighted-deduplication
title: "Conveyor Weighted Deduplication"
difficulty: Easy
difficulty_score: 36
topics:
  - Stack
  - Simulation
  - Strings
tags:
  - stack
  - simulation
  - strings
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-003: Conveyor Weighted Deduplication

## Problem Statement

You are given a string `s` and an array of weights `w` of the same length. Process characters from left to right. When the current character matches the top of the stack, you may remove the pair only if the sum of their weights is even. The removed sum is added to a running total. The remaining characters form the reduced string.

Output the reduced string and the total removed weight.

![Problem Illustration](../images/STK-003/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: `n` space-separated integers `w[i]` (where `n = |s|`)

## Output Format

- First line: reduced string
- Second line: total removed weight

## Constraints

- `1 <= |s| <= 200000`
- `1 <= w[i] <= 1000`

## Example

**Input:**

```
xxyyz
1 3 2 2 5
```

**Output:**

```
xyz
4
```

**Explanation:**

The pair `y` with weights 2 and 2 is removed, contributing 4 to the total.

![Example Visualization](../images/STK-003/example-1.png)

## Notes

- Use a stack of (char, weight)
- Only adjacent equal characters can be removed
- Each character is pushed and popped at most once
- Time complexity: O(n)

## Related Topics

Stack, Simulation, String Processing

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    class Item {
        char c;
        int w;
        Item(char c, int w) {
            this.c = c;
            this.w = w;
        }
    }

    public String[] reduce(String s, int[] w) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            StringBuilder sBuilder = new StringBuilder();
            int[] w = new int[n];
            
            for (int i = 0; i < n; i++) {
                if (sc.hasNext()) {
                    String c = sc.next();
                    sBuilder.append(c);
                    if (sc.hasNextInt()) {
                        w[i] = sc.nextInt();
                    }
                }
            }
            
            Solution sol = new Solution();
            String[] res = sol.reduce(sBuilder.toString(), w);
            
            if (res[0].isEmpty()) {
                System.out.println("EMPTY " + res[1]);
            } else {
                System.out.println(res[0] + " " + res[1]);
            }
        }
        sc.close();
    }
}
```

### Python

```python
def reduce_stack(s: str, w: list[int]) -> tuple[str, int]:
    return ""
def main():
    import sys
    # Read all lines
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        chars = []
        weights = []
        for _ in range(n):
            chars.append(next(iterator))
            weights.append(int(next(iterator)))
        
        s = "".join(chars)
        
        res_s, res_removed = reduce_stack(s, weights)
        
        if not res_s:
            print(f"EMPTY {res_removed}")
        else:
            print(f"{res_s} {res_removed}")
            
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

struct Item {
    char c;
    int w;
};

class Solution {
public:
    pair<string, long long> reduce(string s, vector<int> w) {
        vector<Item> stack; // Use vector as stack for easy iteration
        long long totalRemoved = 0;
        
        for (size_t i = 0; i < s.length(); i++) {
            char currentChar = s[i];
            int currentWeight = w[i];
            
            if (!stack.empty() && stack.back().c == currentChar && (stack.back().w + currentWeight) % 2 == 0) {
                totalRemoved += (long long)stack.back().w + currentWeight;
                stack.pop_back();
            } else {
                stack.push_back({currentChar, currentWeight});
            }
        }
        
        string resS = "";
        for (const auto& item : stack) {
            resS += item.c;
        }
        
        return {resS, totalRemoved};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    string s = "";
    vector<int> w(n);
    
    for (int i = 0; i < n; i++) {
        char c;
        int weight;
        cin >> c >> weight;
        s += c;
        w[i] = weight;
    }
    
    Solution sol;
    pair<string, long long> res = sol.reduce(s, w);
    
    if (res.first.empty()) {
        cout << "EMPTY " << res.second << endl;
    } else {
        cout << res.first << " " << res.second << endl;
    }
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  reduce(s, w) {
    return 0;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});

rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  let s = "";
  const w = [];
  
  for (let i = 0; i < n; i++) {
    s += data[idx++];
    w.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  const res = solution.reduce(s, w);
  
  if (res[0] === "") {
    console.log(`EMPTY ${res[1]}`);
  } else {
    console.log(`${res[0]} ${res[1]}`);
  }
});
```

