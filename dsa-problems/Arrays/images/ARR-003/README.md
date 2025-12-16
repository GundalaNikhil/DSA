# Image Placeholders for ARR-003

This directory contains images for the Shuttle Shift With Blackout problem.

## Required Images

1. **header.png** - Problem header/banner image
2. **problem-illustration.png** - Main problem concept illustration
3. **rotation-visual.png** - Visual representation of rotation with blackout
4. **example-walkthrough.png** - Step-by-step example walkthrough
5. **algorithm-steps.png** - Algorithm phases visualization
6. **example-1.png** - Example 1 detailed visualization

## Image Guidelines

- Use consistent color scheme across all images
- Blackout indices should be highlighted in red/orange
- Movable elements in blue/green
- Arrows to show rotation direction
- Clear labels and annotations

## Image Prompts

### Problem Images
- **header.png**: A futuristic 1200x300 banner depicting a high-tech shuttle conveyor belt moving left. Specific "blackout" stations are glowing red with lock icons, while movable cargo boxes slide left with a motion blur effect. Title "Shuttle Shift With Blackout" in a crisp, flat design style.
- **problem-illustration.png**: A horizontal array indexed 0 to 4. Cells 1 and 3 are shaded red with lock icons to represent "blackout" zones. A curved arrow above indicates a left rotation by `k=2`. Movable cells are colored blue/green and are shown shifting positions, while blackout cells remain static.
- **rotation-visual.png**: A ring diagram with five nodes. Blackout nodes are fixed in place (red, no movement lines). Blue nodes have curved arrows indicating a counter-clockwise rotation of two steps (1 -> 2 steps). Caption "Rotate Only Movable" in the center.
- **example-walkthrough.png**: Four frames for array `[1, 2, 3, 4, 5]`, blackout `{1, 3}`, `k=2`. Frame 1: Mark blackout positions. Frame 2: Extract movable values `[1, 3, 5]`. Frame 3: Rotate extracted list to `[5, 1, 3]`. Frame 4: Write back to indices 0, 2, 4 resulting in `[5, 2, 1, 4, 3]`. Use clear arrows and labels for each phase.
- **algorithm-steps.png**: A flowchart. Input "arr, k, blackoutSet" -> Process "Gather movable indices list & values" -> Process "Rotate values by k % len" (visualized with a slicing arrow) -> Loop "For each movable index, write rotated value back" -> Output. Tags: "O(n) Time", "O(m) Space".
- **example-1.png**: Before/After horizontal arrays. Before: `[1, 2, 3, 4, 5]` with indices 1 and 3 highlighted red. After: `[5, 2, 1, 4, 3]` with green arrows tracing the path of each movable element. Include a small note "k=2".

### Editorial Images
- **header.png**: A control panel UI with a toggle switch labeled "Blackout Indices" set to "ON" and a rotary knob set to `k=2`. Title "Constrained Rotation" in a futuristic dashboard aesthetic.
- **problem-illustration.png**: A ring of nodes. Blackout nodes are anchored with heavy chain icons. Movable nodes orbit around them with direction arrows. Side callout: "Blackout set stored in Hash Set for O(1) checks".
- **algorithm-steps.png**: A timeline sweep showing an index pointer moving `0 -> n-1`. It skips blackout slots (red) and fills only movable positions with pre-rotated values. Label "Single Linear Pass".
- **visualization.png**: A matrix grid of position vs. time step as rotation progresses. Blackout columns are shaded dark and remain unchanged. Movable columns shift upward-left. Annotation of complexity "O(n)".
