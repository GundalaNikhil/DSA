# Playlist Pair Swap

**Difficulty:** Easy
**Topic:** Arrays, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A music streaming app allows users to swap adjacent songs in their playlist. Given an array `playlist` representing song IDs and an integer `position`, swap the song at `position` with the song at `position + 1`.

Return the modified playlist array. If the swap cannot be performed (position out of bounds), return the original array.

## Constraints

- `2 <= playlist.length <= 1000`
- `1 <= playlist[i] <= 10000`
- `0 <= position < playlist.length`

## Examples

### Example 1
```
Input: playlist = [101, 205, 367, 489], position = 1
Output: [101, 367, 205, 489]
Explanation: Songs at positions 1 and 2 (205 and 367) are swapped.
```

### Example 2
```
Input: playlist = [501, 602], position = 0
Output: [602, 501]
Explanation: The only two songs are swapped.
```

### Example 3
```
Input: playlist = [701, 802, 903], position = 2
Output: [701, 802, 903]
Explanation: Position 2 cannot swap with position 3 (out of bounds), return original.
```

## Function Signature

### Python
```python
def swap_playlist_songs(playlist: list[int], position: int) -> list[int]:
    pass
```

### JavaScript
```javascript
function swapPlaylistSongs(playlist, position) {
    // Your code here
}
```

### Java
```java
public int[] swapPlaylistSongs(int[] playlist, int position) {
    // Your code here
}
```

## Hints

1. Check if position + 1 is within array bounds
2. Use a temporary variable for swapping
3. Modify the array in-place or create a copy

## Tags
`array` `swap` `boundary-check` `easy`
