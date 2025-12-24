# Image Placeholders for DP-006

This directory contains image assets for the Strict Jump LIS With Max Gap problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Difference window `[d, g]` constraint visual
3. **real-world-scenario.png** - Controlled temperature sampling scenario
4. **algorithm-steps.png** - Coordinate compression + range max query steps
5. **algorithm-visualization.png** - Segment tree query range `[x-g, x-d]` and update at `x`
6. **example-1.png** - Example walkthrough for the sample

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (values / nodes)
  - Green: #10B981 (valid predecessor range)
  - Orange: #F59E0B (current value x and update)
- PNG format, optimized for web (<500KB each)

## Image Prompts

### Problem Images

- **header.png**: A 1200x300 banner showing an increasing line chart with “bounded jumps” highlighted. Add a badge “d ≤ Δ ≤ g”. Modern infographic style.

- **problem-illustration.png**: A number line with a current value `x`. Highlight the valid predecessor interval `[x-g, x-d]` in green. Show a few points representing previous array values and an arrow selecting the best predecessor.

- **example-1.png**: Visualize `[1,3,4,9,10]` with chosen subsequence `1 -> 3 -> 9`. Show difference labels `+2` and `+6` and highlight they are within [2,6].

### Editorial Images

- **real-world-scenario.png**: A server room temperature chart with annotations: “Ignore spikes” and “Select stable rising sequence.” Include d/g slider knobs.

- **algorithm-steps.png**: A flowchart: (1) compress values, (2) for each x compute bounds lo=x-g, hi=x-d, (3) query segment tree for max dp in [lo,hi], (4) update dp at x.

- **algorithm-visualization.png**: A compressed value axis and a segment tree block showing a highlighted query interval and an update point. Include tiny labels “query max” and “update max”.

