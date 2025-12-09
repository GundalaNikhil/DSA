# Encryption Key Validator

**Problem ID:** MATH-005
**Display ID:** 112
**Question Name:** Encryption Key Validator
**Slug:** encryption-key-validator
**Title:** Check if Number is Prime for RSA Keys
**Difficulty:** Medium
**Premium:** No
**Tags:** Math, Prime Numbers, Number Theory, Cryptography, Miller-Rabin

## Problem Description

You are building a certificate authority system that generates SSL/TLS certificates. A critical step in RSA encryption is verifying that key components are prime numbers. Given a large positive integer `n`, determine if it's prime using an efficient primality test. For numbers larger than a threshold (n > 1000), implement the Miller-Rabin probabilistic primality test with k=5 iterations. For smaller numbers, trial division is acceptable.

## A Simple Scenario (Daily Life Usage)

Imagine you're a security engineer at Let's Encrypt generating free SSL certificates for websites. When someone requests a certificate for "mywebsite.com", your system needs to generate RSA keys. The security of the entire internet relies on using prime numbers for these keys! Your validator checks that the number 982,451,653 is prime before using it in the key pair. A non-prime number would make the encryption breakable, putting user data at risk.

## Your Task

Write a function that takes a positive integer `n` and returns `true` if it's prime, `false` otherwise. For efficiency, implement the Miller-Rabin primality test for large numbers. Handle edge cases like n ≤ 1, n = 2, and even numbers.

## Why is it Important?

This problem teaches you how to:

- Implement efficient primality testing algorithms
- Understand the mathematics behind RSA encryption
- Apply modular exponentiation techniques
- Work with probabilistic algorithms
- Optimize for large number computations

## Examples

### Example 1:

**Input:** `n = 17`
**Output:** `true`
**Explanation:** 17 is prime (only divisible by 1 and 17).

### Example 2:

**Input:** `n = 982451653`
**Output:** `true`
**Explanation:** This large number is prime, commonly used in cryptographic applications.

### Example 3:

**Input:** `n = 1000000007`
**Output:** `true`
**Explanation:** A billion and seven - prime number often used in competitive programming for modulo operations.

### Example 4:

**Input:** `n = 1024`
**Output:** `false`
**Explanation:** 1024 = 2^10, clearly not prime.

### Example 5:

**Input:** `n = 561`
**Output:** `false`
**Explanation:** 561 = 3 × 11 × 17 (This is a Carmichael number - tricky composite that passes Fermat's test!)

## Constraints

- 1 ≤ n ≤ 10^12
- Must handle edge cases: n = 1 (not prime), n = 2 (prime), even numbers > 2 (not prime)
- For n > 1000, implement Miller-Rabin with at least 5 iterations
- For n ≤ 1000, trial division up to √n is acceptable
- Time complexity should be better than O(n)

## Follow-up

1. Can you explain why the Miller-Rabin test is probabilistic? What's the error rate with k=5 iterations?
2. How would you modify this to find the next prime number after n?
3. What's the difference between this and the Fermat primality test?

## Asked by Companies

- Let's Encrypt
- DigiCert
- Cloudflare
- AWS Certificate Manager
- VeriSign
- GlobalSign
