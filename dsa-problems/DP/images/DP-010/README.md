# Image Placeholders for DP-010

This directory contains image assets for the LCS With Limited Skips in A problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - LCS diagram with skip budget
3. **real-world-scenario.png** - API compatibility / code pruning analogy
4. **algorithm-steps.png** - LCS DP + budget check
5. **algorithm-visualization.png** - DP table (space-optimized rows) example
6. **example-1.png** - Example walkthrough for `a="abcde", b="ace", s=2`

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (characters kept)
  - Red: #EF4444 (characters deleted from `a`)
  - Green: #10B981 (matches)
- Keep labels and numbers readable (≥14pt).
- PNG format, optimized for web (<500KB each).

## Image Prompts

### Problem Images

- **header.png**: A 1200x300 banner showing two strings aligned, with some characters crossed out on the `a` side and a badge “skip budget s”. Title text “LCS with Limited Skips in A”.

- **problem-illustration.png**: Visualize strings `a` and `b` with arrows showing matched characters forming a subsequence. Highlight deleted chars in `a` in red and a counter “deletions = |a| - L ≤ s”.

- **example-1.png**: For `a="abcde"`, `b="ace"`, `s=2`, show deleting `b` and `d` from `a` (2 deletions) to match “ace”. Annotate “LCS=3, deletions=2 ≤ s”.

### Editorial Images

- **real-world-scenario.png**: An API diff view where some endpoints in `a` are struck out (limited count), matching endpoints in `b`. A gauge shows “skip budget”.

- **algorithm-steps.png**: A flowchart:
  1) Compute LCS with standard DP
  2) Let deletions = |a| - LCS
  3) If deletions ≤ s ⇒ answer = LCS else answer = -1

- **algorithm-visualization.png**: A small DP table for two short strings, with a highlighted path producing the LCS. Show the rolling-row optimization (previous row / current row).
