---
problem_id: ARR_TEMP_OFFLINE_RANGES__5631
display_id: ARR-004
slug: lab-temperature-offline-ranges
title: "Lab Temperature Offline Ranges"
difficulty: Medium
difficulty_score: 46
topics:
  - Arrays
  - Difference Array
  - Prefix Sum
tags:
  - arrays
  - difference-array
  - prefix-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-004: Lab Temperature Offline Ranges

## Problem Statement

You are given an array of temperatures and a list of queries. Each query is either an add-range operation or a sum-range request.
All add queries appear before sum queries and should be applied cumulatively. 
After applying all adds, answer each sum query in order.

![Problem Illustration](../images/ARR-004/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers temps[i]
- Third line: integer q, the number of queries
- Next q lines: either "add l r x" or "sum l r"

## Output Format

Print the answers to sum queries in order, space-separated.

## Constraints

- `1 <= n, q <= 100000`
- `-1000000000 <= temps[i], x <= 1000000000`
- `0 <= l <= r < n`

## Example

**Input:**
```
3
1 2 3
4
add 0 1 5
add 2 2 -1
sum 0 2
sum 1 2
```

**Output:**
```
15 9
```

**Explanation:**

After both add queries, temps become [6, 7, 2].
Then sum 0..2 is 15 and sum 1..2 is 9.

![Example Visualization](../images/ARR-004/example-1.png)

## Notes

- All add queries appear before sum queries.
- Use 64-bit integers for sums.

## Related Topics

Difference Array, Prefix Sum, Range Queries

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] processTemperatureQueries(int[] temps, List<Query> queries) {
        // Your implementation here
        return new long[0];
    }
}

public class Main {
    static class Query {
        String type;
        int l;
        int r;
        int x;
        Query(String type, int l, int r, int x) {
            this.type = type;
            this.l = l;
            this.r = r;
            this.x = x;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] temps = new int[n];
        for (int i = 0; i < n; i++) {
            temps[i] = sc.nextInt();
        }
        int q = sc.nextInt();
        List<Query> queries = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            String type = sc.next();
            int l = sc.nextInt();
            int r = sc.nextInt();
            int x = 0;
            if ("add".equals(type)) {
                x = sc.nextInt();
            }
            queries.add(new Query(type, l, r, x));
        }

        Solution solution = new Solution();
        long[] result = solution.processTemperatureQueries(temps, queries);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```


### Python

```python
def process_temperature_queries(temps: list[int], queries: list[tuple]) -> list[int]:
    # Your implementation here
    return []

def main():
    n = int(input())
    temps = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        parts = input().split()
        if parts[0] == "add":
            queries.append((parts[0], int(parts[1]), int(parts[2]), int(parts[3])))
        else:
            queries.append((parts[0], int(parts[1]), int(parts[2])))

    result = process_temperature_queries(temps, queries)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
```


### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <tuple>
using namespace std;

struct Query {
    string type;
    int l;
    int r;
    long long x;
};

class Solution {
public:
    vector<long long> processTemperatureQueries(vector<int>& temps, vector<Query>& queries) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> temps(n);
    for (int i = 0; i < n; i++) {
        cin >> temps[i];
    }
    int q;
    cin >> q;
    vector<Query> queries;
    queries.reserve(q);
    for (int i = 0; i < q; i++) {
        Query query;
        cin >> query.type >> query.l >> query.r;
        query.x = 0;
        if (query.type == "add") {
            cin >> query.x;
        }
        queries.push_back(query);
    }

    Solution solution;
    vector<long long> result = solution.processTemperatureQueries(temps, queries);
    for (size_t i = 0; i < result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```


### JavaScript

```javascript
const fs = require("fs");
const data = fs.readFileSync(0, "utf8").trim().split(/\s+/);
if (data.length === 1 && data[0] === "") {
  process.exit(0);
}

class Solution {
  processTemperatureQueries(temps, queries) {
    // Your implementation here
    return [];
  }
}

let idx = 0;
const n = Number(data[idx++]);
const temps = [];
for (let i = 0; i < n; i++) {
  temps.push(Number(data[idx++]));
}
const q = Number(data[idx++]);
const queries = [];
for (let i = 0; i < q; i++) {
  const type = data[idx++];
  const l = Number(data[idx++]);
  const r = Number(data[idx++]);
  let x = 0;
  if (type === "add") {
    x = Number(data[idx++]);
  }
  queries.push({ type, l, r, x });
}

const solution = new Solution();
const result = solution.processTemperatureQueries(temps, queries);
console.log(result.join(" "));
```

