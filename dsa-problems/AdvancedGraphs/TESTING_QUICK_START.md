# AGR Testing Summary - C++, Java & Python

## Quick Reference

**Test Script Location:** `/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs/test_all_languages.py`

**To Run All Tests:**

```bash
cd /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs
python3 test_all_languages.py
```

## What's Been Set Up

### 1. Comprehensive Test Script ✅

- **File:** `test_all_languages.py`
- **Tests:** All 16 AGR problems (AGR-001 through AGR-016)
- **Languages:** C++, Java, Python
- **Features:**
  - Extracts solutions from editorial markdown files
  - Compiles C++ and Java code
  - Runs all test cases (samples, public, hidden)
  - Compares outputs and reports errors
  - Detailed error messages with context

### 2. Solution Verification ✅

All 16 editorial files contain complete solutions:

- **C++ solutions:** 16/16 ✓
- **Java solutions:** 16/16 ✓
- **Python solutions:** 16/16 ✓

### 3. Test Case Files ✅

All 16 test case YAML files present:

- `AGR-001-min-cut-small-graph.yaml`
- `AGR-002-max-flow-vertex-capacity.yaml`
- `AGR-003-k-shortest-loopless-paths.yaml`
- `AGR-004-apsp-with-negatives.yaml`
- `AGR-005-bridges-and-2ecc.yaml`
- `AGR-006-articulation-and-bcc.yaml` (31 test cases)
- `AGR-007-eulerian-trail-directed.yaml`
- `AGR-008-scc-compression.yaml`
- `AGR-009-bipartite-matching-node-capacity.yaml`
- `AGR-010-bipartite-min-cost-vertex-cover.yaml`
- `AGR-011-dinic-with-scaling.yaml`
- `AGR-012-mincost-flow-demands.yaml`
- `AGR-013-k-edge-disjoint-paths.yaml`
- `AGR-014-tree-diameter-after-removal.yaml`
- `AGR-015-directed-cycle-basis.yaml`
- `AGR-016-offline-lca-with-mods.yaml`

## How the Test Works

1. **For each problem:**

   - Loads the editorial from `editorials/AGR-XXX-*.md`
   - Extracts C++, Java, and Python code blocks
   - Loads test cases from `testcases/AGR-XXX-*.yaml`

2. **For each language:**

   - **C++:** Compiles with `g++ -std=c++17 -O2`, runs executable
   - **Java:** Compiles with `javac`, runs with `java`
   - **Python:** Runs directly with `python3`

3. **For each test case:**
   - Feeds input to the compiled/interpreted program
   - Captures output
   - Compares with expected output
   - Reports: ✅ PASS or ❌ FAIL with details

## Expected Output Format

```
================================================================================
AGR TEST CASE VALIDATION - ALL LANGUAGES
================================================================================
================================================================================
AGR-001: AGR-001-min-cut-small-graph
================================================================================

  [C++] Testing... ✅ Passed: 15/15
  [Java] Testing... ✅ Passed: 15/15
  [Python] Testing... ✅ Passed: 15/15

================================================================================
AGR-002: AGR-002-max-flow-vertex-capacity
================================================================================

  [C++] Testing... ✅ Passed: 20/20
  [Java] Testing... ❌ Passed: 19/20, Failed: 1
       • hidden[5]: WRONG_ANSWER
         Expected: 42...
         Actual:   41...
  [Python] Testing... ✅ Passed: 20/20

... (continues for all 16 problems)

================================================================================
SUMMARY
================================================================================

C++:
  Total Test Cases: 250
  ✅ Passed: 248
  ❌ Failed: 2
  Pass Rate: 99.2%

  Problems with failures:
    • AGR-003: 1 failures

Java:
  Total Test Cases: 250
  ✅ Passed: 247
  ❌ Failed: 3
  Pass Rate: 98.8%

  Problems with failures:
    • AGR-002: 1 failures
    • AGR-007: 2 failures

Python:
  Total Test Cases: 250
  ✅ Passed: 250
  ❌ Failed: 0
  Pass Rate: 100.0%

================================================================================
Overall: 745 passed, 5 failed
```

## Running Subset Tests

### Test Only Python (Legacy Script)

```bash
python3 test_solutions.py
```

### Test Only AGR-006

```bash
python3 test_quick.py
```

### Test Specific Problem Range

Edit `test_all_languages.py` and change line:

```python
for i in range(1, 17):  # Change to range(6, 7) for just AGR-006
```

## Troubleshooting

### If Compilation Fails

- **C++:** Ensure `g++` is installed and supports C++17
- **Java:** Ensure `javac` and `java` are in PATH

### If Tests Hang

- Default timeout is 5 seconds per test case
- Some complex problems may need more time
- Adjust timeout in the `run_test_case` method

### If Output Doesn't Match

- Check for trailing whitespace issues
- Verify sorting order (some problems require sorted output)
- Check empty line handling

## Test Execution Time

- **Per Problem:** ~30-60 seconds (all 3 languages)
- **All 16 Problems:** ~10-15 minutes
- Factors: compilation time, test case count, problem complexity

## Files Reference

```
AdvancedGraphs/
├── test_all_languages.py      # Main comprehensive test script
├── test_solutions.py           # Legacy Python-only test script
├── test_quick.py               # Quick test for AGR-006
├── test_simple.py              # Basic functionality test
├── run_tests.sh                # Shell wrapper script
├── TEST_EXECUTION_REPORT.md    # Detailed documentation
├── THIS_FILE.md                # Quick reference (this file)
├── editorials/                 # 16 editorial files with solutions
│   ├── AGR-001-*.md
│   ├── AGR-002-*.md
│   └── ...
└── testcases/                  # 16 test case YAML files
    ├── AGR-001-*.yaml
    ├── AGR-002-*.yaml
    └── ...
```

## Next Steps

1. **Run the tests:**

   ```bash
   cd /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs
   python3 test_all_languages.py | tee full_test_results.txt
   ```

2. **Review results:**

   ```bash
   # View all output
   cat full_test_results.txt

   # View only summary
   tail -80 full_test_results.txt

   # Count passes/failures
   grep -c "✅ Passed" full_test_results.txt
   grep -c "❌" full_test_results.txt
   ```

3. **Fix any failures:**
   - Identify which problem/language failed
   - Review the error message
   - Update the solution in the editorial
   - Rerun tests

## Status: ✅ Ready to Execute

All infrastructure is in place. Simply run the command above to test all solutions!
