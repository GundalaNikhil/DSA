# Images for ARR-014

This folder contains visualization images for problem ARR-014.

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
- **header.png**: A vivid 1200x300 banner illustrating a boarding queue with three zones: 0s, 1s (fixed), and 2s. The 1s are pinned with heavy anchor icons. Arrows show 0s drifting to the left and 2s drifting to the right. Title "Fixed Ones, Sort Around".
- **problem-illustration.png**: An array with slots labeled by index. Cells with value `1` have pushpin icons indicating they cannot move. Arrows push loose `0`s to the earliest free spots left of pins, and `2`s to the latest free spots right of pins.
- **example-1.png**: Walkthrough for `[2, 1, 0, 2, 0, 1]`. Mark fixed 1s at indices 1 and 5. Show "Fill Step": placing 0s into positions 0 and 2. Then place 2s into remaining free slots. Final array `[0, 1, 0, 1, 2, 2]` is highlighted.
- **example-2.png**: For `[0, 1, 2, 1, 0]`. Pins at indices 1 and 3. Fill 0s into leftmost free positions, 2s into rightmost. Final `[0, 1, 0, 1, 2]` with anchors unchanged.
- **algorithm-steps.png**: A two-pass schematic. Pass 1: Left -> Right fill with 0s, skipping pinned 1s. Pass 2: Right -> Left fill with 2s, skipping pinned 1s and already filled cells. Tags "O(n) Time", "O(1) Space".
- **visualization.png**: Before/After arrays color-coded by value (0=Blue, 1=Gray, 2=Green). Fixed positions are marked with anchors. Side counters show counts of 0s and 2s consumed during fills.

### Editorial Images
- **header.png**: A clean tri-color stripe graphic. The middle stripe (1s) has anchor markers. Caption "Sort Around Anchors" in modern font.
- **problem-illustration.png**: Side-by-side comparison. Left: "Wrong Approach" swapping a 1 out (marked with red X). Right: "Correct Approach" leaving 1s fixed (green check) while moving 0s and 2s around them.
- **algorithm-steps.png**: A flowchart showing `leftFill` pointer advancing (skipping anchors) to place 0s, and `rightFill` pointer retreating to place 2s. Complexity notes "O(n) Time", "O(1) Space".
- **visualization.png**: A timeline of pointer movements with index markers. Skipped anchors are highlighted. Placements of 0s and 2s are annotated step-by-step.
