# Unix File Permission Checker

**Problem ID:** BIT-002
**Display ID:** 97
**Question Name:** Unix File Permission Checker
**Slug:** permission-access-controller
**Title:** Unix File Permission Checker
**Difficulty:** Medium
**Premium:** No
**Tags:** Bit Manipulation, Bitmask, Operating Systems

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Implement a Unix-style file permission system using bitwise operations. In Unix, permissions are stored as a 9-bit value representing read (r), write (w), and execute (x) permissions for owner, group, and others. Each permission set uses 3 bits: read=4, write=2, execute=1. For example, `chmod 755` means owner has rwx (7), group has r-x (5), others have r-x (5).

## A Simple Scenario (Daily Life Usage)

You're a system administrator managing a Linux server. You need to check if a user can read a file. The file has permissions `644` (owner: rw-, group: r--, others: r--). When user "alice" (in the file's group) tries to open it, your system checks: does the group bit pattern allow reading? Yes! The read bit (4) is set, so access is granted.

## Your Task

Implement the following functions:
- `hasPermission(permissions, userType, action)`: Check if a user type (owner/group/others) can perform an action (read/write/execute)
- `grantPermission(permissions, userType, action)`: Grant a specific permission
- `revokePermission(permissions, userType, action)`: Revoke a specific permission
- `getOctalRepresentation(permissions)`: Convert 9-bit permissions to octal string (e.g., "755")

Where:
- `permissions` is a 9-bit integer (0-511)
- `userType`: 0 (owner), 1 (group), 2 (others)
- `action`: "read" (4), "write" (2), or "execute" (1)

## Why is it Important?

This problem teaches you how to:

- Work with multi-level bitmasks
- Understand Unix file permissions
- Use bit shifts for extracting permission groups
- Combine multiple bitwise operations
- Apply security concepts through bit manipulation
- Convert between binary and octal representations

## Examples

### Example 1:

**Input:** `permissions = 493, userType = 0, action = "read"`
**Output:** `true`
**Explanation:** 493 = 0b111101101 = 755 octal. Owner bits are 111 (rwx), read bit (4) is set.

### Example 2:

**Input:** `permissions = 420, userType = 2, action = "write"`
**Output:** `false`
**Explanation:** 420 = 0b110100100 = 644 octal. Others bits are 100 (r--), write bit (2) is not set.

### Example 3:

**Input:** `permissions = 420, userType = 1, action = "read", operation = "grantPermission"`
**Output:** `436`
**Explanation:** 420 = 644. Granting read to group (already set) keeps it 644 = 436.

### Example 4:

**Input:** `permissions = 511, userType = 1, action = "write", operation = "revokePermission"`
**Output:** `493`
**Explanation:** 511 = 777. Revoking group write: 777 -> 757 = 493.

### Example 5:

**Input:** `permissions = 493, operation = "getOctalRepresentation"`
**Output:** `"755"`
**Explanation:** 493 in binary is 111101101, which is 755 in octal notation.

## Constraints

- 0 ≤ permissions ≤ 511 (9 bits maximum)
- userType ∈ {0, 1, 2}
- action ∈ {"read", "write", "execute"}
- All operations should run in O(1) time
- Do not use string parsing or loops

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Linux Foundation
- Red Hat
- Canonical
- Microsoft

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
