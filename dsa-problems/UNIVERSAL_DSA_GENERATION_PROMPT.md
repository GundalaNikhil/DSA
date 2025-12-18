# Universal DSA Problem Generation Prompt

## Purpose

This is a **generic, reusable prompt** for generating consistent DSA problem content across **ALL topics** (Arrays, Graphs, Trees, DP, Strings, etc.). It maintains the structure established by DP-001 but is topic-agnostic.

---

## 📁 File Structure (Required for Every Problem)

```
[TOPIC]/
├── problems/[TOPIC]-XXX-[slug].md          # Problem statement
├── editorials/[TOPIC]-XXX-[slug].md        # Complete editorial with solutions
├── testcases/[TOPIC]-XXX-[slug].yaml       # Test cases (samples + public + hidden)
├── quizzes/[TOPIC]-XXX-[slug].yaml         # Quiz questions
└── images/[TOPIC]-XXX/README.md            # Image generation prompts (optional)
```

**Examples:**

- `Arrays/problems/ARR-001-two-sum.md`
- `Graphs/problems/GRP-015-shortest-path-dijkstra.md`
- `Trees/problems/TRE-008-lowest-common-ancestor.md`

---

## 🎯 Naming Conventions

### Topic Prefixes

| Topic           | Prefix | Example |
| --------------- | ------ | ------- |
| Arrays          | ARR    | ARR-001 |
| Strings         | STR    | STR-001 |
| LinkedLists     | LL     | LL-001  |
| Stacks          | STK    | STK-001 |
| Queues          | QUE    | QUE-001 |
| Trees           | TRE    | TRE-001 |
| Graphs          | GRP    | GRP-001 |
| GraphsBasics    | GRB    | GRB-001 |
| AdvancedGraphs  | AGR    | AGR-001 |
| Hashing         | HSH    | HSH-001 |
| Heaps           | HEP    | HEP-001 |
| DP              | DP     | DP-001  |
| Greedy          | GRD    | GRD-001 |
| Sorting         | SRT    | SRT-001 |
| Recursion       | REC    | REC-001 |
| Bitwise         | BIT    | BIT-001 |
| MathAdvanced    | MTH    | MTH-001 |
| NumberTheory    | NUM    | NUM-001 |
| Geometry        | GEO    | GEO-001 |
| SegmentTree     | SEG    | SEG-001 |
| Tries           | TRI    | TRI-001 |
| TreesDP         | TDP    | TDP-001 |
| StringsClassic  | STC    | STC-001 |
| GameTheory      | GMT    | GMT-001 |
| Probabilistic   | PRB    | PRB-001 |
| ProbabilisticDS | PDS    | PDS-001 |
| Concurrency     | CON    | CON-001 |

### Problem ID Format

```
[TOPIC]_[DESCRIPTION_CAPS]__[4_RANDOM_DIGITS]
```

**Examples:**

- `ARR_TWO_SUM__4821`
- `GRP_SHORTEST_PATH_DIJKSTRA__7392`
- `TRE_LCA_BINARY_TREE__1847`
- `DP_CLIMB_CRACKED_MAXJ__7314`

---

## 📋 1. PROBLEM FILE TEMPLATE

**Path:** `[TOPIC]/problems/[TOPIC]-XXX-[slug].md`

### Frontmatter (Exact Format)

```yaml
---
problem_id: [TOPIC]_[DESCRIPTION]__[4_DIGITS]
display_id: [TOPIC]-XXX
slug: [kebab-case-description]
title: "[Clear Problem Title]"
difficulty: [Easy|Medium|Hard]
difficulty_score: [10-90]
topics:
  - [Main Topic: Arrays, Graphs, Trees, etc.]
  - [Secondary Topic 1]
  - [Secondary Topic 2]
tags:
  - [topic-lowercase]
  - [technique-name]
  - [difficulty-level]
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
```

### Content Structure (150-250 lines)

```markdown
# [TOPIC]-XXX: [Problem Title]

## Problem Statement

[Clear, detailed problem description]
[What you're given, what you need to compute, constraints]
[Any special rules or conditions]

![Problem Illustration](../images/[TOPIC]-XXX/problem-illustration.png)

## Input Format

- [Line 1: description]
- [Line 2: description]
- [Additional lines as needed]

## Output Format

[Single line describing exact output format]

## Constraints

- [Constraint 1 with range: e.g., `1 <= n <= 100000`]
- [Constraint 2]
- [Constraint 3]
- [Edge case constraints]

## Example

**Input:**
```

[Exact input format]

```

**Output:**
```

[Exact output format]

````

**Explanation:**

[Step-by-step walkthrough of the example]
[Why this is the answer]
[Show intermediate steps if helpful]

![Example Visualization](../images/[TOPIC]-XXX/example-1.png)

## Notes

- [Important clarification 1]
- [Important clarification 2]
- [Important clarification 3]

## Related Topics

[Topic 1], [Topic 2], [Topic 3]

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public [ReturnType] [methodName]([parameters]) {
        // Your implementation here
        return [default_value];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Read input
        [input_parsing_code]

        Solution solution = new Solution();
        [ReturnType] result = solution.[methodName]([arguments]);

        System.out.println(result);
        sc.close();
    }
}
````

### Python

```python
def [function_name]([parameters]) -> [ReturnType]:
    # Your implementation here
    return [default_value]

def main():
    # Read input
    [input_parsing_code]

    result = [function_name]([arguments])
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    [ReturnType] [methodName]([parameters]) {
        // Your implementation here
        return [default_value];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Read input
    [input_parsing_code]

    Solution solution;
    cout << solution.[methodName]([arguments]) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  [methodName]([parameters]) {
    // Your implementation here
    return [default_value];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  // Parse input
  [input_parsing_code]

  const solution = new Solution();
  console.log(solution.[methodName]([arguments]));
});
```

````

**Critical Requirements:**
- ✅ **Exactly 1 example** (not multiple)
- ✅ **All 4 language templates** (Java, Python, C++, JavaScript)
- ✅ **Include `time_limit: 2000` and `memory_limit: 256`** in frontmatter
- ✅ **Image references** (even if not generated yet)
- ✅ **150-250 lines total**

---

## 📝 2. EDITORIAL FILE TEMPLATE

**Path:** `[TOPIC]/editorials/[TOPIC]-XXX-[slug].md`

### Frontmatter (NO time_limit/memory_limit)

```yaml
---
problem_id: [SAME_AS_PROBLEM]
display_id: [TOPIC]-XXX
slug: [same-slug]
title: "[Same Title]"
difficulty: [Same]
difficulty_score: [Same]
topics:
  - [Same as problem]
tags:
  - [Same as problem]
premium: true
subscription_tier: basic
---
````

### Content Structure (500-750 lines)

```markdown
# [TOPIC]-XXX: [Problem Title]

## 📋 Problem Summary

[2-3 sentence concise summary]
[Key challenge that makes it interesting]

## 🌍 Real-World Scenario

**Scenario Title:** [Engaging, Realistic Context]

[3-4 paragraphs describing realistic application]
[Make it relatable to software engineering]
[Explain why efficient solution matters]

**Why This Problem Matters:**

- [Practical reason 1]
- [Practical reason 2]
- [Practical reason 3]

![Real-World Application](../images/[TOPIC]-XXX/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: [Concept Visualization]
```

[Create ASCII art showing problem structure]
[Label key components]
[Show relationships]
[Include legend]

Example for Array problem:
Index: 0 1 2 3 4
Array: [3] [7] [1] [9] [2]
↑ ↑
|---------|
target sum = 10

Legend:
[ ] = array element
↑ = pointer/index
--- = relationship

```

## ✅ Input/Output Clarifications (Read This Before Coding)

- [Critical clarification 1]
- [Critical clarification 2]
- [Critical clarification 3]

Common interpretation mistake:

- ❌ [Wrong interpretation]
- ✅ [Correct interpretation]

### [Core Concept Section]

[Explain the fundamental approach]

### Why [Naive Approach] is too slow

[Explain time complexity issue]
[Give concrete numbers]

## Naive Approach

### Intuition

[Natural first thought]

### Algorithm

1. [Step 1]
2. [Step 2]
3. [Step 3]

### Time Complexity

- [Big-O with explanation]

### Space Complexity

- [Big-O with explanation]

### Why This Works

[Correctness explanation]

### Limitations

- [Why it's too slow]
- [What constraints it violates]

## [Optional: Better Intermediate Approach]

[If applicable, show progression]

### Intuition

[Key insight]

### Algorithm

1. [Step 1]
2. [Step 2]

### Time Complexity

- [Big-O]

### Space Complexity

- [Big-O]

### Decision Tree

```

[ASCII decision tree or flow diagram]

Example:
For each element in array:
│
├─ Check condition A
│ │
│ ├─ YES: [action 1]
│ │
│ └─ NO: [action 2]
│
└─ Update [data structure]

````

## Optimal Approach

### Key Insight

[Critical optimization insight]
[Why this makes it faster]

### Algorithm

1. [Step 1 with details]
2. [Step 2 with details]
3. [Step 3 with details]

### Time Complexity

- [Big-O with full explanation]

### Space Complexity

- [Big-O with explanation]

### Why This Is Optimal

[Theoretical argument]

![Algorithm Visualization](../images/[TOPIC]-XXX/algorithm-visualization.png)
![Algorithm Steps](../images/[TOPIC]-XXX/algorithm-steps.png)

## Implementations

### Java

```java
[Full, complete, working solution with comments]
[Include input parsing in main]
````

### Python

```python
[Full, complete, working solution with comments]
[Include input parsing in main]
```

### C++

```cpp
[Full, complete, working solution with comments]
[Include fast I/O: ios::sync_with_stdio(false)]
```

### JavaScript

```javascript
[Full, complete, working solution with comments]
[Include readline interface setup]
```

## 🧪 Test Case Walkthrough (Dry Run)

Use the sample:

- [List input values]
- [List special conditions]

We maintain:

- [Variable 1] = [description]
- [Variable 2] = [description]

Initialize:

- [Initial state]
- [Why these values]

Now iterate:

| Step | [col1] | [col2] | Explanation | [col3] | [col4] |
| ---: | :----: | -----: | ----------- | ------ | -----: |
|    1 | [val]  |  [val] | [reasoning] | [val]  |  [val] |
|    2 | [val]  |  [val] | [reasoning] | [val]  |  [val] |
|    3 | [val]  |  [val] | [reasoning] | [val]  |  [val] |

[Observations from table]

Answer is `[final_answer]`.

![Example Visualization](../images/[TOPIC]-XXX/example-1.png)

## ✅ Proof of Correctness

### Invariant

[Loop invariant or key property]

### Why the approach is correct

[Mathematical/logical argument]
[Base case and inductive step if applicable]

## 💡 Interview Extensions (High-Value Add-ons)

- **[Extension 1]:** [Variation or follow-up]
- **[Extension 2]:** [Another extension]
- **[Extension 3]:** [Advanced follow-up]

## Common Mistakes to Avoid

1. **[Mistake 1 Title]**

   - [Description]
   - ❌ Wrong: [what not to do]
   - ✅ Correct: [what to do]

2. **[Mistake 2 Title]**

   - [Description]
   - [Why wrong]
   - [How to fix]

3. **[Mistake 3 Title]**

   - [Description]
   - [Impact]
   - [Prevention]

4. **[Mistake 4 Title]**

   - [Description]

5. **[Mistake 5 Title]**

   - [Description]

## Related Concepts

- [Concept 1]
- [Concept 2]
- [Concept 3]
- [Concept 4]

````

**Critical Requirements:**
- ✅ **500-750 lines**
- ✅ **Emojis:** 📋 🌍 ✅ 🧪 💡
- ✅ **Real-world scenario:** 3-4 paragraphs
- ✅ **ASCII diagrams** for visualization
- ✅ **Full implementations** in all 4 languages
- ✅ **Common mistakes:** 3-5 with ❌ ✅
- ✅ **NO time_limit/memory_limit** in frontmatter

---

## 🧪 3. TEST CASES FILE TEMPLATE

**Path:** `[TOPIC]/testcases/[TOPIC]-XXX-[slug].yaml`

### Exact Format (CRITICAL)

```yaml
problem_id: [SAME_AS_PROBLEM_AND_EDITORIAL]
samples:
  - input: |-
      [multi-line input]
    output: |-
      [multi-line output]
  - input: |-
      [second sample]
    output: |-
      [second sample output]
public:
  - input: |-
      [test case 1]
    output: |-
      [output 1]
  - input: |-
      [test case 2]
    output: |-
      [output 2]
  - input: |-
      [test case 3]
    output: |-
      [output 3]
hidden:
  - input: |-
      [hidden test 1]
    output: |-
      [output 1]
  - input: |-
      [hidden test 2]
    output: |-
      [output 2]
  # ... 35+ total hidden tests
````

### STRICT REQUIREMENTS

✅ **MUST HAVE:**

- `problem_id` (top level)
- `samples`, `public`, `hidden` sections
- `input` and `output` fields only
- Use `|-` for multi-line values

❌ **NEVER INCLUDE:**

- `id` field
- `type` field
- `explanation` field
- `difficulty` field
- Any other metadata

### Test Distribution

- **Samples:** 2 (match problem examples)
- **Public:** 3 (for debugging)
- **Hidden:** 35+ (for evaluation)
- **Total:** Minimum 40

### Coverage Strategy

1. **Edge cases:** Empty, single element, minimum constraints
2. **Boundary cases:** Maximum values, limits
3. **Special cases:** Problem-specific edge scenarios
4. **Average cases:** Typical inputs
5. **Large inputs:** Performance testing
6. **Corner cases:** Tricky scenarios

---

## 📊 4. QUIZ FILE TEMPLATE

**Path:** `[TOPIC]/quizzes/[TOPIC]-XXX-[slug].yaml`

### Structure

```yaml
---
problem_id: [SAME_AS_ALL_OTHER_FILES]
display_id: [TOPIC]-XXX
slug: [same-slug]
title: "[Problem Title] - Quiz"
---

# Problem-Related Questions (PRQ)

problem_questions:
  - quiz_id: "PRQ-XXX-Q001"
    category: "problem"
    type: single_choice
    question: "[Question about problem understanding]"
    options:
      - option_id: "A"
        text: "[Option A]"
        correct: false
      - option_id: "B"
        text: "[Option B - correct]"
        correct: true
      - option_id: "C"
        text: "[Option C]"
        correct: false
      - option_id: "D"
        text: "[Option D]"
        correct: false
    explanation: "[Why B is correct and others wrong]"
    difficulty: easy
    points: 10

  - quiz_id: "PRQ-XXX-Q002"
    category: "problem"
    type: multiple_choice
    question: "[Multiple correct answers question]"
    options:
      - option_id: "A"
        text: "[Option A]"
        correct: true
      - option_id: "B"
        text: "[Option B]"
        correct: false
      - option_id: "C"
        text: "[Option C]"
        correct: true
      - option_id: "D"
        text: "[Option D]"
        correct: false
    explanation: "[Why A and C are correct]"
    difficulty: medium
    points: 15

  # 5-7 problem questions total

# Editorial/Algorithm Questions (EDQ)

editorial_questions:
  - quiz_id: "EDQ-XXX-Q001"
    category: "editorial"
    type: single_choice
    question: "[Question about algorithm/complexity]"
    options:
      - option_id: "A"
        text: "O(N²)"
        correct: false
      - option_id: "B"
        text: "O(N log N)"
        correct: true
      - option_id: "C"
        text: "O(N)"
        correct: false
      - option_id: "D"
        text: "O(2^N)"
        correct: false
    explanation: "[Explain the complexity]"
    difficulty: medium
    points: 15

  - quiz_id: "EDQ-XXX-Q002"
    category: "editorial"
    type: scenario
    question: "[Real-world application question]"
    options:
      - option_id: "A"
        text: "[Approach A]"
        correct: false
      - option_id: "B"
        text: "[Approach B - correct]"
        correct: true
      - option_id: "C"
        text: "[Approach C]"
        correct: false
      - option_id: "D"
        text: "[Approach D]"
        correct: false
    explanation: "[Why B works in this scenario]"
    difficulty: medium
    points: 15

  # 6-8 editorial questions total
```

### Question Requirements

**Problem Questions (PRQ):** 5-7 questions

- Test problem understanding
- Test constraints knowledge
- Test I/O format
- Test edge cases

**Editorial Questions (EDQ):** 6-8 questions

- Test algorithm understanding
- Test complexity analysis
- Test optimization techniques
- Include scenario questions

**Difficulty Distribution:**

- Easy (10 pts): 40%
- Medium (15 pts): 40%
- Hard (20 pts): 20%

**Type Distribution:**

- single_choice: 60-70%
- multiple_choice: 20-30%
- scenario: 10-20%

---

## 🖼️ 5. IMAGES README (Optional)

**Path:** `[TOPIC]/images/[TOPIC]-XXX/README.md`

```markdown
# Image Generation Prompts for [TOPIC]-XXX: [Problem Title]

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual of problem concept

**Generation Prompt:**
```

Create a technical diagram showing [problem concept]:

- Display [element 1]
- Show [element 2]
- Highlight [element 3]
- Clean, professional style with blue/gray tones
- Size: 1200x800px

```

### 2. real-world-scenario.png

**Purpose:** Real-world application visualization

**Generation Prompt:**
```

Illustrate [real-world scenario]:

- Context: [setting]
- Elements: [components]
- Modern professional style
- Size: 1200x800px

```

### 3. algorithm-visualization.png

**Purpose:** Algorithm flow diagram

**Generation Prompt:**
```

Create flowchart showing [algorithm]:

- Start state
- Transitions
- Decision points
- Annotations
- Size: 1600x900px

```

### 4. algorithm-steps.png

**Purpose:** Step-by-step execution

**Generation Prompt:**
```

Show algorithm execution:

- State at each step
- Data structure evolution
- Color coding
- Size: 1600x900px

```

### 5. example-1.png

**Purpose:** Example walkthrough

**Generation Prompt:**
```

Visualize the example:

- Input visualization
- Process steps
- Output result
- Size: 1200x800px

```

## Specifications

- Format: PNG
- Resolution: 1200x800px standard, 1600x900px complex
- Style: Technical documentation
- Colors: Blues (#2563eb), Greens (#059669), Grays (#6b7280)
```

---

## ✅ QUALITY CHECKLIST

### Problem File

- [ ] Frontmatter has 12 fields (including `time_limit`, `memory_limit`)
- [ ] Only 1 example
- [ ] All 4 solution templates
- [ ] Clear constraints
- [ ] Notes section
- [ ] Image references
- [ ] 150-250 lines

### Editorial File

- [ ] Frontmatter has 10 fields (NO `time_limit`, NO `memory_limit`)
- [ ] 📋 Problem Summary
- [ ] 🌍 Real-World Scenario (3-4 paragraphs)
- [ ] ASCII diagrams
- [ ] ✅ Input/Output Clarifications
- [ ] Naive → Optimal progression
- [ ] All 4 implementations
- [ ] 🧪 Test walkthrough with table
- [ ] ✅ Proof of correctness
- [ ] 💡 Interview extensions
- [ ] 3-5 Common Mistakes (❌ ✅)
- [ ] Related concepts
- [ ] 500-750 lines

### Test Cases File

- [ ] `problem_id` matches all files
- [ ] 2 samples
- [ ] 3 public tests
- [ ] 35+ hidden tests (40+ total)
- [ ] ONLY `input` and `output` fields
- [ ] Uses `|-` for multi-line
- [ ] Edge/boundary/large cases covered

### Quiz File

- [ ] 5-7 PRQ questions
- [ ] 6-8 EDQ questions
- [ ] Mix of types (single/multiple/scenario)
- [ ] Difficulty: 40% easy, 40% medium, 20% hard
- [ ] Clear explanations

### Consistency

- [ ] All `problem_id` identical
- [ ] All `slug` identical
- [ ] Display ID format correct ([TOPIC]-XXX)
- [ ] No AI artifacts
- [ ] Valid YAML syntax
- [ ] Markdown formatted correctly

---

## 🚀 QUICK START

```bash
# Step 1: Choose your topic and number
TOPIC="Arrays"
PREFIX="ARR"
NUMBER="042"
SLUG="two-sum-sorted"

# Step 2: Create files
cd /path/to/dsa-problems/$TOPIC

touch problems/${PREFIX}-${NUMBER}-${SLUG}.md
touch editorials/${PREFIX}-${NUMBER}-${SLUG}.md
touch testcases/${PREFIX}-${NUMBER}-${SLUG}.yaml
touch quizzes/${PREFIX}-${NUMBER}-${SLUG}.yaml
mkdir -p images/${PREFIX}-${NUMBER}
touch images/${PREFIX}-${NUMBER}/README.md

# Step 3: Use templates above to fill each file

# Step 4: Verify
grep "problem_id:" problems/${PREFIX}-${NUMBER}-*.md \
                   editorials/${PREFIX}-${NUMBER}-*.md \
                   testcases/${PREFIX}-${NUMBER}-*.yaml \
                   quizzes/${PREFIX}-${NUMBER}-*.yaml

# All should match!
```

---

## 📚 TOPIC-SPECIFIC TIPS

### Arrays

- Focus on: Two pointers, sliding window, prefix sums
- Common patterns: Subarrays, pairs, triplets
- Complexity: Usually O(N) or O(N log N) optimal

### Graphs

- Focus on: BFS, DFS, shortest paths, MST
- Common patterns: Traversal, cycles, connectivity
- Complexity: Often O(V + E)

### Trees

- Focus on: Traversals, recursion, parent pointers
- Common patterns: LCA, paths, subtrees
- Complexity: Usually O(N) or O(log N)

### DP

- Focus on: State definition, transitions, optimization
- Common patterns: Memoization, tabulation, sliding window
- Complexity: Often O(N·K) → O(N) with optimization

### Strings

- Focus on: Pattern matching, manipulation, parsing
- Common patterns: Sliding window, KMP, Z-algorithm
- Complexity: O(N) or O(N·M)

---

## 🎯 GENERATION PROMPT (Copy-Paste Ready)

```
Generate a complete DSA problem for the [TOPIC] category following this structure:

**Problem Details:**
- Topic: [Arrays/Graphs/Trees/DP/etc.]
- Display ID: [TOPIC]-[NUMBER]
- Slug: [kebab-case-description]
- Title: [Clear Problem Title]
- Difficulty: [Easy/Medium/Hard]
- Difficulty Score: [10-90]

**Required Files (4 total):**

1. **Problem File** (150-250 lines)
   - Frontmatter with 12 fields (include time_limit: 2000, memory_limit: 256)
   - Problem statement with 1 example
   - All 4 solution templates (Java, Python, C++, JavaScript)
   - Clear constraints and notes

2. **Editorial File** (500-750 lines)
   - Frontmatter with 10 fields (NO time_limit, NO memory_limit)
   - 📋 Problem Summary, 🌍 Real-World Scenario (3-4 paragraphs)
   - ASCII diagrams, ✅ Clarifications
   - Naive → Optimal progression with full implementations
   - 🧪 Test walkthrough, ✅ Proof, 💡 Extensions
   - 3-5 Common Mistakes (❌ ✅), Related concepts

3. **Test Cases File**
   - problem_id matching all files
   - 2 samples, 3 public, 35+ hidden (40+ total)
   - ONLY input/output fields (use |- for multi-line)
   - Edge/boundary/large cases

4. **Quiz File**
   - 5-7 PRQ (problem) questions
   - 6-8 EDQ (editorial) questions
   - Mix: single_choice, multiple_choice, scenario
   - Difficulty: 40% easy, 40% medium, 20% hard

**Critical Rules:**
- Use exact emoji set: 📋 🌍 ✅ 🧪 💡
- All problem_id values must be identical
- Include ASCII diagrams for visualization
- Full working code in all 4 languages
- NO extra fields in YAML test cases
- Match DP-001 structure exactly

Generate all 4 files maintaining consistency across problem_id, slug, and display_id.
```

---

**Version:** 2.0 (Universal)  
**Based On:** DP-001 Structure  
**Applies To:** All DSA Topics  
**Status:** ✅ Production Ready
