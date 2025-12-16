# Images for ARR-006

This folder contains visualization images for problem ARR-006.

## Required Images:

1. **header.png** - Problem header image
2. **problem-illustration.png** - Main problem concept illustration
3. **example-1.png** - Visualization of first example
4. **example-2.png** - Visualization of second example (if applicable)
5. **algorithm-steps.png** - Step-by-step algorithm visualization
6. **visualization.png** - Additional visualizations

## Image Guidelines:

- Use clear, professional diagrams
- Maintain consistent styling across all images
- Include labels and annotations
- Optimize for web (reasonable file size)
- Recommended format: PNG with transparency

## Image Prompts

### Problem Images
- **header.png**: A dynamic 1200x300 banner showing a conveyor belt moving numbered crates. Zeros are depicted as transparent or "ghost" crates sliding to the right. A digital counter reading "m swaps" is ticking down. Blue and green accents with a clean vector look.
- **problem-illustration.png**: An array of boxes labeled with indices. Zero values are faded. Non-zero values are shown shifting left over the zeros with curved motion arrows. A red stop sign appears to indicate when the swap limit `m` is reached.
- **example-1.png**: A three-panel strip for array `[0, 4, 0, 5, 7]`, `m=1`. Panel 1: Initial state. Panel 2: Swap 4 with the first zero (Swap Count 1/1). Panel 3: Stop with array `[4, 0, 0, 5, 7]`. Overlay a "Swap Counter" badge showing the limit reached.
- **example-2.png**: Four panels for array `[0, 0, 3, 0, 5]`, `m=3`. Show "Write Pointer" and swap actions. Swap 3 forward (1/3), Swap 5 forward (2/3). Final state `[3, 5, 0, 0, 0]`. Note "1 Unused Swap" to show budget was sufficient.
- **algorithm-steps.png**: A pointer diagram. "Read Index" scans forward, while "Write Index" waits at the next non-zero slot. Decrement a "Swap Counter" on each swap. Condition box: "If swaps > m: Break". Tags: "O(n) Time", "O(1) Space".
- **visualization.png**: A timeline chart with rows representing each step. Show the array state and the "Swap Count Remaining" bar. Highlight the difference between "Early Termination" (budget ran out) vs "Full Zero-Push" (budget sufficient).

### Editorial Images
- **header.png**: A minimalist slider control labeled "Swap Budget" positioned beside drifting zero digits. Background is a sleek, modern gradient.
- **problem-illustration.png**: A split view. Left: "Unbounded" scenario showing all zeros pushed to the end. Right: "Budget Capped" scenario showing the process stopping mid-array, with a red cap line labeled "Budget Reached".
- **algorithm-steps.png**: A flowchart. Init `write=0, swaps=0` -> Loop `i` in `0..n-1` -> Decision `if arr[i]!=0 and i!=write` -> Action `swap arr[i], arr[write]`, `swaps++` -> Check `if swaps > m break` -> `write++` -> End. Include complexity badges.
- **visualization.png**: Before/After bar arrays. Annotations "Swaps Used: X/m". Small note "O(n)". Highlights showing the exact positions where zeros shifted.
