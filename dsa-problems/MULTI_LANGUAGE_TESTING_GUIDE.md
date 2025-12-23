# Multi-Language Testing Framework Guide

## Overview

This framework allows testing DSA solutions across **C++, Java, Python, and JavaScript** independently, making it easy to identify language-specific issues.

## 📁 Files

```
dsa-problems/
├── test_language.py           # Core testing framework
├── test_cpp.sh                # C++ test runner
├── test_java.sh               # Java test runner
├── test_python.sh             # Python test runner
├── test_javascript.sh         # JavaScript test runner
└── UNIVERSAL_TESTCASE_GENERATION_PROMPT.md
```

## 🚀 Quick Start

### Test All Languages for a Topic

```bash
# Test all problems in AdvancedGraphs
cd dsa-problems
./test_cpp.sh AdvancedGraphs
./test_java.sh AdvancedGraphs
./test_python.sh AdvancedGraphs
./test_javascript.sh AdvancedGraphs
```

### Test Specific Problems

```bash
# Test specific problems
./test_cpp.sh AdvancedGraphs AGR-001 AGR-002 AGR-006
./test_java.sh Arrays ARR-001 ARR-002
./test_python.sh Graphs GRP-001 GRP-005
```

### Test Single Language with Python Script

```bash
# Direct python invocation
python3 test_language.py cpp AdvancedGraphs AGR-001
python3 test_language.py java Arrays
python3 test_language.py python Graphs GRP-001 GRP-002
```

## 📊 Output Format

```
================================================================================
C++ TEST RESULTS
================================================================================

AGR-001: ✅ 31/31
AGR-002: ✅ 30/30
AGR-003: ❌ 27/28 (Failed: 1)
  • hidden[7]: WRONG_ANSWER
    Expected: 20
99 100 100 100 100 100 100 ...
    Actual:   ...

================================================================================
SUMMARY - C++
================================================================================
Total Tests: 451
✅ Passed: 450
❌ Failed: 1
Pass Rate: 99.8%
```

## 🔧 How It Works

### 1. Solution Extraction

The framework extracts solutions from editorial markdown files:

````markdown
### C++

​`cpp
#include <iostream>
// ... solution code
​`

### Java

​`java
import java.util.*;
// ... solution code
​`

### Python

​```python
import sys

# ... solution code

​```

### JavaScript

​`javascript
const readline = require("readline");
// ... solution code
​`
````

### 2. Compilation (C++/Java)

- **C++**: `g++ -std=c++17 -O2 file.cpp -o file`
- **Java**: `javac File.java` then `java -cp . ClassName`
- **Python**: No compilation needed
- **JavaScript**: No compilation needed (Node.js)

### 3. Test Execution

For each test case:

1. Feed input to the compiled/interpreted solution
2. Capture stdout
3. Compare with expected output (exact string match)
4. Report: PASS, WRONG_ANSWER, COMPILE_ERROR, RUNTIME_ERROR, or TIMEOUT

### 4. Result Aggregation

- Count passed/failed per problem
- Show first 2 failures with details
- Calculate overall pass rate

## 📋 Test Case File Structure

Test cases are stored in YAML format:

```yaml
problem_id: CATEGORY_PROBLEM_NAME__ID
samples:
  - input: |-
      4 4
      0 1
      1 2
      2 0
      1 3
    output: |-
      1
      1
public:
  - input: |-
      1 0
    output: |-
      0
      0
hidden:
  - input: |-
      5 5
      ...
    output: |-
      ...
```

## 🎯 Benefits of Separate Testing

### 1. **Isolate Language-Specific Issues**

```bash
# Test only Java to find Java-specific bugs
./test_java.sh AdvancedGraphs

# Result: Java has compilation error in AGR-016
# → Fix only Java code, no need to check C++/Python
```

### 2. **Faster Iteration**

```bash
# After fixing C++ solution, test only C++
./test_cpp.sh AdvancedGraphs AGR-006

# No need to wait for Java/Python tests
```

### 3. **Parallel Testing**

```bash
# Run all 4 languages in parallel
./test_cpp.sh AdvancedGraphs &
./test_java.sh AdvancedGraphs &
./test_python.sh AdvancedGraphs &
./test_javascript.sh AdvancedGraphs &
wait
```

### 4. **CI/CD Integration**

```yaml
# GitHub Actions example
jobs:
  test-cpp:
    runs-on: ubuntu-latest
    steps:
      - run: ./test_cpp.sh AdvancedGraphs

  test-java:
    runs-on: ubuntu-latest
    steps:
      - run: ./test_java.sh AdvancedGraphs

  test-python:
    runs-on: ubuntu-latest
    steps:
      - run: ./test_python.sh AdvancedGraphs
```

## 🔍 Debugging Failed Tests

### 1. **Identify the Failure**

```bash
./test_python.sh AdvancedGraphs AGR-006
```

Output:

```
AGR-006: ❌ 16/29 (Failed: 13)
  • samples[1]: WRONG_ANSWER
    Expected: 0
1
3 0 1 2...
    Actual:   0

1
3 0 1 2...
```

### 2. **Extract Test Case**

```bash
# View the specific test case
cat AdvancedGraphs/testcases/AGR-006-articulation-and-bcc.yaml | grep -A 10 "samples:"
```

### 3. **Run Solution Manually**

```bash
# Extract Python solution
grep -A 100 "### Python" AdvancedGraphs/editorials/AGR-006*.md > temp_solution.py

# Run with test input
echo "3 3
0 1
1 2
2 0" | python3 temp_solution.py
```

### 4. **Compare Outputs**

The issue in AGR-006 was: **Extra blank line when no articulation points**

Expected:

```
0
1
3 0 1 2
```

Actual (wrong):

```
0

1
3 0 1 2
```

### 5. **Fix and Retest**

```bash
# After fixing the editorial
./test_python.sh AdvancedGraphs AGR-006

# Result: ✅ 29/29
```

## 📝 Adding New Topics

### 1. Create Topic Structure

```bash
mkdir -p NewTopic/{editorials,testcases,problems,quizzes}
```

### 2. Add Editorials with Solutions

Each editorial must have sections for all languages:

````markdown
### Java

​`java
// Solution
​`

### Python

​```python

# Solution

​```

### C++

​`cpp
// Solution
​`

### JavaScript

​`javascript
// Solution
​`
````

### 3. Generate Test Cases

Use `UNIVERSAL_TESTCASE_GENERATION_PROMPT.md` to generate comprehensive test cases.

### 4. Run Tests

```bash
./test_cpp.sh NewTopic
./test_java.sh NewTopic
./test_python.sh NewTopic
./test_javascript.sh NewTopic
```

## ⚙️ Configuration

### Timeout

Default: 5 seconds per test case

To modify, edit `test_language.py`:

```python
result = subprocess.run(
    cmd,
    input=test_input,
    capture_output=True,
    text=True,
    timeout=10  # Change this
)
```

### Compilation Flags

**C++**: Modify in `compile_code()`:

```python
['g++', '-std=c++17', '-O2', '-Wall', temp_file, '-o', output_file]
```

**Java**: Modify in `compile_code()`:

```python
['javac', '-Xlint:all', temp_file]
```

## 🐛 Common Issues

### Issue 1: "g++ not found"

**Solution**: Install g++

```bash
# macOS
xcode-select --install

# Ubuntu/Debian
sudo apt-get install g++
```

### Issue 2: "javac not found"

**Solution**: Install Java JDK

```bash
# macOS
brew install openjdk

# Ubuntu/Debian
sudo apt-get install default-jdk
```

### Issue 3: "node not found"

**Solution**: Install Node.js

```bash
# macOS
brew install node

# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Issue 4: Test hangs

**Cause**: Infinite loop or reading too much input

**Solution**:

1. Check solution code for infinite loops
2. Verify input format matches what solution expects
3. Increase timeout if needed

### Issue 5: Output mismatch on whitespace

**Cause**: Extra spaces, newlines, or missing newlines

**Solution**: Fix output format in editorial solution to match EXACTLY:

```python
# Wrong
print(f"{n}")
print(f"{result}")

# Right
print(f"{n}\n{result}")  # Or use separate prints
```

## 📊 Interpreting Results

### 100% Pass Rate ✅

All solutions are correct and properly formatted.

### 95-99% Pass Rate ⚠️

- Minor formatting issues
- Edge case handling
- Usually quick fixes

### 85-95% Pass Rate 🔧

- Multiple problems need attention
- Output format inconsistencies
- Some edge cases missing

### <85% Pass Rate 🚨

- Major issues with solutions or test cases
- Review problem specification
- Regenerate test cases if needed

## 🎯 Best Practices

1. **Test early and often** - Don't wait until all problems are done
2. **Fix one language at a time** - Use separate test scripts
3. **Verify test cases first** - If Python fails, check test case correctness
4. **Match output format exactly** - One extra newline = failure
5. **Document edge cases** - Note special cases in test case comments

## 📚 Related Documentation

- `UNIVERSAL_TESTCASE_GENERATION_PROMPT.md` - How to generate test cases
- `AdvancedGraphs/COMPREHENSIVE_TEST_RESULTS.md` - Example test results
- `AdvancedGraphs/BUG_FIX_REPORT.md` - Common bugs and fixes

## 🚀 Next Steps

1. Make scripts executable:

```bash
chmod +x test_*.sh
```

2. Test existing topics:

```bash
./test_python.sh AdvancedGraphs
```

3. Fix any failures

4. Apply to new topics:

```bash
./test_cpp.sh Arrays
./test_java.sh Graphs
```

---

**Happy Testing! 🎉**
