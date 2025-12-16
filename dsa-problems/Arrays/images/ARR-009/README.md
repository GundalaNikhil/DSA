# Images for ARR-009

This folder contains visualization images for problem ARR-009.

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
- **header.png**: A sleek 1200x300 banner featuring a rolling line graph of array values. A digital paintbrush hovers over one interior point, applying a "smooth" blend effect that softens a sharp peak. Tagline "One Smooth Move" in modern typography against a cool gradient background.
- **problem-illustration.png**: A detailed bar chart representing an array with clear index labels. One middle bar is shown being replaced by a translucent "averaged" bar, derived from blending its neighbors. The value is explicitly shown as a floor calculation. The maximum subarray segment is highlighted with a glowing neon bracket.
- **example-1.png**: A three-panel sequence for `[-2, 3, -4, 5]`. Panel 1: Original bars with max subarray sum 5 highlighted. Panel 2: Smoothing index 2 changes `-4` to `1` (derived from `floor((3-4+5)/3)`), resulting in `[-2, 3, 1, 5]`. Panel 3: New max subarray sum 9 highlighted over `[3, 1, 5]`.
- **example-2.png**: For `[5, -10, 3, -2, 8]`. Show smoothing at index 3 changing `-2` to `3` (derived from `floor((3-2+8)/3)`). The resulting array `[5, -10, 3, 3, 8]` is displayed, with the max subarray sum 14 spanning the last three elements clearly marked.
- **algorithm-steps.png**: A diagram with three parallel tracks: `Left Max Ending [i-1]`, `Right Max Starting [i+1]`, and `Smoothed Val`. Arrows combine these three components to compute a candidate sum. A note "Kadane Precompute" connects to the side tracks.
- **visualization.png**: A heatmap table indexed by array position. Each cell shows the potential smoothed value and the resulting max subarray sum. The brightest cell marks the optimal smoothing position. Caption "Choose Best Index".

### Editorial Images
- **header.png**: An engineering dashboard interface with a "Smoothing Knob" adjusting a signal waveform. Subtitle "Kadane with a Tweak" in a clean, technical UI style.
- **problem-illustration.png**: Side-by-side comparison. Left panel: "Brute Force" showing red, heavy nested loops recomputing sums for every smooth position. Right panel: "Optimized" showing green, light linear passes precomputing prefix/suffix Kadane arrays. Badges "O(n^2)" vs "O(n)".
- **algorithm-steps.png**: A flowchart. Compute `leftBestEnding[]` via Kadane -> Compute `rightBestStarting[]` (reversed Kadane) -> Loop `i` from `1` to `n-2` -> Calculate `smoothedVal = floor((a[i-1]+a[i]+a[i+1])/3)` -> `candidate = max(0, leftBestEnding[i-1]) + smoothedVal + max(0, rightBestStarting[i+1])` -> Track Max -> Output.
- **visualization.png**: A line graph plotting the "Max Subarray Sum Achievable" if smoothing is applied at each index. The original max sum is overlaid as a baseline. Improvement peaks are labeled to show the impact of smoothing specific outliers.
