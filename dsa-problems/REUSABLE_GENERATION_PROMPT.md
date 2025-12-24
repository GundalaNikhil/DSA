# Reusable Prompt Template for DSA Educational Content Generation

## Purpose

This prompt template generates complete DSA problem materials that are **CI-sync ready** with the backend platform. All generated content must match the Arrays folder format exactly for seamless integration.

---

## 🎯 Generation Request Template

```
Generate complete educational materials for the following DSA problems from [TOPIC_FOLDER]:

**Source File:** /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/[TOPIC_FOLDER]/[source-practice-file].md

**Problems to Generate:** [LIST_PROBLEM_NUMBERS]
Example: Problems 1-5, or Problems 4, 7, 9, or All 16 problems

**Reference Format:** /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Arrays/
- Use ARR-001 files as the exact template
- Match all formatting, structure, and conventions exactly

**Requirements:**
1. Generate 4 files per problem (editorial, problem, testcases, images README)
2. Follow the exact structure verified in Bitwise/FORMAT_VERIFICATION.md
3. Ensure CI-sync compatibility with backend platform
```

---

## 📋 Required Files Per Problem

For each problem `[TOPIC]-[NUMBER]`, generate:

### 1. Editorial File

**Path:** `[TOPIC_FOLDER]/editorials/[TOPIC]-[NUMBER]-[slug].md`

**Structure:**

```markdown
---
problem_id: [TOPIC]_[DESCRIPTION_CAPS]__[4_DIGIT_RANDOM]
display_id: [TOPIC]-[NUMBER]
slug: [kebab-case-title]
title: "[Problem Title]"
difficulty: [Easy|Medium|Hard]
difficulty_score: [10-90]
topics:
  - [Topic 1]
  - [Topic 2]
tags:
  - [tag1]
  - [tag2]
premium: true
subscription_tier: basic
---

# [TOPIC]-[NUMBER]: [Title]

## 📋 Problem Summary

[2-3 sentence summary]

## 🌍 Real-World Scenario

**Scenario Title:** [Engaging real-world context]

[3-4 paragraphs describing realistic application]

**Why This Problem Matters:**

- [Reason 1]
- [Reason 2]
- [Reason 3]

![Real-World Application](../images/[TOPIC]-[NUMBER]/real-world-scenario.png)

## Detailed Explanation

[Comprehensive explanation with examples]

## Naive Approach

**Intuition:**
[Clear explanation]

**Algorithm:**

1. Step 1
2. Step 2
3. Step 3

**Time Complexity:** O(...)
**Space Complexity:** O(...)

**Why This Works:**
[Explanation]

**Limitations:**

- [Limitation 1]
- [Limitation 2]

## Optimal Approach

**Key Insight:**
[Critical optimization insight]

**Algorithm:**

1. Step 1
2. Step 2
3. Step 3

**Time Complexity:** O(...)
**Space Complexity:** O(...)

**Why This Is Optimal:**
[Explanation]

![Algorithm Visualization](../images/[TOPIC]-[NUMBER]/algorithm-visualization.png)

## Implementations

### Java

[Full working solution with comments]

### Python

[Full working solution with comments]

### C++

[Full working solution with comments]

### JavaScript

[Full working solution with comments]

## Common Mistakes to Avoid

1. **[Mistake 1]**

   - [Description]
   - ❌ Wrong approach
   - ✅ Correct approach

2. **[Mistake 2]**

   - [Description]

3. **[Mistake 3]**
   - [Description]


## Related Concepts

- [Concept 1]
- [Concept 2]
- [Concept 3]
```

**Length:** 500-750 lines
**Key Points:**

- Use emojis: 📋 (Problem Summary), 🌍 (Real-World Scenario)
- Real-world scenario must be engaging and realistic (3-4 paragraphs)
- Include both naive and optimal approaches
- Provide full implementations in all 4 languages
- 3 common mistakes minimum

---

### 2. Problem Statement File

**Path:** `[TOPIC_FOLDER]/problems/[TOPIC]-[NUMBER]-[slug].md`

**Structure:**

```markdown
---
problem_id: [SAME_AS_EDITORIAL]
display_id: [TOPIC]-[NUMBER]
slug: [kebab-case-title]
title: "[Problem Title]"
difficulty: [Easy|Medium|Hard]
difficulty_score: [10-90]
topics:
  - [Topic 1]
  - [Topic 2]
tags:
  - [tag1]
  - [tag2]
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# [TOPIC]-[NUMBER]: [Title]

## Problem Statement

[Clear problem description with context]

![Problem Illustration](../images/[TOPIC]-[NUMBER]/problem-illustration.png)

## Input Format

- [Input format details]

## Output Format

[Output format details]

## Constraints

- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

## Example

**Input:**
```

[sample input]

```

**Output:**

```

[sample output]

````

**Explanation:**

[Detailed step-by-step explanation]

![Example Visualization](../images/[TOPIC]-[NUMBER]/example-1.png)

## Notes

- [Important note 1]
- [Important note 2]
- [Important note 3]

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
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Read input

        Solution solution = new Solution();
        [ReturnType] result = solution.[methodName]([args]);

        System.out.println(result);
        sc.close();
    }
}
````

### Python

```python
def [function_name]([parameters]) -> [ReturnType]:
    # Your implementation here
    pass

def main():
    # Read input
    result = [function_name]([args])
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    [ReturnType] [methodName]([parameters]) {
        // Your implementation here
    }
};

int main() {
    // Read input

    Solution solution;
    [ReturnType] result = solution.[methodName]([args]);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  [methodName]([parameters]) {
    // Your implementation here
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  // Read input

  const solution = new Solution();
  const result = solution.[methodName]([args]);

  console.log(result);
  rl.close();
});
```

````

**Length:** 150-250 lines
**Key Points:**
- Frontmatter includes `time_limit` and `memory_limit` (unlike editorial)
- Use ONLY 1 example (not multiple)
- All 4 solution templates required
- Image references in problem and example sections

---

### 3. Test Cases File
**Path:** `[TOPIC_FOLDER]/testcases/[TOPIC]-[NUMBER]-[slug].yaml`

**Structure:**
```yaml
problem_id: [SAME_AS_EDITORIAL]
samples:
  - input: |-
      [multi-line input]
    output: |-
      [multi-line output]
  - input: |-
      [multi-line input]
    output: |-
      [multi-line output]
public:
  - input: |-
      [input]
    output: |-
      [output]
  - input: |-
      [input]
    output: |-
      [output]
  - input: |-
      [input]
    output: |-
      [output]
hidden:
  - input: |-
      [input]
    output: |-
      [output]
  - input: |-
      [input]
    output: |-
      [output]
  # ... 35 more hidden test cases
````

**Requirements:**

- **Samples:** 2 test cases (match examples in problem statement)
- **Public:** 3 test cases (visible to users)
- **Hidden:** 35 test cases (for evaluation)
- **Total:** 40 test cases minimum
- **Format:** Use `|-` for multi-line input/output
- **NO extra fields:** No `id`, `type`, `explanation`, `difficulty`, etc.
- **Only fields:** `input` and `output` under each category

**Test Case Coverage:**

- Edge cases (empty, single element, boundaries)
- Constraint boundaries (min/max values)
- Average cases
- Large inputs (performance testing)
- Special patterns (if applicable)

---

### 4. Images Folder README

**Path:** `[TOPIC_FOLDER]/images/[TOPIC]-[NUMBER]/README.md`

**Structure:**

```markdown
# Image Generation Prompts for [TOPIC]-[NUMBER]: [Title]

## Overview

This directory contains placeholder references for images used in the problem and editorial.

## Required Images

### 1. problem-illustration.png

**Purpose:** Main visual representation of the problem concept

**Generation Prompt:**
```

[Detailed DALL-E/Midjourney prompt describing the illustration]

- Style: [technical diagram / infographic / illustration]
- Elements: [list key visual elements]
- Colors: [color scheme]
- Size: 1200x800px

```

### 2. real-world-scenario.png
**Purpose:** Visualization of the real-world application

**Generation Prompt:**
```

[Detailed prompt for real-world scenario visualization]

```

### 3. algorithm-visualization.png
**Purpose:** Step-by-step algorithm flow diagram

**Generation Prompt:**
```

[Detailed prompt for algorithm visualization]

```

### 4. example-1.png
**Purpose:** Visual walkthrough of the example

**Generation Prompt:**
```

[Detailed prompt for example visualization]

```

### 5. complexity-comparison.png
**Purpose:** Compare naive vs optimal approach

**Generation Prompt:**
```

[Detailed prompt for complexity comparison chart]

```

### 6. common-mistakes.png
**Purpose:** Illustrate common pitfalls

**Generation Prompt:**
```

[Detailed prompt for mistakes illustration]

```

## Image Specifications
- Format: PNG with transparency
- Resolution: 1200x800px (or 1600x900px for complex diagrams)
- Style: Consistent with technical documentation
- Color Scheme: Professional (blues, greens, grays)
- Text: Clear, readable fonts (minimum 14pt)
```

**Key Points:**

- 6 image prompts minimum
- Detailed generation prompts for AI image tools
- Consistent naming convention
- Image specifications included

---

## 🚫 Critical Don'ts - CI Sync Blockers

### Test Cases YAML - NEVER Include:

❌ `id: TC-001`
❌ `type: sample/public/hidden`
❌ `explanation: "..."`
❌ `difficulty: easy`
❌ `tags: [...]`
❌ Any field except `input` and `output`

### Problem/Editorial Files - NEVER Include:

❌ AI thinking artifacts ("Wait, let me reconsider...")
❌ Verbose intermediate calculations
❌ Multiple examples (use 1 only in problem statement)
❌ Inconsistent emoji usage
❌ Extra frontmatter fields not in Arrays template

### Frontmatter - Exact Match Required:

✅ **Editorial:** 10 fields (no time_limit, no memory_limit)
✅ **Problem:** 12 fields (includes time_limit, memory_limit)
✅ **Test Cases:** Only `problem_id` at top level

---

## 📂 Folder Structure Example

```
[TopicFolder]/
├── editorials/
│   ├── [TOPIC]-001-[slug].md
│   ├── [TOPIC]-002-[slug].md
│   └── ...
├── problems/
│   ├── [TOPIC]-001-[slug].md
│   ├── [TOPIC]-002-[slug].md
│   └── ...
├── testcases/
│   ├── [TOPIC]-001-[slug].yaml
│   ├── [TOPIC]-002-[slug].yaml
│   └── ...
├── images/
│   ├── [TOPIC]-001/
│   │   └── README.md
│   ├── [TOPIC]-002/
│   │   └── README.md
│   └── ...
└── [source-practice-file].md
```

---

## 🔄 Topic-Specific Customization Guide

### Topic Prefix Codes

- **ARR** = Arrays
- **BIT** = Bitwise
- **CON** = Concurrency
- **DP** = Dynamic Programming
- **GRA** = Graphs
- **GRB** = Graph Basics
- **GRE** = Greedy
- **HAS** = Hashing
- **HEA** = Heaps
- **LNK** = Linked Lists
- **MAT** = Math Advanced
- **NUM** = Number Theory
- **PRO** = Probabilistic
- **PDS** = Probabilistic Data Structures
- **QUE** = Queues
- **REC** = Recursion
- **SEG** = Segment Tree
- **SOR** = Sorting
- **STK** = Stacks
- **STR** = Strings
- **STC** = Strings Classic
- **TRE** = Trees
- **TDP** = Trees DP
- **TRI** = Tries
- **AGR** = Advanced Graphs
- **GEO** = Geometry
- **GAM** = Game Theory

### Topic-Specific Considerations

**For Bitwise:**

- Focus on bit manipulation techniques (XOR, AND, OR, shifts)
- Include binary representations in explanations
- Real-world: cryptography, network security, compression

**For Concurrency:**

- Focus on thread safety, synchronization, race conditions
- Include timing diagrams
- Real-world: server systems, parallel processing, databases

**For Dynamic Programming:**

- Focus on state transitions, memoization, tabulation
- Include DP table visualizations
- Real-world: optimization problems, resource allocation

**For Graphs:**

- Focus on traversal, shortest paths, connectivity
- Include graph diagrams
- Real-world: navigation, social networks, routing

**For Trees:**

- Focus on traversal patterns, recursion, tree properties
- Include tree structure diagrams
- Real-world: file systems, organization hierarchies, parsing

[Add similar guidelines for other topics]

---

## ✅ Quality Checklist (Run Before Submission)

### Per Problem:

- [ ] Editorial file: 500-750 lines with real-world scenario
- [ ] Problem file: 150-250 lines with 1 example, 4 templates
- [ ] Test cases: 40 cases (2+3+35) in clean YAML format
- [ ] Images folder: README.md with 6 prompts
- [ ] All frontmatter fields match Arrays format
- [ ] No AI artifacts or thinking comments
- [ ] problem_id consistent across all 4 files
- [ ] Slug matches filename

### Format Verification:

- [ ] Compare with Arrays/problems/ARR-001-snack-restock-snapshot.md
- [ ] Compare with Arrays/editorials/ARR-001-snack-restock-snapshot.md
- [ ] Compare with Arrays/testcases/ARR-001-snack-restock-snapshot.yaml
- [ ] Compare with Arrays/images/ARR-001/README.md
- [ ] Run: `diff -u [YourFile] [ArraysFile]` to verify structure

### CI Sync Ready:

- [ ] Test cases YAML has NO extra fields
- [ ] All solution templates present (Java, Python, C++, JS)
- [ ] Image references included (even if images not generated yet)
- [ ] No formatting errors in markdown or YAML

---

## 📊 Example Usage

### Generate Single Problem

```
Generate complete educational materials for Concurrency problem 1:

**Source:** /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Concurrency/basic-concurrency-practice.md
**Problem:** 1. Odd-Even Concurrent Printer with Threads
**Format:** Match Arrays folder exactly (verified in Bitwise/FORMAT_VERIFICATION.md)
```

### Generate Multiple Problems

```
Generate complete educational materials for DP problems 1-5:

**Source:** /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/DP/basic-dp-practice.md
**Problems:** 1-5 (First 5 problems)
**Format:** Match Arrays folder exactly (verified in Bitwise/FORMAT_VERIFICATION.md)
```

### Generate All Problems

```
Generate complete educational materials for all 16 Graphs problems:

**Source:** /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Graphs/basic-graph-practice.md
**Problems:** All 16 problems
**Format:** Match Arrays folder exactly (verified in Bitwise/FORMAT_VERIFICATION.md)
```

---

## 🔍 Verification Commands

After generation, run these commands to verify:

```bash
# Check file structure
ls -R [TopicFolder]/

# Count lines in editorial (should be 500-750)
wc -l [TopicFolder]/editorials/[TOPIC]-001-*.md

# Count lines in problem (should be 150-250)
wc -l [TopicFolder]/problems/[TOPIC]-001-*.md

# Verify YAML format (should show clean structure)
cat [TopicFolder]/testcases/[TOPIC]-001-*.yaml | head -50

# Compare with Arrays reference
diff -u [TopicFolder]/problems/[TOPIC]-001-*.md Arrays/problems/ARR-001-snack-restock-snapshot.md | head -100
```

---

## 📝 Notes

- **Total Time Per Problem:** ~30-45 minutes for complete generation
- **Content Length:** ~1,000-1,200 lines total per problem
- **CI Sync:** All files are immediately importable via backend CI pipeline
- **Image Generation:** Separate step; prompts provided for AI tools
- **Quality Over Speed:** Better to generate fewer problems correctly than many with errors

---

## 🎓 Reference Examples

**Perfect Examples (CI-Sync Ready):**

- `/Bitwise/editorials/BIT-001-odd-after-bit-salt.md`
- `/Bitwise/problems/BIT-001-odd-after-bit-salt.md`
- `/Bitwise/testcases/BIT-001-odd-after-bit-salt.yaml`
- `/Bitwise/images/BIT-001/README.md`

**Verification Documents:**

- `/Bitwise/FORMAT_VERIFICATION.md` - Detailed format comparison
- `/Bitwise/CI-SYNC-READY.md` - CI sync checklist
- `/Bitwise/FINAL-VERIFICATION.md` - Side-by-side comparison

**Always Reference:** `/Arrays/` folder as the gold standard template

---

## 🚀 Next Steps After Generation

1. **Verify Format:** Use checklist above
2. **Run Diff:** Compare with Arrays reference files
3. **Test YAML:** Validate YAML syntax with `yamllint`
4. **Generate Images:** Use provided prompts with DALL-E/Midjourney
5. **Backend Sync:** Files are ready for CI import pipeline
6. **Update Docs:** Add to topic STATUS.md file

---

**Version:** 1.0
**Last Updated:** December 18, 2025
**Based On:** Arrays folder format + Bitwise BIT-001/002/003 verified structure
**CI Status:** ✅ Production Ready
