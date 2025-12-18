# BIT-002: Two Unique With Triple Others Under Mask - Image Specifications

This document contains detailed specifications for generating images for the BIT-002 problem using AI image generation tools (DALL-E, Midjourney, Stable Diffusion, etc.).

## Color Scheme

- **Primary Blue**: `#3B82F6` - For main elements and headers
- **Purple Accent**: `#8B5CF6` - For highlighting XOR operations
- **Green Success**: `#10B981` - For correct results and unique numbers
- **Orange Warning**: `#F59E0B` - For triples and repeated elements
- **Dark Gray**: `#1F2937` - For text and code
- **Light Gray**: `#F3F4F6` - For backgrounds

## Image 1: Header Image

**Filename**: `header.png`

**Dimensions**: 1200x400px

**Description**:
A modern, tech-focused banner showing the concept of finding two unique elements among triples.

**Prompt**:

```
Create a modern technical banner (1200x400px) for a coding problem titled "Two Unique With Triple Others Under Mask".

Show:
- Center: Three groups of three identical glowing cubes (representing triples) in orange (#F59E0B)
- Left and right: Two single unique cubes in bright green (#10B981)
- Background: Dark gradient with subtle binary code pattern
- Top right: A blue digital mask overlay (#3B82F6) showing binary bits
- Bottom: Subtle XOR symbol (⊕) in purple (#8B5CF6)

Style: Clean, modern, technical, professional
Colors: Blue #3B82F6, Purple #8B5CF6, Green #10B981, Orange #F59E0B
Mood: Algorithmic, precise, computer science themed
```

## Image 2: Problem Illustration

**Filename**: `problem-illustration.png`

**Dimensions**: 800x600px

**Description**:
Visual representation of the manufacturing quality control scenario with components.

**Prompt**:

```
Create an infographic illustration (800x600px) showing a semiconductor manufacturing quality control system.

Show:
- Top: Assembly line with 8 components (represented as chips/circuits)
- Components labeled: 5, 5, 5, 9, 9, 9, 3, 6
- Under each component: inspection checkmarks
  * Components 5: Three green checkmarks (passed 3 inspections)
  * Components 9: Three green checkmarks (passed 3 inspections)
  * Component 3: One red X (failed, only 1 scan) - highlight in green
  * Component 6: One red X (failed, only 1 scan) - highlight in green
- Bottom: Display showing "Defective IDs: 3, 6" in bright green
- Top right corner: Binary mask "M = 0010" in blue

Style: Clean, isometric or flat design, technical documentation
Colors: Blue #3B82F6 for mask, Green #10B981 for defective highlights, Orange #F59E0B for components
```

## Image 3: Algorithm Steps Visualization

**Filename**: `algorithm-steps.png`

**Dimensions**: 1000x800px

**Description**:
Three-phase algorithm breakdown with visual flow.

**Prompt**:

```
Create a technical flowchart (1000x800px) showing a 3-phase algorithm for finding unique numbers.

Layout (vertical flow):

PHASE 1 (Top, Blue #3B82F6):
- Title: "Phase 1: Count Bits Mod 3"
- Show: Array [5,5,5,9,9,9,3,6] with bit counting table
- Table showing bit positions 0-3 with counts: 7, 2, 4, 3
- Arrow pointing to remainders: 1, 2, 1, 0
- Result: XOR_both = 0101 (binary) = 5

PHASE 2 (Middle, Purple #8B5CF6):
- Title: "Phase 2: Find Differentiating Bit"
- Show: XOR_both = 0101 with mask M = 0010
- Highlight: Choosing bit position (rightmost set bit)
- Result: diff_bit selected

PHASE 3 (Bottom, Green #10B981):
- Title: "Phase 3: Partition & Extract"
- Show: Two groups separated by diff_bit
- Group 0: [5,5,5,9,9,9,3] → Extract 3
- Group 1: [6] → Extract 6
- Final result: 3, 6 in green boxes

Style: Clean flowchart, technical diagram
Use arrows to show flow between phases
```

## Image 4: Bit Counting Table

**Filename**: `bit-counting-example.png`

**Dimensions**: 900x700px

**Description**:
Detailed bit-by-bit counting visualization for Example 1.

**Prompt**:

```
Create a detailed table visualization (900x700px) showing bit counting modulo 3.

Title: "Bit Counting Mod 3: Example [5,5,5,9,9,9,3,6]"

Main table:
- Rows: Numbers 5, 5, 5, 9, 9, 9, 3, 6
- Columns: Bit 3, Bit 2, Bit 1, Bit 0
- Each cell shows the bit value (0 or 1) with color coding:
  * Triples in orange (#F59E0B)
  * Uniques in green (#10B981)

Binary representations shown:
5 = 0101
9 = 1001
3 = 0011
6 = 0110

Bottom summary:
- Sum per bit column: 3, 4, 2, 7
- Modulo 3 result: 0, 1, 2, 1
- XOR contribution: Only remainders 1 contribute
- Final XOR_both = 0101

Style: Clean data table, educational, technical
Colors: Orange for triples, green for uniques, blue headers
Add mathematical notation (Σ, %, ⊕)
```

## Image 5: XOR Properties

**Filename**: `xor-properties.png`

**Dimensions**: 800x600px

**Description**:
Key XOR properties used in the algorithm.

**Prompt**:

```
Create an educational infographic (800x600px) explaining XOR properties for bit manipulation.

Show 4 key properties in quadrant layout:

Top Left - Self-Inverse:
- a ⊕ a = 0
- Visual: Two identical binary numbers canceling out
- Color: Purple #8B5CF6

Top Right - Identity:
- a ⊕ 0 = a
- Visual: Number XOR with zero remains unchanged
- Color: Blue #3B82F6

Bottom Left - Commutative:
- a ⊕ b = b ⊕ a
- Visual: Order doesn't matter
- Color: Green #10B981

Bottom Right - Associative:
- (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)
- Visual: Grouping doesn't matter
- Color: Orange #F59E0B

Center: Large ⊕ symbol connecting all quadrants

Style: Modern educational poster, clean icons, mathematical
Background: Light gray #F3F4F6 with subtle grid
```

## Image 6: Complexity Comparison

**Filename**: `complexity-comparison.png`

**Dimensions**: 700x500px

**Description**:
Side-by-side comparison of naive vs optimal approach.

**Prompt**:

```
Create a comparison chart (700x500px) showing two approaches to solving the problem.

Left side - Naive Approach (Gray #6B7280):
- Icon: Hash map / dictionary symbol
- Time: O(n)
- Space: O(n)
- Method: "Count frequencies"
- Visual: Memory blocks representing hash map storage

Right side - Optimal Approach (Green #10B981):
- Icon: Bit manipulation symbol (XOR ⊕)
- Time: O(n)
- Space: O(1)
- Method: "Bit counting mod 3"
- Visual: Single bit array (32 elements)

Center: Large "VS" separator with arrow pointing right (optimal wins)

Bottom: Winner badge on optimal side showing "O(1) Space Champion"

Style: Technical comparison chart, infographic style
Colors: Gray for naive, green for optimal, blue accents
Include memory visualization diagrams
```

---

## Usage Instructions

1. **For DALL-E 3**: Copy each prompt directly into ChatGPT with DALL-E enabled
2. **For Midjourney**: Add `--ar 3:1` for header, `--ar 4:3` for most others, `--v 6` for latest version
3. **For Stable Diffusion**: Add negative prompt: "blurry, low quality, text artifacts, distorted"
4. **Post-processing**: Use tools like Canva or Figma to add precise text overlays if needed

## File Naming Convention

Save generated images as:

- `header.png`
- `problem-illustration.png`
- `algorithm-steps.png`
- `bit-counting-example.png`
- `xor-properties.png`
- `complexity-comparison.png`

All images should be saved in this directory: `/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Bitwise/images/BIT-002/`
