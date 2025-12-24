# Image Placeholders for DP-004

This directory contains image assets for the Exact Count Subset Sum problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Array + target + exact k constraint visual
3. **real-world-scenario.png** - Scholarship shortlist scenario
4. **algorithm-steps.png** - DP-by-count and bitset update `bits[c] |= bits[c-1] << x`
5. **algorithm-visualization.png** - Bitset shifting and OR-ing across counts
6. **example-1.png** - Example walkthrough (`[3,1,9,7]`, target 10, k=2)

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (array elements / base)
  - Green: #10B981 (reachable sums / true states)
  - Gray: #6B7280 (unreachable / false states)
- Minimal text, clear arrows
- PNG format, optimized for web (<500KB each)

## Image Prompts

### Problem Images

- **header.png**: A clean 1200x300 banner showing an array of number tiles and a highlighted “k = exact count” badge. Include a target bullseye icon labeled “target”. Flat infographic style, blue/green palette.

- **problem-illustration.png**: A diagram showing selecting exactly `k` items from an array. Use checkmarks on chosen elements. Show “sum = target” on the right. Emphasize “exactly k” with a small counter icon.

- **example-1.png**: Visualize the array `[3,1,9,7]` with chosen subset `{3,7}` highlighted. Show `k=2` and `3+7=10` with a clear equation box. Include a small note “exactly 2 elements”.

### Editorial Images

- **real-world-scenario.png**: Scholarship committee table scene with student score cards. A rule card reads “Pick exactly k students” and a scoreboard reads “Total = target”. Clean vector style.

- **algorithm-steps.png**: A 4-step flow:
  1) Initialize `bits[0]=1`
  2) For each x, process counts from k down to 1
  3) Update `bits[c] |= bits[c-1] << x`
  4) Check bit `target` in `bits[k]`

- **algorithm-visualization.png**: A bitset row (0..target) with green dots for reachable sums. Show a shift-left operation by `x` (arrow shifting dots right), then an OR merge. Show two rows for `c-1` and `c`.

