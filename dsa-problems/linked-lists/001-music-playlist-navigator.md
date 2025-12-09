# Music Playlist Navigator

**Problem ID:** LL-001
**Display ID:** 12
**Question Name:** Music Playlist Navigator
**Slug:** music-playlist-navigator
**Title:** Reverse a Linked List
**Difficulty:** Easy
**Premium:** No
**Tags:** Linked List, Recursion, Iteration

## Problem Description

Given the head of a singly linked list representing a music playlist, reverse the list and return the new head. Each node contains a song, and you need to reverse the order so the playlist plays backwards.

## A Simple Scenario (Daily Life Usage)

You're building a music app feature called "Rewind Through Memories" where users can play their playlist in reverse order. Instead of starting from Song 1 → Song 2 → Song 3, the playlist should play Song 3 → Song 2 → Song 1. This gives users a nostalgic experience, like rewinding through their favorite moments.

## Your Task

Write a function that takes the head of a singly linked list and reverses it in-place, returning the new head of the reversed list.

## Why is it Important?

This problem teaches you:

- Pointer manipulation in linked lists
- In-place algorithm optimization (O(1) space)
- Iterative vs recursive approaches
- Understanding node connections and references

## Examples

### Example 1:

**Input:** `head = [1, 2, 3, 4, 5]`
**Output:** `[5, 4, 3, 2, 1]`
**Explanation:** The entire list is reversed.

### Example 2:

**Input:** `head = [1, 2]`
**Output:** `[2, 1]`
**Explanation:** Two-node list is reversed.

### Example 3:

**Input:** `head = []`
**Output:** `[]`
**Explanation:** Empty list remains empty.

## Constraints

- The number of nodes in the list is in the range [0, 5000]
- -5000 ≤ Node.val ≤ 5000

## Asked by Companies

- Spotify
- Apple Music
- YouTube Music
- Amazon Music
