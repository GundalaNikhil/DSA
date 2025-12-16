# Images for ARR-012

This folder contains visualization images for problem ARR-012.

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
- **header.png**: A clean 1200x300 banner depicting an array timeline. An even-length measuring ruler overlays a teal-highlighted segment. The segment represents a "Zero Sum". Bold title "Even Zero Sum".
- **problem-illustration.png**: A prefix sum line chart. Repeated values are linked by highlighted horizontal bands. Parity markers (Even/Odd Index) are clearly shown on the x-axis, emphasizing that matching prefix sums must also match in index parity to yield an even length.
- **example-1.png**: Array `[1, -1, 3, -3, 2]`. Mark subarray indices 0-3 with sum 0 and length 4 (even). Show running prefix sums: `0 (start) -> 1 -> 0 -> 3 -> 0`. Highlight the return to 0 at indices 0 and 4 (length 4). Green highlight.
- **example-2.png**: Array `[2, -2, 5, -5, 1, -1]`. Show entire array sums to 0, length 6 (even). A green ribbon wraps the full range. Prefix sum starts at 0 and ends at 0, both at even indices (0 and 6).
- **algorithm-steps.png**: A Hash Map table keyed by `(PrefixSum, Parity)`. It stores the "Earliest Index". A timeline shows the scan: when a later index has the same key, it yields an even-length zero-sum subarray. Pseudo-note "If seen before, update maxLen".
- **visualization.png**: Split view. Left: Brute-force `O(n^2)` pair checking grid shaded red. Right: `O(n)` Prefix-Hash scan with arrows linking matching prefix sums of the same parity. Complexity badges.

### Editorial Images
- **header.png**: A clean number line with mirrored positive and negative bars canceling each other out to zero. Caption "Balance Over Even Spans".
- **problem-illustration.png**: "Parity Buckets" illustration. Prefix sums are plotted with "Even-Index Dots" vs "Odd-Index Dots". Matching color/level pairs indicate valid even-length segments.
- **algorithm-steps.png**: A flowchart. `runningSum += a[i]` -> `key = (sum, i % 2)` -> `if key unseen store i` -> `else candidateLen = i - firstIndex` -> `update maxLen`. Tags: "O(n) Time", "O(n) Space".
- **visualization.png**: A matrix plot of prefix sum occurrences. Bands show even spacing. The zero line is bold. Candidate bands are highlighted where parity matches.
