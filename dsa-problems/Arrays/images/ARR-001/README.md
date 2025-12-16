# Image Placeholders for ARR-001

This directory contains image assets for the Snack Restock Snapshot problem.

## Required Images

1. **header.png** - Problem header/banner (1200x300px)
2. **problem-illustration.png** - Main concept visualization
3. **algorithm-steps.png** - Algorithm breakdown
4. **visualization.png** - Solution visualization
5. **example-1.png** - Example 1 walkthrough
6. **example-2.png** - Example 2 walkthrough

## Status

⏳ Placeholders - Replace with actual images

## Guidelines

- Use consistent colors (Blue: #3B82F6, Green: #10B981)
- Clear labels and annotations
- PNG format, optimized for web (<500KB each)

## Image Prompts

### Problem Images
- **header.png**: A high-quality, wide banner (1200x300px) featuring a stylized, modern illustration of a campus snack shop. On the left, neatly arranged shelves stocked with colorful snack boxes in vibrant but professional colors. On the right, a clipboard with the text "Prefix Averages" in a clean, bold sans-serif font. The background should be a subtle gradient of professional blue (#3B82F6) and green (#10B981). The style should be flat infographic with thin, elegant outlined icons, ensuring a clean and academic look suitable for a technical educational platform.
- **problem-illustration.png**: A clear, horizontal visualization of an array labeled "Day 1" through "Day n". Each array element is represented by a bar with stacked snack boxes, varying in height to represent quantity. Above these bars, a smooth, flowing polyline graph connects dot markers representing the "running average". A legend clearly distinguishes "Daily Deliveries" (bars) from "Prefix Average" (line). The background is a faint, clean grid to emphasize precision.
- **algorithm-steps.png**: A three-step horizontal strip diagram. Step 1: A "Running Sum" box filling up with liquid or blocks as it accumulates `arr[i]`. Step 2: A mathematical operation showing `avg = floor(sum / (i+1))` with a clear division symbol and floor brackets. Step 3: An arrow pointing to a result array where the calculated average is written. Connect steps with sleek arrows. Include a small "O(n)" complexity note in the corner.
- **visualization.png**: A side-by-side comparison using small multiples. Left chart: A bar chart showing daily deliveries with a dip at `arr[i]=0`. Right chart: A line chart showing the prefix average, highlighting how the zero value pulls the average down but doesn't crash it. Use clear axis labels "Day" and "Items" with consistent units.
- **example-1.png**: A timeline visualization for the array `[4, 6, 6, 0]`. For each day, show a box with the value. Below it, show the cumulative sum evolving: `4 -> 10 -> 16 -> 16`. Below that, show the prefix averages: `4 -> 5 -> 5 -> 4`. Use connecting arrows and captions "Day 0" to "Day 3" to guide the viewer through the progression.
- **example-2.png**: A three-day case for array `[10, 20, 30]`. Display sums `10 -> 30 -> 60` and averages `10 -> 15 -> 20` in clearly stacked rows. Include a "floor division" icon or annotation to explicitly show integer division, even though the results are exact integers in this case.

### Editorial Images
- **header.png**: A stylized, top-down view of a cashier checkout scene. A scanner beam highlights snack items moving across a belt. The headline "Running Totals, Quick Decisions" appears in a modern, sleek font against a smooth gradient background.
- **problem-illustration.png**: A split-panel comparison. Left panel: "Brute Force" approach showing circular, repetitive arrows over subarrays with a red "X" indicating inefficiency. Right panel: "Optimal" approach showing a single forward pass with a green arrow accumulating a running sum, labeled "Reuse Sum".
- **algorithm-steps.png**: A clean flowchart. Start node "sum = 0" -> Loop node "i from 0 to n-1" -> Process node "sum += arr[i]" -> Calculation node "avg = floor(sum / (i+1))" -> Output node "result[i] = avg". Include small tags for "O(n) Time" and "O(1) Extra Space".
- **visualization.png**: A contrast graphic. Left side: A grid of additions representing O(n^2) work, shaded in soft red. Right side: A single vertical column of n steps, shaded in fresh green. Overlay text "n^2 vs n" to emphasize the efficiency gain.
