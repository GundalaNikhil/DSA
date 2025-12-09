---
id: INT-001
display_id: 114
title: Find Available Time Slots
difficulty: Easy
tags: [intervals, arrays, sorting]
companies: [Booking.com, Expedia, Airbnb, Marriott]
premium: false
---

# Find Available Time Slots

## Problem Statement

You are building a hotel room booking system. Given a list of existing bookings represented as time intervals `[start, end]` (where both are inclusive), and the hotel's operating hours `[openTime, closeTime]`, find all available time slots where new bookings can be made.

Each booking represents when a room is occupied. You need to find the gaps between bookings where the room is available for new guests.

**Real-world Application**: This problem is crucial for hotel reservation systems like Booking.com and Expedia, where customers need to see available time slots for room bookings. It's also used in restaurant table reservations, conference room booking systems, and medical appointment scheduling.

## Examples

### Example 1:
```
Input:
bookings = [[5, 10], [15, 20], [25, 30]]
openTime = 0
closeTime = 35

Output: [[0, 4], [11, 14], [21, 24], [31, 35]]

Explanation:
- Room is available from 0 to 4 (before first booking)
- Room is available from 11 to 14 (between first and second booking)
- Room is available from 21 to 24 (between second and third booking)
- Room is available from 31 to 35 (after last booking)
```

### Example 2:
```
Input:
bookings = [[2, 5], [6, 9]]
openTime = 0
closeTime = 10

Output: [[0, 1], [10, 10]]

Explanation:
- Room is available from 0 to 1 (before first booking)
- Room is available at time 10 (after last booking)
- No gap between bookings at [2,5] and [6,9] since they are back-to-back
```

### Example 3:
```
Input:
bookings = [[1, 5], [3, 8], [10, 15]]
openTime = 0
closeTime = 20

Output: [[0, 0], [9, 9], [16, 20]]

Explanation:
- First two bookings overlap, merged to [1, 8]
- Room is available at time 0 (before first booking)
- Room is available at time 9 (between merged booking and third booking)
- Room is available from 16 to 20 (after last booking)
```

## Constraints

- `0 <= bookings.length <= 1000`
- `bookings[i].length == 2`
- `0 <= openTime < closeTime <= 10^8`
- `openTime <= bookings[i][0] < bookings[i][1] <= closeTime`
- All bookings fall within `[openTime, closeTime]`

## Approach Hints

### Hint 1
Sort the bookings by start time first. This will help you process them in chronological order.

### Hint 2
You may need to merge overlapping bookings before finding the gaps.

### Hint 3
After merging, the gaps are the intervals between consecutive bookings. Don't forget to check for availability before the first booking and after the last booking.

## Solution

```python
def find_available_slots(bookings, openTime, closeTime):
    """
    Find all available time slots between bookings.

    Args:
        bookings: List of [start, end] intervals (inclusive)
        openTime: Start of operating hours
        closeTime: End of operating hours

    Returns:
        List of available time slots as [start, end] intervals
    """
    if not bookings:
        return [[openTime, closeTime]]

    # Sort bookings by start time
    bookings.sort()

    # Merge overlapping bookings
    merged = []
    for start, end in bookings:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent, merge them
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    # Find gaps between merged bookings
    available = []

    # Check if there's availability before first booking
    if merged[0][0] > openTime:
        available.append([openTime, merged[0][0] - 1])

    # Check gaps between consecutive bookings
    for i in range(len(merged) - 1):
        gap_start = merged[i][1] + 1
        gap_end = merged[i + 1][0] - 1
        if gap_start <= gap_end:
            available.append([gap_start, gap_end])

    # Check if there's availability after last booking
    if merged[-1][1] < closeTime:
        available.append([merged[-1][1] + 1, closeTime])

    return available
```

## Complexity Analysis

- **Time Complexity**: O(n log n) where n is the number of bookings
  - O(n log n) for sorting
  - O(n) for merging overlapping intervals
  - O(n) for finding gaps

- **Space Complexity**: O(n) for storing merged intervals

## Follow-up Questions

1. What if bookings could be cancelled? How would you handle dynamic updates?
2. How would you modify this to find the longest available time slot?
3. What if you need to find available slots of a minimum duration (e.g., at least 2 hours)?
4. How would you handle multiple rooms with different booking schedules?

## Related Problems

- Merge Intervals (Medium)
- Insert Interval (Medium)
- Meeting Rooms II (Medium)
- Employee Free Time (Hard)
