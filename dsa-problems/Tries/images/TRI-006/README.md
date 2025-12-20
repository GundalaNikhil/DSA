# Image Placeholders for TRI-006

This directory contains image assets for the Lexicographic k-th String Not Present problem.

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

- **header.png**: Wide banner showing a username registration interface with taken usernames "alice", "bob" crossed out in red, and available suggestions "aa", "ab", "ac" in green. Central trie structure glowing in blue. Modern web app design aesthetic.
- **problem-illustration.png**: Lexicographic sequence visualization showing strings: "a" (taken, red X), "aa" (available, green ✓), "ab" (available, green ✓), "b" (taken, red X), "ba" (available, green ✓). k=1 pointer highlighting "aa" as answer.
- **algorithm-steps.png**: Three-panel flowchart: 1) Build Trie from inserted strings, 2) DFS traversal with counter, 3) Navigate to k-th missing string. Include tree diagrams and counter decrements.
- **visualization.png**: Large trie diagram with nodes for "a" and "b" marked as endpoints. Show all 26 possible children from root labeled a-z. Highlight missing nodes in green, taken in red.
- **example-1.png**: Step-by-step DFS for k=1. Show trie with "a", "b" inserted. Trace path: root → try 'a' (taken) → try 'aa' (missing, count=1) → found! Result "aa" in green box.
- **example-2.png**: Visualization for k=3. Show counting process: miss #1 (aa), miss #2 (ab), miss #3 (ac). Highlight "ac" as final answer with checkmark.

### Editorial Images

- **header.png**: Modern banner showing combinatorial counting concept with tree structure and mathematical formulas for 26^L calculations.
- **problem-illustration.png**: Comparison graphic: "Generate All" approach showing explosion of 26^6 strings versus "Smart DFS" showing clean tree traversal.
- **algorithm-steps.png**: Detailed DFS algorithm flowchart with pseudocode boxes and decision diamonds for k tracking.
- **visualization.png**: Full trie visualization with depth markers and missing count annotations at each subtree level.
