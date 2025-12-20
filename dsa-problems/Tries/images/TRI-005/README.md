# Image Placeholders for TRI-005

This directory contains image assets for the Binary Trie Min XOR Pair Under Limit problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Main concept visualization
3. **algorithm-steps.png** - Algorithm breakdown
4. **visualization.png** - Solution visualization
5. **example-1.png** - Example 1 walkthrough
6. **example-2.png** - Example 2 walkthrough

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors (Blue: #3B82F6, Green: #10B981)
- Clear labels and annotations
- PNG format, optimized for web (<500KB each)

## Image Prompts

### Problem Images

- **header.png**: A wide banner (1200x300px) showing a network router with glowing connections between IP address nodes. Binary numbers float around the connections with XOR symbols. Center shows a binary trie tree structure in neon blue. Professional tech background with circuit board patterns.
- **problem-illustration.png**: A diagram showing four numbers (3, 10, 5, 25) in boxes with their binary representations below. Arrows connect pairs with XOR values labeled. Valid pairs (XOR ≤ 8) in green, invalid in red. Highlight the minimum valid XOR of 6 between 3 and 5.
- **algorithm-steps.png**: Three-panel flowchart. Panel 1: "Build Binary Trie" showing a tree with 0/1 edges. Panel 2: "Query Each Number" showing greedy bit-by-bit traversal. Panel 3: "Track Minimum" showing comparison logic with limit L.
- **visualization.png**: A detailed binary trie with 4-5 levels. Show the path for querying number 5 (0101) to find closest match. Color-code preferred paths in green, alternate paths in gray. Label each node with bit position.
- **example-1.png**: Step-by-step for array [3,10,5,25] with L=8. Show all 6 possible pairs with XOR calculations. Use checkmarks for valid pairs (≤8) and X marks for invalid. Highlight minimum 6 in a large green box.
- **example-2.png**: Binary representation walkthrough for 3 XOR 5. Show 3=0011 and 5=0101 aligned vertically. Perform bit-by-bit XOR with result 0110=6. Include truth table for XOR operation.

### Editorial Images

- **header.png**: Modern banner showing binary tree structure with glowing bits. Network optimization theme with data packets flowing through trie paths.
- **problem-illustration.png**: Side-by-side comparison "Naive O(n²)" with nested loops versus "Binary Trie O(n log MAX)" with elegant tree structure.
- **algorithm-steps.png**: Detailed flowchart showing insertion and query operations in binary trie with bit manipulation details.
- **visualization.png**: Large binary trie diagram for example array showing all numbers inserted and query paths highlighted in different colors.
