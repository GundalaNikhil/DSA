# Judge0 Integration Guide - Main Function Management

## Overview

When solutions are tested on Judge0 or similar online judges, they run as complete programs. Any changes to the `main` function or input/output handling in **editorial solutions** must be synchronized with the **problem template files**.

## 📋 Why This Matters

### Editorial Solution (editorials/PROB-ID.md)

```python
def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    # ... process and output
    sys.stdout.write(result)

if __name__ == "__main__":
    main()
```

### Problem Template (problems/PROB-ID.md)

```python
def solution(n, arr):
    # User writes this
    pass

# DO NOT MODIFY BELOW THIS LINE
def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    result = solution(n, arr)
    sys.stdout.write(str(result))

if __name__ == "__main__":
    main()
```

**These MUST match!** The input parsing and output formatting must be identical.

---

## 🔄 Synchronization Rules

### Rule 1: Input Parsing Must Match

If editorial solution reads:

```python
n, m = map(int, input().split())
```

Problem template must read:

```python
n, m = map(int, input().split())
```

### Rule 2: Output Format Must Match

If editorial outputs:

```python
print(f"{count}\n{result}")
```

Problem template must output:

```python
print(f"{count}\n{result}")
```

### Rule 3: Edge Case Handling Must Match

If editorial handles empty input:

```python
if not data:
    return
```

Problem template must handle it the same way.

---

## 📝 Step-by-Step Synchronization Process

### Step 1: Identify the Change

Example: Fixing AGR-006 output format

**Before (Wrong):**

```python
# Editorial
print(f"{len(aps)}\n")  # Extra newline!
for ap in aps:
    print(ap, end=' ')
```

**After (Fixed):**

```python
# Editorial
print(len(aps))
if aps:
    print(' '.join(map(str, aps)))
```

### Step 2: Update Problem Template

Find the problem file: `problems/AGR-006-articulation-and-bcc.md`

Locate the `main` function or runner code section:

````markdown
## Template Code

### Python

​```python
def articulation_and_bcc(n: int, edges: list[tuple[int, int]]):
"""
Find articulation points and biconnected components.

    Returns:
        tuple: (sorted_articulation_points, list_of_bccs)
    """
    # TODO: Implement your solution here
    pass

# DO NOT MODIFY BELOW THIS LINE

import sys

def main():
input = sys.stdin.read
data = input().split()
if not data:
return

    n = int(data[0])
    m = int(data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        edges.append((u, v))
        idx += 2

    aps, bccs = articulation_and_bcc(n, edges)

    # OUTPUT - MUST MATCH EDITORIAL
    print(len(aps))
    if aps:
        print(' '.join(map(str, aps)))
    print(len(bccs))
    for bcc in bccs:
        print(f"{len(bcc)} {' '.join(map(str, bcc))}")

if **name** == "**main**":
main()
​```
````

### Step 3: Verify All Languages

Update the same output format in **all four languages**:

#### C++

```cpp
// Problem template
int main() {
    // ... input parsing (must match editorial)

    auto result = solution.solve(n, edges);

    // OUTPUT - MUST MATCH EDITORIAL
    cout << result.aps.size();
    if (result.aps.size() > 0) {
        cout << "\n";
        for (int i = 0; i < result.aps.size(); i++) {
            if (i) cout << ' ';
            cout << result.aps[i];
        }
    }
    // ... rest of output
}
```

#### Java

```java
// Problem template
public class Main {
    public static void main(String[] args) {
        // ... input parsing (must match editorial)

        Solution solution = new Solution();
        Result result = solution.solve(n, edges);

        // OUTPUT - MUST MATCH EDITORIAL
        System.out.print(result.aps.length);
        if (result.aps.length > 0) {
            System.out.print("\n");
            for (int i = 0; i < result.aps.length; i++) {
                if (i > 0) System.out.print(' ');
                System.out.print(result.aps[i]);
            }
        }
        // ... rest of output
    }
}
```

#### JavaScript

```javascript
// Problem template
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  // ... input parsing (must match editorial)

  const solution = new Solution();
  const result = solution.solve(n, edges);

  // OUTPUT - MUST MATCH EDITORIAL
  process.stdout.write(String(result.aps.length));
  if (result.aps.length > 0) {
    process.stdout.write("\n");
    process.stdout.write(result.aps.join(" "));
  }
  // ... rest of output
});
```

---

## 🔍 Finding What Needs Updating

### Method 1: Automated Script

Create `sync_problem_templates.py`:

```python
#!/usr/bin/env python3
"""
Find problems that need template updates after editorial changes.
"""
import os
import re
from pathlib import Path

def extract_main_function(file_path, language):
    """Extract main function from editorial."""
    with open(file_path, 'r') as f:
        content = f.read()

    if language == 'python':
        pattern = r'def main\(\):.*?if __name__ == "__main__":\s+main\(\)'
    elif language == 'cpp':
        pattern = r'int main\(\) \{.*?\}'
    elif language == 'java':
        pattern = r'public static void main\(String\[\] args\) \{.*?\}'

    match = re.search(pattern, content, re.DOTALL)
    return match.group(0) if match else None

def compare_editorial_and_problem(prob_id, topic_dir):
    """Compare main functions between editorial and problem template."""
    editorial_file = Path(topic_dir) / 'editorials' / f'{prob_id}*.md'
    problem_file = Path(topic_dir) / 'problems' / f'{prob_id}*.md'

    editorial_files = list(Path(topic_dir).glob(f'editorials/{prob_id}*.md'))
    problem_files = list(Path(topic_dir).glob(f'problems/{prob_id}*.md'))

    if not editorial_files or not problem_files:
        return None

    # Extract and compare
    editorial_main = extract_main_function(editorial_files[0], 'python')
    problem_main = extract_main_function(problem_files[0], 'python')

    if editorial_main != problem_main:
        return {
            'problem_id': prob_id,
            'editorial_file': editorial_files[0],
            'problem_file': problem_files[0],
            'needs_update': True
        }

    return None

# Usage
topic_dir = 'AdvancedGraphs'
problems = ['AGR-001', 'AGR-002', 'AGR-006']

for prob_id in problems:
    result = compare_editorial_and_problem(prob_id, topic_dir)
    if result:
        print(f"⚠️  {prob_id} needs template update!")
```

### Method 2: Manual Checklist

After modifying editorial, check:

- [ ] Python main function updated in problem template
- [ ] C++ main function updated in problem template
- [ ] Java main function updated in problem template
- [ ] JavaScript main function updated in problem template
- [ ] Input parsing matches across all languages
- [ ] Output format matches across all languages
- [ ] Edge case handling matches across all languages

---

## 📊 Common Scenarios

### Scenario 1: Fixing Output Formatting

**Change:** Remove extra newline in editorial

**Update Required:**

1. Editorial solution (all 4 languages)
2. Problem template (all 4 languages)

**Verification:**

```bash
# Test editorial
./test_python.sh AdvancedGraphs AGR-006

# Test problem template manually
# (Would need Judge0 or manual compilation)
```

### Scenario 2: Changing Input Parsing

**Change:** Switch from `sys.stdin.read()` to `input()`

**Update Required:**

1. Editorial solution Python section
2. Problem template Python section
3. Document the change in problem description

**Verification:**

```bash
./test_python.sh AdvancedGraphs AGR-006
```

### Scenario 3: Adding Edge Case Handling

**Change:** Handle empty input gracefully

**Update Required:**

1. Editorial solution (all languages)
2. Problem template (all languages)
3. Add test case for empty input

**Verification:**

```bash
# Run all tests
./test_cpp.sh AdvancedGraphs AGR-006
./test_java.sh AdvancedGraphs AGR-006
./test_python.sh AdvancedGraphs AGR-006
```

---

## 🎯 Judge0 Specific Considerations

### Input Method

Judge0 provides input via stdin. Ensure:

```python
# Correct
input = sys.stdin.read
data = input().split()

# Also correct
n = int(input())
arr = list(map(int, input().split()))

# Avoid (may not work on Judge0)
n = int(sys.argv[1])  # Command-line args
```

### Output Method

```python
# Correct
print(result)
sys.stdout.write(str(result))

# Avoid
return result  # Nothing gets printed!
```

### Imports

Ensure all imports are included:

```python
# Editorial
import sys
import collections
from typing import List

# Problem template - MUST include same imports
import sys
import collections
from typing import List

def solution(...):
    # User code here
    pass

# Runner code with same imports
```

---

## 🔧 Automation Tools

### Tool 1: Template Sync Script

````python
#!/usr/bin/env python3
"""
sync_templates.py - Sync main functions from editorial to problem templates
"""
import sys
import re
from pathlib import Path

def sync_problem_template(prob_id, topic_dir, language='python'):
    editorial_file = list(Path(topic_dir).glob(f'editorials/{prob_id}*.md'))[0]
    problem_file = list(Path(topic_dir).glob(f'problems/{prob_id}*.md'))[0]

    # Extract main from editorial
    with open(editorial_file, 'r') as f:
        editorial_content = f.read()

    # Extract main function for the language
    if language == 'python':
        pattern = r'(def main\(\):.*?if __name__ == "__main__":\s+main\(\))'
        main_func = re.search(pattern, editorial_content, re.DOTALL)

    if not main_func:
        print(f"Could not find main function for {language} in {prob_id}")
        return False

    # Update problem template
    with open(problem_file, 'r') as f:
        problem_content = f.read()

    # Replace main function in problem template
    updated_content = re.sub(
        r'# DO NOT MODIFY BELOW THIS LINE.*?(?=```|\Z)',
        f"# DO NOT MODIFY BELOW THIS LINE\n{main_func.group(1)}\n",
        problem_content,
        flags=re.DOTALL
    )

    with open(problem_file, 'w') as f:
        f.write(updated_content)

    print(f"✅ Updated {prob_id} problem template")
    return True

# Usage
if __name__ == '__main__':
    prob_id = sys.argv[1]
    topic_dir = sys.argv[2]
    sync_problem_template(prob_id, topic_dir)
````

Usage:

```bash
python3 sync_templates.py AGR-006 AdvancedGraphs
```

### Tool 2: Validation Script

```python
#!/usr/bin/env python3
"""
validate_templates.py - Ensure problem templates match editorials
"""
def validate_template(prob_id, topic_dir):
    # Extract main from editorial
    # Extract main from problem
    # Compare
    # Return True if match, False if mismatch
    pass
```

---

## 📚 Checklist for Changes

When you modify an editorial solution:

### Phase 1: Update Editorial

- [ ] Modify main function in editorial
- [ ] Update all 4 languages (C++, Java, Python, JS)
- [ ] Test editorial solutions
- [ ] Verify all test cases pass

### Phase 2: Update Problem Templates

- [ ] Sync main function to Python template
- [ ] Sync main function to C++ template
- [ ] Sync main function to Java template
- [ ] Sync main function to JavaScript template
- [ ] Verify input/output format matches

### Phase 3: Verify

- [ ] Run test_python.sh to verify editorial
- [ ] Manually test problem template (or use Judge0)
- [ ] Check edge cases work correctly
- [ ] Document the change

### Phase 4: Commit

- [ ] Commit editorial changes
- [ ] Commit problem template changes
- [ ] Update changelog/docs

---

## 🚨 Red Flags

Watch out for these common mistakes:

❌ **Different input parsing**

```python
# Editorial
n = int(input())

# Problem template (WRONG!)
n = int(data[0])
```

❌ **Different output format**

```python
# Editorial
print(result)

# Problem template (WRONG!)
return result  # Nothing printed!
```

❌ **Missing imports**

```python
# Editorial
import sys
from collections import defaultdict

# Problem template (WRONG!)
# Missing imports!
```

❌ **Different edge case handling**

```python
# Editorial
if not data:
    return

# Problem template (WRONG!)
# No check for empty input
```

---

## ✅ Best Practices

1. **Always update all 4 languages** - Don't leave any out
2. **Test after every change** - Use the test scripts
3. **Keep templates simple** - User code separate from runner code
4. **Document the contract** - What user function should return
5. **Automate when possible** - Use sync scripts

---

## 📖 Example: Complete Update Flow

### 1. Identify Issue

```bash
./test_cpp.sh AdvancedGraphs AGR-006
# Result: 13 failures due to output format
```

### 2. Fix Editorial

Edit `editorials/AGR-006-articulation-and-bcc.md`:

- Update C++ main function
- Update Java main function
- Update Python main function
- Update JavaScript main function

### 3. Test Editorial

```bash
./test_cpp.sh AdvancedGraphs AGR-006
./test_java.sh AdvancedGraphs AGR-006
./test_python.sh AdvancedGraphs AGR-006
# All pass!
```

### 4. Update Problem Templates

Edit `problems/AGR-006-articulation-and-bcc.md`:

- Sync C++ runner code
- Sync Java runner code
- Sync Python runner code
- Sync JavaScript runner code

### 5. Verify Templates

Manually test or use Judge0 to verify templates work.

### 6. Document

Update changelog noting the output format fix.

---

**Remember:** Editorial and problem template must always be in sync for Judge0 integration to work correctly!
