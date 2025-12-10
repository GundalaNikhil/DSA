# Merging Ranked Playlists

**Difficulty:** Medium
**Topic:** Linked Lists, Two Pointers, Merge
**License:** Free to use for commercial purposes

## Problem Statement

A music streaming service wants to combine two user playlists that are already ranked by song popularity score (in ascending order). The goal is to create a single unified playlist that maintains the ascending order of popularity scores.

Given the heads of two sorted linked lists `playlist_A` and `playlist_B`, merge them into one sorted list by splicing together the nodes.

Return the head of the merged linked list.

## Constraints

- `0 <= number of songs <= 50` in each playlist
- `-100 <= song.score <= 100`
- Both playlists are sorted in non-decreasing order

## Examples

### Example 1
```
Input: playlist_A = [10, 30, 50], playlist_B = [20, 40, 60]
Output: [10, 20, 30, 40, 50, 60]
Explanation: Merging two interleaved sorted lists.
```

### Example 2
```
Input: playlist_A = [], playlist_B = []
Output: []
Explanation: Two empty playlists result in an empty merged playlist.
```

### Example 3
```
Input: playlist_A = [], playlist_B = [15]
Output: [15]
Explanation: Merging an empty list with a non-empty list.
```

### Example 4
```
Input: playlist_A = [5, 10, 15], playlist_B = [2, 3, 20]
Output: [2, 3, 5, 10, 15, 20]
```

## Function Signature

### Python
```python
def merge_playlists(playlist_A: ListNode, playlist_B: ListNode) -> ListNode:
    pass
```

### JavaScript
```javascript
function mergePlaylists(playlistA, playlistB) {
    // Your code here
}
```

### Java
```java
public ListNode mergePlaylists(ListNode playlistA, ListNode playlistB) {
    // Your code here
}
```

## Hints

1. Use dummy node to simplify edge cases
2. Compare values and link smaller node
3. Handle remaining nodes
4. Time: O(n+m), Space: O(1)

## Tags
`linked-list` `two-pointers` `merge` `sorted` `medium`
