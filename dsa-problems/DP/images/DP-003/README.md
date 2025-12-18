# Image Placeholders for DP-003

This directory contains image assets for the Required Weight Knapsack problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Items, capacity `W`, and required minimum `R`
3. **real-world-scenario.png** - Lab kit packing scenario (minimum required kit weight)
4. **algorithm-steps.png** - DP state + transition + answer extraction from `[R..W]`
5. **algorithm-visualization.png** - DP array update visualization (descending weight loop)
6. **example-1.png** - Visual walkthrough of the example

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (capacity bar)
  - Green: #10B981 (valid weights ≥ R)
  - Red: #EF4444 (invalid weights < R)
- Keep labels readable (minimum 14pt)
- PNG format, optimized for web (<500KB each)

## Image Prompts

### Problem Images

- **header.png**: A clean 1200x300 banner showing a knapsack icon with a capacity gauge labeled `W`. A second marker labeled `R` indicates a minimum required fill. Several item cards (weight/value) appear as small tiles. Flat infographic style with professional blue/green palette.

- **problem-illustration.png**: A diagram with a horizontal weight bar from 0 to W. Highlight the required region `[R..W]` in green, and the region `[0..R-1]` in red. Show items as blocks with weights, and an arrow indicating “choose subset so total weight lands in green zone”.

- **example-1.png**: For the sample (n=3, W=6, R=5), show the three items as cards: (2,4), (3,5), (4,6). Show two valid combinations: weight 5 value 9 and weight 6 value 10 (highlight best). Use clear sum visuals.

### Editorial Images

- **real-world-scenario.png**: A college lab kit packing scene: safety box with a “max weight W” warning label and a checklist stating “minimum required kit weight R”. Items like goggles, gloves, beakers are shown as icons with weight/value tags.

- **algorithm-steps.png**: A 4-step flow: (1) initialize `dp[0]=0`, others `-INF`; (2) for each item, loop `wt=W..wi` descending; (3) update `dp[wt]=max(dp[wt], dp[wt-wi]+vi)`; (4) take answer as `max(dp[R..W])` (highlight that answer is not always dp[W]).

- **algorithm-visualization.png**: A grid/table showing dp indices 0..W and how an item update changes dp values. Emphasize descending iteration with arrows going right-to-left. Add a “0/1 only” note to show why descending order prevents reuse.

