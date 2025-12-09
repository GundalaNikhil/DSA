# Count Leading Zeros for Mining Difficulty

**Problem ID:** BIT-006
**Display ID:** 101
**Question Name:** Count Leading Zeros for Mining Difficulty
**Slug:** crypto-hash-validator
**Title:** Count Leading Zeros for Mining Difficulty
**Difficulty:** Hard
**Premium:** No
**Tags:** Bit Manipulation, Cryptography, Mining

## Problem Description

Implement a Bitcoin-style proof-of-work validator. In cryptocurrency mining, a hash is considered valid if it has a certain number of leading zero bits (the "difficulty"). Given a 256-bit hash (represented as an array of 8 32-bit integers), count the number of leading zero bits and determine if it meets the difficulty requirement. Additionally, implement efficient bit-level operations to find the position of the first set bit and validate multiple hashes quickly.

## A Simple Scenario (Daily Life Usage)

You're running a Bitcoin mining operation. The network requires hashes with at least 20 leading zeros (difficulty = 20). Your mining rig generates a hash: `0x00000AB3...`. Converting to binary, you count: 0000 0000 0000 0000 0000 1010 = 20 zeros before the first 1. Success! This hash is valid. Your mining software validates millions of hashes per second using optimized bit-counting algorithms, checking each one until it finds a valid hash to earn Bitcoin rewards.

## Your Task

Implement the following functions:
- `countLeadingZeros(hash)`: Count leading zero bits in a 256-bit hash
- `isValidHash(hash, difficulty)`: Check if hash meets difficulty requirement
- `findFirstSetBit(value)`: Find position of first 1-bit in a 32-bit integer
- `compareHashDifficulty(hash1, hash2)`: Compare which hash has more leading zeros
- `estimateMiningAttempts(difficulty)`: Estimate average attempts needed for difficulty

Where:
- `hash` is an array of 8 32-bit unsigned integers (representing 256 bits)
- `difficulty` is the required number of leading zero bits (0-256)
- Hash is stored in big-endian order: hash[0] contains the most significant bits

## Why is it Important?

This problem teaches you how to:

- Count leading zeros efficiently using bit manipulation
- Work with multi-word (256-bit) integers
- Understand proof-of-work consensus mechanisms
- Apply binary search techniques to bit operations
- Optimize critical performance paths
- Understand computational difficulty scaling

## Examples

### Example 1:

**Input:** `hash = [0x00000000, 0x00000000, 0x00000AB3, 0x12345678, 0x9ABCDEF0, 0x11111111, 0x22222222, 0x33333333]`
**Output:** `84` leading zeros
**Explanation:**
- hash[0] = 0x00000000: 32 leading zeros
- hash[1] = 0x00000000: 32 leading zeros
- hash[2] = 0x00000AB3 = 0b00000000 00000000 00001010 10110011: 20 leading zeros
- Total: 32 + 32 + 20 = 84 leading zeros

### Example 2:

**Input:** `hash = [0x00000000, 0x00000000, 0x00000AB3, ...], difficulty = 84`
**Output:** `true`
**Explanation:** Hash has exactly 84 leading zeros, meets difficulty requirement.

### Example 3:

**Input:** `hash = [0x00000000, 0x00000000, 0x00000AB3, ...], difficulty = 85`
**Output:** `false`
**Explanation:** Hash has 84 leading zeros, which is less than required 85.

### Example 4:

**Input:** `value = 0x00000AB3, operation = "findFirstSetBit"`
**Output:** `20`
**Explanation:** 0x00000AB3 in binary has 20 leading zeros, first 1-bit is at position 20 (0-indexed from left).

### Example 5:

**Input:**
- `hash1 = [0x00000000, 0x00000000, 0x00000AB3, ...]` (84 leading zeros)
- `hash2 = [0x00000000, 0x00000000, 0x00AB3000, ...]` (72 leading zeros)
**Output:** `1`
**Explanation:** hash1 has more leading zeros, return 1. Return -1 if hash2 is better, 0 if equal.

### Example 6:

**Input:** `difficulty = 20, operation = "estimateMiningAttempts"`
**Output:** `1048576`
**Explanation:** Probability of a random hash having 20 leading zeros is 1/(2^20). Expected attempts = 2^20 = 1048576.

### Example 7:

**Input:** `hash = [0x80000000, 0x00000000, 0x00000000, ...]`
**Output:** `0` leading zeros
**Explanation:** First bit is 1 (0x80000000 = 0b10000000...), so 0 leading zeros.

### Example 8:

**Input:** `hash = [0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000001]`
**Output:** `255` leading zeros
**Explanation:** Only the last bit of the 256-bit hash is set, giving 255 leading zeros.

### Example 9:

**Input:** `hash = [0x00000000, 0x00000001, 0x23456789, ...], difficulty = 32`
**Output:** `true`
**Explanation:** hash[0] has 32 zeros, hash[1] starts with 31 zeros. Total 32+31=63, which exceeds difficulty of 32.

## Constraints

- hash is an array of exactly 8 32-bit unsigned integers
- 0 ≤ difficulty ≤ 256
- Hash represents a 256-bit number in big-endian order
- countLeadingZeros should run in O(1) average case using bit tricks
- Do not convert to strings or use logarithms
- Use efficient bit manipulation techniques (binary search, lookup tables, or CPU intrinsics)

## Advanced Optimization Challenge

For a perfect solution, implement `countLeadingZeros` to run in O(1) time by:
1. Using a lookup table for 8-bit chunks, OR
2. Using binary search on each 32-bit word, OR
3. Using bit manipulation tricks (e.g., De Bruijn sequences)

## Asked by Companies

- Coinbase
- Binance
- Kraken
- BlockFi
