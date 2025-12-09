# Extract RGB Components from Hex

**Problem ID:** BIT-003
**Display ID:** 98
**Question Name:** Extract RGB Components from Hex
**Slug:** rgb-color-mixer
**Title:** Extract RGB Components from Hex
**Difficulty:** Easy
**Premium:** No
**Tags:** Bit Manipulation, Bit Shifts, Graphics

## Problem Description

Given a 24-bit integer representing an RGB color in hexadecimal format (0xRRGGBB), extract the individual Red, Green, and Blue components. Additionally, implement functions to construct an RGB color from components and to blend two colors by averaging their components.

## A Simple Scenario (Daily Life Usage)

You're building a color picker tool for a design app like Figma. A designer selects the color `#FF5733` (orange). Your app needs to show them: Red=255, Green=87, Blue=51. They want to blend it 50/50 with `#3498DB` (blue). Your function extracts both colors' RGB values, averages them: R=(255+52)/2=153, G=(87+152)/2=119, B=(51+219)/2=135, creating `#99779B` (purple).

## Your Task

Implement the following functions:
- `extractRed(color)`: Extract the red component (bits 16-23)
- `extractGreen(color)`: Extract the green component (bits 8-15)
- `extractBlue(color)`: Extract the blue component (bits 0-7)
- `constructRGB(red, green, blue)`: Combine components into a 24-bit color
- `blendColors(color1, color2)`: Blend two colors by averaging each component

Where `color` is an integer between 0 and 0xFFFFFF (16777215).

## Why is it Important?

This problem teaches you how to:

- Use right bit shifts to extract high-order bits
- Use bitwise AND with masks to isolate bit ranges
- Use left bit shifts to pack values
- Apply bit manipulation to graphics programming
- Understand RGB color representation
- Work with hexadecimal numbers

## Examples

### Example 1:

**Input:** `color = 0xFF5733, operation = "extractRed"`
**Output:** `255`
**Explanation:** 0xFF5733 in binary is `11111111 01010111 00110011`. Red is bits 16-23 = 11111111 = 255.

### Example 2:

**Input:** `color = 0xFF5733, operation = "extractGreen"`
**Output:** `87`
**Explanation:** Green is bits 8-15 = 01010111 = 87.

### Example 3:

**Input:** `color = 0xFF5733, operation = "extractBlue"`
**Output:** `51`
**Explanation:** Blue is bits 0-7 = 00110011 = 51.

### Example 4:

**Input:** `red = 255, green = 87, blue = 51, operation = "constructRGB"`
**Output:** `0xFF5733` (16733011 in decimal)
**Explanation:** Shift red left 16 bits, green left 8 bits, combine with blue using OR.

### Example 5:

**Input:** `color1 = 0xFF5733, color2 = 0x3498DB, operation = "blendColors"`
**Output:** `0x99779B` (10057627 in decimal)
**Explanation:**
- color1: R=255, G=87, B=51
- color2: R=52, G=152, B=219
- Average: R=(255+52)/2=153, G=(87+152)/2=119, B=(51+219)/2=135
- Result: 0x99779B

### Example 6:

**Input:** `color1 = 0x000000, color2 = 0xFFFFFF, operation = "blendColors"`
**Output:** `0x7F7F7F` (8355711 in decimal)
**Explanation:** Blending black and white gives medium gray (127, 127, 127).

## Constraints

- 0 ≤ color ≤ 0xFFFFFF (16777215)
- 0 ≤ red, green, blue ≤ 255
- All operations should run in O(1) time
- Use only bitwise operations (no string parsing)
- For blending, use integer division (floor)

## Asked by Companies

- Adobe
- Figma
- Canva
- Sketch
