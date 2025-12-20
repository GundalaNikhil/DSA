# Image Generation Prompts for GMT-001: Pile Split Choice

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual of problem concept

**Generation Prompt:**
```
Create a technical diagram showing the Pile Split Game:
- Display a pile of 6 stones.
- Show an arrow splitting it into two piles: one with 2 stones, one with 4 stones.
- Label: "Valid Move: Different Sizes".
- Show another arrow splitting it into 3 and 3 stones with a red "X" cross.
- Label: "Invalid Move: Equal Sizes".
- Clean, professional style with blue/gray tones.
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Real-world application visualization

**Generation Prompt:**
```
Illustrate the Uneven Break scenario:
- Context: A person breaking a wooden stick or chocolate bar.
- Action: Breaking it into two clearly unequal pieces.
- Metaphor: "Must be uneven to continue".
- Modern professional style.
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Algorithm flow diagram

**Generation Prompt:**
```
Create flowchart showing Grundy Calculation:
- Node: State n.
- Edges: All valid splits (a, b).
- Calculation: G(n) = mex({ G(a) XOR G(b) }).
- Example: G(6) derived from splits (1,5), (2,4).
- Size: 1600x900px
```

### 4. example-1.png

**Purpose:** Example walkthrough

**Generation Prompt:**
```
Visualize the example n=3:
- Initial: Pile of 3.
- Move: Split into 1 and 2.
- Result: Piles {1, 2}.
- Annotation: "No valid moves from 1 or 2".
- Outcome: "Player 1 Wins".
- Size: 1200x800px
```

## Specifications

- Format: PNG
- Resolution: 1200x800px standard, 1600x900px complex
- Style: Technical documentation
- Colors: Blues (#2563eb), Greens (#059669), Grays (#6b7280)
