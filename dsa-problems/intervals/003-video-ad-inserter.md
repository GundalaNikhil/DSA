---
id: INT-003
display_id: 116
title: Insert Ad Breaks Without Overlap
difficulty: Medium
tags: [intervals, arrays, greedy]
companies: [YouTube, Hulu, Netflix, Twitch]
premium: false
---

# Insert Ad Breaks Without Overlap

## Problem Statement

You are building a video streaming platform that needs to insert advertisements into videos. Given a video duration and a list of protected intervals `[start, end]` where important content occurs (that cannot be interrupted), determine if you can insert an ad of duration `adDuration` starting at position `adStart`.

The ad can be inserted if and only if the interval `[adStart, adStart + adDuration - 1]` does not overlap with any protected interval.

Additionally, implement a function that returns all valid starting positions where the ad could be placed.

**Real-world Application**: This problem is critical for streaming platforms like YouTube and Hulu that need to place ads without interrupting key moments (like goals in sports, punchlines in comedy, or crucial plot points in shows). It ensures user experience isn't degraded while maximizing ad revenue.

## Examples

### Example 1:
```
Input:
videoDuration = 100
protectedIntervals = [[10, 20], [30, 40], [50, 60]]
adDuration = 5
adStart = 25

Output: true

Explanation:
- Ad would occupy [25, 29] (25 + 5 - 1 = 29)
- [25, 29] doesn't overlap with any protected interval
- Valid placement
```

### Example 2:
```
Input:
videoDuration = 100
protectedIntervals = [[10, 20], [30, 40], [50, 60]]
adDuration = 5
adStart = 18

Output: false

Explanation:
- Ad would occupy [18, 22]
- This overlaps with protected interval [10, 20] (at positions 18-20)
- Invalid placement
```

### Example 3:
```
Input:
videoDuration = 50
protectedIntervals = [[5, 15], [25, 35]]
adDuration = 8

Output (all valid positions): [[0, 4], [16, 24], [36, 42]]

Explanation:
- Can place ad at positions 0-4 (before first protected interval)
- Can place ad at positions 16-24 (between protected intervals)
- Can place ad at positions 36-42 (after last protected interval, ensuring ad ends at 42+8-1=49, within video)
- Returns ranges of valid starting positions
```

### Example 4:
```
Input:
videoDuration = 30
protectedIntervals = [[0, 10], [10, 20], [20, 30]]
adDuration = 5

Output (all valid positions): []

Explanation:
- Protected intervals cover entire video
- No valid position to insert ad
```

## Constraints

- `1 <= videoDuration <= 10^6`
- `0 <= protectedIntervals.length <= 10^4`
- `protectedIntervals[i].length == 2`
- `0 <= start_i < end_i < videoDuration`
- `1 <= adDuration <= videoDuration`
- `0 <= adStart < videoDuration`
- Protected intervals may overlap or touch each other

## Approach Hints

### Hint 1
First, merge all overlapping protected intervals to simplify the problem.

### Hint 2
For checking a single position: An ad at position `adStart` occupies `[adStart, adStart + adDuration - 1]`. Check if this overlaps with any merged protected interval.

### Hint 3
For finding all valid positions: After merging, the valid regions are the gaps between protected intervals. For each gap, calculate which starting positions would keep the entire ad within that gap.

### Hint 4
Two intervals `[a1, a2]` and `[b1, b2]` overlap if `a1 <= b2` AND `b1 <= a2`.

## Solution

```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.
    """
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


def can_insert_ad(videoDuration, protectedIntervals, adDuration, adStart):
    """
    Check if an ad can be inserted at a specific position.

    Args:
        videoDuration: Total length of video
        protectedIntervals: List of [start, end] protected regions
        adDuration: Length of the advertisement
        adStart: Proposed starting position for ad

    Returns:
        True if ad can be inserted, False otherwise
    """
    # Check if ad fits within video duration
    ad_end = adStart + adDuration - 1
    if ad_end >= videoDuration:
        return False

    # Merge protected intervals
    merged = merge_intervals(protectedIntervals)

    # Check if ad overlaps with any protected interval
    ad_interval = [adStart, ad_end]

    for protected_start, protected_end in merged:
        # Check overlap: ad and protected interval overlap if
        # ad_start <= protected_end AND protected_start <= ad_end
        if adStart <= protected_end and protected_start <= ad_end:
            return False

    return True


def find_all_valid_positions(videoDuration, protectedIntervals, adDuration):
    """
    Find all valid ranges where ad can start.

    Returns:
        List of [start, end] ranges where ad can begin
    """
    # Merge protected intervals
    merged = merge_intervals(protectedIntervals) if protectedIntervals else []

    valid_ranges = []

    # Check range before first protected interval
    if not merged:
        # No protected intervals, entire video is available
        if adDuration <= videoDuration:
            valid_ranges.append([0, videoDuration - adDuration])
        return valid_ranges

    # Before first protected interval
    if merged[0][0] >= adDuration:
        valid_ranges.append([0, merged[0][0] - adDuration])

    # Between protected intervals
    for i in range(len(merged) - 1):
        gap_start = merged[i][1] + 1
        gap_end = merged[i + 1][0] - 1
        gap_size = gap_end - gap_start + 1

        if gap_size >= adDuration:
            # Ad can start from gap_start to (gap_end - adDuration + 1)
            valid_ranges.append([gap_start, gap_end - adDuration + 1])

    # After last protected interval
    last_protected_end = merged[-1][1]
    remaining_space = videoDuration - last_protected_end - 1

    if remaining_space >= adDuration:
        valid_ranges.append([last_protected_end + 1, videoDuration - adDuration])

    return valid_ranges


def count_valid_positions(videoDuration, protectedIntervals, adDuration):
    """
    Count total number of valid starting positions for ad.
    """
    valid_ranges = find_all_valid_positions(videoDuration, protectedIntervals, adDuration)
    total_positions = sum(end - start + 1 for start, end in valid_ranges)
    return total_positions
```

## Complexity Analysis

### can_insert_ad()
- **Time Complexity**: O(n log n) where n is the number of protected intervals
  - O(n log n) for sorting during merge
  - O(n) for checking overlap

- **Space Complexity**: O(n) for merged intervals

### find_all_valid_positions()
- **Time Complexity**: O(n log n)
  - O(n log n) for merging
  - O(n) for finding gaps

- **Space Complexity**: O(n) for storing merged intervals and valid ranges

## Key Insights

1. **Merging first simplifies logic**: Dealing with merged intervals is much simpler than checking all original intervals
2. **Overlap condition**: Two intervals overlap if neither one ends before the other starts
3. **Edge cases**: Always check if ad fits within video duration, handle empty protected intervals
4. **Gap calculation**: A gap of size G can accommodate an ad of duration D starting at G - D + 1 different positions

## Follow-up Questions

1. **Multiple ads**: How would you place K ads of equal duration in the video?
2. **Variable ad durations**: Given multiple ads of different durations, maximize the number of ads you can place?
3. **Maximize revenue**: Each starting position has a different revenue value. Find the valid position with maximum revenue.
4. **Dynamic updates**: How would you handle real-time updates where protected intervals are added/removed?
5. **Minimum ads**: What's the minimum number of ads needed to cover all non-protected time?

## Use Cases

1. **YouTube ads**: Place pre-roll, mid-roll, and post-roll ads in user-generated content
2. **Live sports**: Avoid placing ads during active play, only during breaks
3. **Podcast ads**: Insert sponsorship messages without interrupting key content
4. **Educational videos**: Protect important explanations from interruption
5. **Content rating**: Ensure ads are not placed during violent or sensitive scenes

## Related Problems

- Insert Interval (Medium)
- Merge Intervals (Medium)
- Non-overlapping Intervals (Medium)
- Interval List Intersections (Medium)
- Meeting Rooms II (Medium)
