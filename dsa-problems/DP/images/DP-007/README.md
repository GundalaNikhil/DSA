# Image Placeholders for DP-007

This directory contains image assets for the Auditorium Max Sum With Gap Three problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - “Pick with gap >= 3” constraint visualization
3. **real-world-scenario.png** - Auditorium volunteer placement scenario
4. **algorithm-steps.png** - DP recurrence steps (`dp[i]=max(dp[i-1], a[i]+dp[i-3])`)
5. **algorithm-visualization.png** - DP progression across indices (skip vs take)
6. **example-1.png** - Example walkthrough for `[4,1,2,9,3]`

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (array cells)
  - Green: #10B981 (chosen indices / optimal path)
  - Red: #EF4444 (blocked neighbors i±1, i±2)
- Clear labels and arrows; minimal text.
- PNG format, optimized for web (<500KB each)

## Image Prompts

### Problem Images

- **header.png**: A 1200x300 banner showing an auditorium seating row as a horizontal array. Some seats are highlighted in green as “selected” with a visible gap of 2 seats between selections. Include title text “Max Sum with Gap ≥ 3” in a modern sans-serif font.

- **problem-illustration.png**: A diagram of array indices 0..n-1. Highlight a chosen index `i` and shade indices `i-2, i-1, i+1, i+2` in red with a “forbidden” icon. Show that the next allowed selection is `i+3` or later with a green arrow.

- **example-1.png**: For `[4,1,2,9,3]`, show selecting indices 0 and 3. Display sum `4 + 9 = 13`. Mark the blocked indices around 0 and 3 to reinforce the constraint visually.

### Editorial Images

- **real-world-scenario.png**: A simple illustration of an auditorium with volunteers placed in rows with buffer rows in between. Add a small sign: “Keep 2-row buffer for safety.” Clean vector style.

- **algorithm-steps.png**: A 3-step flow:
  1) “Skip i” ⇒ `dp[i-1]`
  2) “Take i” ⇒ `a[i] + dp[i-3]`
  3) “Choose max” ⇒ `dp[i]`
  Include an “O(n)” label.

- **algorithm-visualization.png**: A table with columns `i`, `a[i]`, `take`, `skip`, `dp[i]`. Show a highlighted row where `take` wins (at i=3 in the sample). Use green highlight for the chosen branch.

