# Image Generation Prompts for TDP-004: Rerooting for Weighted Distance Variance

## Overview

This directory contains placeholder references for images used in the problem and editorial for TDP-004.

## Required Images

### 1. problem-illustration.png

**Purpose:** Visual representation of weighted distance squared calculation

**Generation Prompt:**

```
Create a technical diagram showing a small tree (5-6 nodes) with each node having:
- Node number (in circle)
- Weight value (below node, in a box, e.g., "w=20")
For one chosen root node (highlighted in blue):
- Show calculation for 2-3 other nodes
- Display distance (number of edges)
- Show formula: w[j] × dist² for each node
- Sum total at bottom: "Total Cost = ..."

Example annotation for one node:
"Node 4: w=50, dist=2 → 50 × 2² = 200"

- Style: Clean technical diagram with mathematical annotations
- Colors: Blue for selected root, green for weights, red for distances
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Telecom network optimization visualization

**Generation Prompt:**

```
Create an infographic showing a network topology:
- Cities as nodes (different sizes representing population weights)
- Network connections as edges
- Central hub (highlighted) with signal waves radiating outward
- Show latency formula: "Latency ∝ Distance²"
- Include annotations:
  * "Signal Degradation increases with distance²"
  * "Population weight × latency cost"
  * "Optimal hub minimizes total weighted latency"
- Icons: Cell towers, fiber optic cables, city skylines
- Style: Professional network diagram
- Colors: Corporate blues, technology greens, warning reds for high latency
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Rerooting DP technique step-by-step

**Generation Prompt:**

```
Create a 4-panel progression diagram:

Panel 1 - "Initial Root (Node 1)":
- Tree rooted at node 1
- Show down[v] values computed for all nodes
- Label: "Phase 1: Compute downward DP"

Panel 2 - "Reroot to Node 2":
- Highlight edge 1→2
- Show transition: nodes in subtree of 2 get distance -1, others +1
- Formula displayed: "cost_change = effect of distance shift"

Panel 3 - "Propagate Upward Values":
- Show up[v] values being computed
- Arrows showing parent-to-child propagation
- Label: "Phase 2: Compute upward DP"

Panel 4 - "Complete Solution":
- All nodes with their total costs: down[i] + up[i]
- Minimum cost node highlighted in gold
- Checkmark for solution

- Style: Educational flowchart with clear transitions
- Colors: Phase 1 (blue), Phase 2 (green), Solution (gold)
- Size: 1600x900px
```

### 4. example-walkthrough.png

**Purpose:** Detailed walkthrough of Example 1

**Generation Prompt:**

```
Create a comprehensive example visualization:

Tree: 1 -- 2 -- 3 with weights [1, 2, 1]

Show three cost calculations side-by-side:

**Root = 1:**
Table:
| Node | Weight | Distance | w × d² |
|------|--------|----------|--------|
| 1    | 1      | 0        | 0      |
| 2    | 2      | 1        | 2      |
| 3    | 1      | 2        | 4      |
Total: 6

**Root = 2:** (highlighted as optimal)
Table showing total = 2
Green checkmark

**Root = 3:**
Table showing total = 6

- Style: Clean comparison table with highlighting
- Colors: Green for optimal, neutral for others
- Size: 1200x800px
```

### 5. complexity-comparison.png

**Purpose:** Compare naive vs rerooting approaches

**Generation Prompt:**

```
Create a side-by-side comparison:

**Left Panel - Naive O(n²):**
- Show tree with multiple BFS/DFS traversals
- Each root has its own full traversal (illustrated with different colored paths)
- Text: "Compute cost for each root independently"
- Example: n=1000 → 1,000,000 operations
- Red complexity label

**Right Panel - Rerooting O(n):**
- Show single downward pass (blue arrows)
- Show single upward pass (green arrows)
- Text: "Compute once, propagate changes"
- Example: n=1000 → 2,000 operations
- Green complexity label

**Bottom: Performance Graph:**
- X-axis: Number of nodes (0 to 10,000)
- Y-axis: Operations (logarithmic scale)
- Red curve (quadratic) vs Green line (linear)
- Highlight performance difference at n=1000 and n=10000

- Style: Technical performance comparison
- Colors: Red for naive, green for optimal
- Size: 1200x800px
```

### 6. common-mistakes.png

**Purpose:** Illustrate implementation pitfalls

**Generation Prompt:**

```
Create a three-panel error guide:

**Panel 1 - "Integer Overflow":**
- Show calculation: 10⁶ (weight) × 2000² (distance)
- Result: 4 × 10¹² (overflows int)
- Red X with "int" type
- Green checkmark with "long long" type
- Code snippet showing proper type usage

**Panel 2 - "Incorrect Transition Formula":**
- Show wrong formula: up[v] = up[parent] + down[parent]
- Red X mark
- Correct formula: up[v] = up[parent] + adjusted_down[parent]
- Explanation: "Must subtract child's contribution"
- Tree diagram showing the error

**Panel 3 - "Bidirectional Edge Confusion":**
- Show graph with edges added both ways
- DFS recursion going back to parent (infinite loop)
- Red X mark
- Correct code: `if (v == parent) continue;`
- Green checkmark

- Style: Educational error illustrations with code
- Elements: Code snippets, formulas, tree diagrams
- Colors: Red for errors, green for fixes
- Size: 1600x900px
```

## Image Specifications

- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for multi-panel)
- Style: Clean, professional technical documentation
- Color Scheme: Blues, greens, reds for semantic highlighting
- Text: Readable fonts (minimum 14pt labels, 18pt titles)
- Mathematical notation: Use proper symbols (×, ², Σ)
