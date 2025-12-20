# Image Placeholders for TRI-002

This directory contains image assets for the Longest Common Prefix After One Deletion problem.

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

- **header.png**: A wide banner (1200x300px) featuring a stylized illustration of three word cards with letters. Each card shows a word like "interview", "internet", "interval" with one letter highlighted in red to indicate potential deletion. In the center, a glowing prefix "interv" appears in green. Background is a professional gradient of blue (#3B82F6) to purple. Use clean, flat design style with modern typography.
- **problem-illustration.png**: A diagram showing three words stacked vertically: "interview", "internet", "interval". Above each word, show colored boxes for each letter. Some boxes have a small red 'X' to show deletion possibilities. Below the words, show a growing prefix "i" → "in" → "int" → "inte" → "inter" → "interv" with checkmarks. Use arrows to connect aligned letters.
- **algorithm-steps.png**: A flowchart with three main steps: 1) "Build Trie with all words" showing a tree structure, 2) "Try deleting each character" showing branching paths with deletion markers, 3) "Find longest common prefix" showing a highlighted path. Use clean icons and arrows with step numbers.
- **visualization.png**: A trie tree diagram with nodes representing characters. Show three paths for "interview", "internet", "interval". Mark nodes in different colors: green for common prefix, yellow for positions where deletion helps, red for divergence points. Include a legend.
- **example-1.png**: A step-by-step walkthrough for ["interview", "internet", "interval"]. Show each word with character positions 0-8 labeled. Highlight the divergence at position 6 (v vs n vs v). Show deletion of 'v' from "interview" and "interval" to align with "internet". Final result "interv" shown in a green box.
- **example-2.png**: A simpler example with ["abc", "abd"]. Show both words aligned character-by-character. Highlight position 2 where 'c' and 'd' differ. Show deletion of 'c' to get "ab" and deletion of 'd' to get "ab". Result "ab" shown in a green box with a checkmark.

### Editorial Images

- **header.png**: A modern banner showing a software autocomplete interface with multiple suggestions appearing. The suggestions share a common prefix that's highlighted in green. Background shows code editor theme with professional blue tones.
- **problem-illustration.png**: A split comparison showing "Before Deletion" with three diverging paths in a trie, and "After Deletion" with paths converging to a longer common prefix. Use before/after arrows and clear labeling.
- **algorithm-steps.png**: A detailed flowchart showing: 1) Input processing, 2) Trie construction, 3) DFS traversal with deletion tracking, 4) Prefix length calculation, 5) Output generation. Include complexity annotations.
- **visualization.png**: A large trie visualization with multiple words inserted. Color-code nodes by depth and highlight the longest common prefix path. Show deletion operations as dotted bypass edges.
