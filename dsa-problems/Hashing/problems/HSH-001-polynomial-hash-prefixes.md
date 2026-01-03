---
problem_id: HSH_POLYNOMIAL_HASH_PREFIXES__3824
display_id: HSH-001
slug: polynomial-hash-prefixes
title: "Polynomial Hash of Prefixes"
difficulty: Easy
difficulty_score: 25
topics:
  - Hashing
  - Rolling Hash
  - String Algorithms
tags:
  - hashing
  - rolling-hash
  - polynomial-hash
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-001: Polynomial Hash of Prefixes

## Problem Statement

Given a lowercase string `s`, compute the polynomial rolling hash for all prefixes using base `B` and modulus `M`.

The polynomial hash for a string is computed as:
- `hash("") = 0`
- `hash(s[0..i]) = (hash(s[0..i-1]) * B + s[i]) mod M`

where `s[i]` is treated as its ASCII value.

Return an array containing the hash values for all prefixes: `hash(s[0..0]), hash(s[0..1]), ..., hash(s[0..n-1])`.

![Problem Illustration](../images/HSH-001/problem-illustration.png)

## Input Format

- First line: string `s` (lowercase letters only)
- Second line: two integers `B M` (base and modulus)

## Output Format

- Single line with `n` space-separated integers representing hash values of all prefixes

## Constraints

- `1 <= |s| <= 2*10^5`
- `1 <= B <= 10^9 + 6`
- `1 <= M <= 10^9 + 7`
- String contains only lowercase English letters

## Example

**Input:**
```
abc
911382323 1000000007
```

**Output:**
```
97 374134515 549818522
```

**Explanation:**

String: "abc"
- Prefix "a": hash = 97 (ASCII of 'a')
- Prefix "ab": hash = (97 * 911382323 + 98) mod 1000000007 = 374134515
- Prefix "abc": hash = (374134515 * 911382323 + 99) mod 1000000007 = 549818522

![Example Visualization](../images/HSH-001/example-1.png)

## Notes

- Use modular arithmetic to prevent integer overflow
- Hash values depend on both the base and modulus chosen
- This technique is fundamental for string matching and comparison
- Time complexity: O(n)
- Space complexity: O(n) for storing results

## Related Topics

Polynomial Hash, Rolling Hash, String Hashing, Rabin-Karp

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public long[] computePrefixHashes(String s, long B, long M) {
        //Implemention here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> lines = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            lines.add(line);
        }
        if (lines.size() < 2) return;
        String s = lines.get(0);
        String[] parts = lines.get(1).trim().split("\\s+");
        if (parts.length < 2) return;
        long B = Long.parseLong(parts[0]);
        long M = Long.parseLong(parts[1]);

        Solution solution = new Solution();
        long[] result = solution.computePrefixHashes(s, B, M);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) out.append(' ');
            out.append(result[i]);
        }
        System.out.print(out.toString());
    }
}
```

### Python

```python
import sys

def compute_prefix_hashes(s, B, M):
    # //Implemention here
    return []

def main():
    lines = sys.stdin.read().split('\n')
    if len(lines) < 2:
        return
    s = lines[0]
    parts = lines[1].strip().split()
    if len(parts) < 2:
        return
    B = int(parts[0])
    M = int(parts[1])
    result = compute_prefix_hashes(s, B, M)
    sys.stdout.write(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<long long> compute_prefix_hashes(const string& s, long long B, long long M) {
    //Implemention here
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<string> lines;
    string line;
    while (getline(cin, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        lines.push_back(line);
    }
    if (lines.size() < 2) return 0;
    string s = lines[0];
    stringstream ss(lines[1]);
    long long B, M;
    if (!(ss >> B >> M)) return 0;

    vector<long long> result = compute_prefix_hashes(s, B, M);
    for (size_t i = 0; i < result.size(); i++) {
        if (i > 0) cout << ' ';
        cout << result[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function computePrefixHashes(s, B, M) {
  //Implemention here
  return [];
}

const raw = fs.readFileSync(0, "utf8");
if (raw.length === 0) {
  process.exit(0);
}
const lines = raw.replace(/\r/g, "").split(/\n/);
if (lines.length < 2) {
  process.exit(0);
}
const s = lines[0];
const parts = lines[1].trim().split(/\s+/);
if (parts.length < 2) {
  process.exit(0);
}
const B = Number(parts[0]);
const M = Number(parts[1]);
const result = computePrefixHashes(s, B, M);
process.stdout.write(result.map(String).join(' '));
```

