# Image Placeholders for DP-002

This directory contains image assets for the Capped Coin Change With Penalty problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Coin types, caps, and penalty threshold concept
3. **real-world-scenario.png** - Hostel canteen token usage scenario
4. **algorithm-steps.png** - DP transition + remainder-class optimization steps
5. **algorithm-visualization.png** - Sliding-window minima with two windows (no-penalty vs penalty)
6. **example-1.png** - Walkthrough of the sample input

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors (Blue: #3B82F6, Green: #10B981, Orange: #F59E0B for “penalty activates”)
- Keep text readable (minimum 14pt)
- PNG format, optimized for web (<500KB each)

## Image Prompts

### Problem Images

- **header.png**: A clean 1200x300 banner featuring a minimalist set of coins labeled “d[i]”, a stack-limit indicator labeled “c[i]”, and a warning badge “penalty p[i] after half”. Professional flat infographic style, subtle gradient background with blue/green accents.

- **problem-illustration.png**: An infographic showing two coin types. Each coin type row includes: denomination icon, a bar showing maximum count `c`, a marked threshold at `floor(c/2)`, and a highlighted region beyond the threshold labeled “+p penalty”. Add a legend explaining: “Using more than half triggers a one-time penalty.”

- **example-1.png**: A step-by-step breakdown for sample 1: target 7 with coin types (1,4,2) and (5,2,1). Show picking one 5-coin and two 1-coins. Show that 2 ones are at the threshold (no penalty). Total cost displayed as 3.

### Editorial Images

- **real-world-scenario.png**: A hostel canteen counter scene with token stacks (₹1, ₹5). A “bulk usage fee” sign appears when a student tries to use too many ₹1 tokens. Clean vector style suitable for technical docs.

- **algorithm-steps.png**: A 4-panel flowchart: (1) Convert each type to effective cap `min(c, target/d)`, (2) Split decision into “no penalty (≤t)” and “penalty (>t)”, (3) Group sums by remainder mod d, (4) Use monotonic deque for sliding minimum to update dp in O(target).

- **algorithm-visualization.png**: A table for a fixed remainder class showing q indices and values `prev[q]-q`. Overlay two moving windows: Window A (no penalty) and Window B (penalty). Highlight the minimum element in each window and show computed candidates `q + min(...)` and `q + p + min(...)`.

