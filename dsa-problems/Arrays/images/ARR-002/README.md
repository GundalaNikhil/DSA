# Image Placeholders for ARR-002

This directory contains image assets for the Bench Flip With Locked Ends problem.

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
- **header.png**: A high-quality 1200x300 banner showing a long park bench viewed from above. The first and last seats are securely chained and locked with prominent padlock icons. The middle seats are shown in a dynamic "mid-flip" motion with curved arrows indicating reversal. Title "Bench Flip: Ends Locked" in bold, modern typography with blue/green accents.
- **problem-illustration.png**: A horizontal array of boxes indexed 0 to 4. Boxes 0 and 4 feature distinct lock icons and a subtle glow to indicate they are fixed. Curved arrows demonstrate the swapping of the inner segment (indices 1 to 3). Caption "Reverse Middle Only" in a clean font.
- **algorithm-steps.png**: A two-pointer diagram on the array `[9, 3, 8, 1, 5]`. Pointer `l` starts at index 1, and `r` starts at index 3. Show arrows `l -> 2 -> 3` and `r -> 2 -> 1` indicating the movement towards the center. The end cells (0 and 4) are shaded gray and labeled "Fixed". Include tags "O(n) Time" and "O(1) Space".
- **visualization.png**: A "Before/After" comparison. Top panel: `[9, 3, 8, 1, 5]`. Bottom panel: `[9, 1, 8, 3, 5]`. The anchored ends (9 and 5) are highlighted in green to show stability. The middle positions are annotated with a bracket labeled "Reversed Slice".
- **example-1.png**: A step-by-step frame sequence. Frame (a): Initial state `[9, 3, 8, 1, 5]`. Frame (b): Swap indices 1 and 3, resulting in `[9, 1, 8, 3, 5]`. Use clear arrows and labels "Swap 3 <-> 1" to visualize the action.
- **example-2.png**: A four-element case `[1, 2, 3, 4]`. Highlight the locked elements 1 and 4. Show the swap of the middle segment `[2, 3]` becoming `[3, 2]`. Final state `[1, 3, 2, 4]` with locks still visibly intact.

### Editorial Images
- **header.png**: A minimalist graphic of a split bench. Locks are prominent on the ends. Arrows meet in the center to symbolize the reversal process. Overlay text "Reverse Mid, Ends Locked" in a clean, flat style.
- **problem-illustration.png**: Two side-by-side panels. Left panel: Shows a full reversal (ends moving) crossed out with a red "X". Right panel: Shows the correct middle-only reversal with padlocks on the endpoints, checked with a green tick.
- **algorithm-steps.png**: A flowchart. Initialization box "l = 1, r = n-2" -> Decision diamond "while l < r" -> Action box "swap arr[l], arr[r]; l++; r--" -> End. Annotate with "O(1) Extra Space" and "O(n) Time".
- **visualization.png**: A pointer trace timeline across array positions. Show `l` and `r` positions for each iteration. Fixed endpoints remain shaded throughout. Snapshots of the array state after each swap are displayed below the timeline.
