# Secure Random PIN Generator

**Problem ID:** MATH-002
**Display ID:** 109
**Question Name:** Secure Random PIN Generator
**Slug:** secure-random-pin-generator
**Title:** Generate Non-Repeating PIN Codes
**Difficulty:** Medium
**Premium:** No
**Tags:** Math, Modular Arithmetic, Number Theory, Hash Function

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are developing a PIN generation system for ATM cards. Given a user's account number and a timestamp, generate a unique 4-digit PIN code using modular arithmetic. The PIN should be deterministic (same inputs always produce same PIN) but appear random. Use the formula: PIN = ((accountNumber * timestamp) % 10000) where the result must be exactly 4 digits (pad with leading zeros if needed).

## A Simple Scenario (Daily Life Usage)

Imagine you're a software engineer at a bank implementing a new ATM card system. When customers activate their cards, they need a temporary PIN to get started. Your system must generate PINs that appear random but can be reproduced if needed for verification. Using the customer's account number (123456) and activation timestamp (1678901234), your algorithm generates PIN 4704, which gets texted to their phone for security.

## Your Task

Write a function that takes an account number (long integer) and a Unix timestamp (long integer), then generates a 4-digit PIN as a string (with leading zeros if necessary). Additionally, implement a validation function that checks if a given PIN matches the generated PIN for the account and timestamp.

## Why is it Important?

This problem teaches you how to:

- Apply modular arithmetic for pseudo-random generation
- Work with deterministic hash functions
- Understand the mathematics behind PIN generation systems
- Handle edge cases with leading zeros
- Implement basic cryptographic concepts without complex libraries

## Examples

### Example 1:

**Input:** `accountNumber = 123456, timestamp = 1678901234`
**Output:** `"4704"`
**Explanation:** (123456 * 1678901234) % 10000 = 4704

### Example 2:

**Input:** `accountNumber = 987654321, timestamp = 1609459200`
**Output:** `"0432"`
**Explanation:** The result is 432, but we pad to 4 digits: "0432"

### Example 3:

**Input:** `accountNumber = 555555, timestamp = 1234567890`
**Output:** `"5850"`
**Explanation:** (555555 * 1234567890) % 10000 = 5850

### Example 4:

**Input:** `accountNumber = 111111, timestamp = 9000000`
**Output:** `"0000"`
**Explanation:** The product modulo 10000 gives 0, resulting in "0000"

## Constraints

- 1 ≤ accountNumber ≤ 9,999,999,999 (10 digits max)
- 1,000,000,000 ≤ timestamp ≤ 2,147,483,647 (valid Unix timestamps)
- PIN must always be exactly 4 characters
- The multiplication may exceed 64-bit integers, handle accordingly
- Return PIN as a string with leading zeros

## Follow-up

Can you implement a validation function `validatePIN(accountNumber, timestamp, inputPIN)` that returns true/false?

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Visa
- Mastercard
- PayPal
- Square
- Stripe
- American Express

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
