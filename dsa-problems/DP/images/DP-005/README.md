# Image Placeholders for DP-005

This directory contains image assets for the Keyboard Row Edit Distance with Shift Penalty problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Keyboard rows/hands and operation costs
3. **real-world-scenario.png** - Auto-correct / typing effort scenario
4. **algorithm-steps.png** - Edit distance recurrence (insert/delete/replace with custom cost)
5. **algorithm-visualization.png** - DP grid visualization (rolling rows)
6. **example-1.png** - Example walkthrough (`type -> tap`)

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (DP table)
  - Green: #10B981 (chosen min path)
  - Orange: #F59E0B (replacement cost highlight)
- Keep text readable (minimum 14pt)
- PNG format, optimized for web (<500KB each)

## Image Prompts

### Problem Images

- **header.png**: A 1200x300 banner showing a small QWERTY keyboard illustration split into three rows. A path arrow transforms string “a” to “b” with a cost label “weighted edit distance”. Clean infographic style.

- **problem-illustration.png**: A QWERTY keyboard diagram with rows shaded differently. Left-hand keys shaded light blue, right-hand keys shaded light purple. Include a legend explaining replace cost rules: same row = 1, same hand different row = 2, different hand = 3. Insert/delete shown as cost 1.

- **example-1.png**: Show `type -> tap` transformation. Depict the sequence: insert `a`, delete `y`, delete `e`. Use arrows and cost bubbles (1 each) to show total cost 3.

### Editorial Images

- **real-world-scenario.png**: An auto-correct UI on a laptop where corrections within same row are highlighted green (cheap), cross-hand changes highlighted red (expensive). Clean vector style.

- **algorithm-steps.png**: A 3-branch recurrence diagram for dp[i][j] showing min of delete, insert, replace. In the replace branch, show a small keyboard icon that outputs 0/1/2/3 cost based on row/hand.

- **algorithm-visualization.png**: A DP grid with axes labeled characters of a and b. Show a highlighted optimal path (diagonal/left/up moves). Emphasize rolling array optimization by showing only two rows retained.

