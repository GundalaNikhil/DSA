# Images for ARR-013

This folder contains visualization images for problem ARR-013.

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
- **header.png**: A sophisticated 1200x300 analytics dashboard banner. Bar charts are shown fading in opacity as they move left (representing age). Subtitle "Top-K with Recency Decay" in a sleek, modern data-viz style. Background is a deep, professional blue.
- **problem-illustration.png**: A timeline of events where each event is a dot labeled with `(value, timestamp)`. Exponential decay curves are plotted for each value, converging towards the time "Now". Badges show the current decayed scores.
- **example-1.png**: Events: `(3,0), (1,0), (3,5), (2,6), (1,9)`. `Now=10`, `D=5`, `k=2`. Compute scores: `1 -> 0.954`, `3 -> 0.503`, `2 -> 0.449`. A leaderboard displays Rank 1: Value 1, Rank 2: Value 3. The formula `e^(-(now-t)/D)` is clearly labeled.
- **example-2.png**: Events `(5,0), (5,1), (3,2)`. `Now=5`, `D=2`, `k=1`. Visual comparison of decay weights for Value 5 vs Value 3. Value 3 has a higher score due to recency. The output "3" is highlighted in gold.
- **algorithm-steps.png**: A flow diagram. Iterate Events -> Update Score Map: `score[v] += exp(-(now-t)/D)` (shown in a formula bubble) -> After Loop -> Sort by `(-score, value)` -> Take Top K. Note "O(n log n)".
- **visualization.png**: A scatter plot of timestamps per value. Color intensity represents weight (brighter = more recent). An adjacent leaderboard panel lists values sorted by their final decayed score.

### Editorial Images
- **header.png**: A neon-style leaderboard titled "Decay-Weighted Frequency". The background gradient moves from bright (recent) to dim (old), visually reinforcing the concept of decay.
- **problem-illustration.png**: Side-by-side bar charts. Left: "Raw Counts" (no decay). Right: "Decayed Scores" (older events faded). Arrows show the shift in ranking caused by the recency factor.
- **algorithm-steps.png**: Flowchart cards. Compute Score Map with Exp Decay -> Priority Queue / Sort by Score then Value. Include complexity "O(n log n)" and a stability note "Smaller Value on Tie".
- **visualization.png**: An exponential decay curve plot with sample time points marked. A table beside it computes per-value scores for a small sample dataset, highlighting the winning value(s).
