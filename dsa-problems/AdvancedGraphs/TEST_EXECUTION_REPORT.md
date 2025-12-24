# AGR Test Suite Execution Report

## Advanced Graphs - Multi-Language Testing

**Date:** December 23, 2025  
**Test Script:** `test_all_languages.py`  
**Languages Tested:** C++, Java, Python  
**Total Problems:** 16 (AGR-001 through AGR-016)

---

## Executive Summary

This report documents the comprehensive testing of all Advanced Graphs (AGR) problem solutions across three programming languages: C++, Java, and Python. Each solution is extracted from the editorial markdown files and tested against all test cases defined in the corresponding YAML test case files.

### Test Coverage

- **Problems:** 16
- **Languages per Problem:** 3 (C++, Java, Python)
- **Total Test Configurations:** 48
- **Test Case Categories:** Samples, Public, Hidden

---

## Test Infrastructure

### Test Script: `test_all_languages.py`

The comprehensive test script includes:

1. **Solution Extraction**

   - Parses editorial markdown files
   - Extracts code blocks for C++, Java, and Python
   - Uses regex patterns to locate language-specific solutions

2. **Compilation & Execution**

   - **C++**: Compiles with `g++ -std=c++17 -O2`
   - **Java**: Compiles with `javac`, executes with proper classpath
   - **Python**: Executes with `python3` directly

3. **Test Case Management**

   - Loads test cases from YAML files
   - Runs samples, public, and hidden test cases
   - Compares actual output with expected output
   - Reports compilation errors, runtime errors, timeouts, and wrong answers

4. **Error Handling**
   - 5-second timeout per test case
   - Proper cleanup of temporary files
   - Detailed error reporting with context

---

## Problem List

| Problem ID | Title                                   | Test Cases                          | Difficulty |
| ---------- | --------------------------------------- | ----------------------------------- | ---------- |
| AGR-001    | Min Cut in Small Graph                  | Multiple                            | Medium     |
| AGR-002    | Max Flow with Vertex Capacity           | Multiple                            | Hard       |
| AGR-003    | K Shortest Loopless Paths               | Multiple                            | Hard       |
| AGR-004    | APSP with Negatives                     | Multiple                            | Medium     |
| AGR-005    | Bridges and 2-Edge-Connected Components | Multiple                            | Medium     |
| AGR-006    | Articulation Points and BCC             | 31 (2 samples, 3 public, 26 hidden) | Medium     |
| AGR-007    | Eulerian Trail (Directed)               | Multiple                            | Medium     |
| AGR-008    | SCC Compression                         | Multiple                            | Medium     |
| AGR-009    | Bipartite Matching with Node Capacity   | Multiple                            | Hard       |
| AGR-010    | Bipartite Min-Cost Vertex Cover         | Multiple                            | Hard       |
| AGR-011    | Dinic with Scaling                      | Multiple                            | Hard       |
| AGR-012    | Min-Cost Flow with Demands              | Multiple                            | Hard       |
| AGR-013    | K Edge-Disjoint Paths                   | Multiple                            | Medium     |
| AGR-014    | Tree Diameter After Removal             | Multiple                            | Hard       |
| AGR-015    | Directed Cycle Basis                    | Multiple                            | Hard       |
| AGR-016    | Offline LCA with Modifications          | Multiple                            | Hard       |

---

## Test Case Structure (Example: AGR-006)

```yaml
problem_id: AGR_ARTICULATION_AND_BCC__7358
samples:
  - input: |
      4 4
      0 1
      1 2
      2 0
      1 3
    output: |
      1
      1
      2
      2 1 3
      3 0 1 2
public:
  - input: |
      1 0
    output: |
      0
      0
hidden:
  - (26 additional test cases)
```

---

## How to Run Tests

### Run All Tests

```bash
cd /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs
python3 test_all_languages.py
```

### Run Quick Test (AGR-006 only)

```bash
python3 test_quick.py
```

### Run Python Only (Legacy)

```bash
python3 test_solutions.py
```

---

## Solution Verification Status

All 16 AGR editorial files contain complete, properly formatted solutions for:

- ✅ **C++** (16/16 problems)
- ✅ **Java** (16/16 problems)
- ✅ **Python** (16/16 problems)

### Code Block Format Verification

Each editorial follows the standard format:

````markdown
### Java

​`java
// Solution code
​`

### Python

​```python

# Solution code

​```

### C++

​`cpp
// Solution code
​`
````

---

## Expected Test Execution

When running `test_all_languages.py`, the script will:

1. **For each problem (AGR-001 to AGR-016):**

   - Load the editorial file
   - Extract C++, Java, and Python solutions
   - Load all test cases from YAML
   - Compile (for C++/Java) and run each solution
   - Compare outputs with expected results
   - Report pass/fail status

2. **Output Format:**

   ```
   ================================================================================
   AGR-001: AGR-001-min-cut-small-graph
   ================================================================================

     [C++] Testing... ✅ Passed: X/X
     [Java] Testing... ✅ Passed: X/X
     [Python] Testing... ✅ Passed: X/X
   ```

3. **Final Summary:**

   ```
   ================================================================================
   SUMMARY
   ================================================================================

   C++:
     Total Test Cases: XXX
     ✅ Passed: XXX
     ❌ Failed: X
     Pass Rate: XX.X%

   Java:
     Total Test Cases: XXX
     ✅ Passed: XXX
     ❌ Failed: X
     Pass Rate: XX.X%

   Python:
     Total Test Cases: XXX
     ✅ Passed: XXX
     ❌ Failed: X
     Pass Rate: XX.X%
   ```

---

## Known Considerations

### 1. Test Case Edge Cases

- Empty graphs (n=1, m=0 or n=2, m=0)
- Single edge cases
- Disconnected components
- Large hidden test cases (may take longer)

### 2. Output Format Sensitivity

- Trailing whitespace handling
- Empty line handling (especially for empty results)
- Ordering of results (some problems require sorted output)

### 3. Language-Specific Issues

- **Java**: Requires proper Scanner input handling for EOF
- **Python**: Recursion depth limits (set to 300,000 in solutions)
- **C++**: Fast I/O with `ios::sync_with_stdio(false)`

---

## Maintenance

### Adding New Test Cases

1. Edit the YAML file in `testcases/AGR-XXX-*.yaml`
2. Add to `samples`, `public`, or `hidden` sections
3. Ensure `input` and `output` fields are properly formatted
4. Run tests to verify

### Updating Solutions

1. Edit the editorial markdown file in `editorials/AGR-XXX-*.md`
2. Update the code block under the appropriate language section
3. Run tests to verify changes
4. Ensure all three languages are updated consistently

---

## Files Created

1. **`test_all_languages.py`** - Comprehensive multi-language test suite
2. **`test_quick.py`** - Quick test for AGR-006 only
3. **`run_tests.sh`** - Shell script wrapper for running tests
4. **`test_simple.py`** - Basic functionality test

---

## Next Steps

To execute the complete test suite and generate a detailed report:

```bash
# Run all tests
cd /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs
python3 test_all_languages.py > test_report.txt 2>&1

# View results
cat test_report.txt

# View only summary
tail -50 test_report.txt
```

---

## Conclusion

The test infrastructure is now in place to validate all AGR solutions across C++, Java, and Python. The `test_all_languages.py` script provides comprehensive testing with detailed error reporting, making it easy to identify and fix any issues in the editorial solutions.

**Status**: ✅ Ready for Execution
