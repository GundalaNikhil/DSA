# Image Generation Prompts for DP-013: Paint Fence With Switch Cost

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of the problem concept

**Generation Prompt:**
```
illustration of workers painting a long wooden fence with colored stripes, showing at most two identical colors in a row; some posts have a small wrench icon indicating a switch cost; clean infographic style with labels "post i", "switch cost s[i]", "no 3-in-a-row"; bright professional palette (blues, greens, oranges); resolution 1200x800px
```

### 2. real-world-scenario.png
**Purpose:** Visualization of the real-world application
```
theme park queue barriers being wrapped with colored tape, maintenance crew swapping tape rolls causing extra effort, signage that bans three identical colors in a row, visitors walking by; semi-realistic illustration with warm daylight colors; resolution 1200x800px
```

### 3. algorithm-visualization.png
**Purpose:** Step-by-step algorithm flow diagram
```
flowchart of dynamic programming for fence painting: states dp1(color, streak=1) and dp2(color, streak=2); arrows showing extend to streak 2 and switch with cost s[i]; highlight best/second-best tracking for O(k) transition; technical diagram style; resolution 1200x800px
```

### 4. example-1.png
**Purpose:** Visual walkthrough of the example
```
three fence posts labeled 1,2,3 colored A,A,B; cost annotations "1", "1", "1 + switch 1 = 2", total cost 4; simple clean infographic on light background; resolution 1200x800px
```

### 5. complexity-comparison.png
**Purpose:** Compare naive vs optimal approach
```
split chart comparing O(n*k^2) naive transitions vs O(n*k) optimized min-tracking; bars or time-cost illustration with explanatory labels; modern flat design; resolution 1200x800px
```

### 6. common-mistakes.png
**Purpose:** Illustrate common pitfalls
```
visual of mistakes: three identical colors crossed out, incorrect switch cost added when color unchanged, missing impossibility when k=1 and n>2; checklist style with red crosses and green checks; resolution 1200x800px
```

## Image Specifications
- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for complex diagrams)
- Style: Consistent with technical documentation
- Color Scheme: Professional (blues, greens, grays)
- Text: Clear, readable fonts (minimum 14pt)
