# Image Placeholders for DP-008

This directory contains image assets for the Grid Paths With Turn Limit problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Grid with right/down moves and turn counting
3. **real-world-scenario.png** - Robot navigation with limited turns
4. **algorithm-steps.png** - DP state: dpR/dpD with turn increments
5. **algorithm-visualization.png** - DP table for small grid showing transitions
6. **example-1.png** - Example walkthrough for `m=2, n=3, T=1`

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (right moves / dpR)
  - Green: #10B981 (down moves / dpD)
  - Orange: #F59E0B (turns highlight)
- Keep annotations minimal and readable (≥14pt).
- PNG format, optimized for web (<500KB each).

## Image Prompts

### Problem Images

- **header.png**: A 1200x300 banner with a small grid diagram. Highlight a path with a “turn counter” icon showing “≤ T turns”. Modern flat style, blue/green accents.

- **problem-illustration.png**: A 4x4 grid. Show a path going right and down with markers where direction changes (turns). Label “Right”, “Down”, and “Turn”. Add a bubble “First move is not a turn”.

- **example-1.png**: For `2x3` grid, draw the three possible paths `RRD`, `RDR`, `DRR` and mark which are valid for `T=1`. Show the count “2” prominently.

### Editorial Images

- **real-world-scenario.png**: A corridor-like grid map with a small delivery robot. Show a “turn budget” gauge and a route with few bends.

- **algorithm-steps.png**: A flowchart of the recurrence:
  - `dpR[r][c][t] += dpR[r][c-1][t]`
  - `dpR[r][c][t] += dpD[r][c-1][t-1]`
  - same for dpD from top
  Include a note “first move doesn’t count as a turn”.

- **algorithm-visualization.png**: A small 3x3 grid DP table with arrows showing how `dpR` and `dpD` fill. Color-code directions, and mark when `t` increases on a direction change.
