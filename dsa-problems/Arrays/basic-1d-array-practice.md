# 1D Array Practice Set (16 Questions)

## 1) Snack Restock Snapshot

- **Problem ID**: `ARRAY-001`
- **Display ID**: `A001`
- **Slug**: `snack-restock-snapshot`
- **Difficulty**: Easy
- **Tags**: `prefix-sum`, `arrays`, `mathematics`
- **Problem**: Given daily deliveries `arr[i]`, output prefix averages rounded down for each day.
- **Constraints**:
  - `1 <= n <= 10^5`
  - `0 <= arr[i] <= 10^6`
  - All values are non-negative integers
- **Hint**: Maintain running sum; avg = sum//(i+1).
- **Examples**:
  - Example 1:
    - Input: `[4, 6, 6, 0]`
    - Output: `[4, 5, 5, 4]`
    - Explanation: Day 0: 4/1=4, Day 1: 10/2=5, Day 2: 16/3=5, Day 3: 16/4=4
  - Example 2:
    - Input: `[10, 20, 30]`
    - Output: `[10, 15, 20]`
    - Explanation: Running averages are 10, 15, and 20 respectively

### Function Signatures:

```java
// Java
class Solution {
    public int[] prefixAverages(int[] arr) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        int[] result = sol.prefixAverages(arr);
        System.out.println(Arrays.toString(result));
    }
}
```

```python
# Python
def prefix_averages(arr: list[int]) -> list[int]:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = prefix_averages(arr)
    print(result)
```

```cpp
// C++
class Solution {
public:
    vector<int> prefixAverages(vector<int>& arr) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution sol;
    vector<int> result = sol.prefixAverages(arr);
    for (int x : result) cout << x << " ";
    return 0;
}
```

### Quiz Question:

**Q**: When computing prefix averages, what is the time complexity if we recalculate the sum from scratch for each position versus maintaining a running sum?

- A) O(n) vs O(n²)
- B) O(n²) vs O(n)
- C) O(n log n) vs O(n)
- D) Both are O(n)

**Answer**: B) O(n²) vs O(n) - Recalculating from scratch requires nested loops (O(n²)), while maintaining a running sum is linear (O(n)).

## 2) Bench Flip With Locked Ends

- **Problem ID**: `ARRAY-002`
- **Display ID**: `A002`
- **Slug**: `bench-flip-locked-ends`
- **Difficulty**: Easy
- **Tags**: `two-pointers`, `arrays`, `in-place`
- **Problem**: Reverse the array in place but keep the first and last elements fixed; only the middle segment reverses.
- **Constraints**:
  - `2 <= n <= 2 * 10^5`
  - `-10^9 <= arr[i] <= 10^9`
- **Hint**: Two-pointer from positions 1 and n-2.
- **Examples**:
  - Example 1:
    - Input: `[9, 3, 8, 1, 5]`
    - Output: `[9, 1, 8, 3, 5]`
    - Explanation: First (9) and last (5) stay; middle [3,8,1] reversed to [1,8,3]
  - Example 2:
    - Input: `[1, 2, 3, 4]`
    - Output: `[1, 3, 2, 4]`
    - Explanation: Middle [2,3] reversed to [3,2]

### Function Signatures:

```java
// Java
class Solution {
    public void benchFlipLockedEnds(int[] arr) {
        // Implementation (in-place modification)
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        sol.benchFlipLockedEnds(arr);
        System.out.println(Arrays.toString(arr));
    }
}
```

```python
# Python
def bench_flip_locked_ends(arr: list[int]) -> None:
    # Implementation (in-place modification)
    pass

# Custom Input
if __name____ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    bench_flip_locked_ends(arr)
    print(arr)
```

```cpp
// C++
class Solution {
public:
    void benchFlipLockedEnds(vector<int>& arr) {
        // Implementation (in-place modification)
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution sol;
    sol.benchFlipLockedEnds(arr);
    for (int x : arr) cout << x << " ";
    return 0;
}
```

### Quiz Question:

**Q**: What is the space complexity of reversing a subarray in-place using the two-pointer technique?

- A) O(n)
- B) O(log n)
- C) O(1)
- D) O(n²)

**Answer**: C) O(1) - Two-pointer reversal only uses a constant amount of extra space for the pointers and temporary swap variable.

## 3) Shuttle Shift With Blackout

- **Problem ID**: `ARRAY-003`
- **Display ID**: `A003`
- **Slug**: `shuttle-shift-blackout`
- **Difficulty**: Easy-Medium
- **Tags**: `arrays`, `rotation`, `simulation`
- **Problem**: Rotate the array left by `k` but positions listed in `blackout` stay in place; only other positions rotate cyclically among themselves.
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - `0 <= k <= 10^9`
  - `|blackout| <= n`
  - All blackout indices are valid (0 to n-1)
- **Hint**: Extract movable elements, rotate them, then reinsert.
- **Examples**:
  - Example 1:
    - Input: `arr=[1,2,3,4,5], k=2, blackout={1,3}`
    - Output: `[3,2,5,4,1]`
    - Explanation: Elements at indices 1,3 stay (2,4). Others [1,3,5] rotate left by 2 to [5,1,3]
  - Example 2:
    - Input: `arr=[10,20,30,40], k=1, blackout={0}`
    - Output: `[10,30,40,20]`
    - Explanation: Index 0 (10) stays, others [20,30,40] rotate left by 1 to [30,40,20]

### Function Signatures:

```java
// Java
class Solution {
    public int[] shuttleShiftBlackout(int[] arr, int k, Set<Integer> blackout) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int k = sc.nextInt();
        int b = sc.nextInt();
        Set<Integer> blackout = new HashSet<>();
        for (int i = 0; i < b; i++) {
            blackout.add(sc.nextInt());
        }
        Solution sol = new Solution();
        int[] result = sol.shuttleShiftBlackout(arr, k, blackout);
        System.out.println(Arrays.toString(result));
    }
}
```

```python
# Python
def shuttle_shift_blackout(arr: list[int], k: int, blackout: set[int]) -> list[int]:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    b = int(input())
    blackout = set(map(int, input().split())) if b > 0 else set()
    result = shuttle_shift_blackout(arr, k, blackout)
    print(result)
```

```cpp
// C++
class Solution {
public:
    vector<int> shuttleShiftBlackout(vector<int>& arr, int k, unordered_set<int>& blackout) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int k, b;
    cin >> k >> b;
    unordered_set<int> blackout;
    for (int i = 0; i < b; i++) {
        int idx;
        cin >> idx;
        blackout.insert(idx);
    }
    Solution sol;
    vector<int> result = sol.shuttleShiftBlackout(arr, k, blackout);
    for (int x : result) cout << x << " ";
    return 0;
}
```

### Quiz Question:

**Q**: When rotating an array with blackout positions, why is it important to use modulo operation on k?

- A) To handle negative rotations
- B) To handle k larger than the number of movable elements
- C) To optimize memory usage
- D) To maintain sorted order

**Answer**: B) To handle k larger than the number of movable elements - When k exceeds the count of movable elements, rotating by k is equivalent to rotating by k % (movable_count).

## 4) Lab Temperature Offline Ranges

- **Problem ID**: `ARRAY-004`
- **Display ID**: `A004`
- **Slug**: `lab-temperature-offline-ranges`
- **Difficulty**: Medium
- **Tags**: `difference-array`, `prefix-sum`, `range-queries`
- **Problem**: Given temps array and queries `[l,r]`, some queries are type "add x to range" (offline, applied cumulatively), others ask for range sum after all adds. Return answers to sum queries.
- **Constraints**:
  - `1 <= n, q <= 10^5`
  - `-10^9 <= temp[i], x <= 10^9`
  - `0 <= l <= r < n`
  - All add queries are processed before sum queries
- **Hint**: Use difference array to accumulate adds, then prefix for final temps before answering sums with prefix sums.
- **Examples**:
  - Example 1:
    - Input: `temps=[1,2,3], queries=[("add",0,1,5),("sum",0,2),("add",2,2,-1),("sum",1,2)]`
    - Output: `[16,9]`
    - Explanation: After adds: [6,7,2], sum(0,2)=15, then [6,7,2]→[6,7,2], sum(1,2)=9
  - Example 2:
    - Input: `temps=[5,5,5], queries=[("add",0,2,3),("sum",0,2)]`
    - Output: `[24]`
    - Explanation: After add: [8,8,8], sum(0,2)=24

### Function Signatures:

```java
// Java
class Solution {
    public long[] processTemperatureQueries(int[] temps, List<Query> queries) {
        // Implementation
        // Query class: { String type; int l; int r; int x; }
    }
}

// Custom Input
import java.util.*;
public class Main {
    static class Query {
        String type;
        int l, r, x;
        Query(String type, int l, int r, int x) {
            this.type = type; this.l = l; this.r = r; this.x = x;
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
            int l = sc.nextInt(), r = sc.nextInt();
            int x = type.equals("add") ? sc.nextInt() : 0;
            queries.add(new Query(type, l, r, x));
        }
        Solution sol = new Solution();
        long[] result = sol.processTemperatureQueries(temps, queries);
        System.out.println(Arrays.toString(result));
    }
}
```

```python
# Python
def process_temperature_queries(temps: list[int], queries: list[tuple]) -> list[int]:
    # Implementation
    # queries format: [("add", l, r, x), ("sum", l, r), ...]
    pass

# Custom Input
if __name__ == "__main__":
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
    print(result)
```

```cpp
// C++
class Solution {
public:
    vector<long long> processTemperatureQueries(vector<int>& temps,
                                                  vector<tuple<string, int, int, int>>& queries) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> temps(n);
    for (int i = 0; i < n; i++) {
        cin >> temps[i];
    }
    int q;
    cin >> q;
    vector<tuple<string, int, int, int>> queries;
    for (int i = 0; i < q; i++) {
        string type;
        int l, r, x = 0;
        cin >> type >> l >> r;
        if (type == "add") cin >> x;
        queries.push_back({type, l, r, x});
    }
    Solution sol;
    vector<long long> result = sol.processTemperatureQueries(temps, queries);
    for (auto x : result) cout << x << " ";
    return 0;
}
```

### Quiz Question:

**Q**: What is the advantage of using a difference array for batch range updates compared to updating each element individually?

- A) It reduces space complexity
- B) It reduces time complexity from O(n\*q) to O(n+q)
- C) It handles negative numbers better
- D) It automatically sorts the array

**Answer**: B) It reduces time complexity from O(n\*q) to O(n+q) - Difference arrays mark range boundaries in O(1), then reconstruct the array in O(n), avoiding O(n) work per query.

## 5) Weighted Balance Point

- **Problem ID**: `ARRAY-005`
- **Display ID**: `A005`
- **Slug**: `weighted-balance-point`
- **Difficulty**: Medium
- **Tags**: `prefix-sum`, `arrays`, `mathematics`
- **Problem**: Find smallest index `i` where `sum(left)*L == sum(right)*R` for given weights `L` and `R`; left excludes `i`, right excludes `i`. If none, return -1.
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - `-10^9 <= a[i] <= 10^9`
  - `1 <= L, R <= 10^6`
  - Integer overflow possible, use long
- **Hint**: Precompute total; iterate maintaining left sum.
- **Examples**:
  - Example 1:
    - Input: `a=[2,3,-1,3,2], L=2, R=1`
    - Output: `2` 
    - Explanation: At index 2, left sum=5, right sum=8; 5*2 == 8*1.
    
  - Example 2:
    - Input: `a=[1,2,3,4], L=1, R=1`
    - Output: `-1`
    - Explanation: No index satisfies the weighted balance condition.
    

### Function Signatures:

```java
// Java
class Solution {
    public int weightedBalancePoint(int[] a, int L, int R) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        int L = sc.nextInt();
        int R = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.weightedBalancePoint(a, L, R));
    }
}
```

```python
# Python
def weighted_balance_point(a: list[int], L: int, R: int) -> int:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    L, R = map(int, input().split())
    result = weighted_balance_point(a, L, R)
    print(result)
```

```cpp
// C++
class Solution {
public:
    int weightedBalancePoint(vector<int>& a, int L, int R) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int L, R;
    cin >> L >> R;
    Solution sol;
    cout << sol.weightedBalancePoint(a, L, R);
    return 0;
}
```

### Quiz Question:

**Q**: In the weighted balance point problem, why do we need to use long data type even though input values fit in int?

- A) To store the array size
- B) Because multiplication of sums by weights can overflow int range
- C) To handle negative numbers
- D) For better performance

**Answer**: B) Because multiplication of sums by weights can overflow int range - Sum can be up to 2*10^14 (10^5 elements * 10^9 each), multiplied by weight up to 10^6 exceeds int.

## 6) Zero Slide With Limit

- **Problem ID**: `ARRAY-006`
- **Display ID**: `A006`
- **Slug**: `zero-slide-limit`
- **Difficulty**: Easy-Medium
- **Tags**: `two-pointers`, `arrays`, `simulation`
- **Problem**: Move all zeros to the end but allow at most `m` swaps total; stop once swaps exceed `m`. Return resulting array.
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - `0 <= m <= 10^9`
  - Array contains integers
- **Hint**: Use write pointer; count swaps when writing non-zero over zero.
- **Examples**:
  - Example 1:
    - Input: `[0,4,0,5,7], m=1`
    - Output: `[4,0,0,5,7]`
    - Explanation: One swap moves 4 to position 0, then stop
  - Example 2:
    - Input: `[0,0,3,0,5], m=3`
    - Output: `[3,5,0,0,0]`
    - Explanation: Move 3 (swap), then 5 (swap), total 2 swaps

### Function Signatures:

```java
// Java
class Solution {
    public int[] zeroSlideWithLimit(int[] arr, int m) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int m = sc.nextInt();
        Solution sol = new Solution();
        int[] result = sol.zeroSlideWithLimit(arr, m);
        System.out.println(Arrays.toString(result));
    }
}
```

```python
# Python
def zero_slide_with_limit(arr: list[int], m: int) -> list[int]:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    result = zero_slide_with_limit(arr, m)
    print(result)
```

```cpp
// C++
class Solution {
public:
    vector<int> zeroSlideWithLimit(vector<int>& arr, int m) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int m;
    cin >> m;
    Solution sol;
    vector<int> result = sol.zeroSlideWithLimit(arr, m);
    for (int x : result) cout << x << " ";
    return 0;
}
```

### Quiz Question:

**Q**: When moving zeros to the end with a swap limit, what determines the minimum number of swaps needed?

- A) The total array size
- B) The number of zeros in the array
- C) The number of non-zeros that have zeros before them
- D) The number of distinct elements

**Answer**: C) The number of non-zeros that have zeros before them - Each non-zero element that needs to "jump over" zeros to reach its final position requires one swap.

## 7) Hostel Roster Merge With Gap

- **Problem ID**: `ARRAY-007`
- **Display ID**: `A007`
- **Slug**: `hostel-roster-merge-gap`
- **Difficulty**: Medium
- **Tags**: `two-pointers`, `merge`, `sorting`, `arrays`
- **Problem**: Merge two sorted arrays `A` and `B` into sorted order, but if two equal elements come from different arrays, place the one from `A` before the one from `B`. Return merged array.
- **Constraints**:
  - `0 <= n, m <= 10^5`
  - `-10^9 <= A[i], B[i] <= 10^9`
  - Both arrays are sorted in non-decreasing order
- **Hint**: Standard merge with tie-break on source.
- **Examples**:
  - Example 1:
    - Input: `A=[1,3,3], B=[3,4]`
    - Output: `[1,3,3,3,4]`
    - Explanation: When merging, A's elements come first on equality
  - Example 2:
    - Input: `A=[2,5], B=[1,3,6]`
    - Output: `[1,2,3,5,6]`
    - Explanation: Standard merge as no equal elements

### Function Signatures:

```java
// Java
class Solution {
    public int[] mergeWithPriority(int[] A, int[] B) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        int m = sc.nextInt();
        int[] B = new int[m];
        for (int i = 0; i < m; i++) {
            B[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        int[] result = sol.mergeWithPriority(A, B);
        System.out.println(Arrays.toString(result));
    }
}
```

```python
# Python
def merge_with_priority(A: list[int], B: list[int]) -> list[int]:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split())) if n > 0 else []
    m = int(input())
    B = list(map(int, input().split())) if m > 0 else []
    result = merge_with_priority(A, B)
    print(result)
```

```cpp
// C++
class Solution {
public:
    vector<int> mergeWithPriority(vector<int>& A, vector<int>& B) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    int m;
    cin >> m;
    vector<int> B(m);
    for (int i = 0; i < m; i++) {
        cin >> B[i];
    }
    Solution sol;
    vector<int> result = sol.mergeWithPriority(A, B);
    for (int x : result) cout << x << " ";
    return 0;
}
```

### Quiz Question:

**Q**: In a stable merge operation with priority to array A on equal elements, what is the time complexity?

- A) O(n log m)
- B) O((n+m) log(n+m))
- C) O(n + m)
- D) O(n \* m)

**Answer**: C) O(n + m) - Standard merge with two pointers processes each element exactly once, regardless of the tie-breaking rule.

## 8) Partner Pair Sum With Forbidden

- **Problem ID**: `ARRAY-008`
- **Display ID**: `A008`
- **Slug**: `partner-pair-sum-forbidden`
- **Difficulty**: Easy-Medium
- **Tags**: `two-pointers`, `arrays`, `hashing`
- **Problem**: Given sorted array and target, find if a pair sums to target such that neither element index is in `forbidden` set.
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - `|forbidden| <= n`
  - `-10^9 <= arr[i], target <= 10^9`
  - Array is sorted in non-decreasing order
- **Hint**: Two-pointer skipping forbidden indices.
- **Examples**:
  - Example 1:
    - Input: `arr=[1,4,6,7], target=11, forbidden={0}`
    - Output: `true` (4 + 7 = 11, indices 1 and 3)
    - Explanation: Index 0 is forbidden, but 4+7=11 works
  - Example 2:
    - Input: `arr=[2,3,5,8], target=10, forbidden={1,3}`
    - Output: `true` (2 + 8 = 10, indices 0 and 3... wait 3 forbidden. Actually 2+8, but need valid)
    - Explanation: 2+8=10 but index 3 forbidden, 5+5 not available, return false

### Function Signatures:

```java
// Java
class Solution {
    public boolean hasPairWithForbidden(int[] arr, int target, Set<Integer> forbidden) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int target = sc.nextInt();
        int f = sc.nextInt();
        Set<Integer> forbidden = new HashSet<>();
        for (int i = 0; i < f; i++) {
            forbidden.add(sc.nextInt());
        }
        Solution sol = new Solution();
        System.out.println(sol.hasPairWithForbidden(arr, target, forbidden));
    }
}
```

```python
# Python
def has_pair_with_forbidden(arr: list[int], target: int, forbidden: set[int]) -> bool:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    f = int(input())
    forbidden = set(map(int, input().split())) if f > 0 else set()
    result = has_pair_with_forbidden(arr, target, forbidden)
    print(result)
```

```cpp
// C++
class Solution {
public:
    bool hasPairWithForbidden(vector<int>& arr, int target, unordered_set<int>& forbidden) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int target, f;
    cin >> target >> f;
    unordered_set<int> forbidden;
    for (int i = 0; i < f; i++) {
        int idx;
        cin >> idx;
        forbidden.insert(idx);
    }
    Solution sol;
    cout << (sol.hasPairWithForbidden(arr, target, forbidden) ? "true" : "false");
    return 0;
}
```

### Quiz Question:

**Q**: When using two-pointer technique on a sorted array with forbidden indices, what should you do when a pointer lands on a forbidden index?

- A) Return false immediately
- B) Skip to the next valid index in the appropriate direction
- C) Remove the element from the array
- D) Restart the algorithm

**Answer**: B) Skip to the next valid index in the appropriate direction - Continue moving the pointer until it reaches a non-forbidden index while maintaining the two-pointer invariant.

## 9) Best Streak With One Smoothing

- **Problem ID**: `ARRAY-009`
- **Display ID**: `A009`
- **Slug**: `best-streak-one-smoothing`
- **Difficulty**: Medium
- **Tags**: `kadane`, `prefix-suffix`, `dynamic-programming`, `arrays`
- **Problem**: You may choose exactly one index `i` and replace `a[i]` with `floor((a[i-1]+a[i]+a[i+1])/3)` (use existing neighbors; for endpoints, smoothing not allowed). Then compute the maximum subarray sum. Find the maximum achievable sum.
- **Constraints**:
  - `3 <= n <= 2 * 10^5`
  - `-10^9 <= a[i] <= 10^9`
  - Must smooth exactly one middle element (not first or last)
- **Hint**: Precompute best prefix/suffix Kadane values; test smoothing effect as replacing `a[i]` with new value and combining left/right bests.
- **Examples**:
  - Example 1:
    - Input: `[-2, 3, -4, 5]`
    - Output: `9` (smooth -4 with neighbors -> floor((3-4+5)/3)=1; subarray 3+1+5=9)
    - Explanation: Original max subarray is 5. After smoothing index 2: [−2,3,1,5], max subarray is 3+1+5=9
  - Example 2:
    - Input: `[5, -10, 3, -2, 8]`
    - Output: `14` (smooth -2 with neighbors -> floor((3-2+8)/3)=3; subarray 3+3+8=14)
    - Explanation: Original max subarray is 8. After smoothing index 3: [5, -10, 3, 3, 8], max subarray is 3+3+8=14


### Function Signatures:

```java
// Java
class Solution {
    public long bestStreakWithSmoothing(int[] a) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.bestStreakWithSmoothing(a));
    }
}
```

```python
# Python
def best_streak_with_smoothing(a: list[int]) -> int:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    result = best_streak_with_smoothing(a)
    print(result)
```

```cpp
// C++
class Solution {
public:
    long long bestStreakWithSmoothing(vector<int>& a) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    Solution sol;
    cout << sol.bestStreakWithSmoothing(a);
    return 0;
}
```

### Quiz Question:

**Q**: In the smoothing problem, why do we need to precompute prefix and suffix Kadane arrays instead of just running Kadane after each smoothing attempt?

- A) To handle negative numbers correctly
- B) To reduce time complexity from O(n²) to O(n)
- C) To save memory
- D) To avoid integer overflow

**Answer**: B) To reduce time complexity from O(n²) to O(n) - Running Kadane for each of n possible smoothing positions would be O(n²). Precomputing lets us evaluate each position in O(1).

## 10) Early Discount With Stay Window and Ceiling

- **Problem ID**: `ARRAY-010`
- **Display ID**: `A010`
- **Slug**: `early-discount-stay-window`
- **Difficulty**: Medium
- **Tags**: `sliding-window`, `stock-trading`, `arrays`, `greedy`
- **Problem**: You may buy once and sell once. You must hold the item for at least `dMin` days and at most `dMax` days, and the sell price must not exceed a ceiling `C` (if price > C, you are forced to sell at C). Return maximum achievable profit (or 0 if not profitable).
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - `0 <= price[i] <= 10^9`
  - `1 <= dMin <= dMax <= n`
  - `0 <= C <= 10^9`
- **Hint**: Track best effective buy value up to day i-dMin; when selling on day i, profit = min(price[i], C) - best buy in window [i-dMax, i-dMin].
- **Examples**:
  - Example 1:
    - Input: `prices=[7,2,5,1,9], dMin=1, dMax=3, C=6`
    - Output: `5` (buy at 1 on day 3, sell at min(9,6)=6 on day 4)
    - Explanation: Buy at price 1, sell at capped price 6, profit=5
  - Example 2:
    - Input: `prices=[5,4,3,2,1], dMin=1, dMax=2, C=10`
    - Output: `0` (prices declining, no profit possible)
    - Explanation: All valid buy-sell pairs result in negative profit

### Function Signatures:

```java
// Java
class Solution {
    public int maxProfitWithConstraints(int[] prices, int dMin, int dMax, int C) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] prices = new int[n];
        for (int i = 0; i < n; i++) {
            prices[i] = sc.nextInt();
        }
        int dMin = sc.nextInt();
        int dMax = sc.nextInt();
        int C = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.maxProfitWithConstraints(prices, dMin, dMax, C));
    }
}
```

```python
# Python
def max_profit_with_constraints(prices: list[int], dMin: int, dMax: int, C: int) -> int:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    dMin, dMax, C = map(int, input().split())
    result = max_profit_with_constraints(prices, dMin, dMax, C)
    print(result)
```

```cpp
// C++
class Solution {
public:
    int maxProfitWithConstraints(vector<int>& prices, int dMin, int dMax, int C) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> prices(n);
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }
    int dMin, dMax, C;
    cin >> dMin >> dMax >> C;
    Solution sol;
    cout << sol.maxProfitWithConstraints(prices, dMin, dMax, C);
    return 0;
}
```

### Quiz Question:

**Q**: In the stock trading problem with holding period constraints, why do we need to track the minimum buy price in a sliding window rather than the global minimum?

- A) To reduce memory usage
- B) Because we can only sell within a specific time window after buying
- C) To handle the price ceiling correctly
- D) To avoid negative profits

**Answer**: B) Because we can only sell within a specific time window after buying - The holding period [dMin, dMax] means we can't use prices outside this window relative to our buy day.

## 11) Leaky Roof Reinforcement

- **Problem ID**: `ARRAY-011`
- **Display ID**: `A011`
- **Slug**: `leaky-roof-reinforcement`
- **Difficulty**: Medium
- **Tags**: `prefix-suffix`, `arrays`, `greedy`, `optimization`
- **Problem**: Given roof heights, you can add planks on top of any positions (increase height) so that water will not spill off either end when raining (heights become non-decreasing from left to peak and non-increasing to right). Find the minimum total plank height to add to achieve a single-peak non-leaking profile; peak can be any index.
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - `0 <= height[i] <= 10^9`
  - Can only add planks (increase height), not remove
- **Hint**: Precompute non-decreasing prefix maxima and suffix maxima; for each peak, cost = sum(maxLeft[i],maxRight[i]) - current heights; take minimum.
- **Examples**:
  - Example 1:
    - Input: `[4,1,3,1,5]`
    - Output: `7`
    - Explanation: Choose peak at index 4 (height 5). Left: [4,4,4,4,5] adds 0+3+1+3=7, right adds 0. Total=7
  - Example 2:
    - Input: `[1,2,3,2,1]`
    - Output: `0`
    - Explanation: Already forms a peak at index 2, no planks needed

### Function Signatures:

```java
// Java
class Solution {
    public long minPlanksForRoof(int[] height) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] height = new int[n];
        for (int i = 0; i < n; i++) {
            height[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.minPlanksForRoof(height));
    }
}
```

```python
# Python
def min_planks_for_roof(height: list[int]) -> int:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    height = list(map(int, input().split()))
    result = min_planks_for_roof(height)
    print(result)
```

```cpp
// C++
class Solution {
public:
    long long minPlanksForRoof(vector<int>& height) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }
    Solution sol;
    cout << sol.minPlanksForRoof(height);
    return 0;
}
```

### Quiz Question:

**Q**: In the leaky roof problem, why do we need to try each position as a potential peak rather than just choosing the maximum height?

- A) The maximum might be at an endpoint
- B) The cost depends on both left and right reinforcement needs, not just peak height
- C) To handle duplicate heights
- D) To optimize memory usage

**Answer**: B) The cost depends on both left and right reinforcement needs, not just peak height - A lower peak position might require less total reinforcement than forcing everything to reach the global maximum.

## 12) Longest Zero-Sum Even Length

- **Problem ID**: `ARRAY-012`
- **Display ID**: `A012`
- **Slug**: `longest-zero-sum-even`
- **Difficulty**: Medium
- **Tags**: `prefix-sum`, `hashing`, `arrays`, `subarray`
- **Problem**: Find the maximum even length of a subarray with sum zero.
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - `-10^9 <= arr[i] <= 10^9`
  - Return 0 if no such subarray exists
- **Hint**: Prefix sums with hashmap of first index for each parity bucket.
- **Examples**:
  - Example 1:
    - Input: `[1, -1, 3, -3, 2]`
    - Output: `4` (subarray [1,-1,3,-3] from indices 0..3)
    - Explanation: Sum is 0, length is 4 (even)
  - Example 2:
    - Input: `[2, -2, 5, -5, 1, -1]`
    - Output: `6` (entire array sums to 0)
    - Explanation: All elements sum to 0, length 6 is even

### Function Signatures:

```java
// Java
class Solution {
    public int longestZeroSumEvenLength(int[] arr) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.longestZeroSumEvenLength(arr));
    }
}
```

```python
# Python
def longest_zero_sum_even_length(arr: list[int]) -> int:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_zero_sum_even_length(arr)
    print(result)
```

```cpp
// C++
class Solution {
public:
    int longestZeroSumEvenLength(vector<int>& arr) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution sol;
    cout << sol.longestZeroSumEvenLength(arr);
    return 0;
}
```

### Quiz Question:

**Q**: When finding zero-sum subarrays using prefix sums, what does it mean if two indices have the same prefix sum?

- A) The elements at those indices are equal
- B) The subarray between them has sum zero
- C) The array is sorted
- D) There are no negative numbers

**Answer**: B) The subarray between them has sum zero - If prefix[i] == prefix[j], then sum(i+1 to j) = prefix[j] - prefix[i] = 0.

## 13) Tool Frequency Top K with Recency Decay

- **Problem ID**: `ARRAY-013`
- **Display ID**: `A013`
- **Slug**: `tool-frequency-top-k-decay`
- **Difficulty**: Medium
- **Tags**: `heap`, `hashing`, `arrays`, `priority-queue`
- **Problem**: Each element appears with a timestamp. Score of value v is `sum(exp(-(now - t_i)/D))` over its occurrences (D given). Return the k values with highest decayed score; ties broken by smaller value.
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - Timestamps non-decreasing, up to 1e9
  - `1 <= k <= n`
  - `1 <= D <= 10^6`
  - `0 <= value <= 10^9`
- **Hint**: Aggregate scores per value using decay formula; maintain top-k via min-heap.
- **Examples**:
  - Example 1:
    - Input: `values=[3@0,1@0,3@5,2@6,1@9], now=10, D=5, k=2`
    - Output: `[3,1]`
    - Explanation: Score(3)=e^(-10/5)+e^(-5/5)≈0.135+0.368=0.503; Score(1)=e^(-10/5)+e^(-1/5)≈0.135+0.819=0.954; Top 2: [1,3] but ties broken by value, so [3,1]
  - Example 2:
    - Input: `values=[5@0,5@1,3@2], now=5, D=2, k=1`
    - Output: `[5]`
    - Explanation: Score(5)=e^(-5/2)+e^(-4/2)≈0.082+0.135=0.217; Score(3)=e^(-3/2)≈0.223; Top 1 is [3]

### Function Signatures:

```java
// Java
class Solution {
    public List<Integer> topKWithDecay(int[][] events, int now, int D, int k) {
        // Implementation
        // events[i] = {value, timestamp}
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] events = new int[n][2];
        for (int i = 0; i < n; i++) {
            events[i][0] = sc.nextInt(); // value
            events[i][1] = sc.nextInt(); // timestamp
        }
        int now = sc.nextInt();
        int D = sc.nextInt();
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.topKWithDecay(events, now, D, k));
    }
}
```

```python
# Python
def top_k_with_decay(events: list[tuple[int, int]], now: int, D: int, k: int) -> list[int]:
    # Implementation
    # events: [(value, timestamp), ...]
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    events = []
    for _ in range(n):
        value, timestamp = map(int, input().split())
        events.append((value, timestamp))
    now, D, k = map(int, input().split())
    result = top_k_with_decay(events, now, D, k)
    print(result)
```

```cpp
// C++
class Solution {
public:
    vector<int> topKWithDecay(vector<pair<int,int>>& events, int now, int D, int k) {
        // Implementation
        // events: {value, timestamp}
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<int,int>> events(n);
    for (int i = 0; i < n; i++) {
        cin >> events[i].first >> events[i].second;
    }
    int now, D, k;
    cin >> now >> D >> k;
    Solution sol;
    vector<int> result = sol.topKWithDecay(events, now, D, k);
    for (int x : result) cout << x << " ";
    return 0;
}
```

### Quiz Question:

**Q**: In the exponential decay scoring problem, why is a min-heap of size k more efficient than sorting all values by score?

- A) Min-heaps use less memory
- B) It reduces time complexity from O(n log n) to O(n log k)
- C) It handles ties better
- D) It avoids floating point errors

**Answer**: B) It reduces time complexity from O(n log n) to O(n log k) - Maintaining a heap of size k requires O(log k) per insertion, vs O(n log n) for full sorting, where k << n.

## 14) Boarding Order With Fixed Ones

- **Problem ID**: `ARRAY-014`
- **Display ID**: `A014`
- **Slug**: `boarding-order-fixed-ones`
- **Difficulty**: Medium
- **Tags**: `sorting`, `arrays`, `three-way-partition`, `stable-sort`
- **Problem**: Array contains only 0s,1s,2s. All 1s are already in correct relative order and must not move. Sort the array (0s before 1s before 2s) while keeping 1s in place.
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - Array contains only values 0, 1, 2
  - Relative order of 1s must be preserved
- **Hint**: Two-pass to fill 0s from left skipping 1s, then fill 2s from right skipping 1s.
- **Examples**:
  - Example 1:
    - Input: `[2,1,0,2,0,1]`
    - Output: `[0,1,0,1,2,2]`
    - Explanation: 1s at positions 1,5 stay; place 0s in remaining left positions, 2s in right
  - Example 2:
    - Input: `[0,1,2,1,0]`
    - Output: `[0,1,0,1,2]`
    - Explanation: 1s at positions 1,3 fixed; rearrange 0s and 2s around them

### Function Signatures:

```java
// Java
class Solution {
    public void sortWithFixedOnes(int[] arr) {
        // Implementation (in-place)
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        sol.sortWithFixedOnes(arr);
        System.out.println(Arrays.toString(arr));
    }
}
```

```python
# Python
def sort_with_fixed_ones(arr: list[int]) -> None:
    # Implementation (in-place)
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    sort_with_fixed_ones(arr)
    print(arr)
```

```cpp
// C++
class Solution {
public:
    void sortWithFixedOnes(vector<int>& arr) {
        // Implementation (in-place)
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution sol;
    sol.sortWithFixedOnes(arr);
    for (int x : arr) cout << x << " ";
    return 0;
}
```

### Quiz Question:

**Q**: What is the key challenge in sorting an array with fixed elements compared to standard Dutch National Flag problem?

- A) Handling negative numbers
- B) Maintaining stability while some positions are immovable
- C) Counting the number of each element
- D) Managing memory efficiently

**Answer**: B) Maintaining stability while some positions are immovable - We must work around fixed 1s and correctly place 0s and 2s in available positions without disturbing the 1s.

## 15) Seat Gap After Removals

- **Problem ID**: `ARRAY-015`
- **Display ID**: `A015`
- **Slug**: `seat-gap-after-removals`
- **Difficulty**: Easy-Medium
- **Tags**: `arrays`, `simulation`, `greedy`
- **Problem**: Seats are sorted; remove seats at given indices (by position in array, not seat number). After removals, return max gap between remaining consecutive seats.
- **Constraints**:
  - `2 <= n <= 2 * 10^5`
  - `0 <= seats[i] <= 10^9`
  - Seats array is sorted
  - `1 <= |removals| <= n-2` (at least 2 seats remain)
  - Removal indices are valid (0 to n-1)
- **Hint**: Use set of indices; iterate remaining to compute gaps.
- **Examples**:
  - Example 1:
    - Input: `seats=[2,5,9,10], remove indices=[1]` (remove seat 5)
    - Output: `7` (gap between 2 and 9)
    - Explanation: Remaining seats [2,9,10], gaps are 7 and 1, max is 7
  - Example 2:
    - Input: `seats=[1,3,7,12,20], remove indices=[0,2]` (remove 1 and 7)
    - Output: `9` (gap between 3 and 12)
    - Explanation: Remaining [3,12,20], gaps 9 and 8, max is 9

### Function Signatures:

```java
// Java
class Solution {
    public int maxGapAfterRemovals(int[] seats, int[] removeIndices) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] seats = new int[n];
        for (int i = 0; i < n; i++) {
            seats[i] = sc.nextInt();
        }
        int r = sc.nextInt();
        int[] removeIndices = new int[r];
        for (int i = 0; i < r; i++) {
            removeIndices[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.maxGapAfterRemovals(seats, removeIndices));
    }
}
```

```python
# Python
def max_gap_after_removals(seats: list[int], remove_indices: list[int]) -> int:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    seats = list(map(int, input().split()))
    r = int(input())
    remove_indices = list(map(int, input().split()))
    result = max_gap_after_removals(seats, remove_indices)
    print(result)
```

```cpp
// C++
class Solution {
public:
    int maxGapAfterRemovals(vector<int>& seats, vector<int>& removeIndices) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> seats(n);
    for (int i = 0; i < n; i++) {
        cin >> seats[i];
    }
    int r;
    cin >> r;
    vector<int> removeIndices(r);
    for (int i = 0; i < r; i++) {
        cin >> removeIndices[i];
    }
    Solution sol;
    cout << sol.maxGapAfterRemovals(seats, removeIndices);
    return 0;
}
```

### Quiz Question:

**Q**: When computing maximum gap after removals, what data structure provides efficient O(1) lookup to check if an index should be removed?

- A) Array
- B) HashSet
- C) LinkedList
- D) Stack

**Answer**: B) HashSet - Converting removal indices to a HashSet allows O(1) lookup when iterating through seats to determine which to skip.

## 16) Power Window With Drop

- **Problem ID**: `ARRAY-016`
- **Display ID**: `A016`
- **Slug**: `power-window-with-drop`
- **Difficulty**: Medium
- **Tags**: `sliding-window`, `arrays`, `greedy`, `optimization`
- **Problem**: Given positive integers and window size `k`, find the maximum sum of any window after optionally removing one element from that window (you may also remove none). Return that maximal adjusted sum.
- **Constraints**:
  - `1 <= n <= 2 * 10^5`
  - `1 <= k <= n`
  - `1 <= arr[i] <= 10^9`
  - All elements are positive integers
- **Hint**: Maintain window sum and track minimum element in window to consider dropping.
- **Examples**:
  - Example 1:
    - Input: `arr=[2,1,5,3,2], k=3`
    - Output: `10` (window [5,3,2] sum=10, no drop needed)
    - Explanation: Windows: [2,1,5]=8 drop 1→7, [1,5,3]=9 drop 1→8, [5,3,2]=10 no drop. Max is 10
  - Example 2:
    - Input: `arr=[10,1,20,30], k=3`
    - Output: `50` (window [1,20,30] sum=51, drop 1→50)
    - Explanation: Window [10,1,20]=31 drop 1→30, [1,20,30]=51 drop 1→50. Max is 50

### Function Signatures:

```java
// Java
class Solution {
    public long maxWindowSumWithDrop(int[] arr, int k) {
        // Implementation
    }
}

// Custom Input
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.maxWindowSumWithDrop(arr, k));
    }
}
```

```python
# Python
def max_window_sum_with_drop(arr: list[int], k: int) -> int:
    # Implementation
    pass

# Custom Input
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    result = max_window_sum_with_drop(arr, k)
    print(result)
```

```cpp
// C++
class Solution {
public:
    long long maxWindowSumWithDrop(vector<int>& arr, int k) {
        // Implementation
    }
};

// Custom Input
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int k;
    cin >> k;
    Solution sol;
    cout << sol.maxWindowSumWithDrop(arr, k);
    return 0;
}
```

### Quiz Question:

**Q**: In the power window with drop problem, why do we track the minimum element in each window?

- A) To calculate the average
- B) To drop it and potentially maximize the sum
- C) To maintain sorted order
- D) To handle negative numbers

**Answer**: B) To drop it and potentially maximize the sum - Since we can drop at most one element, removing the minimum from each window gives the maximum possible sum for that window.
