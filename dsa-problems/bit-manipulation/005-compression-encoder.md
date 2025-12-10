# Pack Multiple Values in Single Integer

**Problem ID:** BIT-005
**Display ID:** 100
**Question Name:** Pack Multiple Values in Single Integer
**Slug:** compression-encoder
**Title:** Pack Multiple Values in Single Integer
**Difficulty:** Medium
**Premium:** No
**Tags:** Bit Manipulation, Bit Packing, Compression

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

In game development, efficiently storing character states is crucial for performance. Implement a bit-packing system that stores a game character's state in a single 32-bit integer: health (10 bits, 0-1023), mana (10 bits, 0-1023), level (7 bits, 0-127), and status effects (5 bits as flags). Create functions to pack, unpack, and modify individual components without unpacking the entire state.

## A Simple Scenario (Daily Life Usage)

You're developing a multiplayer game like League of Legends. Instead of sending 4 separate numbers over the network for each player (health=850, mana=420, level=18, status=3), you pack them into one integer: `0b00011_0010100_0110100100_1101010010` (32 bits). This reduces network bandwidth by 75%! When rendering health bars, you extract just the health bits without touching the rest. When a player levels up, you update only the level bits. Fast and memory-efficient!

## Your Task

Implement the following functions:
- `packCharacterState(health, mana, level, status)`: Pack all values into a single 32-bit integer
- `unpackHealth(state)`: Extract health value (bits 0-9)
- `unpackMana(state)`: Extract mana value (bits 10-19)
- `unpackLevel(state)`: Extract level value (bits 20-26)
- `unpackStatus(state)`: Extract status flags (bits 27-31)
- `updateHealth(state, newHealth)`: Update only the health bits
- `updateMana(state, newMana)`: Update only the mana bits

Where:
- `health`: 0-1023 (10 bits)
- `mana`: 0-1023 (10 bits)
- `level`: 0-127 (7 bits)
- `status`: 0-31 (5 bits for flags: poisoned, stunned, shielded, invisible, burning)

## Why is it Important?

This problem teaches you how to:

- Pack multiple values into a single integer
- Use bit masks to isolate bit ranges
- Use bit shifts for positioning values
- Clear specific bit ranges before updating
- Optimize memory usage in games and systems
- Balance between space efficiency and access speed

## Examples

### Example 1:

**Input:** `health = 850, mana = 420, level = 18, status = 3`
**Output:** `state = 402677074`
**Explanation:**
- health (850) = 0b1101010010 (bits 0-9)
- mana (420) = 0b0110100100 (bits 10-19)
- level (18) = 0b0010010 (bits 20-26)
- status (3) = 0b00011 (bits 27-31)
- Combined: 0b00011_0010010_0110100100_1101010010 = 402677074

### Example 2:

**Input:** `state = 402677074, operation = "unpackHealth"`
**Output:** `850`
**Explanation:** Extract bits 0-9: state & 0x3FF = 850

### Example 3:

**Input:** `state = 402677074, operation = "unpackMana"`
**Output:** `420`
**Explanation:** Extract bits 10-19: (state >> 10) & 0x3FF = 420

### Example 4:

**Input:** `state = 402677074, operation = "unpackLevel"`
**Output:** `18`
**Explanation:** Extract bits 20-26: (state >> 20) & 0x7F = 18

### Example 5:

**Input:** `state = 402677074, operation = "unpackStatus"`
**Output:** `3`
**Explanation:** Extract bits 27-31: (state >> 27) & 0x1F = 3

### Example 6:

**Input:** `state = 402677074, newHealth = 1000, operation = "updateHealth"`
**Output:** `402677096`
**Explanation:**
- Clear bits 0-9: state & 0xFFFFFC00
- Set new health: result | 1000
- Other values unchanged: mana=420, level=18, status=3

### Example 7:

**Input:** `state = 402677074, newMana = 0, operation = "updateMana"`
**Output:** `402246226`
**Explanation:**
- Clear bits 10-19: state & 0xFFF003FF
- Set new mana: result | (0 << 10)
- Other values unchanged: health=850, level=18, status=3

### Example 8:

**Input:** `health = 0, mana = 0, level = 0, status = 31`
**Output:** `state = 4160749568`
**Explanation:** Only status bits (27-31) are set: 0b11111_0000000_0000000000_0000000000

## Constraints

- 0 ≤ health ≤ 1023
- 0 ≤ mana ≤ 1023
- 0 ≤ level ≤ 127
- 0 ≤ status ≤ 31
- All operations should run in O(1) time
- Use only bitwise operations (shifts, AND, OR, NOT)
- State fits in a 32-bit unsigned integer

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Unity Technologies
- Epic Games
- Valve
- Riot Games

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
