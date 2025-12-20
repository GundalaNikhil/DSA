# Image Generation Prompts for TRI-014: Longest Word Buildable by At Least K Prefixes

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of prefix counting concept

**Generation Prompt:**

```
Create a technical diagram showing word prefix analysis:
- Center: The word "apple" broken down into prefixes
- Show each prefix with existence check:
  - "a" → ✓ exists in dictionary
  - "ap" → ✓ exists in dictionary
  - "app" → ✓ exists in dictionary
  - "appl" → ✗ not in dictionary
  - "apple" → (the word itself, not counted)
- Counter showing: "3 valid prefixes >= k=3" with green checkmark
- Side panel showing dictionary: ["a", "ap", "app", "apple", "apex"]
- Highlight "apple" as the answer (length 5, meets k=3)
- Style: Educational breakdown diagram
- Color scheme: Green for valid prefixes, red for missing, blue for result
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Visualization of language learning application

**Generation Prompt:**

```
Create an illustration of a language learning app interface:
- Mobile phone screen showing "Progressive Vocabulary Builder"
- Display showing student's learned words:
  - Basic: "a", "ap", "app" (marked with green badges)
  - Ready to learn: "apple" (highlighted, marked "Recommended!")
  - Not ready: "apex" (grayed out, marked "Learn 1 more prefix first")
- Progress bar showing: "3/3 prefixes known for 'apple'"
- Visual representation using building blocks:
  - Bottom blocks: "a", "ap", "app" (solid, learned)
  - Top block: "apple" (ready to stack on top)
- Side panel showing learning path with arrows
- Include educational mascot/character encouraging user
- Style: Modern mobile app interface, gamified learning
- Color scheme: Friendly colors (blue, green, yellow), engaging design
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Step-by-step algorithm flow

**Generation Prompt:**

```
Create a detailed algorithm visualization:

Step 1 - Build Trie:
Insert words: ["a", "ap", "app", "apple", "apex"]
```

         root
          |
          a (END)
          |
          p (END)
         / \
       p    e
     (END)  |
      |     x
      l    (END)
      |
      e
    (END)

```

Step 2 - Count Prefixes for "apple":
- Traverse: root → a (END! count++) → p (END! count++) → p (END! count++) → l → e (END, but final)
- Show counter incrementing: 0 → 1 → 2 → 3
- Result: 3 prefixes >= k=3 ✓

Step 3 - Count Prefixes for "apex":
- Traverse: root → a (END! count++) → p (END! count++) → e → x (END, but final)
- Show counter: 0 → 1 → 2
- Result: 2 prefixes < k=3 ✗

Step 4 - Select Best:
- Valid candidates: ["apple" (length 5)]
- Result: "apple"

Use flowchart arrows, color coding, and step numbers
- Style: Technical algorithm flowchart
- Size: 1600x1200px
```

### 4. example-1.png

**Purpose:** Visual walkthrough of main example

**Generation Prompt:**

```
Create a detailed example walkthrough:

Title: "Finding Longest Word with k=3 Prefixes"

Dictionary: ["a", "ap", "app", "apple", "apex"]

Analysis Table:
| Word   | Prefixes              | In Dict? | Count | Valid? |
|--------|----------------------|----------|-------|--------|
| a      | -                    | -        | 0     | ✗      |
| ap     | a                    | ✓        | 1     | ✗      |
| app    | a, ap                | ✓, ✓     | 2     | ✗      |
| apple  | a, ap, app, appl     | ✓,✓,✓,✗  | 3     | ✓      |
| apex   | a, ap, ape           | ✓,✓,✗    | 2     | ✗      |

Visual Trie showing paths for each word
Highlight "apple" as the only valid word (green)
Show length comparison (apple: 5 chars)

Result box: "apple" (largest green box)
- Style: Educational table with visual trie
- Color scheme: Green for valid, red for invalid
- Size: 1200x1000px
```

### 5. prefix-building.png

**Purpose:** Illustration of progressive word building

**Generation Prompt:**

```
Create a diagram showing word building progression:

Show building "algorithm" from prefixes:
Level 1: "a" (1 char) - foundation block
Level 2: "al" (2 chars) - stacking
Level 3: "alg" (3 chars) - growing
Level 4: "algo" (4 chars)
Level 5: "algor" (5 chars)
Level 6: "algori" (6 chars)
Level 7: "algorit" (7 chars)
Level 8: "algorith" (8 chars)
Level 9: "algorithm" (9 chars) - complete!

Visualize as:
- Left: Vertical stacking blocks, each labeled with prefix
- Center: Trie structure showing branching
- Right: Progress bar showing "k=4" requirement
  - Markers at levels where prefixes exist in dictionary
  - Count display showing accumulation

Include annotations:
- "Each prefix builds on previous"
- "Need k=4 existing prefixes to qualify"
- "Count: 1, 2, 3, 4... ✓ meets requirement!"

- Style: Educational building blocks metaphor
- Color scheme: Gradient from light to dark showing progression
- Size: 1400x900px
```

### 6. comparison-same-length.png

**Purpose:** Show lexicographic tie-breaking

**Generation Prompt:**

```
Create a comparison diagram for tie-breaking:

Scenario: Two words with same length both meet k requirement

Example: Dictionary has paths for both "apple" and "apply"
- Both length 5
- Both have >= k prefixes
- Need to choose lexicographically smallest

Visual comparison:
Left panel - "apple":
- Length: 5 ✓
- Prefix count: 3 ✓
- Lexicographic: "apple"

Right panel - "apply":
- Length: 5 ✓
- Prefix count: 3 ✓
- Lexicographic: "apply"

Center: Character-by-character comparison:
- a = a ✓
- p = p ✓
- p = p ✓
- 'a' < 'p' in alphabetical order ("apple" < "apply")
- Showing "apple" < "apply" letter by letter

Result arrow pointing to "apple" with gold star

Include lexicographic order reference:
a < b < c < ... < z

- Style: Side-by-side comparison with detailed breakdown
- Color scheme: Blue for comparison, gold for winner
- Size: 1200x700px
```

## Image Specifications

- Format: PNG with transparency where applicable
- Resolution: High-DPI (2x) for Retina displays
- Compression: Optimized for web delivery
- Accessibility: Include alt text descriptions

## Notes

These prompts are designed for AI image generation tools or as briefs for graphic designers. Focus on educational clarity and progressive learning concepts.
