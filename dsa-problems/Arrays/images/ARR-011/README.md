# Images for ARR-011

This folder contains visualization images for problem ARR-011.

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
- **header.png**: A dramatic 1200x300 banner showing a rooftop silhouette against a stormy sky. Carpenters are adding planks to lower sections to reinforce it. A raincloud hovers above to imply leak prevention. Title "Leaky Roof Reinforcement".
- **problem-illustration.png**: An array skyline with valleys and peaks. Translucent overlays show "Added Planks" raising heights to make the left side non-decreasing up to a peak, and the right side non-increasing after the peak. The chosen peak index is marked with a flag.
- **example-1.png**: Heights `[4, 1, 3, 1, 5]`. Highlight choosing peak at index 4 (value 5). Bars show original heights in gray and added planks in hatched orange. The result `[4, 4, 4, 4, 5]` is non-decreasing. Total added height `7` is displayed.
- **example-2.png**: Heights `[1, 2, 3, 2, 1]`. Show that the shape is already a perfect pyramid. A green checkmark and "Cost 0" badge indicate no additions needed.
- **algorithm-steps.png**: Two line charts overlaid. Chart 1: `Prefix Max Non-Decreasing`. Chart 2: `Suffix Max Non-Increasing`. Combine them to show the `Target Height` at each index. Annotation: `Cost = Sum(Target - Original)`. Pick Minimum.
- **visualization.png**: A heatmap or bar chart with "Peak Index" on the x-axis and "Total Added Height" on the y-axis. The lowest bar is highlighted in green as the optimal peak choice.

### Editorial Images
- **header.png**: A blueprint cross-section of a roof with precise dimensions and plank overlays. Caption "Build the Cheapest Peak" in architectural font.
- **problem-illustration.png**: Split panel. Left: "Naive Approach" raising everything to the global maximum height (costly, shaded red). Right: "Optimal Approach" using per-peak prefix/suffix logic (efficient, shaded green). Cost numbers compared.
- **algorithm-steps.png**: A flowchart. Compute `left[i] = max(left[i-1], h[i])` -> Compute `right[i] = max(right[i+1], h[i])` -> `target[i] = min(left[i], right[i])` -> `cost = Sum(target[i] - h[i])` -> Choose Min. Tags: "O(n) Time", "O(n) Space".
- **visualization.png**: A stacked bar chart showing added height per index for several candidate peaks. The cheapest column is highlighted. A note on the "Dynamic Programming Insight".
