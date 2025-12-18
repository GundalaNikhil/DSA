# Image Placeholders for DP-012

This directory contains image assets for the Balanced Partition With Size Limit problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Two groups with sums difference ≤ D and sizes highlighted
3. **real-world-scenario.png** - Team split / workload balancing example
4. **algorithm-steps.png** - DP over (size, sum) transitions
5. **algorithm-visualization.png** - Reachable sums by size (sets/bitmask) and answer extraction
6. **example-1.png** - Example walkthrough for `[3,1,4,2], D=1`

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (group A)
  - Green: #10B981 (group B)
  - Orange: #F59E0B (difference constraint highlight)
- Keep numbers readable (≥14pt).
- PNG format, optimized for web (<500KB each).

## Image Prompts

### Problem Images

- **header.png**: Banner showing two baskets of numbers with a balance scale; a badge shows “|sumA - sumB| ≤ D” and “minimize max size”.

- **problem-illustration.png**: Split array `[3,1,4,2]` into `{3,2}` and `{1,4}`. Show sums 5 and 5 (diff 0), sizes 2/2, larger size 2. Contrast with an invalid split where diff > D.

- **example-1.png**: Explicitly visualize the chosen partition for the sample; include a small table of candidate splits and their larger sizes.

### Editorial Images

- **real-world-scenario.png**: Two teams of students with “workload” icons; a rule card “difference ≤ D” and a note “minimize bigger team”.

- **algorithm-steps.png**: Flowchart:
  1) `dp[k] = reachable sums with k elements`
  2) For each x, update k descending with sums `s+x`
  3) Check all (k, s) where `|total - 2s| ≤ D`
  4) Answer = min `max(k, n-k)`

- **algorithm-visualization.png**: A grid/list of reachable sums per k (e.g., k=0..n). Highlight feasible cells (diff ≤ D) and show the chosen minimum larger-group size. Include note about handling negative sums via sets.
