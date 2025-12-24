# Image Generation Prompts for TRI-009: Wildcard Search

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Visualize wildcard pattern matching on a trie

**Generation Prompt:**

```
Create a technical diagram showing wildcard search on a trie:
- Left: Trie structure with words "code", "coder", "codec"
- Center: Pattern "co*e" with annotation explaining wildcards
  - "co" → match literally
  - "*" → match any characters (highlighted with branching arrows)
  - "e" → match literally
- Right: Search paths highlighted in different colors:
  - Green path: co-d-e (matches "code")
  - Blue path: co-d-e-c (matches "codec")
- Show DFS exploration with dotted lines for attempted paths
- Include legend: ? = any single char, * = any sequence
- Color scheme: Blue for trie, green for matches, gray for non-matches
- Style: Technical diagram with clear path highlighting
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Unix file system search with wildcards

**Generation Prompt:**

```
Create an illustration of terminal/command-line interface:
- Terminal window showing file system search
- Command: `find . -name "*.txt"`
- File tree visualization on left showing:
  - project/
    - README.txt ✓
    - data.csv
    - notes.txt ✓
    - src/
      - main.py
      - config.txt ✓
- Pattern explanation box showing how "*" works
- Results panel highlighting matched files
- Background: Subtle Unix terminal aesthetic (dark theme)
- Include icons for file types
- Color scheme: Terminal green/black with highlighted matches
- Style: Modern terminal UI mockup
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step DFS traversal with wildcards

**Generation Prompt:**

```
Create a flowchart showing wildcard search algorithm:
Step 1: Pattern "co*e", current: root
Step 2: Match 'c' → move to 'c' node
Step 3: Match 'o' → move to 'o' node
Step 4: Encounter '*' → branching decision:
  - Branch A: Match 0 chars → try 'e' (fails, no 'e' child)
  - Branch B: Match 1 char 'd' → move to 'd', retry '*'
    - Sub-branch B1: Match 0 more chars → try 'e' (fails)
    - Sub-branch B2: At 'e' node → SUCCESS!
  - Branch C: Match other children...

Show as a decision tree:
- Nodes: Trie positions
- Edges: Character matches or wildcard decisions
- Color code: Green for successful paths, red for dead ends
- Annotations explaining each step
- Include backtracking arrows

Style: Flowchart with decision diamonds and process boxes
Size: 1600x1000px
```

### 4. example-1.png

**Purpose:** Detailed walkthrough of pattern "co\*e"

**Generation Prompt:**

```
Create step-by-step example visualization:
Top: Input trie with words ["code", "coder", "codec"]
Pattern: "co*e"

Breakdown in panels:
Panel 1: Match "co"
  - Show path root→c→o (solid green line)
  - Status: "Matched 'co'"

Panel 2: Encounter '*'
  - Show '*' can match: 0 chars, 1 char, 2 chars, ...
  - Branching arrows showing possibilities

Panel 3: Try '*' = "d"
  - Path: c→o→d
  - Next char needed: 'e'
  - Check children of 'd': found 'e'!
  - Result: "code" matches ✓

Panel 4: Try '*' = "dec"
  - Path: c→o→d→e→c
  - Next char needed: 'e'
  - No 'e' child from 'c'
  - Result: This path fails ✗

Bottom: Summary showing all matches found

Style: Multi-panel tutorial with clear step labels
Size: 1200x1200px
```

### 5. example-2.png

**Purpose:** Visualization of '?' wildcard

**Generation Prompt:**

```
Create example for pattern "hel?":
- Trie with words: "hello", "help", "helper", "helpful"
- Pattern breakdown:
  - "hel" → match literally (path shown)
  - "?" → try all children from 'l' node
    - Try 'l' → "hell" (not a word end) ✗
    - Try 'p' → "help" (word end) ✓
    - Try 'p' then continue → "helper" (no, pattern ends)

Show branching at '?' position with arrows to all possible children
Highlight successful match with green checkmark
Show failed attempts with red X

Include side-by-side comparison:
- Left: Pattern with '?'
- Right: All possible single-character replacements

Style: Educational diagram with annotations
Size: 1200x800px
```

### 6. complexity-comparison.png

**Purpose:** Performance comparison of wildcard search approaches

**Generation Prompt:**

```
Create performance comparison chart:
Top section: "Approach Comparison"
- Column 1: "Naive (Extract all words)"
  - Icon: List of all words being checked one by one
  - Complexity: O(n × m)
  - Example: 10K words × 20 chars = 200K ops

- Column 2: "Optimized (Trie DFS with pruning)"
  - Icon: Tree with highlighted paths, crossed-out branches
  - Complexity: O(nodes visited)
  - Example: Only 500 nodes visited (95% pruned!)

Bottom section: "Pruning Benefits"
- Graph showing nodes visited vs pattern specificity
  - X-axis: Pattern specificity (specific → generic)
  - Y-axis: Nodes visited
  - Line 1: "Specific pattern (abc*)" - visits few nodes
  - Line 2: "Generic pattern (*)" - visits all nodes

Include examples:
- Pattern "xyz*" on trie with no "xyz" words → Early termination!
- Pattern "*" → Must check all nodes

Color scheme: Performance visualization (green, yellow, red)
Style: Infographic with charts and comparisons
Size: 1200x800px
```
