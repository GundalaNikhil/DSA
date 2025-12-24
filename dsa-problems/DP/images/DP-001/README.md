# Image Placeholders for DP-001

This directory contains image assets for the Staircase With Cracked Steps and Max Jump problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Main concept visualization (safe vs cracked steps)
3. **algorithm-steps.png** - DP + sliding-window steps
4. **algorithm-visualization.png** - WindowSum evolution across i
5. **real-world-scenario.png** - Campus staircase renovation scenario
6. **example-1.png** - Example walkthrough (`n=4, J=3, cracked={2}`)

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors (Blue: #3B82F6, Green: #10B981, Red: #EF4444 for cracked steps)
- Clear labels: step index, jumps, and “cannot land here”
- PNG format, optimized for web (<500KB each)

## Image Prompts

### Problem Images

- **header.png**: A wide 1200x300 banner showing a stylized staircase in a modern campus building. Some steps have a subtle red crack icon and a “no landing” symbol. Title text “DP-001: Staircase Ways” in a clean sans-serif font, with a small badge “Jump 1..J”. Professional flat infographic style, soft gradient background using blue/green accents.

- **problem-illustration.png**: A clean horizontal staircase diagram labeled steps 0..n. Cracked steps colored light red with a cross mark. Arrows showing allowable jumps of length 1..J from each step (faded), emphasizing “can jump over cracked steps but cannot land on them.” Include a legend: Safe step (green), Cracked step (red).

- **example-1.png**: A step-by-step path illustration for `n=4, J=3, cracked={2}`. Show the three valid paths as three separate lines/arrows: `0→1→3→4`, `0→1→4`, `0→3→4`. Step 2 is highlighted red with “blocked”.

### Editorial Images

- **real-world-scenario.png**: A campus staircase with caution tape on certain steps, and a student jumping over a blocked step safely. Include small icons for “Safety rules” and “Navigation app”.

- **algorithm-steps.png**: A 3-panel flow: (1) Build `cracked[]` boolean array, (2) DP recurrence `dp[i]=sum(dp[i-1..i-J])` with `dp[i]=0` if cracked, (3) Sliding window update showing add `dp[i]` and subtract `dp[i-J]`. Add “O(n)” in corner.

- **algorithm-visualization.png**: A table-like visualization for i=0..n showing `dp[i]` and `windowSum`. Highlight the sliding window range for each i with a colored bracket, showing how the window shifts by 1 each step.

