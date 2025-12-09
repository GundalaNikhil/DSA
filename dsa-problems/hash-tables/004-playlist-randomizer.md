# Playlist Randomizer

**Problem ID:** HASH-004
**Display ID:** 39
**Question Name:** Playlist Randomizer
**Slug:** playlist-randomizer
**Title:** Insert Delete GetRandom O(1)
**Difficulty:** Medium
**Premium:** No
**Tags:** Hash Table, Array, Design, Randomized

## Problem Description

Design a data structure that supports inserting, deleting, and getting a random element, all in average O(1) time complexity.

## A Simple Scenario (Daily Life Usage)

You're building a music streaming app's shuffle feature. Users can add songs to their playlist, remove songs they don't like, and get a truly random song to play next. All these operations need to be instant - you can't afford to iterate through thousands of songs every time someone clicks "shuffle" or removes a track.

## Your Task

Implement a class with the following methods:
- `insert(val)`: Adds a value to the set. Returns true if the value was not present, false otherwise.
- `remove(val)`: Removes a value from the set. Returns true if the value was present, false otherwise.
- `getRandom()`: Returns a random element from the current set. Each element must have equal probability of being returned.

## Why is it Important?

This problem teaches you:

- Combining multiple data structures effectively
- Trade-offs between time and space complexity
- Random number generation with uniform distribution
- Real-world system design for music apps

## Examples

### Example 1:

**Input:**
```
["PlaylistRandomizer", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
```
**Output:**
```
[null, true, false, true, 2, true, false, 2]
```
**Explanation:**
- insert(1) returns true (added successfully)
- remove(2) returns false (not present)
- insert(2) returns true (added successfully)
- getRandom() could return 1 or 2 with equal probability
- remove(1) returns true (removed successfully)
- insert(2) returns false (already present)
- getRandom() must return 2 (only element)

## Constraints

- -2^31 ≤ val ≤ 2^31 - 1
- At most 200,000 calls will be made to insert, remove, and getRandom
- There will be at least one element when getRandom is called
- All operations must average O(1) time complexity

## Asked by Companies

- Spotify
- Apple Music
- Pandora
- SoundCloud
