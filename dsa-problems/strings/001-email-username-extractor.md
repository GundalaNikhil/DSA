# Email Username Extractor

**Problem ID:** STR-001
**Display ID:** 6
**Question Name:** Email Username Extractor
**Slug:** email-username-extractor
**Title:** Extract Username from Email
**Difficulty:** Easy
**Premium:** No
**Tags:** String, Parsing

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given a valid email address, extract and return the username part (everything before the @ symbol).

## A Simple Scenario (Daily Life Usage)

You're building a welcome message system. When someone signs up with "john.doe@company.com", you want to greet them as "Welcome, john.doe!" instead of using their full email. You need to extract just the username portion.

## Your Task

Write a function that takes an email string and returns the username portion.

## Why is it Important?

This problem teaches you:

- String parsing and manipulation
- Character-based searching
- Data extraction techniques
- Input validation basics

## Examples

### Example 1:

**Input:** `email = "alice.wonderland@example.com"`
**Output:** `"alice.wonderland"`
**Explanation:** Everything before @ is the username.

### Example 2:

**Input:** `email = "user123@company.org"`
**Output:** `"user123"`
**Explanation:** Simple alphanumeric username extraction.

### Example 3:

**Input:** `email = "first.middle.last@domain.co.uk"`
**Output:** `"first.middle.last"`
**Explanation:** Username can contain multiple dots.

## Constraints

- 5 ≤ email.length ≤ 200
- Email contains exactly one @ symbol
- Username contains only lowercase letters, digits, dots, and hyphens
- Email is guaranteed to be valid format

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Mailchimp
- SendGrid
- Gmail (Google)
- Outlook (Microsoft)

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
