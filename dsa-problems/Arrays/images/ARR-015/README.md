# Images for ARR-015

This folder contains visualization images for problem ARR-015.

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
- **header.png**: A clean 1200x300 banner depicting a theater seating chart from a top view. Some seats are faded or removed with "X" marks. A ruler overlay measures the widest gap between remaining seats. Title "Seat Gap After Removals".
- **problem-illustration.png**: Sorted seat positions on a number line. Indices to remove are crossed out. Arrows span between consecutive kept seats showing the distance. The "Max Gap" arrow is bolded and highlighted.
- **example-1.png**: Seats `[2, 5, 9, 10]`, remove index 1 (value 5). Show remaining seats at 2, 9, 10. Gaps: `9-2=7` and `10-9=1`. Badge "Max Gap = 7".
- **example-2.png**: Seats `[1, 3, 7, 12, 20]`, remove indices 0 and 2. Remaining seats: 3, 12, 20. Gaps: `12-3=9` and `20-12=8`. Badge "Max Gap = 9".
- **algorithm-steps.png**: A flow diagram. Convert `remove_indices` to Hash Set -> Iterate seats in order -> Skip removed -> Track `prev` kept seat -> Compute `gap = current - prev` -> Update `maxGap`. Tags "O(n) Time", "O(r) Space".
- **visualization.png**: Before/After strip. Top: All seats with removed ones grayed out. Bottom: Only kept seats with gap bars between them. A small table lists the gap values.

### Editorial Images
- **header.png**: A minimalist seating aisle graphic with red X markers on removed seats and a ruler measuring the largest distance. Caption "Max Gap After Removals".
- **problem-illustration.png**: A pointer iterating over seat positions. A hash-set icon indicates "O(1) Removed Check". Lines skip over deleted seats. `Prev` pointer is maintained.
- **algorithm-steps.png**: A flowchart. Build `removeSet` -> Find first kept seat as `prev` -> Loop for each next seat -> If not removed, compute gap & update max -> Set `prev = current` -> Output `maxGap`. Note "O(n) Time".
- **visualization.png**: A table listing: Index, Seat Value, Removed? (Yes/No), Computed Gap, Current Max. This illustrates the linear scan process.
