# Image Generation Prompts for DP-016: Exams With Cooldown Gap

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of the problem concept

**Generation Prompt:**
```
timeline of exams as colored bars with start and end times; gap g shown as a shaded buffer between chosen exams; objective arrow pointing to maximum total score; clean scheduling infographic, blue/green palette; 1200x800px
```

### 2. real-world-scenario.png
**Purpose:** Visualization of the real-world application
```
student planning certification exams on a calendar, with mandatory cooldown blocks between appointments; highlighted scores on selected slots; semi-realistic illustration with academic theme; 1200x800px
```

### 3. algorithm-visualization.png
**Purpose:** Step-by-step algorithm flow diagram
```
flowchart of weighted interval scheduling with gap: sort by end time, binary search latest compatible exam using start - g, dp[i] = max(dp[i-1], dp[j]+score); arrows over a timeline; technical diagram style; 1200x800px
```

### 4. example-1.png
**Purpose:** Visual walkthrough of the example
```
three exam bars with times (1-3, 4-6, 6-10) and gap g=1; choose first two bars highlighted, third grayed out; total score annotation 11; light background infographic; 1200x800px
```

### 5. complexity-comparison.png
**Purpose:** Compare naive vs optimal approach
```
side-by-side comparison: exponential DFS tree vs O(n log n) DP with binary search; include Big-O labels; flat professional design; 1200x800px
```

### 6. common-mistakes.png
**Purpose:** Illustrate common pitfalls
```
panels showing mistakes: forgetting the gap g, sorting by start instead of end, using 32-bit scores; red crosses and green corrections; clean checklist style; 1200x800px
```

## Image Specifications
- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for complex diagrams)
- Style: Consistent with technical documentation
- Color Scheme: Professional (blues, greens, grays)
- Text: Clear, readable fonts (minimum 14pt)
