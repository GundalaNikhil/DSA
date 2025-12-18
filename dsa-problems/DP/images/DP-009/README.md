# Image Placeholders for DP-009

This directory contains image assets for the Flooded Campus Min Cost With Free Cells problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Grid with costs and selected free cells
3. **real-world-scenario.png** - Flooded campus / emergency pass concept
4. **algorithm-steps.png** - DP with free-cell budget transitions
5. **algorithm-visualization.png** - 3D DP slice (r,c,k) showing min updates
6. **example-1.png** - Example walkthrough for the 2x2 grid sample

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (paid cells)
  - Green: #10B981 (cells marked free)
  - Gray: #6B7280 (unvisited/neutral)
- Keep text and numbers readable (≥14pt).
- PNG format, optimized for web (<500KB each).

## Image Prompts

### Problem Images

- **header.png**: A 1200x300 banner showing a grid with numeric costs. Highlight a few cells with a “free” badge. Title text “Min Cost with up to f Free Cells”.

- **problem-illustration.png**: A 4x4 grid with example costs. Show a chosen path right/down, and a couple of cells tinted green to indicate they are free (cost 0). Annotate path cost calculation.

- **example-1.png**: For the sample (2x2 with costs 5,3,4,1 and f=1), show making (0,0) free and the resulting path cost `0+3+1=4`.

### Editorial Images

- **real-world-scenario.png**: A campus map with flooded areas; a few checkpoints marked with “free pass” icons. A path is drawn with accumulated cost labels.

- **algorithm-steps.png**: A flow diagram of transitions:
  1) move right/down and pay cost
  2) move right/down and consume a free cell
  Show states `(r,c,k)` and “min” updates.

- **algorithm-visualization.png**: A small DP table with a third dimension for `k`. Show two layers (k and k+1) and arrows indicating how freeing a cell updates the next layer.
