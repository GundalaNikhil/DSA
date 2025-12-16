# Images for ARR-004

This folder contains visualization images for problem ARR-004.

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
- **header.png**: A 1200x300 lab dashboard interface featuring analog temperature gauges and sliders labeled "[l, r]". The title "Offline Range Updates" is displayed in a bold, technical font. The color scheme uses cool blue and green gradients with a crisp vector art style.
- **problem-illustration.png**: A horizontal array of thermometers labeled indices 0 to n-1. Brackets highlight a range `[l, r]` with a `+x` tag applied. To the right, query cards reading "Sum l..r?" have arrows pointing to the final values.
- **example-1.png**: A step-by-step walkthrough for array `[1, 2, 3]`. Operations: `add 0 1 5`, `sum 0 2`, `add 2 2 -1`, `sum 1 2`. Panels show the Difference Array updates (+5 at index 0, -5 at index 2, -1/+1 adjustments), the final temperatures `[6, 7, 2]`, and the answers 16 and 9 highlighted in result boxes.
- **example-2.png**: Bar charts for `[5, 5, 5]`. Range add `0..2` by `+3` is visualized with difference spikes at indices 0 and 3. Resulting temperatures `[8, 8, 8]` are shown. A large badge displays "Sum 0..2 = 24".
- **algorithm-steps.png**: A four-box flow diagram. (1) Init `diff[0..n] = 0`. (2) For each add `l, r, x`: apply `diff[l] += x`, `diff[r+1] -= x`. (3) Prefix Sum of `diff` -> `temps`. (4) Prefix Sum of `temps` -> `prefixSum` to answer queries. Include "O(n+q) Time" and "O(n) Space" tags.
- **visualization.png**: A split view comparison. Left: Naive grid showing repeated range updates shaded red (slow). Right: Efficient pipeline with two prefix passes shaded green, with arrows labeled "One Build -> Many Queries".

### Editorial Images
- **header.png**: A precision thermometer grid background. Overlay text "Diff Array + Prefix Power" in a minimalist tech palette.
- **problem-illustration.png**: A timeline row of queries. Add ranges stack into a difference array (bars accumulating), followed by a "Freeze" icon, then sum queries reading from final prefix sums. Annotate "Offline Process".
- **algorithm-steps.png**: A flowchart. Build `diff` -> Cumulative `temps` via prefix -> Build `prefixSum` -> Answer any sum `l..r` by `prefix[r] - prefix[l-1]`. Include complexity labels for each stage.
- **visualization.png**: A heatmap bar chart showing cumulative additions by index. Overlay a smooth prefix-sum curve. Caption "Apply Once, Query Fast".
