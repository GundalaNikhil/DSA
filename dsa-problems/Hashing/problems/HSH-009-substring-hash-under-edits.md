---
problem_id: HSH_SUBSTRING_HASH_UNDER_EDITS__7394
display_id: HSH-009
slug: substring-hash-under-edits
title: "Substring Hash Under Edits"
difficulty: Medium
difficulty_score: 60
topics:
  - Hashing
  - Data Structures
  - Segment Tree
tags:
  - hashing
  - segment-tree
  - updates
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-009: Substring Hash Under Edits

## Problem Statement

Support two types of operations on a string `s`:

1. **Update**: Change character at position `i` to character `c`
2. **Query**: Return the polynomial hash of substring `s[l..r]`

Use a data structure (Segment Tree or Fenwick Tree) to handle updates and queries efficiently.

![Problem Illustration](../images/HSH-009/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q` (number of operations)
- Next `q` lines: either
  - `U i c` (update position i to character c)
  - `Q l r` (query hash of substring [l, r])

## Output Format

- For each query operation, output the hash value on a new line

## Constraints

- `1 <= |s|, q <= 2*10^5`
- `0 <= i, l, r < |s|`
- Character `c` is a lowercase English letter

## Example

**Input:**

```
abc
3
Q 0 2
U 1 x
Q 0 2
```

**Output:**

```
549818522
650293847
```

**Explanation:**

Initial string: "abc"

Operation 1: Query hash of "abc" (positions 0-2)
Operation 2: Update position 1 to 'x' → string becomes "axc"
Operation 3: Query hash of "axc" (positions 0-2)

![Example Visualization](../images/HSH-009/example-1.png)

## Notes

- Use Segment Tree with each node storing hash value
- Precompute powers of base for combination
- Update: O(log n), Query: O(log n)
- Total time complexity: O(q log n)
- Space complexity: O(n)

## Related Topics

Segment Tree, Fenwick Tree, Hashing, Dynamic Updates

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public List<Long> processOperations(String s, List<String[]> operations) {
        //Implemention here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(' ');
        }
        String input = sb.toString().trim();
        if (input.isEmpty()) return;
        String[] data = input.split("\\s+");
        int idx = 0;
        String s = data[idx++];
        int q = Integer.parseInt(data[idx++]);
        List<String[]> operations = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            String type = data[idx++];
            if (type.equals("U")) {
                String pos = data[idx++];
                String c = data[idx++];
                operations.add(new String[]{type, pos, c});
            } else {
                String l = data[idx++];
                String r = data[idx++];
                operations.add(new String[]{type, l, r});
            }
        }

        Solution solution = new Solution();
        List<Long> result = solution.processOperations(s, operations);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            out.append(result.get(i));
            if (i + 1 < result.size()) out.append('\n');
        }
        System.out.print(out.toString());
    }
}
```

### Python

```python
import sys

def process_operations(s, operations):
    # //Implemention here
    return []

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    s = data[idx]
    idx += 1
    q = int(data[idx])
    idx += 1
    operations = []
    for _ in range(q):
        type_op = data[idx]
        idx += 1
        if type_op == 'U':
            pos = data[idx]
            c = data[idx + 1]
            idx += 2
            operations.append(['U', pos, c])
        else:
            l = data[idx]
            r = data[idx + 1]
            idx += 2
            operations.append(['Q', l, r])
    result = process_operations(s, operations)
    out_lines = [str(val) for val in result]
    sys.stdout.write('\n'.join(out_lines))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<long long> process_operations(const string& s, const vector<vector<string>>& operations) {
    //Implemention here
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int q;
    if (!(cin >> q)) return 0;
    vector<vector<string>> operations;
    operations.reserve(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        if (type == "U") {
            string pos, c;
            cin >> pos >> c;
            operations.push_back({type, pos, c});
        } else {
            string l, r;
            cin >> l >> r;
            operations.push_back({type, l, r});
        }
    }

    vector<long long> result = process_operations(s, operations);
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i + 1 < result.size()) cout << '\n';
    }
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function processOperations(s, operations) {
  //Implemention here
  return [];
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/);
let idx = 0;
const s = data[idx++];
const q = parseInt(data[idx++], 10);
const operations = [];
for (let i = 0; i < q; i++) {
  const type = data[idx++];
  if (type === 'U') {
    const pos = data[idx++];
    const c = data[idx++];
    operations.push(['U', pos, c]);
  } else {
    const l = data[idx++];
    const r = data[idx++];
    operations.push(['Q', l, r]);
  }
}
const result = processOperations(s, operations);
process.stdout.write(result.map(String).join('\n'));
```

