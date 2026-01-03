---
problem_id: STR_CYCLIC_SHIFT_EQUALITY_CLASSES__1015
display_id: STR-015
slug: cyclic-shift-equality-classes
title: "Cyclic Shift Equality Classes"
difficulty: Medium
difficulty_score: 40
topics:
  - String Manipulation
  - Hashing
  - Equivalence Relations
tags:
  - rotation-equivalence
  - canonical-form
  - booth-algorithm
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-015: Cyclic Shift Equality Classes

## Problem Statement

Given `n` strings, group them into equivalence classes where two strings are equivalent if one is a cyclic shift (rotation) of the other. Return the number of equivalence classes.

## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5)
- Next n lines: One string per line (each length ≤ 20)

## Output Format

- A single integer representing the number of equivalence classes

## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- Each string length ≤ 20

## Example 1

**Input:**

```
5
ab
ba
abc
bca
cab
```

**Output:**

```
2
```

**Explanation:**

- Class 1: {"ab", "ba"} (rotations of each other)
- Class 2: {"abc", "bca", "cab"} (rotations of each other)

## Example 2

**Input:**

```
3
aaa
aaa
bbb
```

**Output:**

```
2
```

**Explanation:**

- Class 1: {"aaa", "aaa"}
- Class 2: {"bbb"}

## Notes

- Use minimal rotation (Booth's algorithm) as canonical form
- Hash canonical forms to count unique classes
- O(n × m) time where m is max string length

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int cyclicShiftEquivalenceClasses(List<String> strings) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int strings_n = sc.nextInt();
        List<String> strings = new ArrayList<>();
        for(int i=0; i<strings_n; i++) strings.add(sc.next());
        Solution sol = new Solution();
        System.out.println(sol.cyclicShiftEquivalenceClasses(strings));
        sc.close();
    }
}
```

### Python

```python
def cyclic_shift_equivalence_classes(strings: list[str]) -> int:
    # //Implement here
    return 0

def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    parts = input_data.split()
    if not parts:
        return
        
    iterator = iter(parts)
    try:
        N = int(next(iterator))
        strings = []
        for _ in range(N):
            strings.append(next(iterator))
            
        print(cyclic_shift_equivalence_classes(strings))
    except StopIteration:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

class Solution {
public:
    int cyclicShiftEquivalenceClasses(vector<string>& strings) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int strings_n; cin >> strings_n; vector<string> strings(strings_n); for(int i=0; i<strings_n; i++) cin >> strings[i];
    Solution sol;
    cout << sol.cyclicShiftEquivalenceClasses(strings) << endl;
    return 0;
}
```

### JavaScript

```javascript
function cyclicShiftEquivalenceClasses(strings) {
  //Implement here
  return 0;
}

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const strings_n = parseInt(tokens[ptr++]);
    const strings = [];
    for(let i=0; i<strings_n; i++) strings.push(tokens[ptr++]);
    console.log(cyclicShiftEquivalenceClasses(strings));
});
```
