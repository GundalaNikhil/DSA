# Text Message Compressor

**Problem ID:** STR-003
**Display ID:** 8
**Question Name:** Text Message Compressor
**Slug:** text-message-compressor
**Title:** Run Length Encoding
**Difficulty:** Medium
**Premium:** No
**Tags:** String, Compression, Two Pointers

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Compress a string using run-length encoding where consecutive identical characters are replaced by the character followed by the count. If compression doesn't reduce size, return the original string.

## A Simple Scenario (Daily Life Usage)

You're sending text messages and want to save data. Instead of typing "hellooooo", you send "hel2o5" (h, e, l, 2 l's... wait, that's wrong). Actually: "hello5" won't work either. Let me think: "h1e1l2o5" means h(1), e(1), l(2), o(5). This saves space for repeated characters!

## Your Task

Implement run-length encoding. Each character is followed by its count. Return original if compressed version is longer.

## Why is it Important?

This problem teaches you:

- Data compression algorithms
- Character counting techniques
- String building efficiently
- When to apply optimization

## Examples

### Example 1:

**Input:** `text = "aaabbcccc"`
**Output:** `"a3b2c4"`
**Explanation:** 'a' appears 3 times, 'b' appears 2 times, 'c' appears 4 times.

### Example 2:

**Input:** `text = "abcdef"`
**Output:** `"abcdef"`
**Explanation:** Compression would create "a1b1c1d1e1f1" which is longer, so return original.

### Example 3:

**Input:** `text = "zzzzzzzzzzz"`
**Output:** `"z11"`
**Explanation:** 11 z's compressed to "z11" (saves 8 characters).

## Constraints

- 1 ≤ text.length ≤ 1000
- String contains only lowercase English letters
- Count will not exceed 999 for any character

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- WhatsApp
- Telegram
- Signal
- Zoom

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
