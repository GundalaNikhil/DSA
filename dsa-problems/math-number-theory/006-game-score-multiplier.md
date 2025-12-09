# Game Score Multiplier

**Problem ID:** MATH-006
**Display ID:** 113
**Question Name:** Game Score Multiplier
**Slug:** game-score-multiplier
**Title:** Calculate Power with Modulo for Leaderboards
**Difficulty:** Hard
**Premium:** No
**Tags:** Math, Modular Exponentiation, Number Theory, Fast Power Algorithm

## Problem Description

You are developing a competitive gaming leaderboard system where players' final scores are calculated using a complex multiplier formula. Given a base score `base`, a combo multiplier `exponent`, and a modulo value `mod` (to prevent integer overflow), calculate (base^exponent) % mod efficiently using fast exponentiation. This is crucial for games with exponential scoring systems where combo chains can reach hundreds of multipliers.

## A Simple Scenario (Daily Life Usage)

Imagine you're a backend engineer at Riot Games working on League of Legends' mastery point system. A player just completed a game with a base score of 1847 points and achieved a combo multiplier of 43 through excellent gameplay. To prevent database overflow and ensure fair comparison, you need to calculate their final score modulo 1,000,000,007. Using fast exponentiation, you efficiently compute (1847^43) % 1000000007 = 653,921,782 without your server crashing from integer overflow!

## Your Task

Write a function that takes three integers: `base`, `exponent`, and `mod`, then returns (base^exponent) % mod. Implement the binary exponentiation algorithm (also called exponentiation by squaring) to handle large exponents efficiently. The naive approach of multiplying base by itself exponent times will timeout.

## Why is it Important?

This problem teaches you how to:

- Implement fast exponentiation using binary decomposition
- Apply modular arithmetic properties: (a*b) % m = ((a%m) * (b%m)) % m
- Optimize exponential time complexity to logarithmic
- Handle extremely large numbers without overflow
- Solve a fundamental problem used in cryptography and competitive programming

## Examples

### Example 1:

**Input:** `base = 2, exponent = 10, mod = 1000`
**Output:** `24`
**Explanation:** 2^10 = 1024, and 1024 % 1000 = 24

### Example 2:

**Input:** `base = 1847, exponent = 43, mod = 1000000007`
**Output:** `653921782`
**Explanation:** Calculate (1847^43) % 1000000007 using fast exponentiation to avoid overflow.

### Example 3:

**Input:** `base = 5, exponent = 0, mod = 13`
**Output:** `1`
**Explanation:** Any number to the power of 0 equals 1.

### Example 4:

**Input:** `base = 7, exponent = 256, mod = 1000000007`
**Output:** `902285735`
**Explanation:** Even with a large exponent like 256, fast exponentiation computes this in ~8 steps.

### Example 5:

**Input:** `base = 999999937, exponent = 123456, mod = 1000000007`
**Output:** `259890365`
**Explanation:** Both base and exponent are large, demonstrating why the algorithm must be efficient.

## Constraints

- 0 ≤ base < 10^9
- 0 ≤ exponent ≤ 10^9
- 1 < mod ≤ 10^9 + 7
- Must use O(log exponent) time complexity
- Cannot use built-in power functions with modulo
- Result must fit in a 64-bit integer

## Algorithm Hint

Binary Exponentiation works by:
1. If exponent is 0, return 1
2. If exponent is even: base^n = (base^(n/2))^2
3. If exponent is odd: base^n = base * base^(n-1)
4. Apply modulo at each step to prevent overflow

## Follow-up

1. Can you implement this iteratively instead of recursively?
2. How would you handle negative exponents?
3. What's the time complexity and why is it logarithmic?

## Asked by Companies

- Riot Games
- Supercell
- King (Candy Crush)
- Zynga
- Electronic Arts
- Activision Blizzard
