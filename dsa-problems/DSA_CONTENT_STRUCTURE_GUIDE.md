# DSA Content Structure Guide

> **Complete template structure for maintaining consistency across Problems, Editorials, and Quizzes**

---

## 📁 File Organization Structure

```
DSA/dsa-problems/
└── {TopicName}/                    # e.g., Arrays, Graphs, DP
    ├── problems/                   # Problem statements
    │   ├── {PREFIX}-001-{slug}.md
    │   ├── {PREFIX}-002-{slug}.md
    │   └── ...
    ├── editorials/                 # Solution explanations
    │   ├── {PREFIX}-001-{slug}.md
    │   ├── {PREFIX}-002-{slug}.md
    │   └── ...
    ├── quizzes/                    # Quiz questions
    │   ├── {PREFIX}-001-{slug}.yaml
    │   ├── {PREFIX}-002-{slug}.yaml
    │   └── ...
    └── images/                     # Visual assets
        ├── {PREFIX}-001/
        │   ├── problem-illustration.png
        │   ├── example-1.png
        │   └── header.png
        └── ...
```

### Naming Convention

- **Prefix Codes**: `ARR` (Arrays), `GRF` (Graphs), `DP` (Dynamic Programming), etc.
- **Display ID**: `{PREFIX}-{###}` (e.g., `ARR-001`, `GRF-042`)
- **Slug**: Kebab-case descriptive name (e.g., `snack-restock-snapshot`)
- **Files**: `{PREFIX}-{###}-{slug}.{ext}`

---

## 📝 1. PROBLEM STRUCTURE

### File: `problems/{PREFIX}-###-{slug}.md`

```markdown
## <!-- filepath: /path/to/problems/{PREFIX}-###-{slug}.md -->

problem*id: {PREFIX}*{CATEGORY}\_{UNIQUE_ID} # e.g., ARR_PREFIX_AVG\_\_4252
display_id: {PREFIX}-### # e.g., ARR-001
slug: {kebab-case-name} # e.g., snack-restock-snapshot
title: "{Human Readable Title}" # e.g., "Snack Restock Snapshot"
difficulty: {Easy|Medium|Hard}
difficulty_score: {1-100} # 1-33=Easy, 34-66=Medium, 67-100=Hard
topics:

- {Topic1} # e.g., Array
- {Topic2} # e.g., Prefix Sum
- {Topic3} # e.g., Mathematics
  tags:
- {tag1} # e.g., arrays
- {tag2} # e.g., prefix-sum
- {tag3} # e.g., easy
  premium: {true|false}
  subscription_tier: {basic|premium|free}
  time_limit: {milliseconds} # e.g., 2000
  memory_limit: {megabytes} # e.g., 256

---

# {Problem Title}

## Problem Statement

{Clear, concise problem description in 1-2 sentences}

![Problem Illustration](../images/{PREFIX}-###/problem-illustration.png)

## Input Format

- First line: {Description}
- Second line: {Description}
- ... (as needed)

## Output Format

{Expected output format description}

## Constraints

- Constraint 1 (e.g., 1 ≤ n ≤ 10^5)
- Constraint 2 (e.g., 0 ≤ arr[i] ≤ 10^9)
- ... (all relevant constraints)

## Examples

### Example 1

**Input:**
```

{input data}

```

**Output:**

```

{output data}

```

**Explanation:**

- Point 1 with calculation
- Point 2 with calculation
- ... (detailed step-by-step)

![Example 1 Visualization](../images/{PREFIX}-###/example-1.png)

### Example 2

**Input:**

```

{input data}

```

**Output:**

```

{output data}

````

**Explanation:**

{Step-by-step explanation}

### Example 3 (if needed)

{Follow same pattern}

## Notes

- Important note 1
- Important note 2
- Edge cases to consider

## Related Topics

{Topic1}, {Topic2}, {Topic3}

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public {ReturnType} {functionName}({params}) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Input parsing code
        {input handling}

        Solution solution = new Solution();
        {ReturnType} result = solution.{functionName}({args});

        // Output formatting code
        {output handling}

        sc.close();
    }
}
````

### Python

```python
from typing import List

def {function_name}({params}) -> {ReturnType}:
    # Your implementation here
    pass

def main():
    # Input parsing
    {input handling}

    result = {function_name}({args})

    # Output formatting
    {output handling}

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
    {ReturnType} {functionName}({params}) {
        // Your implementation here
    }
};

int main() {
    // Input parsing
    {input handling}

    Solution solution;
    {ReturnType} result = solution.{functionName}({args});

    // Output formatting
    {output handling}

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  {functionName}({params}) {
    // Your implementation here
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
  if (lines.length === {expected_lines}) {
    // Input parsing
    {input handling}

    const solution = new Solution();
    const result = solution.{functionName}({args});

    // Output formatting
    {output handling}

    rl.close();
  }
});
```

````

---

## 📚 2. EDITORIAL STRUCTURE

### File: `editorials/{PREFIX}-###-{slug}.md`

```markdown
<!-- filepath: /path/to/editorials/{PREFIX}-###-{slug}.md -->
---
problem_id: {PREFIX}_{CATEGORY}_{UNIQUE_ID}
display_id: {PREFIX}-###
slug: {kebab-case-name}
title: "{Problem Title}"
difficulty: {Easy|Medium|Hard}
difficulty_score: {1-100}
topics:
  - {Topic1}
  - {Topic2}
  - {Topic3}
tags:
  - {tag1}
  - {tag2}
  - {tag3}
premium: {true|false}
subscription_tier: {basic|premium|free}
---

# {Problem Title}

![Problem Header](../images/{PREFIX}-###/header.png)

### 📋 Problem Summary

{1-2 sentence recap of the problem}

![Problem Concept](../images/{PREFIX}-###/problem-illustration.png)

### 🌍 Real-World Scenario

**{Scenario Title}**

{Engaging real-world context that makes the problem relatable}

{Bullet points or narrative explaining:}
- What the situation is
- Why this problem matters
- How it applies to everyday scenarios
- What insights can be gained

### 📚 Detailed Explanation

**What is {Core Concept}?**

- Definition in simple terms
- Key formula or relationship
- Why it's called that (etymology/reasoning)

**Key Characteristics:**

1. Characteristic 1
2. Characteristic 2
3. Characteristic 3

### ❌ Naive Approach

**Idea**: {Brief description of the brute force approach}

````

Pseudocode or explanation:
Step 1
Step 2
Step 3

````

**Code Pattern**:

```{language}
// Illustrative code showing the naive approach
{code example}
````

**⏱️ Time Complexity: O({complexity})**

**Why O({complexity})?**

{Detailed explanation with:}

- Operation counting
- Mathematical breakdown
- Real examples with small n values

**Real Impact**:

- n = 100 → X operations
- n = 1,000 → Y operations
- n = 10,000 → Z operations (SLOW!)

**📦 Space Complexity: O({complexity})**

{Explanation of space usage}

### ✅ Optimal Approach

**💡 Key Insight**: {The "aha!" moment that leads to optimization}

{Analogy or metaphor to explain the insight}

**Approach**: {High-level description}

```
Pseudocode:
Step 1
Step 2
Step 3
```

**⏱️ Time Complexity: O({complexity})**

**Detailed Breakdown**:

- Operation 1: {cost}
- Operation 2: {cost}
- Total: {mathematical derivation}

**Improvement Factor**: O(old) → O(new) means X times faster!

- For n=1,000: old_ops → new_ops (speedup)
- For n=10,000: old_ops → new_ops (speedup)

**📦 Space Complexity: O({complexity})**

**Why O({complexity})?**

{Detailed space analysis}

### 🎨 Visual Representation

**Example**: `{input example}`

```
{ASCII art or detailed step-by-step visualization}
```

**Flow Diagram**:

```
{Process flow with arrows showing data transformation}
```

### 🧪 Test Case Walkthrough

**Input**: `{test case}`

**Detailed Step-by-Step**:

```
{Table or structured walkthrough showing:}
- Each step
- Intermediate values
- State changes
- Final result
```

**Trace Visualization**:

```
{Step-by-step execution trace}
```

### ⚠️ Common Mistakes & Pitfalls

#### 1. **{Mistake Name}** 🔴

**Problem**:

```{language}
// ❌ WRONG CODE
{problematic code}
```

**Scenario**: {When this fails}

**Solution**:

```{language}
// ✅ CORRECT CODE
{fixed code}
```

**Why?** {Explanation}

#### 2. **{Mistake Name}** 🔴

{Follow same pattern for each common mistake}

### 🔑 Algorithm Steps

**Optimal O({complexity}) Algorithm**:

1. **Initialize**:

   ```
   {initialization steps}
   ```

2. **Process**:

   ```
   {main algorithm steps}
   ```

3. **Return**:
   ```
   {return statement}
   ```

**Pseudocode**:

```
function {name}(params):
    {detailed pseudocode}
```

### 💻 Implementations

#### Java

```java
class Solution {
    public {ReturnType} {methodName}({params}) {
        // Complete working solution with comments
        {implementation}
    }
}

// Time: O({complexity}), Space: O({complexity})
```

#### Python

```python
def {function_name}({params}) -> {ReturnType}:
    """
    {Docstring explaining function purpose}

    Args:
        param1: description
        param2: description

    Returns:
        description of return value
    """
    # Complete working solution with comments
    {implementation}

# Time: O({complexity}), Space: O({complexity})
```

#### C++

```cpp
class Solution {
public:
    {ReturnType} {methodName}({params}) {
        // Complete working solution with comments
        {implementation}
    }
};

// Time: O({complexity}), Space: O({complexity})
```

#### JavaScript

```javascript
class Solution {
  {methodName}({params}) {
    // Complete working solution with comments
    {implementation}
  }
}

// Time: O({complexity}), Space: O({complexity})
```

### 📊 Comparison Table

| **Aspect**          | **Naive Approach** | **Optimal Approach** |
| ------------------- | ------------------ | -------------------- |
| **Algorithm**       | {description}      | {description}        |
| **Time (n=100)**    | {operations}       | {operations}         |
| **Time (n=1,000)**  | {operations}       | {operations}         |
| **Time (n=10,000)** | {operations}       | {operations}         |
| **Space (extra)**   | O({complexity})    | O({complexity})      |
| **Redundant work?** | {Yes/No}           | {Yes/No}             |
| **Efficiency**      | {rating}           | {rating}             |

### 🎓 Key Takeaways

1. **{Concept 1}**: {Explanation}
2. **{Concept 2}**: {Explanation}
3. **{Concept 3}**: {Explanation}

### 🔗 Related Problems

**Similar Problems:**

- [{Problem Name}]({link}) - {Similarity explanation}
- [{Problem Name}]({link}) - {Similarity explanation}

**Next Steps:**

After mastering this, try:

1. {Problem 1}
2. {Problem 2}
3. {Problem 3}

### 💡 Interview Tips

- **Communication**: {Tip}
- **Edge Cases**: {Tip}
- **Optimization**: {Tip}
- **Testing**: {Tip}

### 📚 Further Reading

- [Resource 1]({link})
- [Resource 2]({link})
- [Resource 3]({link})

````

---

## 🎯 3. QUIZ STRUCTURE

### File: `quizzes/{PREFIX}-###-{slug}.yaml`

```yaml
# filepath: /path/to/quizzes/{PREFIX}-###-{slug}.yaml
---
problem_id: {PREFIX}_{CATEGORY}_{UNIQUE_ID}
display_id: {PREFIX}-###
slug: {kebab-case-name}
title: "{Problem Title} - Quiz"
---

# Problem-Related Questions (PRQ)
# These test understanding of the problem statement, constraints, and requirements

problem_questions:
  - quiz_id: "PRQ-###-Q001"
    category: "problem"
    type: single_choice                    # or multiple_choice, scenario, true_false
    question: "{Clear question text}"
    options:
      - option_id: "A"
        text: "{Option text}"
        correct: false
      - option_id: "B"
        text: "{Option text}"
        correct: false
      - option_id: "C"
        text: "{Option text}"
        correct: true
      - option_id: "D"
        text: "{Option text}"
        correct: false
    explanation: "{Detailed explanation of why the correct answer is correct}"
    difficulty: easy                       # easy, medium, hard
    points: 10                             # Point value for correct answer

  - quiz_id: "PRQ-###-Q002"
    category: "problem"
    type: single_choice
    question: "{Question text with specific example}"
    options:
      - option_id: "A"
        text: "{Option}"
        correct: false
      - option_id: "B"
        text: "{Option}"
        correct: true
      - option_id: "C"
        text: "{Option}"
        correct: false
      - option_id: "D"
        text: "{Option}"
        correct: false
    explanation: "{Step-by-step calculation or reasoning}"
    difficulty: easy
    points: 10

  - quiz_id: "PRQ-###-Q003"
    category: "problem"
    type: multiple_choice                  # Multiple correct answers
    question: "{Question asking for multiple items}"
    options:
      - option_id: "A"
        text: "{Option}"
        correct: true
      - option_id: "B"
        text: "{Option}"
        correct: true
      - option_id: "C"
        text: "{Option}"
        correct: false
      - option_id: "D"
        text: "{Option}"
        correct: false
    explanation: "{Explanation covering all correct and incorrect options}"
    difficulty: medium
    points: 15

# Editorial/Algorithm Questions (EDQ)
# These test understanding of the solution approach, algorithms, and complexity analysis

editorial_questions:
  - quiz_id: "EDQ-###-Q001"
    category: "editorial"
    type: single_choice
    question: "{Question about algorithm or complexity}"
    options:
      - option_id: "A"
        text: "{Option}"
        correct: true
      - option_id: "B"
        text: "{Option}"
        correct: false
      - option_id: "C"
        text: "{Option}"
        correct: false
      - option_id: "D"
        text: "{Option}"
        correct: false
    explanation: "{Explanation of algorithmic concept}"
    difficulty: medium
    points: 15

  - quiz_id: "EDQ-###-Q002"
    category: "editorial"
    type: single_choice
    question: "{Question about implementation detail}"
    options:
      - option_id: "A"
        text: "{Option}"
        correct: false
      - option_id: "B"
        text: "{Option}"
        correct: true
      - option_id: "C"
        text: "{Option}"
        correct: false
      - option_id: "D"
        text: "{Option}"
        correct: false
    explanation: "{Technical explanation with code implications}"
    difficulty: medium
    points: 15

  - quiz_id: "EDQ-###-Q003"
    category: "editorial"
    type: scenario                         # Real-world application
    question: "{Scenario-based question applying the concept}"
    options:
      - option_id: "A"
        text: "{Option}"
        correct: false
      - option_id: "B"
        text: "{Option}"
        correct: true
      - option_id: "C"
        text: "{Option}"
        correct: false
      - option_id: "D"
        text: "{Option}"
        correct: false
    explanation: "{Explanation connecting theory to practice}"
    difficulty: medium
    points: 15

  - quiz_id: "EDQ-###-Q004"
    category: "editorial"
    type: multiple_choice
    question: "{Question about common mistakes or best practices}"
    options:
      - option_id: "A"
        text: "{Mistake/Practice}"
        correct: true
      - option_id: "B"
        text: "{Mistake/Practice}"
        correct: true
      - option_id: "C"
        text: "{Mistake/Practice}"
        correct: true
      - option_id: "D"
        text: "{Mistake/Practice}"
        correct: false
    explanation: "{Comprehensive explanation of each option}"
    difficulty: hard
    points: 20

  - quiz_id: "EDQ-###-Q005"
    category: "editorial"
    type: single_choice
    question: "{Advanced question about optimization or edge cases}"
    options:
      - option_id: "A"
        text: "{Option}"
        correct: false
      - option_id: "B"
        text: "{Option}"
        correct: false
      - option_id: "C"
        text: "{Option}"
        correct: true
      - option_id: "D"
        text: "{Option}"
        correct: false
    explanation: "{Deep technical explanation}"
    difficulty: hard
    points: 20

# Code Analysis Questions (CAQ)
# These test ability to read, debug, and improve code

code_questions:
  - quiz_id: "CAQ-###-Q001"
    category: "code"
    type: single_choice
    question: "What is the output of the following code?"
    code: |
      {code snippet to analyze}
    language: {java|python|cpp|javascript}
    options:
      - option_id: "A"
        text: "{Output option}"
        correct: false
      - option_id: "B"
        text: "{Output option}"
        correct: true
      - option_id: "C"
        text: "{Output option}"
        correct: false
      - option_id: "D"
        text: "{Output option}"
        correct: false
    explanation: "{Trace through code execution}"
    difficulty: medium
    points: 15

  - quiz_id: "CAQ-###-Q002"
    category: "code"
    type: single_choice
    question: "What is wrong with this code?"
    code: |
      {buggy code snippet}
    language: {language}
    options:
      - option_id: "A"
        text: "{Bug description}"
        correct: false
      - option_id: "B"
        text: "{Bug description}"
        correct: true
      - option_id: "C"
        text: "{Bug description}"
        correct: false
      - option_id: "D"
        text: "Code is correct"
        correct: false
    explanation: "{Explain the bug and how to fix it}"
    difficulty: hard
    points: 20

  - quiz_id: "CAQ-###-Q003"
    category: "code"
    type: single_choice
    question: "How can this code be optimized?"
    code: |
      {suboptimal code snippet}
    language: {language}
    options:
      - option_id: "A"
        text: "{Optimization approach}"
        correct: false
      - option_id: "B"
        text: "{Optimization approach}"
        correct: true
      - option_id: "C"
        text: "{Optimization approach}"
        correct: false
      - option_id: "D"
        text: "Cannot be optimized"
        correct: false
    explanation: "{Explain optimization with complexity analysis}"
    difficulty: hard
    points: 20

# Complexity Analysis Questions (CMQ)
# These test understanding of time and space complexity

complexity_questions:
  - quiz_id: "CMQ-###-Q001"
    category: "complexity"
    type: single_choice
    question: "What is the time complexity of this approach?"
    code: |
      {code snippet or algorithm description}
    language: {language}
    options:
      - option_id: "A"
        text: "O(n)"
        correct: false
      - option_id: "B"
        text: "O(n log n)"
        correct: false
      - option_id: "C"
        text: "O(n²)"
        correct: true
      - option_id: "D"
        text: "O(2^n)"
        correct: false
    explanation: "{Detailed complexity analysis with operation counting}"
    difficulty: medium
    points: 15

  - quiz_id: "CMQ-###-Q002"
    category: "complexity"
    type: single_choice
    question: "What is the space complexity excluding output?"
    code: |
      {code snippet}
    language: {language}
    options:
      - option_id: "A"
        text: "O(1)"
        correct: true
      - option_id: "B"
        text: "O(n)"
        correct: false
      - option_id: "C"
        text: "O(n²)"
        correct: false
      - option_id: "D"
        text: "O(log n)"
        correct: false
    explanation: "{Explain what counts as auxiliary space}"
    difficulty: medium
    points: 15
````

---

## 📊 Quiz Question Types

### 1. **single_choice**

- One correct answer
- 4 options (A, B, C, D)
- Used for: Factual questions, specific calculations, concept testing

### 2. **multiple_choice**

- Multiple correct answers possible
- 4 options, any combination can be correct
- Used for: Identifying characteristics, listing valid approaches, finding mistakes

### 3. **scenario**

- Real-world application question
- One correct answer
- Used for: Applying concepts to practical situations

### 4. **true_false**

- Boolean question
- 2 options only
- Used for: Quick concept verification

---

## 🎯 Quiz Categories

### PRQ (Problem-Related Questions)

**Focus**: Understanding problem requirements

- Input/output format
- Constraints
- Example walkthroughs
- Expected behavior
- Edge cases

**Difficulty Distribution**:

- Easy: 60%
- Medium: 30%
- Hard: 10%

**Points**: 10-15 per question

### EDQ (Editorial/Algorithm Questions)

**Focus**: Solution approach and algorithms

- Time/space complexity
- Algorithmic insights
- Optimization techniques
- Data structure choices
- Common mistakes

**Difficulty Distribution**:

- Easy: 30%
- Medium: 50%
- Hard: 20%

**Points**: 10-20 per question

### CAQ (Code Analysis Questions)

**Focus**: Reading and understanding code

- Output prediction
- Bug identification
- Code optimization
- Trace execution
- Refactoring

**Difficulty Distribution**:

- Easy: 20%
- Medium: 40%
- Hard: 40%

**Points**: 15-20 per question

### CMQ (Complexity Analysis Questions)

**Focus**: Performance analysis

- Time complexity calculation
- Space complexity calculation
- Big-O notation
- Worst/average/best case
- Scalability

**Difficulty Distribution**:

- Easy: 30%
- Medium: 50%
- Hard: 20%

**Points**: 15-20 per question

---

## 💡 Best Practices

### Problem Writing

1. ✅ Start with real-world context
2. ✅ Use clear, simple language
3. ✅ Provide 2-3 examples with explanations
4. ✅ Include visual aids (diagrams/images)
5. ✅ List all constraints explicitly
6. ✅ Provide templates in 4 languages

### Editorial Writing

1. ✅ Explain the "why" not just "how"
2. ✅ Start with naive approach
3. ✅ Show optimization journey
4. ✅ Use analogies and metaphors
5. ✅ Include visual walkthroughs
6. ✅ Highlight common mistakes
7. ✅ Provide working code in all languages
8. ✅ Compare approaches with tables

### Quiz Creation

1. ✅ Create 15-20 questions per problem
2. ✅ Balance difficulty levels
3. ✅ Mix question types
4. ✅ Cover all categories (PRQ, EDQ, CAQ, CMQ)
5. ✅ Write detailed explanations
6. ✅ Use code snippets where relevant
7. ✅ Test edge case understanding
8. ✅ Verify questions are unambiguous

---

## 📏 Content Guidelines

### Problem Statement

- **Length**: 300-600 words
- **Examples**: 2-3 minimum
- **Visuals**: At least 1 diagram

### Editorial

- **Length**: 1500-3000 words
- **Code Samples**: All 4 languages (Java, Python, C++, JS)
- **Visuals**: 3-5 diagrams/traces
- **Sections**: All required sections present

### Quiz

- **Total Questions**: 15-20
- **PRQ**: 5-7 questions
- **EDQ**: 5-7 questions
- **CAQ**: 2-3 questions
- **CMQ**: 2-3 questions
- **Point Total**: 200-300 points

---

## 🎨 Visual Asset Guidelines

### Required Images

#### Problems

- `problem-illustration.png` - Main concept diagram
- `example-1.png` - Visualization of first example
- `example-2.png` - Visualization of second example

#### Editorials

- `header.png` - Editorial header image
- `problem-illustration.png` - Same as problem
- `approach-comparison.png` - Comparing naive vs optimal
- `step-by-step.png` - Detailed trace visualization

### Image Specifications

- **Format**: PNG (transparent background preferred)
- **Resolution**: 1200x800 or 16:9 ratio
- **File Size**: < 500KB per image
- **Style**: Consistent color scheme, clean design

---

## ✅ Checklist Template

### Before Publishing

#### Problem

- [ ] Metadata complete (ID, slug, difficulty, tags)
- [ ] Problem statement clear and concise
- [ ] All constraints listed
- [ ] 2-3 examples with explanations
- [ ] Images created and linked
- [ ] All 4 code templates provided
- [ ] Input/output format specified

#### Editorial

- [ ] Metadata matches problem
- [ ] Real-world scenario included
- [ ] Naive approach explained
- [ ] Optimal approach detailed
- [ ] Visual representations present
- [ ] Common mistakes section complete
- [ ] All 4 language implementations
- [ ] Complexity analysis thorough
- [ ] Comparison table included

#### Quiz

- [ ] Metadata matches problem
- [ ] 15-20 questions total
- [ ] All categories covered (PRQ, EDQ, CAQ, CMQ)
- [ ] Difficulty balanced
- [ ] Every question has detailed explanation
- [ ] No ambiguous questions
- [ ] Code snippets formatted correctly
- [ ] Point values assigned

---

## 🔗 Cross-Referencing

### Problem → Editorial

```markdown
[View detailed editorial](../editorials/{PREFIX}-###-{slug}.md)
```

### Editorial → Problem

```markdown
[Back to problem statement](../problems/{PREFIX}-###-{slug}.md)
```

### Quiz → Problem

```yaml
problem_link: "../problems/{PREFIX}-###-{slug}.md"
```

### Quiz → Editorial

```yaml
editorial_link: "../editorials/{PREFIX}-###-{slug}.md"
```

---

## 📝 Example Quick Reference

**Problem**: `ARR-001-snack-restock-snapshot`

- File: `problems/ARR-001-snack-restock-snapshot.md`
- Slug: `snack-restock-snapshot`
- ID: `ARR_PREFIX_AVG__4252`

**Editorial**: Same naming

- File: `editorials/ARR-001-snack-restock-snapshot.md`

**Quiz**: Same naming with .yaml

- File: `quizzes/ARR-001-snack-restock-snapshot.yaml`

**Images**:

- Folder: `images/ARR-001/`
- Files: `problem-illustration.png`, `example-1.png`, `header.png`

---

## 🚀 Getting Started

1. **Choose a problem topic and difficulty**
2. **Assign a unique problem ID** (check existing problems)
3. **Create slug** (descriptive, kebab-case)
4. **Write problem statement** using template
5. **Create editorial** with all sections
6. **Design visual assets** for both
7. **Write comprehensive quiz** (15-20 questions)
8. **Cross-check** using checklist
9. **Review** for consistency and clarity
10. **Publish** all three files together

---

**Last Updated**: December 15, 2025  
**Version**: 1.0  
**Maintained By**: NickTechBytes DSA Team
