# Image Generation Prompts for TRI-001: Autocomplete Top-K with Freshness Decay

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of the autocomplete system with decay scoring

**Generation Prompt:**

```
Create a technical diagram showing an autocomplete search interface with a trie data structure visualization. Show:
- A search bar at the top with partial text "he" being typed
- Below it, a trie structure with nodes branching for words: "he", "hello", "helium"
- Each word node has metadata tags showing: frequency (number), timestamp (clock icon), and calculated decay score
- A ranking panel on the right showing the top-k results ordered by score
- Use a modern, clean design with technical blue and white color scheme
- Include decay formula: score = freq × e^(-(t_current - t_last)/D) as an overlay
- Style: Technical infographic with clear labels
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Visualization of the e-commerce search application

**Generation Prompt:**

```
Create an illustration of an e-commerce platform search interface showing:
- A laptop/desktop screen displaying a search bar with "iPhone" being typed
- Autocomplete dropdown showing suggestions: "iPhone 15 Pro", "iPhone 15", "iPhone 14" with small indicators showing frequency and recency
- A timeline on the side showing search trends over time with decay curves
- Visual metaphor: older searches fading/becoming transparent, recent searches bright and prominent
- Background: Subtle shopping cart icons, product boxes
- Color scheme: E-commerce friendly (blue, orange, white)
- Style: Modern illustration, semi-realistic
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step algorithm flow diagram

**Generation Prompt:**

```
Create a flowchart diagram showing the autocomplete algorithm process:
1. "Input: prefix 'he'" at top
2. Trie traversal: Navigate from root -> h -> e (highlighted path)
3. DFS collection: Branches showing "he", "hello", "helium" being collected
4. Metadata lookup: Hash table with word -> (freq, timestamp) mappings
5. Score calculation: Formula boxes showing decay computation for each word
6. Heap construction: Min-heap visualization with top-k words
7. Output: Ranked list ["he", "hello"]
- Use flowchart arrows connecting steps
- Color code: Blue for trie operations, green for calculations, orange for ranking
- Style: Technical flowchart with clean lines
- Size: 1600x900px for clarity
```

### 4. example-1.png

**Purpose:** Visual walkthrough of the example

**Generation Prompt:**

```
Create a detailed example walkthrough showing:
- Left side: Input data table with columns: Word, Frequency, Timestamp
  Rows: "hello" (5, 0), "helium" (3, 5), "he" (4, 9)
- Middle: Calculation steps showing decay score computation for each word
  Current time = 10, D = 10
  "hello": 5 × e^(-10/10) = 1.84
  "helium": 3 × e^(-5/10) = 1.82
  "he": 4 × e^(-1/10) = 3.62
- Right side: Sorted results with visual bars showing relative scores
  "he" (3.62) - longest bar
  "hello" (1.84) - medium bar
  "helium" (1.82) - short bar
- Highlight top-2 selection with green checkmarks
- Style: Clean data visualization with charts and tables
- Colors: Professional blues, greens, grays
- Size: 1200x800px
```

### 5. complexity-comparison.png

**Purpose:** Compare naive vs optimal approach

**Generation Prompt:**

```
Create a comparison chart showing two approaches:
Left panel: "Naive Approach"
- Linear scan through all N words
- Full sort of matches
- Time complexity: O(N + M log M)
- Illustration: Large array being scanned sequentially

Right panel: "Optimal Approach"
- Trie prefix navigation
- Heap for top-k
- Time complexity: O(P + M log k)
- Illustration: Trie with direct path to prefix, small heap at bottom

Bottom: Performance graph showing time vs number of words
- Two curves: naive (steep linear), optimal (flat with trie)
- X-axis: Number of words (10^3 to 10^6)
- Y-axis: Query time (ms)
- Style: Professional performance comparison chart
- Colors: Red for naive, green for optimal
- Size: 1200x800px
```

### 6. common-mistakes.png

**Purpose:** Illustrate common pitfalls

**Generation Prompt:**

```
Create a three-panel illustration showing common mistakes:

Panel 1: "Incorrect Decay Calculation"
- Show code snippet with integer division bug
- Cross mark (❌): exp(-(t_curr - t_last) / D) with D as int
- Check mark (✅): exp(-(t_curr - t_last) / (double)D)
- Visual: Calculator showing wrong vs right result

Panel 2: "Missing Tie-Breaking"
- Show two words with same score but wrong order
- Cross mark: Only score sorting
- Check mark: Score DESC, then lexicographic ASC
- Visual: Podium with tied scores, arrows showing alphabetical order

Panel 3: "Inefficient Full Sort"
- Show large array being fully sorted unnecessarily
- Cross mark: sort(all_matches) then take first k
- Check mark: Min-heap of size k
- Visual: Heap structure vs large sorted array with waste highlighted

- Style: Educational comic-style panels with code snippets
- Colors: Red for wrong, green for correct
- Size: 1200x800px
```

## Image Specifications

- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for complex diagrams)
- Style: Consistent with technical documentation
- Color Scheme: Professional (blues, greens, grays, with accent colors for highlights)
- Text: Clear, readable fonts (minimum 14pt)
- Annotations: Use arrows, labels, and callouts for clarity
