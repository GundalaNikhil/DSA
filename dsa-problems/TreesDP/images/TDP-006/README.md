# Image Generation Prompts for TDP-006: Tree DP for Vertex Cover

## Overview

This directory contains placeholder references for images used in the problem and editorial for TDP-006.

## Required Images

### 1. problem-illustration.png

**Purpose:** Visual representation of vertex cover concept

**Generation Prompt:**

```
Create a tree diagram showing:
- A tree with 7-8 nodes (circles)
- Edges connecting nodes (lines)
- Highlight a minimum vertex cover:
  * Nodes in the cover: filled with green color
  * Nodes not in cover: white/empty circles
- For each edge, show that at least one endpoint is green
- Include count: "Vertex Cover Size = 3"
- Show one edge with both endpoints highlighted (demonstrating coverage)

Add small annotation: "Every edge has ≥1 green endpoint"

- Style: Clean graph visualization
- Colors: Green for selected vertices, black edges, white for unselected
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Security camera placement scenario

**Generation Prompt:**

```
Create an isometric building floor plan:
- Hallways forming a tree structure (no cycles)
- Intersections as nodes (circles with labels)
- Some intersections have camera icons (selected for cover)
- Hallways are edges between intersections
- Visual indicators showing camera coverage:
  * Green zones for monitored hallways
  * Cameras placed at strategic intersections
- Text annotations:
  * "Minimize cameras"
  * "Every hallway monitored"
  * "Optimal placement: 4 cameras"
- Icons: Security cameras, building layout, coverage zones

- Style: Professional security system diagram
- Colors: Blue for building, green for coverage, red camera icons
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** DP recurrence visualization

**Generation Prompt:**

```
Create a 3-panel explanation:

**Panel 1 - "DP States":**
- Show a node with two states:
  * dp[u][0]: node NOT included (white circle)
  * dp[u][1]: node IS included (green circle)
- Label each state with example values

**Panel 2 - "Recurrence: Node NOT Included":**
- Parent node (white) with 3 children
- All children MUST be green (included)
- Formula: dp[u][0] = Σ dp[child][1]
- Arrows from children to parent
- Visual emphasis: "All children required!"

**Panel 3 - "Recurrence: Node IS Included":**
- Parent node (green) with 3 children
- Children can be any color (green or white)
- Formula: dp[u][1] = 1 + Σ min(dp[child][0], dp[child][1])
- Show minimum choice for each child
- Visual emphasis: "Edge already covered!"

- Style: Educational flowchart
- Colors: Green for included, white for not included
- Size: 1600x900px
```

### 4. example-walkthrough.png

**Purpose:** Step-by-step solution for Example 1

**Generation Prompt:**

```
Show tree from Example 1:
```

1
/ \
2 3

```

Create bottom-up computation:

**Step 1 - Leaves (nodes 2 and 3):**
Table for each leaf:
| State | Value |
|-------|-------|
| dp[2][0] | 0 |
| dp[2][1] | 1 |

Same for node 3.

**Step 2 - Root (node 1):**
Computation:
- dp[1][0] = dp[2][1] + dp[3][1] = 1 + 1 = 2
  (If 1 not included, both children must be)

- dp[1][1] = 1 + min(dp[2][0], dp[2][1]) + min(dp[3][0], dp[3][1])
           = 1 + min(0,1) + min(0,1)
           = 1 + 0 + 0 = 1

**Result:** min(dp[1][0], dp[1][1]) = min(2, 1) = 1

Visual showing the optimal cover: just node 1 (green)

- Style: Clean educational diagram with tables
- Colors: Green highlighting for minimum
- Size: 1200x800px
```

### 5. complexity-comparison.png

**Purpose:** Compare brute force vs DP

**Generation Prompt:**

```
Side-by-side comparison:

**Left - Brute Force O(2^n):**
- Show enumeration tree for subsets
- Binary tree showing all 2^n possibilities
- For n=10: "1024 subsets to check"
- For n=20: "1,048,576 subsets"
- Red exponential curve
- Text: "Try every subset"

**Right - DP O(n):**
- Show single tree traversal
- Bottom-up arrows
- For n=10: "10 nodes to process"
- For n=100: "100 nodes to process"
- Green linear line
- Text: "Single DFS pass"

**Bottom: Performance Graph:**
- X-axis: n (number of nodes)
- Y-axis: Operations (log scale)
- Exponential curve (red) vs Linear (green)
- Marked points at n=10, 20, 50

- Style: Technical comparison
- Colors: Red for exponential, green for linear
- Size: 1200x800px
```

### 6. common-mistakes.png

**Purpose:** Illustrate implementation errors

**Generation Prompt:**

```
Three-panel error guide:

**Panel 1 - "Single Node Edge Case":**
- Show tree with just 1 node, 0 edges
- Wrong answer: 1 (including the node)
- Correct answer: 0 (no edges to cover)
- Red X vs Green checkmark
- Code: Special case handling

**Panel 2 - "Incorrect dp[u][0] Formula":**
- Show parent (not included) with children
- Wrong formula: dp[u][0] = Σ min(dp[child][0], dp[child][1])
  (Using min when shouldn't)
- Correct formula: dp[u][0] = Σ dp[child][1]
  (All children MUST be included)
- Tree diagram showing why: edge u-child needs coverage

**Panel 3 - "Forgetting +1 in dp[u][1]":**
- Show calculation for including node
- Wrong: dp[u][1] = Σ min(...)
- Correct: dp[u][1] = 1 + Σ min(...)
- Highlight the "1" represents node u itself

- Style: Educational error illustrations
- Elements: Tree diagrams, formulas, code snippets
- Colors: Red for wrong, green for correct
- Size: 1600x900px
```

## Image Specifications

- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for multi-panel)
- Style: Clean, professional technical documentation
- Color Scheme: Green for selected/optimal, white/black for graph elements
- Text: Readable fonts (minimum 14pt labels, 18pt titles)
- Formulas: Mathematical notation for DP recurrences
