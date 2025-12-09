# Password Strength Validator

**Problem ID:** STR-002
**Display ID:** 7
**Question Name:** Password Strength Validator
**Slug:** password-strength-validator
**Title:** Check Password Complexity Requirements
**Difficulty:** Easy
**Premium:** No
**Tags:** String, Validation

## Problem Description

Validate if a password meets security requirements: at least 8 characters, contains at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*).

## A Simple Scenario (Daily Life Usage)

You're creating an account on a banking website. The system checks if your password is strong enough. "password123" gets rejected, but "SecurePass123!" is accepted. The validator ensures your account stays safe from hackers.

## Your Task

Return true if the password meets all requirements, false otherwise.

## Why is it Important?

This problem teaches you:

- String validation patterns
- Character type checking
- Security best practices
- Boolean logic combination

## Examples

### Example 1:

**Input:** `password = "StrongP@ss1"`
**Output:** `true`
**Explanation:** Has uppercase (S, P), lowercase (trong, ss), digit (1), special (@), and 11 chars.

### Example 2:

**Input:** `password = "weakpass"`
**Output:** `false`
**Explanation:** Missing uppercase, digit, and special character.

### Example 3:

**Input:** `password = "SHORT1!"`
**Output:** `false`
**Explanation:** Only 7 characters, needs at least 8.

## Constraints

- 1 ≤ password.length ≤ 100
- Password contains only ASCII characters
- Special characters are limited to: !@#$%^&*

## Asked by Companies

- Bank of America
- Chase
- PayPal
- Stripe
