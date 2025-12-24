# BITWISE DSA Problems - Test Case Generation Project

## 📋 Overview

This directory contains comprehensive test case generation for all **16 BITWISE DSA problems**. The project follows the **Universal Test Case Generation Prompt** to ensure high-quality, verified test cases across all problems.

## 📁 Files in This Directory

### Documentation (READ THESE FIRST)
1. **BITWISE_GENERATION_COMPLETION_REPORT.md** - Complete status and what was done
2. **BITWISE_TEST_CASE_GENERATION_SUMMARY.md** - Detailed analysis of each problem
3. **BITWISE_README.md** - This file

### Tools & Scripts
1. **generate_bitwise_all_correct.py** - Main test case generator with reference solutions
2. **test_language.py** - Test runner framework (in parent directory)
3. **test_python.sh** - Python test runner (in parent directory)
4. **test_cpp.sh** - C++ test runner (in parent directory)
5. **test_java.sh** - Java test runner (in parent directory)
6. **test_javascript.sh** - JavaScript test runner (in parent directory)

### Generated Test Cases
```
dsa-problems/Bitwise/testcases/
├── BIT-001-odd-after-bit-salt.yaml ✅ (100% pass)
├── BIT-002-two-unique-with-triples-mask.yaml ⚠️ (needs constraint validation)
├── BIT-003-bitwise-and-skip-multiples.yaml ✅ (100% pass)
├── BIT-004-pairwise-xor-band-index-parity.yaml ⏳ (needs work)
├── BIT-005-max-subarray-xor-with-start.yaml ⏳ (needs work)
├── BIT-006-minimal-bits-flip-range.yaml ✅ (100% pass)
├── BIT-007-count-set-bits-indexed-xor.yaml 🔄 (regenerated)
├── BIT-008-maximize-or-k-picks.yaml 🔄 (regenerated)
├── BIT-009-smallest-absent-xor.yaml ⏳ (needs work)
├── BIT-010-subset-and-equals-x.yaml ⏳ (needs work)
├── BIT-011-toggle-ranges-min-flips.yaml 🔄 (regenerated)
├── BIT-012-distinct-subarray-xors.yaml 🔄 (regenerated)
├── BIT-013-minimize-max-pair-xor.yaml ⏳ (needs work)
├── BIT-014-bitwise-palindromes-balanced-ones.yaml ⏳ (needs editorial fix)
├── BIT-015-swap-adjacent-2bit-blocks.yaml 🔄 (regenerated)
└── BIT-016-max-or-subarray-leq-k.yaml 🔄 (regenerated)
```

### Modified Editorial Files
```
dsa-problems/Bitwise/editorials/
└── BIT-002-two-unique-with-triples-mask.md (✅ FIXED)
    - Python: Added split_bit validation
    - Java: Added split_bit validation
    - C++: Added split_bit validation
```

## 🎯 Status Summary

### ✅ COMPLETE (Ready for Use)
- **BIT-001**: Odd After Bit Salt - 32/32 passing
- **BIT-003**: Bitwise AND Skip Multiples - 41/41 passing
- **BIT-006**: Minimal Bits Flip Range - 33/33 passing

### 🔄 PARTIALLY COMPLETE (Regenerated Tests)
- **BIT-007, BIT-008, BIT-011, BIT-012, BIT-015, BIT-016** - Tests regenerated, need verification

### ⏳ PENDING (Need Editorial Fixes & New Test Cases)
- **BIT-002** - Editorial fixed, tests need constraint validation
- **BIT-004, BIT-005, BIT-009, BIT-010, BIT-013** - Complex algorithms, need reference implementations
- **BIT-014** - Editorial needs input parsing fix

## 🚀 How to Use

### Run Tests
```bash
# Test all BITWISE problems
./test_python.sh Bitwise

# Test specific problem
./test_python.sh Bitwise BIT-001

# Test multiple problems
./test_python.sh Bitwise BIT-001 BIT-003 BIT-006

# Test C++
./test_cpp.sh Bitwise BIT-001

# Test Java
./test_java.sh Bitwise BIT-001

# Test JavaScript
./test_javascript.sh Bitwise BIT-001
```

### Generate New Test Cases
```bash
python3 generate_bitwise_all_correct.py
```

This will regenerate YAML test files for the 10 problems with reference implementations.

## 📊 Current Metrics

| Metric | Value | Target |
|--------|-------|--------|
| Problems Complete | 3/16 | 16/16 |
| Passing Tests | 280/644 | 600+ |
| Pass Rate | 43.5% | 95%+ |
| Languages Tested | Python | All 4 |

## 🔧 What Needs To Be Done

### Priority 1: Editorial Fixes
- [ ] Fix BIT-014 input parsing
- [ ] Verify BIT-002 fix works correctly

### Priority 2: Generate Missing Test Cases
- [ ] BIT-004 (Trie-based Pairwise XOR)
- [ ] BIT-005 (Prefix XOR optimization)
- [ ] BIT-009 (Linear Basis construction)
- [ ] BIT-010 (Bitmask iteration)
- [ ] BIT-013 (Bitmask DP perfect matching)

### Priority 3: Validation & Verification
- [ ] Run full test suite (all 4 languages)
- [ ] Verify 95%+ pass rate
- [ ] Add negative test cases
- [ ] Add special constraint test cases

## 📖 Problem Guide

### Easy Problems (30-35 difficulty)
- **BIT-001**: XOR cancellation - COMPLETE ✅
- **BIT-015**: Bit block swapping - Regenerated 🔄

### Medium Problems (45-50 difficulty)
- **BIT-002**: Modulo 3 bit counting - Editorial FIXED ✅
- **BIT-003**: Range AND with skips - COMPLETE ✅
- **BIT-006**: Minimal bit flip range - COMPLETE ✅
- **BIT-007**: Indexed XOR bit counting - Regenerated 🔄
- **BIT-008**: Greedy OR maximization - Regenerated 🔄
- **BIT-011**: Toggle ranges min flips - Regenerated 🔄
- **BIT-016**: Max OR subarray ≤ K - Regenerated 🔄

### Hard Problems (52-62+ difficulty)
- **BIT-004**: Pairwise XOR with Trie - NEEDS WORK ⏳
- **BIT-005**: Max subarray XOR fixed start - NEEDS WORK ⏳
- **BIT-009**: Linear Basis smallest absent - NEEDS WORK ⏳
- **BIT-010**: Subset AND equals X - NEEDS WORK ⏳
- **BIT-012**: Distinct subarray XORs - Regenerated 🔄
- **BIT-013**: Minimize max pair XOR DP - NEEDS WORK ⏳
- **BIT-014**: Binary palindromes balanced - NEEDS WORK ⏳

## 🎓 Understanding the Test Structure

Each problem has 3 types of test cases in YAML format:

```yaml
problem_id: BIT_PROBLEM_ID__8401
samples:           # 2-3 illustrative examples
  - input: |-
      ...
    output: |-
      ...

public:           # 3-5 tests visible to users
  - input: |-
      ...
    output: |-
      ...

hidden:           # 20-30 comprehensive tests
  - input: |-
      ...
    output: |-
      ...
```

### YAML Formatting Rules
- Use `|-` for literal block scalars (preserves newlines)
- Each line of input/output is prefixed with 2 spaces
- No trailing newlines
- One line per number (space-separated in YAML)

## 💡 Tips for Contributors

### Before Adding Test Cases
1. Read the problem editorial completely
2. Understand all constraints and edge cases
3. Write and test reference solution
4. Generate test cases from reference solution
5. Verify output format matches specification

### When Debugging Failures
1. Check if solution compiles/runs
2. Verify YAML format is correct (use online YAML validator)
3. Test solution manually with same input
4. Compare expected vs actual output exactly
5. Check for trailing spaces/newlines

### YAML Literal Block Syntax
```yaml
# ✅ CORRECT
input: |-
  5
  1 2 3 4 5

# ❌ WRONG
input: |
  5
  1 2 3 4 5

# ❌ WRONG (escaped newlines)
input: "5\n1 2 3 4 5"
```

## 📞 Quick Reference

### Test Commands
```bash
# Test BIT-001 (should pass 100%)
./test_python.sh Bitwise BIT-001

# Test all 3 complete problems
./test_python.sh Bitwise BIT-001 BIT-003 BIT-006

# Test and show failures
./test_python.sh Bitwise 2>&1 | grep "❌"

# Test with timing
time ./test_python.sh Bitwise
```

### Generate Commands
```bash
# Regenerate all test cases
python3 generate_bitwise_all_correct.py

# Show first 20 lines of generated file
head -20 dsa-problems/Bitwise/testcases/BIT-001-odd-after-bit-salt.yaml
```

### Check Editorial
```bash
# View Python solution from editorial
grep -A 50 "### Python" dsa-problems/Bitwise/editorials/BIT-001-odd-after-bit-salt.md
```

## 📈 Progress Tracking

### Completed Work
- ✅ Analysis of all 16 problems
- ✅ Identified root causes
- ✅ Fixed BIT-002 editorial solutions (Python, Java, C++)
- ✅ Generated test cases for 10 problems
- ✅ Verified YAML syntax and formatting
- ✅ Tested 3 problems to 100% pass rate

### In Progress
- 🔄 Regenerated test cases for 6 problems
- 🔄 Waiting for remaining editorial fixes

### Not Started
- ⏳ Fix BIT-014 editorial
- ⏳ Generate test cases for BIT-004, 005, 009, 010, 013, 014
- ⏳ Add negative and special constraint test cases
- ⏳ Full multi-language test suite

## 🎉 Success Criteria

When complete, each problem should have:
- ✅ Correct editorial solution (all 4 languages)
- ✅ 25-30+ comprehensive test cases
- ✅ 95%+ pass rate on Python
- ✅ Consistent output format across all languages
- ✅ Well-documented edge cases

## 📝 Notes

- This project uses the **Universal Test Case Generation Prompt** as specification
- All test cases follow YAML format with proper literal block syntax
- Reference implementations are provided in `generate_bitwise_all_correct.py`
- Test framework is language-independent and supports C++, Java, Python, JavaScript

## 🔗 Related Documents

- See `BITWISE_GENERATION_COMPLETION_REPORT.md` for detailed status
- See `BITWISE_TEST_CASE_GENERATION_SUMMARY.md` for problem-by-problem analysis
- See individual editorial files in `dsa-problems/Bitwise/editorials/` for solutions

---

**Last Updated**: December 23, 2025
**Status**: In Progress - 3/16 problems complete
**Next Goal**: 16/16 problems at 95%+ pass rate
