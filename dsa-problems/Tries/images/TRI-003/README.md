# Image Placeholders for TRI-003

This directory contains image assets for the Distinct Substrings Count via Trie problem.

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

- **header.png**: A wide banner (1200x300px) showing a DNA double helix on the left side with highlighted segments representing substrings. On the right, a modern trie tree structure with glowing nodes. Center text reads "Distinct Substrings" in bold typography. Background is a gradient from deep blue (#3B82F6) to purple. Clean, scientific illustration style.
- **problem-illustration.png**: A horizontal flow diagram showing the string "aaa" broken down into its substrings. Top row shows the original string with position markers. Middle section shows three boxes containing "a", "aa", and "aaa" with checkmarks. Bottom shows a counter displaying "Count: 3". Use clear arrows and clean spacing.
- **algorithm-steps.png**: A three-panel flowchart. Panel 1: "Extract Suffixes" showing "aaa", "aa", "a" in a list. Panel 2: "Build Trie" showing a tree with root→a→a→a structure. Panel 3: "Count Nodes" showing the same tree with nodes numbered 1, 2, 3 and result "3". Use directional arrows between panels.
- **visualization.png**: A side-by-side comparison. Left: A table listing all substrings of "abc" (a, ab, abc, b, bc, c). Right: A trie visualization showing two main branches from root (a and b), with sub-branches forming the complete suffix trie. Color-code nodes by depth: green (depth 1), blue (depth 2), purple (depth 3).
- **example-1.png**: A detailed walkthrough for "aaa". Show three suffix insertions step-by-step. First: Insert "aaa" creates root→a→a→a with 3 new nodes marked in green. Second: Insert "aa" reuses first two nodes (marked in gray) with no new additions. Third: Insert "a" reuses first node (marked in gray). Final count: 3 nodes shown in a highlighted box.
- **example-2.png**: A visual breakdown for "abc". Display the suffix trie with all branches. Show paths: root→a→b→c, root→b→c, root→c. Label each node with the substring it represents ("a", "ab", "abc", "b", "bc", "c"). Use color coding for clarity. Final count "6" in a green badge.

### Editorial Images

- **header.png**: A modern banner featuring a bioinformatics lab setting with computer screens displaying genetic sequences. Overlaid with a glowing trie structure. Professional blue and green color scheme with clean typography.
- **problem-illustration.png**: A comparison infographic showing "Naive Approach" (left) with nested loops and hash set icons, versus "Trie Approach" (right) with a clean tree structure. Include complexity annotations: O(n³) vs O(n²) in prominent text.
- **algorithm-steps.png**: A detailed vertical flowchart showing: 1) Input string "s", 2) Loop through positions 0 to n-1, 3) Extract suffix s[i:], 4) Insert into trie with node counting, 5) Return total count. Include code-style annotations.
- **visualization.png**: A large, detailed trie diagram for the string "abab". Show all nodes with clear labels. Highlight the path for each suffix with different colors. Include a legend showing which color represents which suffix.
