# Probability & Randomized Algorithms Practice Set (16 Questions)

## 1) Coin Flip Streak Probability

- Slug: coin-flip-streak-probability
- Difficulty: Easy-Medium
- Problem: Fair coin flipped `n` times. Compute probability of getting at least one streak of `k` consecutive heads.
- Constraints: `1 <= n <= 60`, `1 <= k <= n`.
- Hint: DP with states (pos, current run).
- Example:
  - Input: `n=3, k=2`
  - Output: `0.25`

## 2) Expected Steps Random Walk 1D

- Slug: expected-steps-random-walk-1d
- Difficulty: Medium
- Problem: On integer line starting at 0, each step move +1 with prob p else -1. Expected steps to hit +a or -b (absorbing). Compute in closed form or via DP.
- Constraints: `1 <= a,b <= 200`, `0 < p < 1`.
- Example:
  - Input: `a=2, b=1, p=0.5`
  - Output: `2`

## 3) Reservoir Sampling K Items

- Slug: reservoir-sampling-k
- Difficulty: Medium
- Problem: Given a stream of unknown length, design a method to sample `k` items uniformly at random without storing full stream. Explain and output sample for a fixed seed.
- Constraints: Stream length up to 10^6.
- Example:
  - Input: stream `[1..10], k=3, seed=42`
  - Output: One valid sample (deterministic under seed)

## 4) Monte Carlo Estimation of Pi

- Slug: monte-carlo-pi
- Difficulty: Easy
- Problem: Estimate π using N random points in unit square; return estimate and error bound with 95% confidence.
- Constraints: `1 <= N <= 10^6`.
- Example:
  - Input: `N=10000`
  - Output: estimate ~3.14, error <= 0.02

## 5) Bloom Filter False Positive Rate

- Slug: bloom-filter-fpr
- Difficulty: Medium
- Problem: Given m bits, k hash functions, and n inserted items, compute false positive probability of a Bloom filter.
- Constraints: `1 <= m,n <= 10^6`, `1 <= k <= 20`.
- Example:
  - Input: m=1000, k=3, n=100
  - Output: ~0.082

## 6) Min-Cut with Randomized Contraction

- Slug: min-cut-random-contraction
- Difficulty: Medium
- Problem: Implement Karger’s randomized contraction to find global min-cut; run enough trials to get success probability >= 0.99. Return best cut size found.
- Constraints: n<=200, m<=2000.
- Example:
  - Input: small graph; output min cut size 2

## 7) Skip List Expected Height

- Slug: skip-list-expected-height
- Difficulty: Medium
- Problem: For skip list with promotion probability p, derive expected height after inserting n elements.
- Constraints: `1 <= n <= 10^6`, `0 < p < 1`.
- Example:
  - Input: n=1024, p=0.5
  - Output: expected height ~ log\_{1/p} n = 10

## 8) Randomized Quickselect Expected Comparisons

- Slug: quickselect-expected-comparisons
- Difficulty: Medium
- Problem: For random pivot quickselect on n distinct elements, compute expected number of comparisons to find k-th order statistic.
- Constraints: `1 <= n <= 10^5`.
- Example:
  - Input: n=5, k=3
  - Output: expected comparisons around 8 (show calculation)

## 9) Treap Priority Invariants

- Slug: treap-priority-invariants
- Difficulty: Medium
- Problem: For a treap with random priorities, compute expected depth of a node and expected total path length for n nodes.
- Constraints: `1 <= n <= 10^6`.
- Example:
  - Input: n=4
  - Output: expected depth of a node ~ H_n

## 10) Markov Chain Absorption

- Slug: markov-chain-absorption
- Difficulty: Medium
- Problem: Given small Markov chain with absorbing states, compute absorption probabilities and expected steps to absorption.
- Constraints: states <= 20.
- Example:
  - Input: transition matrix 3x3 with state2 absorbing
  - Output: absorption probs, expected steps vector

## 11) Coupon Collector Expected Trials

- Slug: coupon-collector-expected
- Difficulty: Easy-Medium
- Problem: With N equally likely coupons, expected draws to collect all.
- Constraints: `1 <= N <= 10^6`.
- Example:
  - Input: N=3
  - Output: `3 * (1 + 1/2 + 1/3) ≈ 5.5`

## 12) Poisson Approximation of Binomial

- Slug: poisson-approx-binomial
- Difficulty: Medium
- Problem: Given n, p where n large, p small, approximate P(X = k) for Binomial(n,p) using Poisson λ=np. Provide error bound.
- Constraints: n<=10^6, p<=0.01.
- Example:
  - Input: n=200, p=0.01, k=3
  - Output: approx value, compare to exact

## 13) Random Walk Hitting Probability 2D

- Slug: random-walk-hitting-prob-2d
- Difficulty: Hard
- Problem: Simple symmetric random walk on Z^2 starting at (0,0). Compute probability of ever hitting point (a,b) (non-zero) within T steps (finite horizon).
- Constraints: |a|,|b|<=10, T<=500.
- Hint: DP over steps and positions bounded by T.
- Example:
  - Input: a=1, b=0, T=2
  - Output: 0.5

## 14) Randomized MST Verification

- Slug: randomized-mst-verification
- Difficulty: Medium
- Problem: Given a graph and a claimed MST weight W, design randomized algorithm to verify with high probability whether MST weight equals W without computing MST exactly.
- Constraints: n<=1e5, m<=2e5.
- Hint: Use random sampling + cut property checks; or random contraction preserving min cuts.
- Example:
  - Input: small graph, claimed W=10
  - Output: accept/reject with probability

## 15) Median of Uniforms CLT

- Slug: median-uniforms-clt
- Difficulty: Medium
- Problem: Sample n i.i.d. U(0,1) variables. Approximate distribution of their median using CLT; compute mean and variance approximation; compare to exact for small n.
- Constraints: n<=1000.
- Example:
  - Input: n=5
  - Output: mean 0.5, variance approx ... (show value)

## 16) Random Permutation Cycle Structure

- Slug: permutation-cycle-structure
- Difficulty: Medium
- Problem: For random permutation of n, compute expected number of cycles of length exactly k, and expected length of longest cycle (qualitative or approximate).
- Constraints: n<=1e5, k<=n.
- Example:
  - Input: n=5, k=2
  - Output: expected cycles of length 2 is ~0.5
