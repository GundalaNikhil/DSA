# Baseball Game Score Tracker

**Problem ID:** STK-003
**Display ID:** 20
**Question Name:** Baseball Game Score Tracker
**Slug:** baseball-game-score-tracker
**Title:** Baseball Game Simulation
**Difficulty:** Easy
**Premium:** No
**Tags:** Stack, Simulation, Array

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You're keeping score for a baseball game with special rules. You have several operations:
- An integer x: Record a new score of x
- "+": Record a new score that is the sum of the previous two scores
- "D": Record a new score that is double the previous score
- "C": Invalidate the previous score, removing it from the record

Return the sum of all the scores on the record after all operations.

## A Simple Scenario (Daily Life Usage)

You're building a scoring system for ESPN or MLB.com. During a game, scorekeepers need to track runs, but sometimes they need to correct mistakes (operation "C"), add bonus points based on previous scores ("+"), or apply special multipliers ("D"). Your system needs to track all valid scores and calculate the final total.

## Your Task

Write a function that takes an array of operations and returns the sum of all valid scores.

## Why is it Important?

This problem teaches you:

- Stack operations (push, pop, peek)
- Simulation and state management
- Handling operations that depend on previous state
- Real-time score tracking systems

## Examples

### Example 1:

**Input:** `ops = ["7", "3", "C", "D", "+"]`
**Output:** `30`
**Explanation:**
- "5": Record 5, scores = [5]
- "2": Record 2, scores = [5, 2]
- "C": Remove 2, scores = [5]
- "D": Record 5*2=10, scores = [5, 10]
- "+": Record 5+10=15, scores = [5, 10, 15]
- Total: 5 + 10 + 15 = 30

### Example 2:

**Input:** `ops = ["6", "-3", "5", "C", "D", "10", "+", "+"]`
**Output:** `27`
**Explanation:**
- "5": scores = [5]
- "-2": scores = [5, -2]
- "4": scores = [5, -2, 4]
- "C": scores = [5, -2]
- "D": scores = [5, -2, -4]
- "9": scores = [5, -2, -4, 9]
- "+": scores = [5, -2, -4, 9, 5] (9 + -4 = 5)
- "+": scores = [5, -2, -4, 9, 5, 14] (9 + 5 = 14)
- Total: 5 + -2 + -4 + 9 + 5 + 14 = 27

### Example 3:

**Input:** `ops = ["8", "C"]`
**Output:** `0`
**Explanation:** Record 1, then cancel it. No scores remain.

## Constraints

- 1 ≤ ops.length ≤ 1,000
- ops[i] is "C", "D", "+", or a string representing an integer in the range [-30,000, 30,000]
- For operation "+", there will always be at least two previous scores
- For operation "D" or "C", there will always be at least one previous score

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- ESPN
- MLB.com
- DraftKings
- FanDuel

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
