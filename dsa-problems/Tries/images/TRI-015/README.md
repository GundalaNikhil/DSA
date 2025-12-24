# Image Generation Prompts for TRI-015: XOR Minimization With Trie

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of XOR minimization concept

**Generation Prompt:**

```
Create a technical diagram showing XOR minimization:
- Top: Array [4, 1, 2] and X=3
- Middle: Show all subarrays with their XOR calculations:
  - [4]: 4 ⊕ 3 = 7
  - [1]: 1 ⊕ 3 = 2
  - [2]: 2 ⊕ 3 = 1
  - [4,1]: 5 ⊕ 3 = 6
  - [1,2]: 3 ⊕ 3 = 0 ← highlighted as minimum
  - [4,1,2]: 7 ⊕ 3 = 4
- Visual binary trie showing prefix XORs
- Bottom: Result = 0 with gold star
- Use color coding: green for minimum, gray for others
- Style: Technical diagram with binary representations
- Color scheme: Blue, green for answer, binary bit visualization
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Visualization of network error detection application

**Generation Prompt:**

```
Create an illustration of network data transmission:
- Background: Network topology with sender and receiver
- Main panel: Data packet transmission display
- Show data stream with XOR-based error detection:
  - Transmitted packets with checksums
  - Receiving end comparing with expected checksum
  - Highlight "Error Detection Window" showing XOR differences
  - Display: "Finding minimum error segment"
- Visual representation of XOR operation on binary data
- Include annotations:
  - "XOR Checksum: 10110011"
  - "Minimum deviation window: bits 10-15"
  - "Error magnitude: 0 (perfect match!)"
- Side panel showing binary trie for efficient search
- Style: Technical network diagram with data flow
- Color scheme: Network blues/greens, red for errors, green for matches
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step algorithm with prefix XOR and binary trie

**Generation Prompt:**

```
Create a comprehensive algorithm flow:

Step 1 - Compute Prefix XOR:
Array: [4, 1, 2]
- prefix[0] = 0
- prefix[1] = 4
- prefix[2] = 4⊕1 = 5
- prefix[3] = 4⊕1⊕2 = 7

Step 2 - Build Binary Trie with Queries:
For each prefix[j], query for best match with (prefix[j] ⊕ X):

j=0: Insert prefix[0]=0 into trie

j=1:
- Query target = 4⊕3 = 7 (binary: 0111)
- Trie has: {0}
- Find closest to 7: result = 0
- Min XOR: 0⊕7 = 7
- Insert prefix[1]=4

j=2:
- Query target = 5⊕3 = 6 (binary: 0110)
- Trie has: {0, 4}
- Traverse trie greedily for 6:
  - Bit 2: want 1, have both 0(from 0) and 1(from 4), take 1→4
  - Match with 4: XOR = 4⊕6 = 2
- Min XOR: 2
- Insert prefix[2]=5

j=3:
- Query target = 7⊕3 = 4 (binary: 0100)
- Trie has: {0, 4, 5}
- Find 4 exactly: XOR = 0
- Min XOR: 0 ← ANSWER!

Show binary trie structure at each step
Use flowchart with decision trees
- Style: Educational algorithm flowchart with binary trees
- Size: 1600x1200px
```

### 4. example-1.png

**Purpose:** Detailed example walkthrough

**Generation Prompt:**

```
Create a detailed example visualization:

Input: a=[4,1,2], X=3

Table showing all subarrays:
| Subarray | Indices | XOR Calculation | Subarray XOR | Result (⊕3) |
|----------|---------|-----------------|--------------|-------------|
| [4]      | [0,0]   | 4               | 4            | 7           |
| [1]      | [1,1]   | 1               | 1            | 2           |
| [2]      | [2,2]   | 2               | 2            | 1           |
| [4,1]    | [0,1]   | 4⊕1             | 5            | 6           |
| [1,2]    | [1,2]   | 1⊕2             | 3            | 0 ✓         |
| [4,1,2]  | [0,2]   | 4⊕1⊕2           | 7            | 4           |

Highlight row [1,2] with green background

Bottom: Show binary representation:
- 3 in binary: 0011
- 3 in binary: 0011
- XOR result:  0000 (= 0)

Result box: "Minimum = 0"
- Style: Clean table with binary visualization
- Color scheme: Green for minimum, gray for others
- Size: 1200x900px
```

### 5. binary-trie-structure.png

**Purpose:** Detailed explanation of binary trie for XOR queries

**Generation Prompt:**

```
Create an educational diagram explaining binary trie:

Left Panel - "Building Binary Trie":
- Show numbers: 0, 4, 5, 7
- Binary representations (5 bits for clarity):
  - 0: 00000
  - 4: 00100
  - 5: 00101
  - 7: 00111
- Trie structure showing shared prefixes

Right Panel - "Querying for Minimum XOR":
- Query: Find number closest to 6 (00110)
- Traversal from MSB to LSB:
  - Bit 4: want 0, have 0 ✓
  - Bit 3: want 0, have 0 ✓
  - Bit 2: want 1, have both 0 and 1, take 1 ✓
  - Bit 1: want 1, take what's available
  - Bit 0: take what's available
- Result: Found 4 (00100), XOR = 4⊕6 = 2

Bottom: Greedy Strategy Explanation:
"At each bit, prefer same bit to minimize XOR"
- Same bit → XOR=0 at this position
- Different bit → XOR=1 at this position
- MSB differences matter more!

- Style: Technical tree diagram with annotations
- Color scheme: Green for matching bits, red for mismatches
- Size: 1400x1000px
```

### 6. prefix-xor-technique.png

**Purpose:** Explain prefix XOR formula

**Generation Prompt:**

```
Create an educational diagram explaining prefix XOR:

Top: "Why Prefix XOR?"

Section 1 - Definition:
- prefix[i] = a[0] ⊕ a[1] ⊕ ... ⊕ a[i-1]
- prefix[0] = 0 (empty subarray)

Section 2 - Key Property:
- Subarray[i, j] XOR = prefix[j+1] ⊕ prefix[i]
- Proof visualization using XOR cancellation:
```

prefix[j+1] = a[0]⊕...⊕a[i-1]⊕a[i]⊕...⊕a[j]
prefix[i] = a[0]⊕...⊕a[i-1]
XOR them: = a[i]⊕...⊕a[j] (cancellation!)

```

Section 3 - Example:
Array: [4, 1, 2]
- prefix = [0, 4, 5, 7]
- Subarray[1,2] = a[1]⊕a[2] = 1⊕2 = 3
- Using prefix: prefix[3]⊕prefix[1] = 7⊕4 = 3 ✓

Visual showing XOR cancellation with colored blocks
- Style: Educational math explanation with visual proof
- Color scheme: Different colors for array segments
- Size: 1200x800px
```

## Image Specifications

- Format: PNG with transparency where applicable
- Resolution: High-DPI (2x) for Retina displays
- Compression: Optimized for web delivery
- Accessibility: Include alt text descriptions

## Notes

These prompts are designed for AI image generation tools or as briefs for graphic designers. Focus on binary representations and XOR operations for clarity.
