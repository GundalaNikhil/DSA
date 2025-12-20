# Image Generation Prompts for GMT-011: Blocking Tokens on DAG

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual of problem concept

**Generation Prompt:**
```
Create a technical diagram showing Two Tokens on a Graph:
- Nodes 1, 2, 3, 4. Edges 1->2, 2->3, 1->3.
- Token A (Red) at Node 1.
- Token B (Blue) at Node 2.
- Arrow from 1 to 2 with a "X" (Blocked).
- Arrow from 1 to 3 (Valid).
- Clean, professional style.
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Real-world application visualization

**Generation Prompt:**
```
Illustrate the Robot Corridor scenario:
- Two robots in narrow corridors.
- One robot blocking the path of the other.
- Sci-fi industrial setting.
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** Algorithm flow diagram

**Generation Prompt:**
```
Create diagram showing State Space Search:
- State (1, 2) -> Moves to (3, 2).
- State (3, 2) -> No moves for P2 (since 2->3 blocked).
- Highlight Winning/Losing states in a small tree.
- Size: 1600x900px
```

### 4. example-1.png

**Purpose:** Example walkthrough

**Generation Prompt:**
```
Visualize the example:
- Initial: {1, 2}.
- P1 moves 1->3. New: {3, 2}.
- P2 at {3, 2}. 2->3 is blocked. 3 has no outgoing.
- P2 Loses.
- Size: 1200x800px
```

## Specifications

- Format: PNG
- Resolution: 1200x800px standard, 1600x900px complex
- Style: Technical documentation
- Colors: Blues (#2563eb), Greens (#059669), Grays (#6b7280)
