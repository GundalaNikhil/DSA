# Image Generation Prompts for GRP-001: Campus Map BFS

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual of BFS concept on a graph

**Generation Prompt:**
```
Create a technical diagram showing a graph with BFS traversal:

- Display an undirected graph with 4-5 nodes labeled 0, 1, 2, 3, 4
- Show edges connecting the nodes
- Highlight the starting node (0) in green
- Use different colors to show BFS levels: level 0 (green), level 1 (blue), level 2 (orange)
- Add arrows showing the order of visitation
- Include a queue visualization showing nodes being processed
- Clean, professional style with blue/gray tones
- Size: 1200x800px
```

### 2. real-world-scenario.png

**Purpose:** Campus navigation system visualization

**Generation Prompt:**
```
Illustrate a university campus map scenario:

- Context: Top-down view of a campus with buildings as nodes
- Elements: Library (node 0), Cafeteria (node 1), Gym (node 2), Classroom (node 3)
- Show walkways as edges connecting buildings
- Highlight BFS exploration from the library
- Use concentric circles or levels to show distance from starting point
- Modern professional style with campus colors
- Size: 1200x800px
```

### 3. algorithm-visualization.png

**Purpose:** BFS algorithm flow diagram

**Generation Prompt:**
```
Create flowchart showing BFS algorithm:

- Start state: Initialize queue with source node
- Main loop: Dequeue, process, enqueue neighbors
- Decision points: "Is queue empty?", "Is neighbor visited?"
- Show queue state at each step
- Include visited array visualization
- Use arrows to show flow
- Annotations explaining each step
- Size: 1600x900px
```

### 4. algorithm-steps.png

**Purpose:** Step-by-step BFS execution

**Generation Prompt:**
```
Show BFS algorithm execution on the example graph:

- Display the graph: nodes 0, 1, 2, 3 with edges (0,1), (0,2), (1,3)
- Show 5 steps side by side:
  Step 1: Queue=[0], Visited=[0], Result=[]
  Step 2: Queue=[1,2], Visited=[0,1,2], Result=[0]
  Step 3: Queue=[2,3], Visited=[0,1,2,3], Result=[0,1]
  Step 4: Queue=[3], Visited=[0,1,2,3], Result=[0,1,2]
  Step 5: Queue=[], Visited=[0,1,2,3], Result=[0,1,2,3]
- Color code: green for current node, blue for enqueued, gray for visited
- Size: 1600x900px
```

### 5. example-1.png

**Purpose:** Example walkthrough visualization

**Generation Prompt:**
```
Visualize the example from the problem:

- Input graph with 4 nodes and edges (0,1), (0,2), (1,3)
- Show the graph structure clearly
- Annotate each node with its level (distance from 0)
- Show the BFS traversal order with numbered arrows: 1→0, 2→1, 3→2, 4→3
- Display the final output: "0 1 2 3"
- Include a legend explaining the notation
- Size: 1200x800px
```

## Specifications

- Format: PNG
- Resolution: 1200x800px standard, 1600x900px for complex diagrams
- Style: Technical documentation, clean and professional
- Colors: Blues (#2563eb), Greens (#059669), Oranges (#ea580c), Grays (#6b7280)
- Fonts: Clear, sans-serif fonts for labels and annotations
- Background: White or light gray (#f9fafb)
