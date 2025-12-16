# Images for ARR-010

This folder contains visualization images for problem ARR-010.

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
- **header.png**: A high-tech 1200x300 trading dashboard banner. A price line chart fluctuates across the screen. A shaded vertical band highlights the "Allowed Holding Window" `[dMin, dMax]`. A horizontal dashed line marks the "Cap C". Title "Early Discount Window".
- **problem-illustration.png**: A timeline of daily prices with days on the x-axis. A "Buy" point is chosen. The "Sell" point is constrained to a window `1..dMax` days later. The sell price is visually clipped to the Cap `C` line. Arrows indicate the duration constraints (min/max days).
- **example-1.png**: Prices `[7, 2, 5, 1, 9]`, `dMin=1`, `dMax=3`, `C=6`. Mark "Buy" at day 3 (price 1). Mark "Sell" at day 4 (price 9), but show it capped to 6. Profit calculation `6 - 1 = +5`. Annotate "Window Length 1 Day Fits Constraints".
- **example-2.png**: Declining prices `[5, 4, 3, 2, 1]`, `dMin=1`, `dMax=2`, `C=10`. Shaded potential windows show no positive spread (sell always lower than buy). A large badge displays "Max Profit = 0".
- **algorithm-steps.png**: A sliding window diagram. A window `[i-dMax, i-dMin]` slides across the price array. Inside, a Deque stores indices of minimum prices. For each sell day `i`, compute `profit = min(price[i], C) - bestBuy`. Update global max. Tag "O(n)".
- **visualization.png**: A dual plot chart. Series 1: Original Price (gray line). Series 2: Capped Price `min(price, C)` (blue line). Highlight the specific segment (buy to sell) that delivers the maximum profit. Annotate buy/sell days and window limits.

### Editorial Images
- **header.png**: A minimalist candlestick strip chart. A shaded region indicates the holding window. A horizontal line indicates the price cap. Title "Constrained Profit" in clean sans-serif.
- **problem-illustration.png**: A moving window depiction. A Deque container holds candidate buy indices. As the day advances, old entries beyond `dMax` drop out the back, and the new price is added. The "Best Buy" is always shown at the front.
- **algorithm-steps.png**: A flowchart. Loop `i` in `0..n-1` -> Add `price[i-dMin]` to Deque -> Remove items older than `dMax` -> `bestBuy = front` -> `sellVal = min(price[i], C)` -> `profit = sellVal - bestBuy` -> Update Max.
- **visualization.png**: Side-by-side comparison. Left: "Naive Exhaustive Search" showing nested loops checking every pair, shaded red. Right: "Sliding Window Min Queue" showing a single efficient pass, shaded green. Notes on time complexity improvement.
