# Images for ARR-007

This folder contains visualization images for problem ARR-007.

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
- **header.png**: A professional 1200x300 banner displaying a hostel roster clipboard with two columns "List A" and "List B" feeding into a single sorted line. Items from List A are tinted blue and have small "Priority" badges. Title "Merge With A First on Ties".
- **problem-illustration.png**: Two conveyor belts labeled "A" and "B" delivering sorted numbered boxes into a central merge funnel. When equal values arrive simultaneously, the box from belt A is shown moving first, while B's box waits. Arrows and a "Tie-Break" note emphasize the rule.
- **example-1.png**: A step table for `A=[1, 3, 3]`, `B=[3, 4]`. Rows show the pick order: `1(A)`, `3(A)`, `3(A)`, `3(B)`, `4(B)`. The final merged array `[1, 3, 3, 3, 4]` is shown below, color-coded by source (A=Blue, B=Green).
- **example-2.png**: Merge of `A=[2, 5]`, `B=[1, 3, 6]`. Step table showing picks: `1(B)`, `2(A)`, `3(B)`, `5(A)`, `6(B)`. Final merged array visualized with colored blocks to show the interleaving.
- **algorithm-steps.png**: A pointer diagram with `i` on Array A and `j` on Array B. Decision boxes: `if A[i] < B[j]` pick A; `else if A[i] > B[j]` pick B; `else` (tie) pick A. Increment pointers accordingly. Tag "O(n+m) Time".
- **visualization.png**: A timeline of chosen elements with source labels (A/B) for each step. Highlight a section where equal values occur, clearly showing A-labeled elements appearing before B-labeled ones.

### Editorial Images
- **header.png**: A modern merge sorter graphic with intertwined ribbons labeled A and B. A badge "A Wins Ties" is prominently displayed.
- **problem-illustration.png**: Side-by-side comparison. Left panel: "Wrong Merge" where B's equal element jumps ahead (marked with red X). Right panel: "Correct Merge" where A's equal elements come first (marked with green check).
- **algorithm-steps.png**: A flowchart of the loop `while(i<n || j<m)`. Compare `A[i]` vs `B[j]`. If equal, choose A then `i++`. Else choose smaller. Append to result. Include time/space tags "O(n+m)", "O(1) Extra".
- **visualization.png**: A bar chart of the merged output where bars are colored by source. Tie positions clearly show A-colored bars preceding B-colored bars at the same value height.
