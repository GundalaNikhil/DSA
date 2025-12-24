# Image Generation Prompts for TRI-008: Dictionary Compression Size

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of trie node counting

**Generation Prompt:**

```
Create a technical diagram showing trie node counting:
- Left side: List of words: "cat", "car", "card", "dog"
- Center: Trie structure with numbered nodes:
  - Node 1: root (circle at top)
  - Node 2: 'c' branch
  - Node 3: 'a' under 'c'
  - Node 4: 't' leaf (word end marker)
  - Node 5: 'r' branch from 'a'
  - Node 6: 'd' branch from root
  - Node 7: 'o' under 'd'
  - (additional nodes for 'g' and 'd' from 'r')
- Each node clearly numbered and labeled
- Right side: Counter showing "Total Nodes: 7"
- Use different colors for internal nodes vs leaf nodes
- Color scheme: Blue for nodes, green for word-end markers
- Style: Clean technical diagram with clear labels
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Visualization of mobile keyboard dictionary optimization

**Generation Prompt:**

```
Create an illustration showing mobile keyboard memory optimization:
- Top: Mobile phone screen displaying a keyboard interface
- Left panel: "Without Trie" showing:
  - List of words stored separately: "hello", "help", "helper"
  - Memory blocks: 5+4+6 = 15 units
  - Icon: Inefficient storage with gaps
- Right panel: "With Trie" showing:
  - Trie structure sharing "hel" prefix
  - Memory blocks: 1(root)+3(hel)+2(lo)+1(p)+2(er) = 9 units
  - Icon: Efficient compact storage
- Bottom: Savings calculation: "40% memory saved!"
- Background: Mobile device outline, memory chip icons
- Color scheme: Modern mobile UI (blue, white, green)
- Style: Infographic with comparison panels
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step node counting during trie construction

**Generation Prompt:**

```
Create a step-by-step trie construction visualization:
1. Initial: root only, count = 1
2. Insert "a": root→a, count = 2
3. Insert "ab": root→a→b (reuse 'a'), count = 3
4. Insert "abc": root→a→b→c (reuse 'a','b'), count = 4

Show each step as a separate panel:
- Panel 1: Just root node, counter: 1
- Panel 2: Root with 'a' child, counter: 2, annotation "New node created"
- Panel 3: Root→a→b, counter: 3, annotation "'a' reused, 'b' created"
- Panel 4: Root→a→b→c, counter: 4, annotation "'a','b' reused, 'c' created"

Visual elements:
- Nodes that are reused highlighted in green
- New nodes highlighted in orange
- Running counter displayed prominently
- Arrows showing node creation vs reuse

Style: Sequential tutorial with clear step labels
Color scheme: Educational (blue, green, orange)
Size: 1600x900px
```

### 4. example-1.png

**Purpose:** Detailed walkthrough of example 1

**Generation Prompt:**

```
Create a detailed example visualization for ["a", "ab", "abc"]:
- Top: Input words displayed as cards: "a", "ab", "abc"
- Middle: Trie construction shown vertically:
```

       root (1)
         |
        'a' (2) ← word "a" ends
         |
        'b' (3) ← word "ab" ends
         |
        'c' (4) ← word "abc" ends

```
- Each node shows its number in a circle
- Word-end markers shown as green checkmarks
- Bottom: Detailed node breakdown table:
| Node # | Character | Created By | Purpose |
|--------|-----------|------------|---------|
| 1      | (root)    | Initial    | Root    |
| 2      | a         | "a"        | End: "a"|
| 3      | b         | "ab"       | End: "ab"|
| 4      | c         | "abc"      | End: "abc"|
- Final answer highlighted: "Total: 4 nodes"
- Style: Educational breakdown with table
- Size: 1000x1200px
```

### 5. example-2.png

**Purpose:** Visualization of branching trie with multiple paths

**Generation Prompt:**

```
Create a visualization for ["cat", "car", "card", "dog"]:
- Top: Input words as cards
- Middle: Tree-like trie structure:
```

           root (1)
           /    \
         c(2)   d(6)
          |      |
         a(3)   o(7)
         / \     |
       t(4) r(5) g(8)
            |
           d(9)

```
- Each node numbered in sequence of creation
- Branching points highlighted (node 3 has two children)
- Word-end markers at appropriate nodes
- Bottom: Explanation:
- "Nodes 1-5: Built from 'cat', 'car'"
- "Node 6-8: New branch for 'dog'"
- "Node 9: Extension for 'card'"
- "Total: 9 nodes" (adjust based on actual count)
- Color coding: Different colors for different word paths
- Style: Tree diagram with clear annotations
- Size: 1200x1000px
```

### 6. complexity-comparison.png

**Purpose:** Memory efficiency comparison

**Generation Prompt:**

```
Create a memory efficiency comparison chart:
Top section: "Storage Comparison"
- Bar chart comparing three approaches:
  1. "Separate Storage": Each word stored individually
     - Example: 100K words × 10 chars = 1M units
     - Red bar (highest)
  2. "Prefix Array": Sorted array with prefix sharing
     - Example: ~600K units
     - Yellow bar (medium)
  3. "Trie Structure": Full prefix sharing
     - Example: ~400K units
     - Green bar (lowest)

Bottom section: "Trie Benefits"
- Icon 1: Fast prefix search O(L)
- Icon 2: Memory efficient (40-60% savings)
- Icon 3: Natural autocomplete support
- Icon 4: Easy insertion/deletion

Include graph showing node count growth:
- X-axis: Number of words
- Y-axis: Node count
- Show sublinear growth due to prefix sharing

Color scheme: Data visualization (red, yellow, green)
Style: Infographic with charts and icons
Size: 1200x800px
```
