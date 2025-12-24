#  Number Theory & Combinatorics Practice Set (16 Questions)

## 1) Classroom GCD Prefix Queries

- Slug: classroom-gcd-prefix-queries
- Difficulty: Easy-Medium
- Problem: Given array `a`, answer queries asking `gcd(a[0..r])` for various `r` in O(1) after preprocessing.
- Constraints: `1 <= n <= 2 * 10^5`, `|a[i]| <= 10^9`, `1 <= q <= 2 * 10^5`.
- Hint: Precompute prefix GCDs; each answer is prefix[r].
- Example:
  - Input: `a=[12,18,6], queries=[0,1,2]`
  - Output: `[12,6,6]`

## 2) Coprime Pair Count Up To N

- Slug: coprime-pair-count
- Difficulty: Medium
- Problem: For given `N`, count ordered pairs `(i,j)` with `1 <= i < j <= N` and `gcd(i,j)=1`.
- Constraints: `1 <= N <= 10^5`.
- Hint: Use Euler’s totient: total pairs = sum\_{k=2..N} phi(k); precompute phi via sieve.
- Example:
  - Input: `N=5`
  - Output: `7` (pairs: (1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4))

## 3) Modular Inverse Existence

- Slug: modular-inverse-existence
- Difficulty: Easy
- Problem: For each query `(a, m)`, report whether `a` has a modular inverse modulo `m` (i.e., gcd(a,m)=1).
- Constraints: `1 <= q <= 10^5`, `1 <= a,m <= 10^9`.
- Hint: Compute gcd via Euclid.
- Example:
  - Input: `(a=4,m=7)`
  - Output: `true`

## 4) Minimal Base Representation

- Slug: minimal-base-representation
- Difficulty: Medium
- Problem: Given integer `x (>=2)`, find the smallest base `b (2<=b<=36)` such that the sum of digits of `x` in base `b` is minimized; return `(b, digitSum)`.
- Constraints: `2 <= x <= 10^12`.
- Hint: For large bases, digit sum approaches x; test bases up to cubic root; also consider representing x as `a*b + c`.
- Example:
  - Input: `x=31`
  - Output: `b=5, digitSum=3` (31 in base5 is 111)

## 5) Factorials With Missing Primes

- Slug: factorials-missing-primes
- Difficulty: Medium
- Problem: Given `n` and a forbidden prime `p`, compute `n!` modulo `p` but with all factors divisible by `p` removed before multiplying. Return result mod p.
- Constraints: `1 <= n <= 10^12`, `p` prime, `2 <= p <= 10^6`.
- Hint: Use multiplicative pattern over blocks of size p; exclude multiples of p.
- Example:
  - Input: `n=6, p=5`
  - Output: `4` (6! without multiples of 5 is 6*4*3*2*1 = 144 mod5 = 4)

## 6) Distinct Prime Factors Count Prefix

- Slug: distinct-prime-factors-prefix
- Difficulty: Medium
- Problem: Precompute number of distinct prime factors for each `1..N`, then answer sum queries on ranges `[l,r]`.
- Constraints: `1 <= N <= 10^6`, `1 <= q <= 10^5`.
- Hint: Modified sieve counting distinct primes; prefix sums to answer queries.
- Example:
  - Input: `N=6`, query `[2,5]`
  - Output: `4` (distinct prime factors: 2->1,3->1,4->1,5->1)

## 7) LCM of Ranges

- Slug: lcm-of-ranges
- Difficulty: Medium
- Problem: Given array `a`, for each query `[l,r]` (small length <= 20), compute `lcm(a[l..r])` modulo `MOD`.
- Constraints: `1 <= n <= 2 * 10^5`, `1 <= a[i], MOD <= 10^9+7`, `r-l <= 20`, `1 <= q <= 10^5`.
- Hint: Prime-factorize on the fly for short ranges; track max exponents.
- Example:
  - Input: `a=[2,6,3], query [0,1], MOD=1000000007`
  - Output: `6`

## 8) Counting Lattice Points On Segment

- Slug: lattice-points-on-segment
- Difficulty: Easy
- Problem: Given endpoints (x1,y1),(x2,y2) integer coordinates, count integer lattice points on the closed segment.
- Constraints: `|coords| <= 10^9`.
- Hint: gcd of differences + 1.
- Example:
  - Input: `(0,0),(6,4)`
  - Output: `3` (points at (0,0),(3,2),(6,4))

## 9) Modular Exponent With Digit Stream

- Slug: modular-exponent-digit-stream
- Difficulty: Medium
- Problem: Given base `a` and a very large exponent provided as a digit string `e` in decimal, compute `a^e mod m`.
- Constraints: `1 <= a,m <= 10^9`, `1 <= |e| <= 10^5`.
- Hint: Process digits: result = pow(result,10)\*pow(a,digit) mod m.
- Example:
  - Input: `a=3, e="5", m=7`
  - Output: `5` (3^5 = 243; 243 mod 7 = 5)

## 10) Sum of Divisors in Range

- Slug: sum-divisors-range
- Difficulty: Medium
- Problem: Given `L,R`, compute sum of divisors function `sigma(n)` for all n in [L,R] modulo `MOD`.
- Constraints: `1 <= L <= R <= 10^6`, `MOD=10^9+7`.
- Hint: Precompute smallest prime factors; compute sigma per n; prefix to answer range sums.
- Example:
  - Input: `L=2, R=4`
  - Output: `14` (sigma(2)=3, sigma(3)=4, sigma(4)=7)

## 11) Ways to Climb With Jumps Set

- Slug: ways-climb-jump-set
- Difficulty: Medium
- Problem: You can climb `n` stairs using jumps only from set `J` (positive ints). Count ways modulo `MOD`.
- Constraints: `1 <= n <= 10^5`, `1 <= |J| <= 20`, `MOD=10^9+7`.
- Hint: DP where dp[i] = sum dp[i-j] over j in J if i>=j.
- Example:
  - Input: `n=4, J={1,3}`
  - Output: `3` (1+1+1+1, 1+3, 3+1)

## 12) Minimal Split for Equal Product

- Slug: minimal-split-equal-product
- Difficulty: Medium
- Problem: Given integer `x`, split its decimal digits into two non-empty numbers (preserving order in each part) so that their product is minimized but non-zero. Return the minimal product.
- Constraints: `10 <= x <= 10^12`.
- Hint: Try all split points; compute products.
- Example:
  - Input: `x=1234`
  - Output: `408` (12 \* 34)

## 13) Count Strings With Exact Vowels

- Slug: count-strings-exact-vowels
- Difficulty: Medium
- Problem: Count strings of length `n` over lowercase letters containing exactly `k` vowels. Return count modulo `MOD`.
- Constraints: `1 <= n <= 10^6`, `0 <= k <= n`, `MOD=10^9+7`.
- Hint: Combinatorics: C(n,k)*5^k*21^{n-k} mod MOD; precompute factorials.
- Example:
  - Input: `n=3, k=1`
  - Output: `3 * 5 * 21^2 mod = 3*5*441=6615 mod... large; choose smaller n: n=2,k=1 => 2*5*21=210`

## 14) Maximum Points on a Line Segment Length Limit

- Slug: maximum-points-line-segment-limit
- Difficulty: Medium
- Problem: Given points, find the maximum number of points that lie on the same line segment of length at most `L` (Euclidean distance between segment endpoints <= L). Return that maximum count.
- Constraints: `1 <= n <= 2000`, `1 <= L <= 10^6`, coordinates in `[-10^6,10^6]`.
- Hint: For each anchor, compute slopes; within each slope group, sort by projection distance and use sliding window of length <= L.
- Example:
  - Input: points `[(0,0),(1,1),(2,2),(0,1)]`, `L=2`
  - Output: `2` (any segment of length 2 covers at most two of the collinear points)

## 15) CRT Existence and Value

- Slug: crt-existence-value
- Difficulty: Medium
- Problem: Given congruences x ≡ ai (mod mi), determine if a solution exists; if yes, return smallest non-negative solution using generalized CRT (moduli not guaranteed coprime).
- Constraints: `1 <= k <= 10`, `1 <= mi <= 10^9`.
- Example:
  - Input: `(x ≡ 2 mod 6), (x ≡ 5 mod 9)`
  - Output: `14`

## 16) Count Surjective Functions

- Slug: count-surjective-functions
- Difficulty: Medium
- Problem: Count surjective functions from an n-element set to a k-element set (n,k up to 30). Return result modulo `MOD`.
- Constraints: `1 <= k <= n <= 30`, `MOD=10^9+7`.
- Hint: Inclusion-exclusion: k! \* S(n,k) or sum (-1)^i C(k,i) (k-i)^n.
- Example:
  - Input: `n=3, k=2`
  - Output: `6` (onto functions from 3 elements to 2)
