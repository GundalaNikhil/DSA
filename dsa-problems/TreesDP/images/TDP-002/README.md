# Image Generation Prompts for TDP-002: Tree Diameter DP

## Overview

This directory contains placeholder references for images used in the problem and editorial for TDP-002.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of tree diameter concept

**Generation Prompt:**

```
Create a technical diagram showing an undirected tree with 12-15 nodes. Highlight the longest path (diameter) between two specific nodes with a thick, bright colored line (orange or yellow). Show other shorter paths in lighter gray to contrast. Label the diameter path with "Diameter = X" where X is the length. Include node numbers in circles. Show the tree structure clearly with:
- Style: Clean technical tree diagram
- Elements: Circular nodes with numbers, undirected edges, highlighted diameter path
- Colors: Gray nodes, black edges, bright orange/yellow for diameter path
- Size: 1200x800px
- Add arrows or markers at the two endpoints of the diameter
```

### 2. real-world-scenario.png

**Purpose:** Visualization of data center network topology

**Generation Prompt:**

```
Create an infographic showing a data center network with servers connected in a tree topology. Show multiple server racks connected via network switches in a hierarchical structure. Highlight the longest network path (diameter) between two servers with a glowing line. Include:
- Server icons/racks at the leaf nodes
- Network switches at internal nodes
- Network cables as edges
- Highlight the critical path with labels showing "Max Latency Path" or "Network Diameter"
- Style: Modern tech infographic with isometric or 2.5D view
- Colors: Tech blues and grays, bright orange for critical path
- Size: 1200x800px
- Add latency numbers on edges (e.g., "5ms" per hop)
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step visualization of diameter calculation using DFS

**Generation Prompt:**

```
Create a multi-panel diagram showing the diameter DP algorithm:

Panel 1 - "DFS from Root":
- Show tree with DFS traversal order
- For each node, show max depth values from children
- Label: "Computing max depths"

Panel 2 - "Track Two Maximum Depths":
- Show a specific node with multiple children
- Highlight the two deepest subtrees
- Show max1 and max2 labels
- Label: "At each node: max1 + max2"

Panel 3 - "Update Global Diameter":
- Show comparison of different (max1 + max2) values
- Highlight the maximum value found
- Label: "Diameter = max(all max1 + max2)"

Panel 4 - "Result":
- Show final diameter path highlighted on the tree
- Checkmark and "Diameter = X" label

- Style: Educational flowchart with code snippets
- Elements: Tree diagrams, DP values, arrows showing computation flow
- Colors: Progressive colors (blue → green → yellow for steps)
- Size: 1600x900px (wide for multi-panel)
```

### 4. example-1.png

**Purpose:** Visual walkthrough of the linear path example

**Generation Prompt:**

```
Create a clear visualization of the example:

Show a tree that is a straight line: 1 - 2 - 3 - 4

Highlight the diameter path from node 1 to node 4 with a thick colored line.

Below the tree, show a table of all pairwise distances:
- 1 to 2: 1
- 1 to 3: 2
- 1 to 4: 3 ✓ (Maximum)
- 2 to 3: 1
- 2 to 4: 2
- 3 to 4: 1

Use checkmark to indicate the maximum distance.

- Style: Clean educational diagram
- Elements: Linear tree, distance table, highlighted maximum
- Colors: Neutral gray for tree, green for maximum path
- Size: 1200x800px
```

### 5. complexity-comparison.png

**Purpose:** Compare naive O(n²) vs optimal O(n) approach

**Generation Prompt:**

```
Create a comparison chart:

Left Side - "Naive Approach O(n²)":
- Show tree with all pairwise arrows (many crossing lines)
- Visual complexity indication
- Text: "Try all pairs"
- Example: n=1000 → ~500,000 operations

Right Side - "DP Approach O(n)":
- Show single DFS traversal with clean arrows
- Much simpler visual
- Text: "Single DFS with DP"
- Example: n=1000 → 1,000 operations

Bottom: Performance graph
- X-axis: Tree size
- Y-axis: Operations
- Two curves: Quadratic (red) vs Linear (green)
- Mark the difference at n=100,000

- Style: Technical comparison infographic
- Colors: Red for naive, green for optimal
- Size: 1200x800px
```

### 6. common-mistakes.png

**Purpose:** Illustrate common errors in diameter calculation

**Generation Prompt:**

```
Create a three-panel error illustration:

Panel 1 - "Mistake: Only Track One Maximum"
- Show tree with node having multiple children
- Wrong code: diameter = max(diameter, max1)
- Red X mark
- Show how this misses the diameter
- Caption: "Must track TWO maximum depths"

Panel 2 - "Mistake: Return Wrong Value"
- Show DFS function returning max1 + max2
- Red X mark
- Show how parent's calculation breaks
- Caption: "Return max1 + 1, not max1 + max2"

Panel 3 - "Mistake: Forget to Check All Nodes"
- Show partially traversed tree
- Red X mark
- Caption: "Diameter might not pass through root"

- Style: Educational error illustrations
- Elements: Code snippets, tree diagrams, error markers
- Colors: Red for errors, green for corrections
- Size: 1600x900px (wide for panels)
```

## Image Specifications

- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for complex multi-panel diagrams)
- Style: Consistent with technical documentation, clean and modern
- Color Scheme: Professional (blues, greens, grays with orange/yellow accents)
- Text: Clear, readable fonts (minimum 14pt for labels, 18pt for titles)
- Diagrams: Use standard graph visualization (circles for nodes, lines for edges)
