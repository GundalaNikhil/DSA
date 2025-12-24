# Image Generation Prompts for TRI-013: Shortest Absent Binary String of Length L

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of finding missing binary strings

**Generation Prompt:**

```
Create a technical diagram showing binary string search:
- Left side: A complete binary tree of depth 2 showing all possible strings
  - Level 0: root
  - Level 1: branches '0' and '1'
  - Level 2: leaves "00", "01", "10", "11"
- Center: Highlight which strings are present in the set
  - "00" - marked with green checkmark (present)
  - "01" - marked with green checkmark (present)
  - "10" - marked with red question mark (missing)
  - "11" - marked with red question mark (missing)
- Right side: Result box showing "10" with annotation "Lexicographically smallest missing"
- Include arrows showing lexicographic traversal order: 00 → 01 → 10 → 11
- Style: Clean binary tree visualization with color coding
- Color scheme: Technical blue/white, green for present, red for missing
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Visualization of binary code generation application

**Generation Prompt:**

```
Create an illustration of firmware/IoT device management system:
- Main display: Computer screen showing device ID assignment interface
- Display showing:
  - Title: "Device ID Manager - 8-bit Binary Codes"
  - Table with columns: Device Name | Binary ID | Status
  - Rows showing assigned IDs:
    - "Sensor-A" | "00000000" | Assigned ✓
    - "Sensor-B" | "00000001" | Assigned ✓
    - "Sensor-C" | "00000011" | Assigned ✓
  - Next available: "00000010" (highlighted in green)
- Side panel: Binary trie visualization showing assigned codes
- Background: IoT devices (sensors, chips) with binary identifiers
- Include annotations: "256 total codes available", "3 assigned", "253 remaining"
- Style: Modern software interface with technical elements
- Color scheme: Dark theme with blue/green accents
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step DFS algorithm visualization

**Generation Prompt:**

```
Create a detailed algorithm flow showing DFS traversal:

Top: Input: L=3, Set={"000", "001", "010", "100"}

Middle: Binary trie with DFS traversal steps numbered:
1. Start at root, try '0' path (exists)
2. At depth 1, try '00' path (exists)
3. At depth 2, try '000' (exists, marked END) - backtrack
4. Try '001' (exists, marked END) - backtrack
5. Back to depth 1, try '01' path (exists)
6. At depth 2, try '010' (exists, marked END) - backtrack
7. Try '011' - NOT EXISTS! ← FOUND!
8. Return "011"

Visualization:
- Show trie structure with nodes
- Use numbered arrows showing DFS path
- Color code: green for explored paths, red for backtracking, gold star for found answer
- Annotate decision points: "Child exists?" "Is END?" "Backtrack or continue?"
- Bottom: Result: "011" with explanation "First missing in lexicographic order"
- Style: Educational flowchart with step numbers
- Size: 1600x1200px
```

### 4. example-1.png

**Purpose:** Visual walkthrough of simple example

**Generation Prompt:**

```
Create a step-by-step example visualization:

Title: "Finding Missing Binary String of Length 2"

Section 1 - All Possibilities:
- Show complete enumeration: ["00", "01", "10", "11"]
- Label: "All 2² = 4 possible strings"

Section 2 - Given Set:
- Show: ["00", "01"] with green background
- Label: "Existing strings (n=2)"

Section 3 - Binary Trie:
```

         root
        /    \
      0(✓)   1(✗)
      /  \
    0(✓) 1(✓)
    END  END

```
- Mark existing paths with checkmarks
- Mark missing branches with X

Section 4 - DFS Search:
- Step 1: Try "00" → exists (green)
- Step 2: Try "01" → exists (green)
- Step 3: Try "10" → MISSING! (red star)
- Result: "10"

Bottom: Large result box showing answer "10"
- Style: Clean educational diagram with numbered steps
- Color scheme: Green for exists, red for missing, gold for answer
- Size: 1200x1000px
```

### 5. lexicographic-order.png

**Purpose:** Explain lexicographic ordering of binary strings

**Generation Prompt:**

```
Create an educational diagram explaining binary lexicographic order:

Left Panel - "What is Lexicographic Order?":
- Definition: Dictionary order, comparing character by character
- For binary: '0' comes before '1'

Center Panel - Visual Comparison:
Show sorted list with detailed comparison:
- "00" vs "01": First char same ('0'='0'), second char '0'<'1' → "00" first
- "01" vs "10": First char different ('0'<'1') → "01" first
- "10" vs "11": First char same ('1'='1'), second char '0'<'1' → "10" first

Right Panel - Complete ordering for L=3:
Vertical list showing all 8 strings in order:
000 ← smallest
001
010
011
100
101
110
111 ← largest

Include arrows and comparison symbols showing why each ordering
- Style: Educational infographic with clear visual comparisons
- Color scheme: Gradient showing progression from smallest to largest
- Size: 1400x800px
```

### 6. complexity-comparison.png

**Purpose:** Compare naive vs trie-based approaches

**Generation Prompt:**

```
Create a performance comparison visualization:

Left Side - Naive Approach:
- Title: "Generate & Check All Possibilities"
- Algorithm box showing:
```

for each of 2^L strings:
check if in HashSet
if not, return it

```
- Complexity: O(2^L × L)
- Visual: Exponential curve graph
- Example: L=20 → check 1,048,576 strings!

Right Side - Trie DFS Approach:
- Title: "Smart DFS Traversal"
- Algorithm box showing:
```

Build trie
DFS with early exit
Return first missing path

```
- Complexity: O(n×L) build + O(L) search
- Visual: Linear graph
- Example: L=20, n=100 → insert 100, find in ≤20 steps

Bottom: Comparison Table:
| L  | Total Strings | Naive Checks | Trie Build | Speedup |
|----|---------------|--------------|------------|---------|
| 10 | 1,024        | ~1,000       | ~100       | 10x     |
| 15 | 32,768       | ~30,000      | ~100       | 300x    |
| 20 | 1,048,576    | ~1,000,000   | ~100       | 10,000x |

Highlight: "Trie approach scales exponentially better!"
- Style: Technical comparison with graphs and tables
- Color scheme: Red for naive, green for optimal
- Size: 1400x1000px
```

## Image Specifications

- Format: PNG with transparency where applicable
- Resolution: High-DPI (2x) for Retina displays
- Compression: Optimized for web delivery
- Accessibility: Include alt text descriptions

## Notes

These prompts are designed for AI image generation tools or as briefs for graphic designers. Focus on clarity and educational value.
