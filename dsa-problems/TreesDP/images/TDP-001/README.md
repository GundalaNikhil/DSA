# Image Generation Prompts for TDP-001: Lowest Common Ancestor (Binary Lifting)

## Overview

This directory contains placeholder references for images used in the problem and editorial for TDP-001.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of a tree with LCA query

**Generation Prompt:**

```
Create a technical diagram showing a rooted tree with 10-12 nodes arranged in a hierarchical structure. The root node should be at the top, clearly labeled as "Root (1)". Highlight two specific nodes in the tree with different colors (e.g., blue and green), and show their Lowest Common Ancestor highlighted in a distinct color (e.g., orange or yellow). Draw arrows from both highlighted nodes pointing upward toward their common ancestor. Include node numbers (1, 2, 3, etc.) inside each circular node. Use a clean, modern graph visualization style with:
- Style: Technical tree diagram with clear hierarchy
- Elements: Circular nodes with numbers, directed edges showing parent-child relationships, highlighted nodes for query
- Colors: White/light gray nodes, blue and green for query nodes, orange for LCA, black edges
- Size: 1200x800px
- Add a legend showing "Query Node U", "Query Node V", and "LCA(U,V)"
```

### 2. real-world-scenario.png

**Purpose:** Visualization of organizational hierarchy for LCA application

**Generation Prompt:**

```
Create an infographic showing a corporate organizational chart as a tree structure. At the top, show a CEO icon/circle, with multiple levels of management below (VPs, Directors, Managers, Team Leads, Individual Contributors). Highlight two specific employees at lower levels in the org chart with glowing outlines, and highlight their common manager (the LCA) with a distinct color and a "Common Manager" label. Include small icons representing people in business attire. Style should be modern and professional:
- Style: Corporate infographic with professional business theme
- Elements: Hierarchical org chart, people icons, connecting lines, highlighted common ancestor
- Colors: Professional blues, grays, with accent colors for highlights (gold/orange for LCA)
- Size: 1200x800px
- Include subtle office/corporate background elements
- Add text labels: "Employee A", "Employee B", "Lowest Common Manager"
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step visualization of binary lifting algorithm

**Generation Prompt:**

```
Create a multi-panel diagram showing the binary lifting algorithm in action:

Panel 1: Show a tree with a 2D table beside it labeled "up[node][j]" showing binary lifting preprocessed values (2^0, 2^1, 2^2, 2^3 ancestors)

Panel 2: Show two query nodes at different depths with arrows showing the "leveling" step where the deeper node jumps up using binary steps to match the depth of the other node

Panel 3: Show both nodes at same depth with simultaneous upward binary jumps until they're one step below meeting

Panel 4: Show the final LCA result with a checkmark

Use a clean technical diagram style:
- Style: Step-by-step algorithm flowchart with tree visualizations
- Elements: Tree structure, binary lifting table, jump arrows with 2^k labels, numbered steps
- Colors: Cool blues and greens for tree, red arrows for jumps, orange for final LCA
- Size: 1600x900px (wider for multi-panel layout)
- Include step numbers (1, 2, 3, 4) and brief text descriptions
```

### 4. example-1.png

**Purpose:** Visual walkthrough of the example test case

**Generation Prompt:**

```
Create a detailed visualization of the example tree from the problem:

Show a tree with 7 nodes arranged as:
```

       1
      / \
     2   3
    / \ / \

4 5 6 7

```

Create three sub-diagrams for the three queries:
- Query 1: Highlight nodes 4 and 5, show path to LCA (node 2)
- Query 2: Highlight nodes 2 and 3, show path to LCA (node 1)
- Query 3: Highlight nodes 6 and 7, show path to LCA (node 3)

For each query, draw the paths from the query nodes to root with different line styles, and highlight where they converge (the LCA) with a star or special marking.

- Style: Clean tree diagram with multiple examples
- Elements: Binary tree structure, highlighted query nodes, path tracings, LCA markers
- Colors: Base tree in gray, query paths in distinct colors (blue/green), LCA nodes in bright orange
- Size: 1200x800px
- Include query labels: "Query 1: LCA(4,5) = 2", etc.
```

### 5. complexity-comparison.png

**Purpose:** Compare naive vs binary lifting approach complexity

**Generation Prompt:**

```
Create a side-by-side comparison chart showing:

Left side - "Naive Approach":
- Show a simple tree with a query
- Illustrate traversal from both nodes to root (many steps)
- Display: "Time: O(n) per query"
- Show example with n=1000: ~1000 operations per query

Right side - "Binary Lifting":
- Show same tree with binary jump arrows (exponential distances)
- Illustrate binary jumps (few steps)
- Display: "Time: O(log n) per query"
- Show example with n=1000: ~10 operations per query

Bottom section: Graph showing performance comparison
- X-axis: Tree size (n)
- Y-axis: Query time
- Two lines: Linear (naive) vs Logarithmic (binary lifting)

- Style: Professional comparison infographic
- Elements: Side-by-side diagrams, performance graphs, complexity annotations
- Colors: Red/orange for naive, green/blue for optimal
- Size: 1200x800px
```

### 6. common-mistakes.png

**Purpose:** Illustrate common pitfalls in LCA implementation

**Generation Prompt:**

```
Create a three-panel infographic showing common mistakes:

Panel 1 - "Mistake: Insufficient LOG value"
- Show a tree with depth 20 but LOG = 4
- Red X mark with error indication
- Show failed query attempt
- Caption: "LOG must be ≥ ceil(log2(n))"

Panel 2 - "Mistake: Not checking same level"
- Show two nodes already at same level
- Highlight unnecessary extra jumping
- Red X mark
- Caption: "Check if u == v after leveling"

Panel 3 - "Mistake: Wrong lifting condition"
- Show the binary lifting loop with incorrect condition (up[u][j] == up[v][j])
- Show how this stops too early
- Red X mark with correction arrow
- Caption: "Use != not == in final loop"

- Style: Educational infographic with clear mistake indicators
- Elements: Tree diagrams, code snippets, error marks, corrections
- Colors: Red for mistakes, green for corrections, neutral gray for tree
- Size: 1600x900px (wider for three panels)
```

## Image Specifications

- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for complex multi-panel diagrams)
- Style: Consistent with technical documentation, clean and modern
- Color Scheme: Professional tech palette (blues, greens, grays with orange/yellow accents)
- Text: Clear, readable fonts (minimum 14pt for labels, 18pt for titles)
- Diagrams: Use standard graph visualization conventions (circles for nodes, directed edges, clear labels)
