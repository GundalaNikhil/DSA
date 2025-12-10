# Phone Number Text Decoder

**Problem ID:** BACK-001
**Display ID:** 60
**Question Name:** Phone Number Text Decoder
**Slug:** phone-number-text-decoder
**Title:** Letter Combinations of Phone Number
**Difficulty:** Medium
**Premium:** No
**Tags:** Backtracking, String, Recursion

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on old telephone buttons) is given below. Note that 1 does not map to any letters.

- 2: abc
- 3: def
- 4: ghi
- 5: jkl
- 6: mno
- 7: pqrs
- 8: tuv
- 9: wxyz

## A Simple Scenario (Daily Life Usage)

Remember the old T9 predictive text on flip phones? Before smartphones, you had to press number keys multiple times to type letters. This problem is similar - given a sequence of numbers, generate all possible text combinations. For example, if you pressed "23", it could mean "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", or "cf".

## Your Task

Write a function that takes a string of digits (2-9) and returns all possible letter combinations that could be formed using the phone keypad mapping.

## Why is it Important?

This problem teaches you how to:

- Implement backtracking algorithms effectively
- Generate all possible combinations recursively
- Handle string manipulation and concatenation
- Understand decision trees and branching factors
- Apply systematic exploration of solution spaces

## Examples

### Example 1:

**Input:** `digits = "23"`
**Output:** `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
**Explanation:**
- 2 maps to "abc"
- 3 maps to "def"
- All combinations: ad, ae, af, bd, be, bf, cd, ce, cf

### Example 2:

**Input:** `digits = ""`
**Output:** `[]`
**Explanation:** No digits provided, return empty array.

### Example 3:

**Input:** `digits = "2"`
**Output:** `["a","b","c"]`
**Explanation:** Only one digit, return all its mapped letters.

### Example 4:

**Input:** `digits = "234"`
**Output:** `["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]`
**Explanation:** With three digits, we get 3 × 3 × 3 = 27 combinations.

## Constraints

- 0 ≤ digits.length ≤ 4
- digits[i] is a digit in the range ['2', '9']

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Google
- Facebook
- Uber
- Microsoft
- Bloomberg

## Hints

1. Use backtracking to explore all possible combinations
2. Build the result string character by character
3. For each digit, try all its corresponding letters
4. Recursively process the remaining digits
5. Base case: when you've processed all digits, add the combination to results

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
