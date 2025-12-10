# URL Slug Generator

**Problem ID:** STR-005
**Display ID:** 10
**Question Name:** URL Slug Generator
**Slug:** url-slug-generator
**Title:** Convert Title to URL Slug
**Difficulty:** Easy
**Premium:** No
**Tags:** String, Formatting

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Convert a blog post title into a URL-friendly slug by converting to lowercase, replacing spaces with hyphens, and removing special characters.

## A Simple Scenario (Daily Life Usage)

You're publishing a blog post titled "Top 10 Tips for Healthy Living!" The URL can't have spaces or special characters. You need to convert it to "top-10-tips-for-healthy-living" so it's a valid, SEO-friendly URL.

## Your Task

Transform a title string into a valid URL slug following these rules:

1. Convert to lowercase
2. Replace spaces with hyphens
3. Remove all characters except letters, numbers, and hyphens
4. Remove consecutive hyphens
5. Trim hyphens from start and end

## Why is it Important?

This problem teaches you:

- String normalization
- Regular expressions
- URL best practices
- Text sanitization

## Examples

### Example 1:

**Input:** `title = "Hello World!"`
**Output:** `"hello-world"`
**Explanation:** Lowercase, space to hyphen, removed exclamation.

### Example 2:

**Input:** `title = "  JavaScript  is   Awesome!!!  "`
**Output:** `"javascript-is-awesome"`
**Explanation:** Trimmed spaces, removed multiple hyphens, removed special chars.

### Example 3:

**Input:** `title = "100% Free Tutorial"`
**Output:** `"100-free-tutorial"`
**Explanation:** Removed % symbol, kept numbers.

## Constraints

- 1 ≤ title.length ≤ 200
- Title contains ASCII characters
- Output should contain only lowercase letters, numbers, and single hyphens

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- WordPress
- Medium
- Ghost
- Substack

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
