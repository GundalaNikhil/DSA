# Image Dimension Scaler

**Problem ID:** MATH-004
**Display ID:** 111
**Question Name:** Image Dimension Scaler
**Slug:** image-dimension-scaler
**Title:** Find Greatest Common Divisor for Aspect Ratio
**Difficulty:** Easy
**Premium:** No
**Tags:** Math, GCD, Euclidean Algorithm, Number Theory

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are building an image resizing tool that needs to reduce image dimensions to their simplest aspect ratio. Given the width and height of an image in pixels, find the greatest common divisor (GCD) of both dimensions, then return the simplified aspect ratio as [width/gcd, height/gcd]. Implement the Euclidean algorithm to find GCD efficiently.

## A Simple Scenario (Daily Life Usage)

Imagine you're a graphic designer using Canva and you have an image that's 1920x1080 pixels. Before uploading to Instagram, you want to know the simplified aspect ratio to understand how it will display. Your tool calculates GCD(1920, 1080) = 120, giving you an aspect ratio of 16:9 - the standard widescreen format. This tells you the image will look great on modern displays!

## Your Task

Write a function that takes image width and height as positive integers, calculates their GCD using the Euclidean algorithm, and returns an array [simplifiedWidth, simplifiedHeight] representing the reduced aspect ratio.

## Why is it Important?

This problem teaches you how to:

- Implement the Euclidean algorithm for GCD
- Understand the mathematical concept of greatest common divisors
- Apply number theory to image processing
- Optimize recursive or iterative solutions
- Solve practical problems in graphics and design

## Examples

### Example 1:

**Input:** `width = 1920, height = 1080`
**Output:** `[16, 9]`
**Explanation:** GCD(1920, 1080) = 120. Aspect ratio: 1920/120 = 16, 1080/120 = 9. This is the standard 16:9 widescreen format.

### Example 2:

**Input:** `width = 800, height = 600`
**Output:** `[4, 3]`
**Explanation:** GCD(800, 600) = 200. Aspect ratio: 800/200 = 4, 600/200 = 3. Classic 4:3 standard definition format.

### Example 3:

**Input:** `width = 1080, height = 1080`
**Output:** `[1, 1]`
**Explanation:** Square images have a 1:1 aspect ratio. Perfect for Instagram posts!

### Example 4:

**Input:** `width = 3840, height = 2160`
**Output:** `[16, 9]`
**Explanation:** 4K resolution (3840x2160) also has a 16:9 aspect ratio, same as Full HD.

### Example 5:

**Input:** `width = 1280, height = 720`
**Output:** `[16, 9]`
**Explanation:** 720p HD video is also 16:9 aspect ratio.

## Constraints

- 1 ≤ width, height ≤ 10,000
- Both width and height are positive integers
- Return result as an array of two integers [width_ratio, height_ratio]
- Must implement GCD calculation (no built-in GCD functions)

## Follow-up

Can you implement both recursive and iterative versions of the Euclidean algorithm? Which one is more efficient for large numbers?

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Adobe
- Canva
- Figma
- Pixlr
- GIMP
- Photopea

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
