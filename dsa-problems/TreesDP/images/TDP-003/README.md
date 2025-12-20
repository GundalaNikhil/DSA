# Image Generation Prompts for TDP-003: Subtree Sum and Size

## Overview

This directory contains placeholder references for images used in the problem and editorial for TDP-003.

## Required Images

### 1. problem-illustration.png

**Purpose:** Visual representation of subtree sums calculation

**Generation Prompt:**

```
Create a technical tree diagram showing a rooted tree with 7-8 nodes. Each node should display two values: the node's own value (in the center) and the subtree sum (in a box below or beside it). Use different colors to distinguish:
- Node value (inside the circle, e.g., in blue)
- Subtree sum (in a colored box, e.g., in green)
Highlight one specific node and visually show all nodes in its subtree with a light background or dotted boundary. Include arrows pointing to the subtree.
- Style: Clean technical diagram
- Elements: Tree structure, node values, subtree sum annotations, highlighted subtree region
- Colors: Blue for node values, green for subtree sums, light yellow background for highlighted subtree
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Corporate budget hierarchy visualization

**Generation Prompt:**

```
Create an organizational chart infographic showing a corporate hierarchy with budget allocations:
- CEO at top (root) with total budget
- Departments as nodes (Engineering, Sales, Marketing, etc.)
- Each department shows its own budget and total budget including sub-departments
- Use money/dollar icons
- Show calculation: "Engineering Division Total = Engineering Dept + R&D + QA"
- Style: Professional corporate infographic
- Elements: Organizational boxes, budget numbers, calculation callouts
- Colors: Corporate blues and greens, gold for money symbols
- Size: 1200x800px
- Include icons for different departments
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step DFS subtree sum calculation

**Generation Prompt:**

```
Create a multi-panel diagram showing DFS bottom-up computation:

Panel 1 - "Leaf Nodes":
- Show leaf nodes with subtree_sum = node_value
- Label: "Base case: sum = value"

Panel 2 - "Parent Computation":
- Show parent node with two children
- Arrows from children to parent
- Calculation: parent_sum = parent_value + child1_sum + child2_sum
- Label: "Aggregate from children"

Panel 3 - "Propagate Upward":
- Show values propagating up the tree
- Highlight the bottom-up flow with colored arrows
- Label: "Bottom-up DP"

Panel 4 - "Complete Tree":
- Final tree with all subtree sums computed
- Checkmark indicating completion

- Style: Educational flowchart
- Elements: Tree diagrams, computation arrows, formulas
- Colors: Progressive colors (green → blue → purple for steps)
- Size: 1600x900px
```

### 4. example-1.png

**Purpose:** Walkthrough of the simple 3-node example

**Generation Prompt:**

```
Create a clear visualization of the example:

Show tree structure:
```

    1 (val=1)

/ \
 2 3
(val=2) (val=3)

```

Below the tree, show computation table:

| Node | Own Value | Children Sums | Subtree Sum |
|------|-----------|---------------|-------------|
| 2    | 2         | 0             | 2           |
| 3    | 3         | 0             | 3           |
| 1    | 1         | 2 + 3 = 5     | 1 + 5 = 6   |

Use arrows to show the computation flow from leaves to root.

- Style: Clean educational diagram
- Elements: Tree, computation table, arrows
- Colors: Neutral with highlights for calculations
- Size: 1200x800px
```

### 5. complexity-comparison.png

**Purpose:** Compare naive O(n²) vs DP O(n) approach

**Generation Prompt:**

```
Create a side-by-side comparison:

Left - "Naive Approach O(n²)":
- Show tree with multiple DFS traversals (one from each node)
- Many overlapping arrows indicating redundant work
- Text: "Separate DFS for each node"
- Example: n=1000 → ~500,000 operations

Right - "DP Approach O(n)":
- Show single DFS with values being computed bottom-up
- Clean, single-pass arrows
- Text: "Single DFS, aggregate from children"
- Example: n=1000 → 1,000 operations

Bottom: Performance graph
- X-axis: Number of nodes
- Y-axis: Operations
- Two curves: Quadratic (red) vs Linear (green)

- Style: Technical comparison
- Colors: Red for naive, green for optimal
- Size: 1200x800px
```

### 6. common-mistakes.png

**Purpose:** Illustrate common implementation errors

**Generation Prompt:**

```
Create a three-panel error guide:

Panel 1 - "Mistake: Forgetting Node's Own Value":
- Show incorrect code: subtree_sum = sum(children)
- Red X mark
- Show correct: subtree_sum = node_value + sum(children)
- Example showing the difference

Panel 2 - "Mistake: Integer Overflow":
- Show code with int type
- Example with large values causing overflow
- Red X mark
- Correct solution: use long/long long
- Show max possible value calculation

Panel 3 - "Mistake: Visiting Parent as Child":
- Show tree with bidirectional edges
- Infinite recursion loop illustration
- Red X mark
- Correct: if (child == parent) continue;

- Style: Educational error illustrations
- Elements: Code snippets, tree diagrams, error markers
- Colors: Red for errors, green for corrections
- Size: 1600x900px
```

## Image Specifications

- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for multi-panel diagrams)
- Style: Clean, professional technical documentation
- Color Scheme: Blues, greens, grays with accent colors for highlights
- Text: Readable fonts (minimum 14pt labels, 18pt titles)
- Diagrams: Standard tree visualization with clear node labels
