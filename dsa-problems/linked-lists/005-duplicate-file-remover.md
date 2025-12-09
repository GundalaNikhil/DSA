# Duplicate File Remover

**Problem ID:** LL-005
**Display ID:** 16
**Question Name:** Duplicate File Remover
**Slug:** duplicate-file-remover
**Title:** Remove Duplicates from Sorted List
**Difficulty:** Easy
**Premium:** No
**Tags:** Linked List, In-place Modification

## Problem Description

Given the head of a sorted linked list representing file sizes in a storage system, delete all duplicates such that each file size appears only once. Return the linked list sorted as well.

## A Simple Scenario (Daily Life Usage)

You're building a file manager that displays unique file sizes. Your system has files of sizes: 1MB → 1MB → 2MB → 3MB → 3MB → 3MB → 4MB. To show a clean summary view to users, you want to display only unique sizes: 1MB → 2MB → 3MB → 4MB. This helps users understand their storage distribution without duplicate clutter.

## Your Task

Write a function that takes the head of a sorted singly linked list and removes all duplicate nodes, keeping only one occurrence of each value. Modify the list in-place.

## Why is it Important?

This problem teaches you:

- In-place linked list modification
- Handling duplicate removal efficiently
- Single-pass algorithm on sorted data
- Proper memory management and node connections

## Examples

### Example 1:

**Input:** `head = [1, 1, 2]`
**Output:** `[1, 2]`
**Explanation:** Remove the duplicate 1.

### Example 2:

**Input:** `head = [1, 1, 2, 3, 3]`
**Output:** `[1, 2, 3]`
**Explanation:** Remove all duplicates, keeping one of each value.

### Example 3:

**Input:** `head = [1, 2, 3]`
**Output:** `[1, 2, 3]`
**Explanation:** No duplicates to remove.

## Constraints

- The number of nodes in the list is in the range [0, 300]
- -100 ≤ Node.val ≤ 100
- The list is guaranteed to be sorted in ascending order

## Asked by Companies

- Dropbox
- Google Drive
- OneDrive
- iCloud
