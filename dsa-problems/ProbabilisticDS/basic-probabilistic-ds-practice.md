# Probabilistic Data Structures Practice Set (14 Questions)

## 1) Bloom Filter Design

- Slug: bloom-filter-design
- Difficulty: Medium
- Problem: Given expected items n and desired false-positive rate f, choose optimal bit array size m and hash count k; compute expected FPR.
- Constraints: `1 <= n <= 10^6`, `0 < f < 1`.
- Example:
  - Input: n=1000, f=0.01
  - Output: m≈9585, k≈7, FPR≈0.01

## 2) Counting Bloom Filter

- Slug: counting-bloom-filter
- Difficulty: Medium
- Problem: Extend Bloom filter to support deletions using counters; compute probability of counter overflow given c-bit counters and n inserts.
- Constraints: `1 <= n <= 10^5`.
- Example:
  - Input: m=1000, k=3, c=4, n=500
  - Output: small overflow probability estimate

## 3) Cuckoo Hashing Success Probability

- Slug: cuckoo-hashing-success
- Difficulty: Medium
- Problem: Given table size m, two hash functions, load factor α, estimate probability of insertion failure due to cycles.
- Constraints: `0 < α < 1`.
- Example:
  - Input: m=1000, α=0.5
  - Output: very low failure probability

## 4) Count-Min Sketch Error Bound

- Slug: count-min-sketch
- Difficulty: Medium
- Problem: For width w, depth d CMS, derive error bound ε and failure δ; given desired ε,δ compute w,d.
- Constraints: `1 <= w,d <= 10^6`.
- Example:
  - Input: ε=0.01, δ=0.01
- Output: w=272, d=5 (approx)

## 5) Frequent Items with Misra-Gries

- Slug: misra-gries
- Difficulty: Medium
- Problem: Using k-1 counters, guarantee finding all items with frequency > n/k. Implement and return candidates.
- Constraints: `1 <= n <= 10^6`, `2 <= k <= 1000`.
- Example:
  - Input: stream [1,2,1,3,1,2,4], k=3
  - Output: candidates [1,2]

## 6) HyperLogLog Cardinality Estimate

- Slug: hyperloglog-estimate
- Difficulty: Medium
- Problem: Given HLL parameters (m registers) and observed register maxima, compute cardinality estimate and bias correction.
- Constraints: m power of two up to 2^16.
- Example:
  - Input: m=16, registers sample => estimate around true count

## 7) Flajolet-Martin Bit Pattern

- Slug: flajolet-martin
- Difficulty: Medium
- Problem: Use FM algorithm to estimate distinct count from hash trailing zeros; compute expected estimate and variance.
- Constraints: stream length <= 10^6.
- Example:
  - Input: hashes with max trailing zeros = 4
  - Output: estimate ~16

## 8) Bottom-k Sampling (Min-Hash)

- Slug: bottom-k-sampling
- Difficulty: Medium
- Problem: Maintain bottom-k hash values to estimate set similarity (Jaccard); compute estimator for intersection/union.
- Constraints: sets up to 10^6 elements.
- Example:
  - Input: sets A,B with hash minima; output Jaccard estimate

## 9) k-Minimum Values (KMV) Distinct Count

- Slug: kmv-distinct-count
- Difficulty: Medium
- Problem: Keep k smallest hash values; estimate distinct count as (k-1)/h_k where h_k is kth smallest hash.
- Constraints: k<=10^5.
- Example:
  - Input: k=3, hashes [0.1,0.2,0.4] => h3=0.4
  - Output: estimate ~5

## 10) Heavy Hitters with Count Sketch

- Slug: count-sketch-heavy-hitters
- Difficulty: Medium
- Problem: Use Count Sketch to approximate frequencies; return top T heavy hitters with error bound.
- Constraints: stream length <= 10^6.
- Example:
  - Input: stream frequencies; output approximate top

## 11) Sliding Window Distinct with Exponential Decay

- Slug: sliding-window-decayed-distinct
- Difficulty: Medium
- Problem: Estimate distinct elements in sliding window with exponential decay using probabilistic DS (e.g., exponential histograms + HLL).
- Constraints: window up to 10^6.
- Example:
  - Input: toy stream; output estimate

## 12) Bloomier Filter Key-Value

- Slug: bloomier-filter
- Difficulty: Hard
- Problem: Store key->value mapping with small false positives using Bloomier filter; design construction with XOR hashing.
- Constraints: keys <= 10^5.
- Example:
  - Input: 3 key-value pairs, queries return correct or false positive default

## 13) XOR Filters

- Slug: xor-filters
- Difficulty: Medium
- Problem: Build an XOR filter for static set of keys; analyze space and FPR.
- Constraints: keys <= 10^5.
- Example:
  - Input: key hashes; output filter array

## 14) Perfect Hashing via Randomization

- Slug: perfect-hashing-random
- Difficulty: Medium
- Problem: For static set, design two-level randomized perfect hash with expected O(n) space and O(1) query.
- Constraints: n<=10^5.
- Example:
  - Input: small key set
  - Output: constructed tables
