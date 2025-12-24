# Image Generation Prompts for TRI-016: Trie-Based Kth Smallest String

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of finding k-th smallest string

**Generation Prompt:**

```
Create a technical diagram showing lexicographic ordering:
- Top: Input strings displayed in input order: ["b", "a", "aa"]
- Middle: Sorted strings in lexicographic order with position numbers:
  - Position 1: "a" (gray)
  - Position 2: "aa" (highlighted in green with gold star)
  - Position 3: "b" (gray)
- Bottom: Trie structure showing the strings:
```

       root
       / \
      a   b
      |   (END)
      a
     (END)

```
- DFS traversal arrows showing order: a → aa → b
- Result box: k=2 → "aa"
- Style: Clean educational diagram
- Color scheme: Green for target, gray for others, blue trie structure
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Visualization of database pagination application

**Generation Prompt:**

```
Create an illustration of database query interface:
- Main screen: Database management console
- Display showing sorted records with pagination:
  - Title: "Dictionary Database - 500,000 Words"
  - Pagination controls: "Page 1000 of 5000" (showing words 100,000-100,100)
  - Current view showing:
    - Word 99,998: "interrelationship"
    - Word 99,999: "interrogate"
    - Word 100,000: "interrogation" ← highlighted "You are here"
    - Word 100,001: "interrupt"
    - Word 100,002: "intersection"
- Side panel: Trie structure visualization showing skip-counting
  - "Skipped 99,999 words efficiently!"
  - "Direct jump to target word"
- Bottom: Performance metrics:
  - "Query time: 0.003s"
  - "No full sort required!"
- Style: Modern database interface
- Color scheme: Professional blue/gray with green highlights
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step DFS with skip counting

**Generation Prompt:**

```
Create a detailed algorithm flow:

Input: words=["b", "a", "aa", "ab", "ba"], k=3

Step 1 - Build Trie with Counts:
```

         root
        /    \
      a(3)   b(2)
      / \     |

a(1) b(1) a(1)
END END END
END

```
(Numbers in parentheses = count of strings in subtree)

Step 2 - DFS Traversal for k=3:

Start: k=3

Node 'a' (count=3):
- Subtree has 3 strings
- 3 >= 3, so answer is in this subtree
- Enter 'a' subtree

At 'a' (END):
- Found string "a", position 1
- k -= 1, k=2 now
- Continue in subtree

Check child 'a' (count=1):
- 1 < 2, skip this subtree
- k -= 1, k=1 now

Check child 'b' (count=1):
- 1 >= 1, enter

At 'ab' (END):
- Found string "ab", position 3 (total)
- k -= 1, k=0
- Return "ab" ✓

Visualization with:
- Numbered steps
- Skip arrows showing subtrees bypassed
- Counter showing k decreasing
- Green path to answer
- Style: Flowchart with trie navigation
- Size: 1600x1200px
```

### 4. example-1.png

**Purpose:** Detailed example walkthrough

**Generation Prompt:**

```
Create a step-by-step example:

Title: "Finding 2nd Smallest String"

Input: ["b", "a", "aa"], k=2

Step 1 - Input Strings (unordered):
- "b"
- "a"
- "aa"

Step 2 - Lexicographic Sorting:
Show comparison process:
- "a" vs "aa": "a" comes first (prefix)
- "a" vs "b": "a" < "b"
- "aa" vs "b": "aa" < "b"

Result: ["a", "aa", "b"]

Step 3 - Position Numbering:
- Position 1: "a"
- Position 2: "aa" ← k=2 (highlighted)
- Position 3: "b"

Step 4 - Trie Representation:
```

      root
      / \
     a   b
     |
     a

```
With DFS order annotations

Bottom: Large result box showing "aa"
- Style: Educational step-by-step with clear visual progression
- Color scheme: Green for answer, numbered steps
- Size: 1200x1000px
```

### 5. skip-counting-optimization.png

**Purpose:** Explain skip-counting technique

**Generation Prompt:**

```
Create a comparison diagram:

Left Panel - "Naive Approach":
- Show traversing every string sequentially
- Strings 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...
- To find k=10, must visit all 10 strings
- Arrows showing linear path through all
- Label: "O(k) string examinations"

Right Panel - "Trie Skip-Counting":
- Show trie with subtree counts
- Example: Finding k=10 in trie
```

       root
      /    \
    a(5)   b(8)

```
- Decision: "Skip 'a' subtree (5 < 10)"
- Jump to 'b' subtree, now looking for k-5=5
- Label: "O(log n) subtree skips + O(L) final path"

Center: Large "VS" with arrow showing improvement

Bottom: Performance Table:
| k Value | Naive Visits | Trie Subtree Checks |
|---------|--------------|---------------------|
| 100     | 100          | ~10                 |
| 1,000   | 1,000        | ~15                 |
| 10,000  | 10,000       | ~20                 |

Highlight: "Skip entire branches using counts!"
- Style: Side-by-side comparison with metrics
- Color scheme: Red for naive, green for optimal
- Size: 1400x900px
```

### 6. lexicographic-order-trie.png

**Purpose:** Show how trie naturally maintains lexicographic order

**Generation Prompt:**

```
Create an educational diagram:

Title: "Trie Structure = Natural Lexicographic Order"

Main visualization showing strings: ["a", "aa", "ab", "b", "ba"]

Top: Alphabetical order if sorted:
1. "a"
2. "aa"
3. "ab"
4. "b"
5. "ba"

Middle: Trie structure:
```

         root
        /    \
       a      b
      / \     |
     a   b    a

(END) (END)(END)
(END)

```

Bottom: DFS Traversal Order:
- Show DFS path with numbered steps:
  1. Visit root → 'a' (left child first)
  2. 'a' is END → output "a"
  3. Visit 'a's children: 'a' first
  4. 'aa' is END → output "aa"
  5. Backtrack, visit 'b' child
  6. 'ab' is END → output "ab"
  7. Backtrack to root, visit 'b'
  8. 'b' is END → output "b"
  9. Visit 'b's child 'a'
  10. 'ba' is END → output "ba"

Annotations:
- "Left-to-right traversal = alphabetical order"
- "Children visited in sorted order"
- "DFS yields strings in lexicographic sequence"

- Style: Educational with clear step-by-step DFS
- Color scheme: Blue for tree, numbered steps in different colors
- Size: 1400x1000px
```

## Image Specifications

- Format: PNG with transparency where applicable
- Resolution: High-DPI (2x) for Retina displays
- Compression: Optimized for web delivery
- Accessibility: Include alt text descriptions

## Notes

These prompts are designed for AI image generation tools or as briefs for graphic designers. Focus on demonstrating skip-counting optimization and lexicographic ordering through trie structure.
