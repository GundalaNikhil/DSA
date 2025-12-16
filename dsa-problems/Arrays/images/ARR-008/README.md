# Images for ARR-008

This folder contains visualization images for problem ARR-008.

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
- **header.png**: A clean 1200x300 banner illustrating a sorted number line with two prominent pointers (L and R) converging. Certain indices are blocked with red "Forbidden" tags. A speech bubble shows "Target Sum T". Background is a clean tech gradient.
- **problem-illustration.png**: A horizontal array showing the Left pointer at the smallest non-forbidden index and the Right pointer at the largest. Forbidden indices are crossed out in red. Arrows indicate pointers moving inward. A valid pair of cells is highlighted in green when found.
- **example-1.png**: Walkthrough for `arr=[1, 4, 6, 7]`, `target=11`, `forbidden={0}`. Frames show: L skipping index 0 (forbidden), landing on 4. R starts on 7. Sum `4 + 7 = 11`. Green checkmark "True".
- **example-2.png**: `arr=[2, 3, 5, 8]`, `target=10`, `forbidden={1, 3}`. Frames show attempts: L=0 (2), R=3 (forbidden) -> R shifts left to 2 (5). Sum `2 + 5 = 7 < 10` -> L moves right. L hits forbidden index 1, skips to 2. Pointers cross. Red "False" badge.
- **algorithm-steps.png**: A flowchart. Set `L=0, R=n-1` -> Loop `while L < R` -> Sub-loop "Advance L while L forbidden" -> Sub-loop "Advance R while R forbidden" -> Check `if L >= R break` -> Compute `s = arr[L] + arr[R]` -> Decision `if s == target return true` -> `else if s < target L++` -> `else R--` -> End "Return False". Complexity "O(n)".
- **visualization.png**: A table tracking the process. Columns: Iteration, L Index/Value, R Index/Value, Sum, Action Taken (Move L, Move R, Skip Forbidden), Result. This visualizes the efficiency of skipping.

### Editorial Images
- **header.png**: A security gate metaphor with blocked slots (forbidden) and a scanning beam searching for two values summing to a target. Sleek gradient backdrop. Title "Two Pointers with Forbidden".
- **problem-illustration.png**: A pointer movement track over an array. A hash-set icon indicates "O(1) Forbidden Checks". Arrows skip over red blocked cells. Green highlight on the accepted pair.
- **algorithm-steps.png**: A state machine diagram. State "Sum < Target" -> Transition "Move L Right". State "Sum > Target" -> Transition "Move R Left". State "Sum == Target" -> Transition "Success". Preprocessing step "Skip Forbidden via Hash Set". Loop termination when "L >= R". Annotate "O(n) Time", "O(f) Space".
- **visualization.png**: A decision tree showing iterations and branches pruned by forbidden indices versus valid comparisons. Final leaves labeled "Found" or "Exhausted".
