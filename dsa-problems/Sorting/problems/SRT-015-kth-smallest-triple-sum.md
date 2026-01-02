---
problem_id: SRT_KTH_SMALLEST_TRIPLE_SUM__7904
display_id: SRT-015
slug: kth-smallest-triple-sum
title: "Kth Smallest Triple Sum"
difficulty: Medium
difficulty_score: 59
topics:
  - Sorting
  - Binary Search
  - Two Pointers
tags:
  - sorting
  - binary-search
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-015: Kth Smallest Triple Sum

## Problem Statement

Given an array `a`, consider all sums `a[i] + a[j] + a[k]` with `i < j < k`. Find the k-th smallest such sum.

![Problem Illustration](../images/SRT-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `k`
- Second line: `n` space-separated integers

## Output Format

- Single integer: the k-th smallest triple sum

## Constraints

- `3 <= n <= 100000`
- `1 <= k <= n*(n-1)*(n-2)/6`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
4 2
1 2 4 7
```

**Output:**

```
10
```

**Explanation:**

Triple sums are 7, 10, 12, 13 in sorted order; the 2nd is 10.

![Example Visualization](../images/SRT-015/example-1.png)

## Notes

- Sort the array first
- Use binary search on the possible sum range
- Count triples with sum <= mid using two pointers
- Time complexity: O(n^2 log R)

## Related Topics

Binary Search, Two Pointers, Sorting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long kthTripleSum(int[] arr, long k) {
        return 0;
    }
    
    private long countLessEqual(int[] arr, long target) {
        long count = 0;
        int n = arr.length;
        for (int i = 0; i < n - 2; i++) {
            // Optimization: If smallest sum starting with arr[i] > target, break
            if ((long)arr[i] + arr[i+1] + arr[i+2] > target) break;
            
            // Optimization: If largest sum starting with arr[i] <= target, add all
            if ((long)arr[i] + arr[n-2] + arr[n-1] <= target) {
                long remaining = n - 1 - i;
                count += remaining * (remaining - 1) / 2;
                continue;
            }
            
            long rem = target - arr[i];
            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                if (arr[l] + arr[r] <= rem) {
                    count += (r - l);
                    l++;
                } else {
                    r--;
                }
            }
        }
        return count;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        long k = sc.nextLong();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.kthTripleSum(arr, k));
        sc.close();
    }
}
```

### Python

```python
def kth_triple_sum(arr: list[int], k: int) -> int:
    return 0
def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = kth_triple_sum(arr, k)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
    long long countLessEqual(const vector<int>& arr, long long target) {
        long long count = 0;
        int n = arr.size();
        for (int i = 0; i < n - 2; i++) {
            if ((long long)arr[i] + arr[i+1] + arr[i+2] > target) break;
            
            if ((long long)arr[i] + arr[n-2] + arr[n-1] <= target) {
                long long remaining = n - 1 - i;
                count += remaining * (remaining - 1) / 2;
                continue;
            }
            
            long long rem = target - arr[i];
            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                if (arr[l] + arr[r] <= rem) {
                    count += (r - l);
                    l++;
                } else {
                    r--;
                }
            }
        }
        return count;
    }

public:
    long long kthTripleSum(vector<int>& arr, long long k) {
        int n = arr.size();
        sort(arr.begin(), arr.end());
        
        long long low = (long long)arr[0] + arr[1] + arr[2];
        long long high = (long long)arr[n-1] + arr[n-2] + arr[n-3];
        long long ans = high;
        
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (countLessEqual(arr, mid) >= k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    cout << solution.kthTripleSum(arr, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  kthTripleSum(arr, k) {
    return 0;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const k = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
console.log(solution.kthTripleSum(arr, k).toString());
```

