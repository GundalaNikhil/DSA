---
unique_problem_id: gametheory_006
display_id: GAMETHEORY-006
slug: divisor-turn-game
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - Number Theory
  - Dynamic Programming
  - Divisors
  - Win-Lose Analysis
---

# Divisor Turn Game

## Problem Description

Start with integer `n`. A move: replace n with any proper divisor (greater than 1). Player who cannot move loses. Determine winner.

## Examples

- Example 1:
  - Input: n = 2
  - Output: `Second`
  - Explanation: From 2, the only proper divisor > 1 is none (1 is not >1). First player cannot move, loses.

- Example 2:
  - Input: n = 6
  - Output: `First`
  - Explanation: Proper divisors of 6 > 1 are: 2, 3. First can move to 2 or 3. From 2: no moves. From 3: no moves. Either move makes opponent lose.

- Example 3:
  - Input: n = 12
  - Output: `First`
  - Explanation: Divisors > 1: 2, 3, 4, 6. First player can move to 2 or 3 (losing positions for opponent).

## Constraints

- `2 <= n <= 10^6`

## Function Signatures

### Java
```java
class Solution {
    public String divisorTurnGame(int n) {
        // Implementation here
    }
}
```

### Python
```python
def divisor_turn_game(n: int) -> str:
    """
    Determine winner of divisor turn game.
    
    Args:
        n: Starting integer
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string divisorTurnGame(int n) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- Single integer n

### Sample Input
```
6
```

## Hints

Precompute win/lose for all values up to n. A position is losing if ALL proper divisors lead to winning positions. Prime numbers have no proper divisors > 1, so they are losing positions.

## Quiz

### Question 1
What is the game state for a prime number p?

A) Win  
B) Lose  
C) Draw  
D) Depends on p

**Correct Answer:** B

**Explanation:** A prime p > 1 has no proper divisors > 1 (only 1 and itself). No valid moves means the current player loses.

### Question 2
What is the game state for n = 4?

A) Win  
B) Lose  
C) Draw  
D) Cannot determine

**Correct Answer:** A

**Explanation:** Divisors of 4 > 1: only 2. Move to 2, which is prime (losing). So 4 is winning.

### Question 3
How can we precompute win/lose states efficiently?

A) Use Sieve of Eratosthenes to find primes, then DP  
B) Brute force factorization for each number  
C) Recursive memoization from n down  
D) All of the above work

**Correct Answer:** D

**Explanation:** Multiple approaches work. Sieve identifies prime (losing) positions; then DP builds win/lose for composites based on their divisors.

### Question 4
What is the time complexity of the precomputation?

A) O(n)  
B) O(n log n) with divisor sieve  
C) O(n sqrt n)  
D) O(n²)

**Correct Answer:** B

**Explanation:** Using a modified sieve, we can find all divisors for numbers up to n in O(n log n) time.
