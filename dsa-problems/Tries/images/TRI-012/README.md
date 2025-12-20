# Image Generation Prompts for TRI-012: Prefix-Free Check After Inserts

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of prefix-free concept in telecommunications

**Generation Prompt:**

```
Create a technical diagram showing phone number routing:
- Left side: A phone system console with incoming calls
- Center: A trie structure visualizing phone numbers being inserted
- Show three phone numbers: "91", "911", "912"
- Use color coding:
  - Green for "91" (first insert, prefix-free ✓)
  - Red for "911" (conflicts with "91", prefix violation ✗)
  - Red for "912" (still conflicts, prefix violation ✗)
- Highlight the conflict: "91" is a prefix of both "911" and "912"
- Right side: Boolean results display: [true, false, false]
- Include a small alert icon showing "Prefix Conflict Detected!"
- Style: Modern technical infographic with telecommunications theme
- Color scheme: Blue, white, green (valid), red (conflict)
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Visualization of telephone routing system application

**Generation Prompt:**

```
Create an illustration of a telecom routing center:
- Background: Network operations center with world map showing call routes
- Foreground: Large display showing phone number trie
- Display panel showing:
  - Emergency numbers: "911" (highlighted in red)
  - Regular numbers: "555-1234", "555-5678"
  - Potential conflict scenario: "911" vs "9112345678"
- Visual representation of call routing ambiguity:
  - When someone dials "911234...", does system route after "911" or continue?
  - Show confusion arrows and question marks
- Include an operator/engineer reviewing the prefix-free validation system
- Bottom: Status display showing "Prefix-Free: ✓" or "Conflict Detected: ✗"
- Style: Professional telecommunications operations center
- Color scheme: Dark blue background, bright accent colors, warning reds
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step visualization of prefix-free checking algorithm

**Generation Prompt:**

```
Create a detailed algorithm flow diagram showing:
1. Initial State: Empty trie (root node only)
2. Insert "91":
   - Traverse: root → 9 → 1 (mark end)
   - Check: No children at end node ✓
   - Check: Didn't pass through any end node ✓
   - Result: Prefix-Free ✓ → true
3. Insert "911":
   - Traverse: root → 9 → 1 (ALREADY END!) ✗
   - Check: Passed through end node of "91" before finishing
   - Result: NOT Prefix-Free ✗ → false
4. Insert "912":
   - Traverse: root → 9 → 1 (ALREADY END!) ✗
   - Result: NOT Prefix-Free ✗ → false
- Use flowchart boxes with decision diamonds
- Color code: Green for successful checks, red for failures
- Show trie structure evolving with each insertion
- Include annotations explaining each check
- Style: Educational algorithm flowchart
- Size: 1600x1200px
```

### 4. example-1.png

**Purpose:** Visual walkthrough of the main example

**Generation Prompt:**

```
Create a detailed example walkthrough showing:
- Top: Input sequence: ["91", "911", "912"]
- Middle section with 3 columns (one per insertion):

  Column 1 - Insert "91":
  - Trie: root → 9(no end) → 1(END)
  - Checks performed:
    ✓ No children at end node
    ✓ Didn't traverse through end node
  - Result: true (green checkmark)

  Column 2 - Insert "911":
  - Trie: root → 9 → 1(END) → 1(END)
  - Checks performed:
    ✗ Traversed through end node "91"
  - Result: false (red X)
  - Highlight conflict: "91" is prefix of "911"

  Column 3 - Insert "912":
  - Trie: root → 9 → 1(END) → [1(END), 2(END)]
  - Checks performed:
    ✗ Traversed through end node "91"
  - Result: false (red X)
  - Highlight conflict: "91" is prefix of "912"

- Bottom: Final result array: [true, false, false]
- Use arrows showing the progression
- Color code: green for valid, red for conflicts
- Style: Step-by-step tutorial with clear visual separation
- Size: 1400x1000px
```

### 5. prefix-violation-types.png

**Purpose:** Illustration of two types of prefix violations

**Generation Prompt:**

```
Create a diagram showing the two violation types:

Left Panel - "New number extends existing":
- Example: Existing "91", inserting "911"
- Trie visualization showing:
  - Path: 9 → 1 (END marker for "91")
  - Continuing: → 1 (want to add END for "911")
- Label: "Traversed through existing end node"
- Result: ✗ NOT prefix-free

Right Panel - "New number is prefix of existing":
- Example: Existing "911", inserting "91"
- Trie visualization showing:
  - Want to end at: 9 → 1 (mark END for "91")
  - But node has children: → 1 (already exists for "911")
- Label: "End node has children"
- Result: ✗ NOT prefix-free

Center: Large "PREFIX-FREE VIOLATIONS" title
- Include summary box explaining both cases
- Use red highlighting for violation points
- Style: Educational comparison diagram
- Color scheme: Technical with clear red violation indicators
- Size: 1200x700px
```

### 6. complexity-comparison.png

**Purpose:** Compare naive vs optimal approach performance

**Generation Prompt:**

```
Create a performance comparison chart:

Left Side - Naive Approach:
- Algorithm: "After each insert, compare new number with all existing"
- Complexity: O(n²·L) where n = numbers, L = avg length
- Visual: Nested loops diagram showing quadratic growth
- Performance graph: Exponential curve showing time vs n

Right Side - Optimal Trie Approach:
- Algorithm: "Insert with prefix checks during traversal"
- Complexity: O(L) per insertion, O(n·L) total
- Visual: Single path traversal in trie
- Performance graph: Linear curve showing time vs n

Bottom: Comparison table:
- n=100: Naive 10,000 ops vs Trie 1,000 ops
- n=1,000: Naive 1,000,000 ops vs Trie 10,000 ops
- n=10,000: Naive 100,000,000 ops vs Trie 100,000 ops

Highlight: "Trie approach is ~n times faster!"
- Style: Professional performance analysis
- Color scheme: Red for naive, green for optimal
- Include graphs and tables
- Size: 1400x900px
```

## Image Specifications

- Format: PNG with transparency where applicable
- Resolution: High-DPI (2x) for Retina displays
- Compression: Optimized for web delivery
- Accessibility: Include alt text descriptions in implementations

## Notes

These prompts are designed for AI image generation tools or as briefs for graphic designers. Adjust style parameters based on the specific tool or designer capabilities.
