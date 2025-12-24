# Image Generation Prompts for TRI-007: Minimum Unique Prefix Lengths

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of minimum unique prefix concept

**Generation Prompt:**

```
Create a technical diagram showing the minimum unique prefix concept:
- Display a list of words on the left: "zebra", "dog", "duck", "dove"
- In the middle, show a trie structure with nodes labeled with characters
- Highlight paths through the trie for each word with different colors
- Mark with a star or badge where each word's path becomes unique (count=1)
- On the right, show a results panel: "zebra"→1, "dog"→2, "duck"→2, "dove"→2
- Use arrows connecting the unique points in the trie to the results
- Color scheme: Technical blue and white with green highlights for unique nodes
- Style: Clean technical infographic
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Visualization of DNS/domain name application

**Generation Prompt:**

```
Create an illustration showing a domain name registration interface:
- A web browser window showing a domain search interface
- Search bar with partial text "tech..." being typed
- Autocomplete dropdown showing:
  - "technology.com" (unique at 5 chars: "techn")
  - "technical.com" (unique at 6 chars: "techni")
  - "techstart.com" (unique at 5 chars: "techs")
  - "apple.com" (unique at 1 char: "a")
- Visual indicators showing minimum unique prefix length for each
- Background: Subtle globe/network icons representing DNS
- Include a small trie structure overlay showing how prefixes are organized
- Color scheme: Modern web interface (blue, white, green for available)
- Style: Modern web application mockup
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step algorithm flow for building trie with counts

**Generation Prompt:**

```
Create a detailed algorithm visualization showing:
1. Input words: ["dog", "duck", "dove"]
2. Step-by-step trie construction:
   - Insert "dog": root→d(1)→o(1)→g(1)
   - Insert "duck": root→d(2)→o(2)→u(1)→c(1)→k(1) and d→u branch
   - Insert "dove": root→d(3)→o(3)→v(1)→e(1) and o→v branch
3. Final trie with count annotations at each node
4. Query phase showing traversal for each word:
   - "dog": d(3)→o(3)→g(1) ✓ unique at position 2, length 2
   - "duck": d(3)→o(3)→u(1) ✓ unique at position 2, length 2
   - "dove": d(3)→o(3)→v(1) ✓ unique at position 2, length 2
- Use flowchart arrows and color coding for each step
- Highlight nodes where count becomes 1
- Style: Technical flowchart with clear step labels
- Size: 1600x1000px
```

### 4. example-1.png

**Purpose:** Visual walkthrough of example 1

**Generation Prompt:**

```
Create a detailed example walkthrough:
- Top: Input list: ["zebra", "dog", "duck", "dove"]
- Middle: Large trie diagram showing:
  - Root node at center
  - Branch 'z' going to zebra (count=1 immediately)
  - Branch 'd' going to 'o' (count=3 at 'd', count=3 at 'o')
    - Then splits to 'g', 'u', 'v' (each count=1)
- Bottom: Results table with columns:
  - Word | Traversal Path | Unique At | Min Length
  - zebra | z(1) | position 0 | 1
  - dog | d(3)→o(3)→g(1) | position 2 | 2
  - duck | d(3)→o(3)→u(1) | position 2 | 2
  - dove | d(3)→o(3)→v(1) | position 2 | 2
- Use color coding: green for unique nodes (count=1), orange for shared (count>1)
- Style: Educational diagram with clear annotations
- Size: 1200x1000px
```

### 5. example-2.png

**Purpose:** Visual walkthrough of example 2 with nested prefixes

**Generation Prompt:**

```
Create a detailed example for nested prefixes:
- Top: Input list: ["apple", "application", "app"]
- Middle: Trie diagram showing:
  - root→a→p→p (count=3)
  - From second 'p': splits to 'l' (count=2) and ends (count=1 for "app")
  - From 'l': splits to 'e' (count=1 for "apple") and 'i' (count=1 for "application")
- Annotations showing:
  - "app" is unique at its end (length 3)
  - "apple" needs "appl" then "e" to be unique (length 5)
  - "application" needs "appl" then "i" to be unique (length 5)
- Bottom: Results: ["apple"→5, "application"→5, "app"→3]
- Visual metaphor: Nested boxes showing prefix containment
- Style: Technical diagram with nested visual elements
- Size: 1200x900px
```

### 6. complexity-comparison.png

**Purpose:** Compare naive vs optimal approach performance

**Generation Prompt:**

```
Create a performance comparison chart:
Left panel: "Naive Approach O(n²×L)"
- Illustration: Grid showing n×n comparisons between all word pairs
- Example: 1000 words = 1,000,000 comparisons
- Icon: Nested loops with complexity notation

Right panel: "Optimal Approach O(n×L)"
- Illustration: Single-pass trie construction and traversal
- Example: 1000 words = 1,000 operations
- Icon: Tree structure with linear path

Bottom: Performance graph
- X-axis: Number of words (100, 1K, 10K, 100K)
- Y-axis: Time (ms)
- Two lines: Naive (exponential curve) vs Optimal (linear)
- Highlight improvement: "10,000× faster for large inputs"

Color scheme: Red for naive, green for optimal
Style: Technical infographic with charts and graphs
Size: 1200x800px
```
