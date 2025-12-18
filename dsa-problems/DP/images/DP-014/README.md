# Image Generation Prompts for DP-014: Constrained Decode Ways

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of the problem concept

**Generation Prompt:**
```
infographic of a digit string being partitioned into codes 1-26, with a bold rule that only the pair '20' can include zero; arrows showing valid splits and red crosses on invalid '10' or '30'; clean technical style, teal and gray palette; 1200x800px
```

### 2. real-world-scenario.png
**Purpose:** Visualization of the real-world application
```
IoT device receiving a numeric OTP, a validator highlighting that zeros must follow an even digit two; security dashboard with checksum badge; semi-realistic illustration with professional blue/green colors; 1200x800px
```

### 3. algorithm-visualization.png
**Purpose:** Step-by-step algorithm flow diagram
```
rolling dynamic programming diagram with prev2, prev1, cur states over a digit string; branches for single-digit decode and two-digit decode with conditions pair==20 or 11..26; arrows showing modulo step; flat technical diagram; 1200x800px
```

### 4. example-1.png
**Purpose:** Visual walkthrough of the example
```
string '2012' split as '20|12' and '20|1|2' highlighted, invalid splits crossed out; annotated counts leading to total 2; simple light background infographic; 1200x800px
```

### 5. complexity-comparison.png
**Purpose:** Compare naive vs optimal approach
```
side-by-side bars: exponential recursion vs linear DP; arrows showing state reuse; concise labels 'O(2^n)' and 'O(n)'; modern flat design; 1200x800px
```

### 6. common-mistakes.png
**Purpose:** Illustrate common pitfalls
```
panel showing three mistakes: treating '10' as valid, accepting leading zero, forgetting modulo; each with red cross; green check next to correct handling; clean checklist style; 1200x800px
```

## Image Specifications
- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for complex diagrams)
- Style: Consistent with technical documentation
- Color Scheme: Professional (blues, greens, grays)
- Text: Clear, readable fonts (minimum 14pt)
