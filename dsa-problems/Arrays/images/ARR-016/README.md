# Images for ARR-016

This folder contains visualization images for problem ARR-016.

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
- **header.png**: A sleek 1200x300 banner featuring a car power window control metaphor overlaying an array. A sliding window is highlighted with a toggle option to "Drop One" element. Title "Power Window With Drop".
- **problem-illustration.png**: A contiguous window of length `k` is highlighted. The smallest element inside the window is faded/optional. Arrows show the choice: "Keep All" vs "Drop One" to maximize the sum. Sums are labeled.
- **example-1.png**: Array `[2, 1, 5, 3, 2]`, `k=3`. Show three windows. Window `[2, 1, 5]`: Drop 1 -> Sum 7. Window `[1, 5, 3]`: Drop 1 -> Sum 8. Window `[5, 3, 2]`: Keep All -> Sum 10 (Best). Annotate "Best 10".
- **example-2.png**: Array `[10, 1, 20, 30]`, `k=3`. Highlight window `[1, 20, 30]`. Dropping 1 yields sum 50. Other windows: `[10, 1, 20]` (Best 30, drop 1). Mark global best 50.
- **algorithm-steps.png**: A sliding window diagram maintaining `windowSum` and `windowMin`. Per step: Compute `candidate = max(windowSum, windowSum - windowMin)` -> Update `maxAns`. Show window moving one step with outgoing/incoming values and a Min Structure (Deque or Multiset) tracking the minimum.
- **visualization.png**: A line plot of window positions vs sum. Two series: "Sum with No Drop" (gray) and "Sum with Best Drop" (green). The peak is highlighted. Include `k` label.

### Editorial Images
- **header.png**: A dashboard gauge labeled "Window Sum Boost" with a "Drop One" toggle lit up. Sleek gradient background.
- **problem-illustration.png**: Side-by-side comparison. Left: "Naive Approach" checking each drop candidate (nested loop icon). Right: "Efficient Approach" maintaining window minimum (deque icon). Labels "O(nk)" vs "O(n)".
- **algorithm-steps.png**: A flowchart. Initialize `windowSum/min` with first `k` -> `best = max(windowSum, windowSum - windowMin)` -> Slide Window: Subtract outgoing, Add incoming, Update Min Structure, Recompute Candidate -> Repeat. Note "O(n) Time".
- **visualization.png**: A timeline showing window positions and the accompanying Deque state (min at front). Computed best sums per position are plotted beneath, with the peak highlighted.
