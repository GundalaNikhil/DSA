# Image Placeholders for TRI-004

This directory contains image assets for the Replace Words with Shortest Rare Prefix problem.

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

- **header.png**: A wide banner (1200x300px) showing a medical records system interface. On the left, display full medical terms like "cardiologist" and "neurologist". On the right, show abbreviated forms like "cardio" and "neuro" with rarity scores in small badges. Center shows a trie structure connecting them. Professional blue gradient background with modern healthcare iconography.
- **problem-illustration.png**: A horizontal flowchart showing word replacement process. Top row: original sentence "the cattle carried" in gray boxes. Middle: dictionary entries "cat:1" and "car:2" in a trie structure. Bottom row: result "the cat car" in green boxes with arrows showing which words were replaced. Use clear color coding: unchanged words in gray, replaced words in green.
- **algorithm-steps.png**: A three-column layout. Column 1: "Build Trie" showing insertion of dictionary roots with rarity labels at nodes. Column 2: "Search Word" showing traversal path through trie for word "cattle". Column 3: "Select Best" showing selection logic with rarity comparison. Use numbered steps and directional arrows.
- **visualization.png**: A detailed trie diagram with multiple branches. Nodes are labeled with characters and contain small rarity badges. Show highlighted paths for different matching scenarios. Include a legend explaining node colors: green for selected prefix, gray for traversed but not selected, white for not visited.
- **example-1.png**: A step-by-step breakdown for "the cattle carried". Show three word cards. Card 1: "the" with X mark (no match). Card 2: "cattle" with arrow pointing to "cat" (rarity 1) marked with checkmark. Card 3: "carried" with arrow pointing to "car" (rarity 2) marked with checkmark. Final output in large green text below.
- **example-2.png**: A vertical comparison for word "aaaa". Show four candidate prefixes: "a" (rarity 3), "aa" (rarity 2), "aaa" (rarity 1), "aaaa" (no match). Use descending arrow showing selection of "aaa" as winner (lowest rarity). Highlight winner in green with star icon.

### Editorial Images

- **header.png**: A modern banner showing a compression algorithm visualization. Left side shows long words, right side shows compressed versions. Center displays a trie with rarity scores glowing at nodes. Professional tech company aesthetic.
- **problem-illustration.png**: Side-by-side comparison of "Naive Linear Search" versus "Trie Optimization". Left shows nested loops with red X. Right shows elegant trie traversal with green checkmark. Include complexity annotations.
- **algorithm-steps.png**: Detailed flowchart showing: 1) Dictionary input, 2) Trie construction with rarity storage, 3) Sentence parsing, 4) Word-by-word trie traversal, 5) Best prefix selection logic, 6) Output generation. Clean professional diagram style.
- **visualization.png**: Large trie visualization for example dictionary. Color-code nodes by rarity level: green (low rarity), yellow (medium), red (high). Show multiple word traversal paths with different line styles.
