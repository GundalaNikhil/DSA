# Image Placeholders for DP-011

This directory contains image assets for the Expression Target Modulo With Required Minus problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Chunking the digit string and inserting +/-
3. **real-world-scenario.png** - Checksum / debit-credit analogy
4. **algorithm-steps.png** - DP state (pos, mod, usedMinus) transitions
5. **algorithm-visualization.png** - Small DP table over positions and remainders
6. **example-1.png** - Example walkthrough for `s=1234, M=7, K=0, Lmax=2`

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors:
  - Blue: #3B82F6 (chunks added)
  - Red: #EF4444 (chunks subtracted)
  - Green: #10B981 (states satisfying remainder)
- Keep chunk boundaries and operators clearly labeled.
- PNG format, optimized for web (<500KB each).

## Image Prompts

### Problem Images

- **header.png**: A 1200x300 banner showing a digit string split into chunks with `+` and `-` between them. A badge says “must include at least one minus”. A modulo circle shows “% M”.

- **problem-illustration.png**: Show the string `1234` split into `12` and `34`, with options `12-34`, `12+34`, etc. Highlight the modulo result bubble “%7 == 0”.

- **example-1.png**: For `1234, M=7, K=0, Lmax=2`, show the 5 valid expressions (list or small grid) and mark the remainder as 0. Make sure a minus is present in each.

### Editorial Images

- **real-world-scenario.png**: Depict a ledger/checksum where some numbers are added and some subtracted, with a rule “at least one debit”. A modulo check wheel is shown.

- **algorithm-steps.png**: Flowchart of transitions:
  1) Choose next chunk (length ≤ Lmax, no leading zeros)
  2) If first chunk, set remainder
  3) Else add or subtract: update `(pos+len, newRem, usedMinus)`
  4) Count states with `usedMinus=1` and `rem=K` at end

- **algorithm-visualization.png**: A small DP grid where rows are positions and columns are remainders. Show arrows for add/subtract and a flag for `usedMinus`. Include a note about modulo handling of negatives.
