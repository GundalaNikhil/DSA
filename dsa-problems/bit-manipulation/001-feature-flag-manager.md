# Toggle Feature Flags with Bitmask

**Problem ID:** BIT-001
**Display ID:** 96
**Question Name:** Toggle Feature Flags with Bitmask
**Slug:** feature-flag-manager
**Title:** Toggle Feature Flags with Bitmask
**Difficulty:** Easy
**Premium:** No
**Tags:** Bit Manipulation, Bitmask, System Design

## Problem Description

You are building a feature flag management system where multiple features can be enabled or disabled for different users. Each feature is represented by a bit position in an integer. Implement functions to check if a feature is enabled, enable a feature, disable a feature, and toggle a feature.

## A Simple Scenario (Daily Life Usage)

Imagine you're working at a company testing new app features. You have 5 features: dark mode (bit 0), notifications (bit 1), analytics (bit 2), beta UI (bit 3), and premium content (bit 4). A user's settings are stored as one integer: `00101` means dark mode and analytics are ON, others are OFF. When they toggle dark mode, it becomes `00100`. This saves database space and makes checks lightning fast!

## Your Task

Implement a FeatureFlagManager class with the following methods:
- `isEnabled(flags, feature)`: Check if a specific feature is enabled
- `enable(flags, feature)`: Enable a specific feature
- `disable(flags, feature)`: Disable a specific feature
- `toggle(flags, feature)`: Toggle a specific feature (on to off, or off to on)

Where `flags` is an integer representing all feature states, and `feature` is the bit position (0-indexed).

## Why is it Important?

This problem teaches you how to:

- Use bitwise OR for setting bits
- Use bitwise AND for checking bits
- Use bitwise XOR for toggling bits
- Use bitwise AND with NOT for clearing bits
- Apply bit manipulation to real-world systems
- Optimize storage and performance

## Examples

### Example 1:

**Input:** `flags = 5, feature = 1, operation = "isEnabled"`
**Output:** `false`
**Explanation:** 5 in binary is `101`. Bit at position 1 is 0 (disabled).

### Example 2:

**Input:** `flags = 5, feature = 1, operation = "enable"`
**Output:** `7`
**Explanation:** 5 is `101`. Setting bit 1 gives `111` = 7.

### Example 3:

**Input:** `flags = 7, feature = 0, operation = "toggle"`
**Output:** `6`
**Explanation:** 7 is `111`. Toggling bit 0 gives `110` = 6.

### Example 4:

**Input:** `flags = 13, feature = 2, operation = "disable"`
**Output:** `9`
**Explanation:** 13 is `1101`. Clearing bit 2 gives `1001` = 9.

## Constraints

- 0 ≤ flags ≤ 2^31 - 1
- 0 ≤ feature ≤ 30
- All operations should run in O(1) time
- Do not use loops or conditionals for bit operations

## Asked by Companies

- LaunchDarkly
- Split.io
- Optimizely
- Flagsmith
