# Text Editor Backspace Handler

**Problem ID:** STK-005
**Display ID:** 22
**Question Name:** Text Editor Backspace Handler
**Slug:** text-editor-backspace-handler
**Title:** Backspace String Compare
**Difficulty:** Easy
**Premium:** No
**Tags:** Stack, String, Two Pointers

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given two strings s and t, return true if they are equal when both are typed into empty text editors. The character '#' represents a backspace character.

Note that after backspacing an empty text, the text will remain empty.

## A Simple Scenario (Daily Life Usage)

You're building a messaging app like Slack, WhatsApp, or Discord. Users type messages but might press backspace to fix typos. Your app needs to compare what users actually typed after all the backspaces to detect if two users sent the same message. For example, "ab#c" (typed a, b, backspace, c) equals "ad#c" (typed a, d, backspace, c) - both result in "ac".

## Your Task

Write a function that compares two strings after processing all backspace characters.

## Why is it Important?

This problem teaches you:

- Stack-based string processing
- Character-by-character simulation
- String comparison after transformations
- Real-time text input handling

## Examples

### Example 1:

**Input:** `s = "ab#c", t = "ad#c"`
**Output:** `true`
**Explanation:**
- s: type 'a', type 'b', backspace (remove 'b'), type 'c' → "ac"
- t: type 'a', type 'd', backspace (remove 'd'), type 'c' → "ac"
- Both result in "ac", so they are equal.

### Example 2:

**Input:** `s = "ab##", t = "c#d#"`
**Output:** `true`
**Explanation:**
- s: type 'a', type 'b', backspace twice (remove both) → ""
- t: type 'c', backspace, type 'd', backspace (remove both) → ""
- Both result in empty strings.

### Example 3:

**Input:** `s = "a#c", t = "b"`
**Output:** `false`
**Explanation:**
- s: type 'a', backspace, type 'c' → "c"
- t: type 'b' → "b"
- "c" ≠ "b"

### Example 4:

**Input:** `s = "a##c", t = "#a#c"`
**Output:** `true`
**Explanation:**
- s: type 'a', backspace twice (remove 'a', then backspace on empty), type 'c' → "c"
- t: backspace (on empty), type 'a', backspace, type 'c' → "c"
- Both result in "c".

## Constraints

- 1 ≤ s.length, t.length ≤ 200
- s and t only contain lowercase letters and '#' characters

## Follow-up Challenge

Can you solve it in O(n) time and O(1) space? (Hint: Use two pointers from the end of both strings)

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google (Google Docs)
- Slack
- WhatsApp (Meta)
- Discord

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
