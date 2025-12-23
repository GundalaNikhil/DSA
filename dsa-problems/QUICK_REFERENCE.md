# Quick Reference - Universal DSA Framework

## 🎯 One-Page Cheat Sheet

### Test Individual Languages

```bash
# Test C++
./test_cpp.sh AdvancedGraphs AGR-001

# Test Java
./test_java.sh AdvancedGraphs AGR-002

# Test Python
./test_python.sh AdvancedGraphs AGR-006

# Test JavaScript
./test_javascript.sh AdvancedGraphs AGR-007
```

### Test All Problems in Topic

```bash
./test_cpp.sh AdvancedGraphs
./test_java.sh Arrays
./test_python.sh Graphs
./test_javascript.sh Trees
```

### Test Multiple Problems

```bash
./test_python.sh AdvancedGraphs AGR-001 AGR-002 AGR-006
```

---

## 📋 Test Case Generation

### Use This Prompt

**File:** `UNIVERSAL_TESTCASE_GENERATION_PROMPT.md`

**Steps:**

1. Read problem statement
2. Note constraints and edge cases
3. Provide problem details to AI with prompt
4. AI generates complete YAML test cases
5. Save to `testcases/PROB-ID-name.yaml`
6. Test with `./test_python.sh Topic PROB-ID`

### YAML Structure

```yaml
problem_id: TOPIC_PROBLEM__ID
samples:
  - input: |-
      [input]
    output: |-
      [output]
public:
  - input: |-
      [input]
    output: |-
      [output]
hidden:
  - input: |-
      [input]
    output: |-
      [output]
```

---

## 🔧 Common Commands

### Make Scripts Executable (First Time)

```bash
chmod +x test_*.sh
```

### Test After Fixing a Problem

```bash
# 1. Edit editorial
nano AdvancedGraphs/editorials/AGR-006-articulation-and-bcc.md

# 2. Test
./test_cpp.sh AdvancedGraphs AGR-006
./test_java.sh AdvancedGraphs AGR-006
./test_python.sh AdvancedGraphs AGR-006

# 3. Update problem template if main() changed
nano AdvancedGraphs/problems/AGR-006-articulation-and-bcc.md
```

### Check All Languages

```bash
./test_cpp.sh Topic PROB-ID && \
./test_java.sh Topic PROB-ID && \
./test_python.sh Topic PROB-ID && \
./test_javascript.sh Topic PROB-ID
```

---

## 📊 Reading Test Output

### Success

```
AGR-001: ✅ 31/31
```

### Failure with Details

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

### Summary

```
================================================================================
SUMMARY - PYTHON
================================================================================
Total Tests: 451
✅ Passed: 448
❌ Failed: 3
Pass Rate: 99.3%
```

---

## 🚨 Troubleshooting

### Test Script Not Found

```bash
ls test_*.sh
# If missing, you're in wrong directory
cd /path/to/dsa-problems
```

### Permission Denied

```bash
chmod +x test_*.sh
```

### g++ Not Found

```bash
# macOS
xcode-select --install

# Ubuntu
sudo apt-get install g++
```

### javac Not Found

```bash
# macOS
brew install openjdk

# Ubuntu
sudo apt-get install default-jdk
```

### node Not Found

```bash
# macOS
brew install node

# Ubuntu
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

---

## 🎓 Best Practices

### DO ✅

- Test one language at a time for faster debugging
- Fix editorial solutions first, then problem templates
- Verify output format exactly matches (no extra spaces/newlines)
- Test edge cases (empty, single element, maximum)
- Keep main() functions identical across editorial and template

### DON'T ❌

- Don't guess test case outputs - always run solution
- Don't skip testing after changes
- Don't leave languages unsynced (fix all or none)
- Don't deploy without 95%+ pass rate
- Don't ignore compilation errors

---

## 📁 File Locations

```
dsa-problems/
├── test_language.py              ← Core engine
├── test_*.sh                     ← Language-specific runners
├── UNIVERSAL_TESTCASE_GENERATION_PROMPT.md  ← TC generation
├── MULTI_LANGUAGE_TESTING_GUIDE.md          ← Testing guide
├── JUDGE0_MAIN_FUNCTION_SYNC_GUIDE.md       ← Sync guide
└── TopicName/
    ├── editorials/PROB-ID.md     ← Reference solutions
    ├── testcases/PROB-ID.yaml    ← Test cases
    ├── problems/PROB-ID.md       ← User templates
    └── quizzes/PROB-ID.md        ← MCQs
```

---

## 🔄 Workflow

### New Problem

1. Write editorial with all 4 language solutions
2. Generate test cases with universal prompt
3. Test: `./test_python.sh Topic PROB-ID`
4. Fix failures
5. Create problem template from editorial
6. Deploy

### Fix Bug

1. Identify: `./test_java.sh Topic PROB-ID`
2. Fix editorial solution
3. Test: `./test_java.sh Topic PROB-ID`
4. Sync problem template if needed
5. Deploy

### Add Test Cases

1. Edit `testcases/PROB-ID.yaml`
2. Add new test cases
3. Test: `./test_cpp.sh Topic PROB-ID`
4. Verify all pass
5. Commit

---

## 📞 Need Help?

- **Test Case Generation:** Read `UNIVERSAL_TESTCASE_GENERATION_PROMPT.md`
- **Testing Issues:** Read `MULTI_LANGUAGE_TESTING_GUIDE.md`
- **Template Sync:** Read `JUDGE0_MAIN_FUNCTION_SYNC_GUIDE.md`
- **Examples:** See `AdvancedGraphs/COMPREHENSIVE_TEST_RESULTS.md`
- **Bug Fixes:** See `AdvancedGraphs/BUG_FIX_REPORT.md`

---

## 🎯 Goals

- ✅ 95%+ pass rate across all languages
- ✅ All edge cases covered
- ✅ Consistent output format
- ✅ Fast test execution (<5min for full topic)
- ✅ Zero deployment bugs

---

**Save this file and reference it often!** 📌
