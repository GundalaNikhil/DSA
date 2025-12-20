# Image Generation Prompts for TRI-010: Trie-Based Spell Checker

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Visualize spell checking with edit distance 1

**Generation Prompt:**

```
Create a diagram showing spell checking concept:
- Center: Query word "teh" in a text box with red squiggly underline
- Around it, three panels showing edit operations:
  - Panel 1: "Substitution" - "teh" → "the" (e↔h highlighted)
  - Panel 2: "Insertion" - "teh" → "tech" (insert 'c')
  - Panel 3: "Deletion" - "teh" → "te" (remove 'h')
- Trie structure in background showing dictionary words
- Green checkmark next to "the" indicating it's in dictionary
- Label: "Edit Distance = 1"
- Color scheme: Educational with red for error, green for correction
- Style: Clean diagram with arrows showing transformations
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Word processor spell checking interface

**Generation Prompt:**

```
Create a word processor interface mockup:
- Document editor showing typed text with misspellings
- Red squiggly underlines under "teh", "recieve", "occured"
- Right-click context menu showing:
  - "Spelling Suggestions:"
  - "the" (highlighted)
  - "tea"
  - "ten"
- Small panel showing "Edit Distance: 1" for each suggestion
- Background: Typical word processor interface (MS Word style)
- Icons: Spelling/grammar check button in toolbar
- Bottom: Statistics showing "Real-time check: 1000 words/sec"
- Color scheme: Professional office app (blue, white, gray)
- Style: Modern application UI mockup
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** DFS traversal through trie with edit budget

**Generation Prompt:**

```
Create algorithm flow visualization:
Top: Query word "cats" searching in trie with ["cat", "bat", "car"]

Step-by-step DFS with edit budget:
Panel 1: Start at root, budget = 0
Panel 2: Match 'c' → move to 'c' node, budget = 0
Panel 3: Match 'a' → move to 'a' node, budget = 0
Panel 4: Match 't' → move to 't' node, budget = 0
Panel 5: Query has 's' left, at word end "cat"
  - Try insertion: Add 's' → budget = 1 ✓
  - Result: "cat" + "s" = "cats" at distance 1!

Also show failed paths in gray:
- "bat": Different first char, would need substitution + more
- "car": Would need substitution 't'→'r' + insertion 's' = 2 edits ✗

Visual elements:
- Green arrows for successful path
- Red X for pruned branches (budget exceeded)
- Counter showing "Edits used: 0 → 1"
- Budget meter: [●○] (1/1 used)

Style: Flowchart with decision nodes and paths
Size: 1600x1000px
```

### 4. example-1.png

**Purpose:** Detailed example of "cats" matching "cat"

**Generation Prompt:**

```
Create detailed example breakdown:
Top: Trie with words ["cat", "bat"]
Query: "cats"

Comparison table:
| Dict Word | Operation | Steps | Distance | Match? |
|-----------|-----------|-------|----------|--------|
| cat       | Insert 's'| cat → cats | 1   | ✓ YES  |
| bat       | Sub b→c, Insert s | bat → cat → cats | 2 | ✗ NO |

Visual trie showing:
- Path c→a→t highlighted
- Dotted extension showing virtual 's' node
- Annotation: "Insert 's' at end = 1 edit"

Bottom: Summary
- "cats" matches "cat" with edit distance 1
- Result: true

Style: Educational breakdown with table and diagram
Size: 1200x900px
```

### 5. edit-operations.png

**Purpose:** Comprehensive visualization of all three edit types

**Generation Prompt:**

```
Create a three-panel educational diagram:

Panel 1: INSERTION
- "cat" → "cats"
- Arrow showing 's' being added
- Trie path: c→a→t→(s)
- Label: "Insert character at any position"
- Examples: cat→acat, cat→caat, cat→crat, cat→cats

Panel 2: DELETION
- "cats" → "cat"
- Arrow showing 's' being removed
- Trie path: c→a→t→s with 's' crossed out
- Label: "Delete character from any position"
- Examples: cats→ats, cats→cts, cats→cas, cats→cat

Panel 3: SUBSTITUTION
- "cat" → "car"
- Arrow showing 't'→'r' replacement highlighted
- Trie paths: c→a→t and c→a→r (branching)
- Label: "Replace character at any position"
- Examples: cat→bat, cat→cbt, cat→car

Bottom: "Total possibilities ≈ 53L where L = word length"

Color scheme: Blue for original, orange for operation, green for result
Style: Educational infographic with clear examples
Size: 1200x1000px
```

### 6. complexity-comparison.png

**Purpose:** Compare naive candidate generation vs DFS with budget

**Generation Prompt:**

```
Create performance comparison:

Left panel: "Naive Approach"
- Generate all candidates at distance 1
- For "hello" (length 5):
  - Insertions: 6 positions × 26 letters = 156
  - Deletions: 5 positions = 5
  - Substitutions: 5 positions × 25 letters = 125
  - Total: 286 candidates
- Icon: Long list of candidate strings
- Then: Check each in trie (286 lookups)
- Complexity: O(L² × 26L) = O(L³)

Right panel: "Optimal DFS with Budget"
- Explore trie with edit budget = 1
- Prune branches when budget exceeded
- For "hello" against 10K word trie:
  - Average nodes visited: ~50-200
  - Early termination on match
- Icon: Tree with many crossed-out branches
- Complexity: O(N) worst case, O(L) average with pruning
- N = trie nodes

Bottom: Performance graph
- X-axis: Dictionary size
- Y-axis: Time per query (ms)
- Two lines: Naive (flat, high) vs Optimal (low, slowly increasing)
- Annotation: "100× faster for large dictionaries!"

Color scheme: Red for naive, green for optimal
Style: Technical infographic with charts
Size: 1200x800px
```
