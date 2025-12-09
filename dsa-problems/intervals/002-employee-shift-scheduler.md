---
id: INT-002
display_id: 115
title: Merge Overlapping Work Shifts
difficulty: Medium
tags: [intervals, sorting, merging]
companies: [Workday, ADP, When I Work, Deputy]
premium: false
---

# Merge Overlapping Work Shifts

## Problem Statement

You are developing a workforce management system that tracks employee work shifts. Multiple employees may work overlapping shifts, and you need to calculate the total time periods during which at least one employee is working.

Given a list of shift intervals `[startTime, endTime]` representing different employee work shifts, merge all overlapping or adjacent shifts and return the consolidated work coverage periods.

**Real-world Application**: This problem is essential for workforce management platforms like Workday and ADP to calculate total labor coverage, ensure adequate staffing levels, identify gaps in coverage, and optimize scheduling. It's also used for calculating total billable hours across multiple contractors and tracking facility access times.

## Examples

### Example 1:
```
Input: shifts = [[9, 12], [11, 15], [17, 20]]

Output: [[9, 15], [17, 20]]

Explanation:
- Shifts [9, 12] and [11, 15] overlap, so they merge into [9, 15]
- Shift [17, 20] is separate with no overlap
- Total coverage: 6 hours from first merged shift, 3 hours from second = 9 hours total
```

### Example 2:
```
Input: shifts = [[8, 10], [10, 14], [14, 18], [18, 22]]

Output: [[8, 22]]

Explanation:
- All shifts are adjacent (end of one equals start of next)
- They merge into one continuous shift covering 14 hours
```

### Example 3:
```
Input: shifts = [[1, 4], [2, 5], [3, 6], [10, 15], [12, 18]]

Output: [[1, 6], [10, 18]]

Explanation:
- First three shifts [1,4], [2,5], [3,6] all overlap, merge to [1, 6]
- Last two shifts [10,15], [12,18] overlap, merge to [10, 18]
- Two separate coverage periods
```

### Example 4:
```
Input: shifts = [[5, 8]]

Output: [[5, 8]]

Explanation: Only one shift, no merging needed.
```

### Example 5:
```
Input: shifts = []

Output: []

Explanation: No shifts to merge.
```

## Constraints

- `0 <= shifts.length <= 10^4`
- `shifts[i].length == 2`
- `0 <= startTime_i < endTime_i <= 24`
- Times are in 24-hour format (0-24)

## Approach Hints

### Hint 1
Start by sorting the shifts. What property should you sort by?

### Hint 2
After sorting, iterate through the shifts. For each shift, check if it overlaps with the previous merged shift.

### Hint 3
Two shifts overlap if the start time of the current shift is less than or equal to the end time of the previous shift.

### Hint 4
When merging, the new end time should be the maximum of both end times.

## Solution

```python
def merge_shifts(shifts):
    """
    Merge overlapping or adjacent work shifts.

    Args:
        shifts: List of [startTime, endTime] intervals

    Returns:
        List of merged shift intervals
    """
    if not shifts:
        return []

    # Sort shifts by start time
    shifts.sort(key=lambda x: x[0])

    merged = [shifts[0]]

    for current_start, current_end in shifts[1:]:
        last_start, last_end = merged[-1]

        # Check if current shift overlaps or is adjacent to last merged shift
        if current_start <= last_end:
            # Merge by extending the end time
            merged[-1][1] = max(last_end, current_end)
        else:
            # No overlap, add as new shift
            merged.append([current_start, current_end])

    return merged


def calculate_total_coverage(shifts):
    """
    Calculate total hours of work coverage.

    Args:
        shifts: List of [startTime, endTime] intervals

    Returns:
        Total hours covered by all shifts
    """
    merged = merge_shifts(shifts)
    total_hours = sum(end - start for start, end in merged)
    return total_hours
```

## Alternative Solution (In-place)

```python
def merge_shifts_inplace(shifts):
    """
    Merge shifts in-place with O(1) extra space.
    """
    if not shifts:
        return []

    shifts.sort(key=lambda x: x[0])

    write_index = 0

    for i in range(1, len(shifts)):
        if shifts[i][0] <= shifts[write_index][1]:
            # Merge
            shifts[write_index][1] = max(shifts[write_index][1], shifts[i][1])
        else:
            # Move to next position
            write_index += 1
            shifts[write_index] = shifts[i]

    return shifts[:write_index + 1]
```

## Complexity Analysis

### Standard Solution
- **Time Complexity**: O(n log n)
  - O(n log n) for sorting the shifts
  - O(n) for merging overlapping intervals

- **Space Complexity**: O(n)
  - O(n) for storing the merged result
  - O(log n) for sorting space (depending on implementation)

### In-place Solution
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1) excluding sorting space

## Key Insights

1. **Sorting is crucial**: Sorting by start time ensures we only need one pass to merge
2. **Adjacent intervals**: Consider whether adjacent intervals (end of one equals start of next) should be merged
3. **End time comparison**: When merging, always take the maximum end time to handle nested intervals

## Follow-up Questions

1. **Calculate gaps**: How would you find all time periods where NO employee is working?
2. **Minimum workers**: Given shifts with employee IDs, find the minimum number of employees needed (if one employee can work multiple non-overlapping shifts)?
3. **Maximum overlap**: What's the maximum number of employees working at the same time?
4. **Insert new shift**: How would you efficiently insert a new shift into already merged shifts?
5. **Remove shift**: How would you handle shift cancellations?

## Use Cases

1. **Labor cost calculation**: Calculate total labor hours for payroll
2. **Coverage verification**: Ensure 24/7 coverage for customer support
3. **Compliance**: Verify employees aren't scheduled for excessive consecutive hours
4. **Facility management**: Track when buildings need to be open/secured
5. **Resource optimization**: Identify overstaffing or understaffing periods

## Related Problems

- Meeting Rooms (Easy)
- Insert Interval (Medium)
- Non-overlapping Intervals (Medium)
- Minimum Number of Arrows to Burst Balloons (Medium)
- Employee Free Time (Hard)
