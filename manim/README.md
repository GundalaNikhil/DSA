# Manim Video Scripts for DSA Problems

This directory contains Manim animation scripts for all DSA problems organized by topic.

## Structure

The folder structure mirrors the `dsa-problems` directory:

```
manim/
├── AdvancedGraphs/
│   └── video-scripts/
│       ├── AGR-001-min-cut-small-graph.py
│       ├── AGR-002-max-flow-vertex-capacity.py
│       └── ...
├── Arrays/
│   └── video-scripts/
│       ├── ARR-001-snack-restock-snapshot.py
│       ├── ARR-002-bench-flip-locked-ends.py
│       └── ...
├── Bitwise/
│   └── video-scripts/
│       └── ...
└── [Other Topics]/
    └── video-scripts/
        └── ...
```

## Topics Covered

1. **AdvancedGraphs** - Advanced graph algorithms (Min-Cut, Max Flow, etc.)
2. **Arrays** - Array manipulation and algorithms
3. **Bitwise** - Bitwise operations and tricks
4. **Concurrency** - Concurrent programming patterns
5. **DP** - Dynamic Programming
6. **GameTheory** - Game theory problems
7. **Geometry** - Computational geometry
8. **Graphs** - Basic and intermediate graph algorithms
9. **GraphsBasics** - Fundamental graph concepts
10. **Greedy** - Greedy algorithms
11. **Hashing** - Hash-based data structures and algorithms
12. **Heaps** - Heap data structures and priority queues
13. **LinkedLists** - Linked list problems
14. **MathAdvanced** - Advanced mathematical algorithms
15. **NumberTheory** - Number theory problems
16. **Probabilistic** - Probabilistic algorithms
17. **ProbabilisticDS** - Probabilistic data structures
18. **Queues** - Queue-based problems
19. **Recursion** - Recursive problem solving
20. **SegmentTree** - Segment tree data structure
21. **Sorting** - Sorting algorithms
22. **Stacks** - Stack-based problems
23. **Strings** - String manipulation
24. **StringsClassic** - Classic string algorithms
25. **Trees** - Tree data structures
26. **TreesDP** - Dynamic programming on trees
27. **Tries** - Trie data structure

## Script Template

Each script file follows this template:

```python
"""
Manim animation script for [PROBLEM-ID]

This script creates an animated visualization for the problem:
[PROBLEM-ID]

Topic: [Topic]
"""

from manim import *


class [ClassName]Scene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("[PROBLEM-ID]", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # TODO: Add animation implementation

        self.wait(2)
```

## Usage

To run a specific animation:

```bash
manim -pql [Topic]/video-scripts/[PROBLEM-ID].py [ClassName]Scene
```

For example:

```bash
manim -pql AdvancedGraphs/video-scripts/AGR-001-min-cut-small-graph.py Agr001MinCutSmallGraphScene
```

## Statistics

- **Total Topics**: 27
- **Total Problem Scripts**: 438
- **Average Problems per Topic**: ~16

## Generation Date

Created: December 24, 2025

---

_This structure was automatically generated to match the problem files in `dsa-problems/[Topic]/problems/`_
