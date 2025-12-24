# Image Generation Prompts for TDP-005: Max Path Sum with Length Limit

## Overview

This directory contains placeholder references for images used in the problem and editorial for TDP-005.

## Required Images

### 1. problem-illustration.png

**Purpose:** Visual representation of path sum calculation with length constraint

**Generation Prompt:**

```
Create a tree diagram showing a tree with 6-7 nodes where:
- Each node displays its value (some positive, some negative)
- Highlight 2-3 different paths with different colors
- For each highlighted path, show:
  * Number of edges (length)
  * Sum of node values
  * Whether it satisfies the length constraint L
- One path marked with green checkmark (valid and optimal)
- One path marked with red X (exceeds length limit)
- Include L value prominently displayed (e.g., "L = 3")

Example annotation:
"Path: 1→2→5 (2 edges, sum = 35) ✓"
"Path: 1→2→4→7 (3 edges, sum = 40) ✗ exceeds L=2"

- Style: Clean technical diagram
- Colors: Green for valid optimal, red for invalid, blue for valid non-optimal
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Supply chain optimization visualization

**Generation Prompt:**

```
Create an infographic showing a distribution network:
- Warehouses as nodes (building icons)
- Each warehouse shows profit/loss value
  * Green buildings for positive values
  * Red buildings for negative values (but strategically located)
- Route highlighted between warehouses
- Clock/timer icon showing delivery time constraint
- Text annotations:
  * "Maximum Profit Route"
  * "Within delivery time: ≤ L stops"
  * Show calculation: "Route Profit = sum of warehouses"
- Include truck icon moving along route
- Dollar signs/coins for profit indicators

- Style: Professional logistics infographic
- Colors: Green for profit, red for cost, blue for route
- Size: 1200x800px
- Icons: Warehouses, trucks, clocks, money
```

### 3. algorithm-visualization.png

**Purpose:** DP algorithm step-by-step visualization

**Generation Prompt:**

```
Create a 3-panel progression:

Panel 1 - "DP State Definition":
- Show tree with one node highlighted
- Display DP table: dp[node][length] = max sum
- Example values filled in for a node
- Label: "Track best path for each length"

Panel 2 - "Extending Paths":
- Show parent node combining paths from children
- Arrows from child paths to parent
- Formula: dp[u][len+1] = max(dp[child][len] + value[u])
- Highlight length increment

Panel 3 - "Combining Paths":
- Show two paths from different subtrees meeting at a node
- Calculation: path1[len1] + path2[len2] + node_value
- Constraint check: len1 + len2 ≤ L
- Final maximum highlighted

- Style: Educational flowchart
- Colors: Progressive (blue → green → gold)
- Size: 1600x900px
```

### 4. example-walkthrough.png

**Purpose:** Detailed example solution

**Generation Prompt:**

```
Create a comprehensive walkthrough for Example 1:

Tree diagram (center):
```

    1(val=1)

/ \
 2 3
(val=-2) (val=3)

```

L = 2 (shown prominently)

Below tree, enumerate all paths:

**Length 0 (single nodes):**
- Node 1: sum = 1
- Node 2: sum = -2
- Node 3: sum = 3

**Length 1 (2 nodes):**
- Path 1-2: sum = 1 + (-2) = -1
- Path 1-3: sum = 1 + 3 = 4 ✓ MAXIMUM

**Length 2 (3 nodes):**
- Path 2-1-3: sum = -2 + 1 + 3 = 2

Result box: "Maximum = 4"

- Style: Clean educational diagram with tables
- Colors: Gold highlight for maximum
- Size: 1200x800px
```

### 5. complexity-comparison.png

**Purpose:** Compare brute force vs DP approach

**Generation Prompt:**

```
Create side-by-side comparison:

**Left - Brute Force O(n³):**
- Show enumeration of all node pairs
- For each pair, show path finding
- Text: "Try every pair of nodes"
- Example: n=1000 → billions of operations
- Red complexity label: "O(n³)"

**Right - DP O(n×L²):**
- Show single DFS traversal
- DP table being filled bottom-up
- Text: "Single pass with DP table"
- Example: n=1000, L=500 → millions of operations
- Green complexity label: "O(n×L²)"

**Bottom: Performance graph**
- X-axis: n (tree size)
- Y-axis: Operations (log scale)
- Two curves: cubic (red) vs quadratic (green)
- Crossover point highlighted

- Style: Technical comparison
- Colors: Red for brute force, green for DP
- Size: 1200x800px
```

### 6. common-mistakes.png

**Purpose:** Illustrate implementation errors

**Generation Prompt:**

```
Create a three-panel error guide:

**Panel 1 - "Ignoring Negative Values":**
- Show path with negative intermediate nodes
- Wrong: Skip negative nodes → miss optimal path
- Correct: Consider all paths, negatives might lead to positives
- Example: [-10] → [+100] results in sum=90 if we traverse -10
- Red X vs Green checkmark

**Panel 2 - "Path Length Confusion":**
- Diagram showing edges vs nodes
- Wrong label: "3 nodes = length 3"
- Correct label: "3 nodes = 2 edges = length 2"
- Visual: 3 circles connected by 2 lines
- Formula: "length = nodes - 1"

**Panel 3 - "Combining Paths from Same Subtree":**
- Tree showing two paths from same child
- Red X: Paths overlap (creates cycle)
- Green checkmark: Paths from different children
- Code snippet showing proper child separation

- Style: Educational error illustrations
- Elements: Tree diagrams, code snippets, formulas
- Colors: Red for errors, green for corrections
- Size: 1600x900px
```

## Image Specifications

- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for multi-panel)
- Style: Clean, professional technical documentation
- Color Scheme: Blues, greens, reds with gold for highlights
- Text: Readable fonts (minimum 14pt labels, 18pt titles)
- Formulas: Use mathematical notation where appropriate
