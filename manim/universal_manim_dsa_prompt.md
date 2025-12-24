Universal Manim DSA Animation Prompt (v2.0)
Use this prompt to generate production-quality, Zero-Overlap Manim animations for any Data Structures and Algorithms (DSA) problem (Arrays, Graphs, Trees, DP, etc.).

1. Core Design Philosophy: "Strict Sequential Flow"
   To ensure 100% overlap prevention at any resolution:

Strict Separation: Never show two large conceptual points simultaneously.
Clear-and-Replace: Point A (centered) -> Wait -> FadeOut -> Point B (centered).
One Object at a Time: Especially during step-by-step traces, only highlight/show the current element of interest.
Standard Transitions: Every scene and every major segment must end with self.play(FadeOut(Group(\*self.mobjects))). 2. Topic-Specific Visualization Patterns
Arrays / Strings
Use Square or Rectangle groups for elements.
Always include indices (small text below/above the cells).
Use a Moving Arrow or a SurroundingRectangle to indicate pointers (e.g., i, j, left, right).
Graphs / Trees
Use Dot or Circle for nodes and Line or Arrow for edges.
BFS/DFS Trace: Change node color (e.g., White -> Green) as they are visited.
Weights: Place small Text next to edges.
Complexity / Logic
Use centered VGroups for multi-line logic.
Strict Rule: If a list has >4 items, split it into two sequential segments. 3. The "Standard Step-by-Step" Blueprint
Follow this scene sequence for every animation:

Intro & Problem: High-level goal and "Given" vs "Goal" (Sequential).
Real-World Analogy: Connect the abstract problem to a physical scenario.
Naive Approach: Explain the "simple but slow" way + Complexity Warning.
The "Epiphany" (Algorithm Insight): The key observation that makes the efficient solution work.
Dry Run / Step-by-Step Trace:
Show the input data structure.
Iteration 1: Show the logic, update the state, highlight changes.
Iteration 2: (Optional) Show a second iteration if the first isn't enough to see the pattern.
Final State: Show the completed data structure/result.
Complexity Analysis: Time and Space (Sequential segments).
Conclusion: Summary and final takeaway. 4. Implementation Guidelines
Color Key: GREEN (Success/Correct), RED (Error/Naive), BLUE (Active/Primary), YELLOW (Highlight), TEAL (Result).
Wait Times: self.wait(2.5) for concepts, self.wait(1.0) between loop steps.
Method Naming:
scene_1_intro
,
scene_2_problem
, etc.
Z-Index: Ensure pointers and highlights are on top. 5. Master Prompt for AI
"Generate a Manim script for [Problem Name].

Use the Strict Sequential Layout strategy (Zero Overlaps).
Every conceptual point must be shown individually in the center, and the previous point must FadeOut completely before the next appears.
For the Step-by-Step Trace, visualize [Array/Graph/Tree] elements clearly with indices and use a [Highlight/Arrow] to track the current operation.
Ensure every scene ends with a global FadeOut.
Focus on the [Optimized Algorithm Name] logic."
