# Images for ARR-005

This folder contains visualization images for problem ARR-005.

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
- **header.png**: A high-quality 1200x300 banner featuring a sleek, modern balanced scale sitting atop a numbered array line. The left pan is labeled "L Weight" and the right pan "R Weight", with the fulcrum perfectly balanced at index `i`. The color palette uses cool professional blues and greens.
- **problem-illustration.png**: A central index `i` highlighted on a horizontal array of 3D blocks. The left side sum is visualized as a stack labeled "Σleft × L", and the right side as "Σright × R". An equal sign `=` glows between them to indicate balance, with faint greater/less than arrows fading in the background.
- **example-1.png**: Step-by-step panels for array `[2, 3, -1, 3, 2]`, `L=2`, `R=1`. Highlight index 1 as the pivot. Show the left sum calculation `2` and right sum `4`. Display the weighted comparison: `2 × 2` vs `4 × 1`, resulting in `4 == 4` with a bright green checkmark. Other indices are lightly shaded to show they were checked and failed.
- **example-2.png**: Array `[1, 2, 3, 4]`, `L=R=1`. Iterate through indices 0 to 3 with small callout bubbles showing left/right sums not matching (e.g., `0 != 9`, `1 != 7`). A red "X" overlay with text "No Balance Index" appears at the end.
- **algorithm-steps.png**: A vertical flow diagram. Top: "Total Sum" computed. Loop: `i` from `0` to `n-1` with "Left Sum" tracked in a cumulative container. Process: Compute `Right Sum = Total - Left - arr[i]`. Decision: Compare `Left Sum * L` to `Right Sum * R`. Result: If equal, record answer and break. Badges: "O(n) Time", "O(1) Space".
- **visualization.png**: A dual line chart plotted across indices. One series represents `Left * L` (blue line), the other `Right * R` (green line). Mark the intersection points clearly. Highlight the smallest index where the lines cross as the solution.

### Editorial Images
- **header.png**: A blueprint-style sketch of a balanced scale superimposed over a technical grid background. Title "Weighted Balance Check" in architectural font. Labels "L" and "R" on the pans.
- **problem-illustration.png**: A split-panel comparison. Left panel: "Naive Approach" showing nested loops recomputing sums for every index, shaded in warning red. Right panel: "Optimized Approach" showing a single pass with running totals, shaded in efficient green. Text callouts "O(n^2)" vs "O(n)".
- **algorithm-steps.png**: A pseudocode card. Variables `total`, `leftSum` are highlighted. Arrows demonstrate the per-index update: `leftSum += arr[i]`, compute `rightSum`, compare products. Style is concise and code-like.
- **visualization.png**: A heatmap bar chart showing the difference `(Left * L) - (Right * R)` over indices. The zero line is bold. Cells near zero are lighter, and the actual zero crossing is marked with a distinct green marker.
