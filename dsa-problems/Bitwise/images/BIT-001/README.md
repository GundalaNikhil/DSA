# Image Placeholders for BIT-001

This directory contains image assets for the Odd After Bit Salt problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Main concept visualization
3. **algorithm-steps.png** - Algorithm breakdown
4. **visualization.png** - Solution visualization
5. **example-1.png** - Example 1 walkthrough
6. **xor-properties.png** - XOR properties visual reference

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors (Blue: #3B82F6, Purple: #8B5CF6, Green: #10B981)
- Clear binary representations with monospace fonts
- PNG format, optimized for web (<500KB each)
- Include bit-level visualizations where relevant

## Image Prompts

### Problem Images

- **header.png**: A high-quality, wide banner (1200x300px) featuring a modern cybersecurity theme. On the left, a stylized digital lock with binary patterns (0s and 1s) flowing around it in a circuit-board pattern. On the right, the text "Odd After Bit Salt" in a clean, bold sans-serif font with a subtle encryption effect. The background should be a professional gradient of deep blue (#3B82F6) and purple (#8B5CF6). The style should be tech-modern with geometric elements, suitable for a computer science educational platform.

- **problem-illustration.png**: A clear horizontal transformation diagram. Top row: Original array `[4, 1, 2, 1, 2, 4, 7]` in blue boxes. Middle: Large XOR symbol (⊕) with "salt=3" next to it. Bottom row: Transformed array `[7, 2, 1, 2, 1, 7, 4]` in purple boxes. Below transformed array, show frequency counts with check marks for even occurrences (✓) and a star for the odd occurrence (⭐). Include binary representations for 1-2 examples showing the XOR operation bit-by-bit.

- **algorithm-steps.png**: A three-panel horizontal flow. Panel 1: "XOR All Original" showing cascading XOR operations with accumulator. Panel 2: "Check Array Length" showing an if-else branch (odd vs even). Panel 3: "Adjust with Salt" showing final XOR with salt if needed. Connect panels with thick arrows. Include complexity notes "O(n) Time" and "O(1) Space" in corner badges.

- **visualization.png**: A side-by-side comparison. Left: "Naive Approach" showing transformed array creation (array icon), hash map (table icon), and frequency counting (chart icon) with space complexity O(n) in red. Right: "Optimal Approach" showing single XOR accumulator icon with mathematical formula, marked O(1) space in green. Use icons and minimal text for clarity.

- **example-1.png**: Step-by-step XOR accumulation for `[4, 1, 2, 1, 2, 4, 7]`. Show a vertical timeline with 7 steps. Each step shows: current element, binary representation, XOR operation, running result in both decimal and binary. At bottom, show final adjustment with salt=3: `7 ⊕ 3 = 4`. Use color coding: original values in blue, intermediate results in gray, final answer in green.

- **xor-properties.png**: A reference card showing four key XOR properties in a 2x2 grid layout:
  1. **Self-Inverse**: `a ⊕ a = 0` with example `5 ⊕ 5 = 0` (binary shown)
  2. **Identity**: `a ⊕ 0 = a` with example `7 ⊕ 0 = 7` (binary shown)
  3. **Commutative**: `a ⊕ b = b ⊕ a` with example `3 ⊕ 5 = 5 ⊕ 3 = 6`
  4. **Associative**: `(a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)` with example grouping
     Each property in its own rounded box with clean typography and binary illustrations.

### Editorial Images

- **header.png**: A split-screen design. Left side: A security system dashboard with ID cards being scanned. Right side: Mathematical XOR operations shown as elegant circuit diagrams. Central text: "Detect Anomalies Without Decryption" in bold modern font. Background: Professional tech gradient.

- **problem-illustration.png**: A conceptual diagram showing the XOR cancellation effect. Display pairs of identical transformed values disappearing (fading out or canceling with "= 0" notation). Show remaining odd occurrence highlighted with spotlight effect. Include visual representation of why `(x⊕s) ⊕ (x⊕s) = 0`.

- **algorithm-steps.png**: A decision tree flowchart. Root: "Start with result = 0". Branch: Loop through array with XOR operations. Decision node: "Is n odd?". Two paths: Yes → "result ⊕= salt", No → "return result". Use clear arrows and box styles. Include mathematical proof notation in small text boxes.

- **visualization.png**: A dramatic before/after comparison. Top: "Brute Force" showing memory-heavy hash map and array with red "High Memory" warning. Bottom: "XOR Magic" showing single variable with green "O(1) Space" badge. Add visual metaphor of heavy storage vs lightweight calculation.

- **complexity-comparison.png**: A table-style visual. Three columns: Approach | Time | Space. Three rows: Naive O(n)/O(n), HashMap O(n)/O(k), Optimal O(n)/O(1). Use checkmarks and X marks to show trade-offs. Highlight optimal solution in green.

- **xor-mathematics.png**: A mathematical proof visualization showing:
  ```
  (arr[0]⊕s) ⊕ (arr[1]⊕s) ⊕ ... ⊕ (arr[n-1]⊕s)
          ↓ Rearrange
  (arr[0] ⊕ arr[1] ⊕ ... ⊕ arr[n-1]) ⊕ (s⊕s⊕...⊕s)
          ↓ Simplify
  XOR_all_arr ⊕ (s if n is odd, else 0)
  ```
  Use clean mathematical typography with arrows showing transformation steps.

## Notes

- Binary representations should use monospace font (Courier New or Monaco)
- Use ⊕ symbol consistently for XOR operations
- Color code: Blue for input, Purple for transformation, Green for output
- Include captions and legends for all diagrams
- Maintain professional, academic aesthetic throughout
