# COMPREHENSIVE DSA TEST CASES AUDIT REPORT

**Date**: Generated from complete audit  
**Scope**: All 27 DSA topics, 431 test files  
**Status**: ✅ All topics have testcases directories

---

## EXECUTIVE SUMMARY

### Overall Statistics

- ✅ **Topics with testcases**: 27/27 (100%)
- 📊 **Total test files**: 431
- ✅ **Perfect topics**: 4 (Recursion, Sorting, StringsClassic, MathAdvanced)
- ⚠️ **Topics needing fixes**: 23
- 🔴 **Critical issues**: 7 topics (need immediate regeneration)
- 🟡 **High priority issues**: 7 topics (need ID corrections)

---

## TOPICS OVERVIEW

### All Topics with Test Files (27 total)

| Topic           | Files | Status                                     |
| --------------- | ----- | ------------------------------------------ |
| AdvancedGraphs  | 16    | ⚠️ 4 critical issues                       |
| Arrays          | 16    | ⚠️ 3 critical issues                       |
| Bitwise         | 17    | ⚠️ 4 critical issues                       |
| Concurrency     | 16    | 🟡 16 ID mismatches                        |
| DP              | 16    | 🟡 16 filename issues                      |
| GameTheory      | 16    | 🟡 16 ID mismatches                        |
| Geometry        | 16    | 🟡 16 ID mismatches                        |
| Graphs          | 18    | 🔴 ALL 18 files critical                   |
| GraphsBasics    | 12    | 🔴 ALL 12 files critical                   |
| Greedy          | 16    | 🔴 ALL 16 files critical (low test counts) |
| Hashing         | 16    | 🟡 1 ID mismatch                           |
| Heaps           | 16    | 🔴 3 completely empty files                |
| LinkedLists     | 16    | ⚠️ 5 files with empty outputs              |
| MathAdvanced    | 14    | ✅ Perfect                                 |
| NumberTheory    | 16    | 🟡 16 ID mismatches                        |
| Probabilistic   | 16    | ✅ Good                                    |
| ProbabilisticDS | 16    | 🔴 ALL missing problem_id                  |
| Queues          | 16    | 🔴 ALL missing problem_id                  |
| Recursion       | 16    | ✅ Perfect                                 |
| SegmentTree     | 16    | 🔴 ALL missing problem_id                  |
| Sorting         | 16    | ✅ Perfect                                 |
| Stacks          | 16    | ✅ 1 minor issue only                      |
| Strings         | 16    | ⚠️ 4 files with issues                     |
| StringsClassic  | 16    | ✅ Perfect                                 |
| Trees           | 18    | 🟢 Generated, pending verification         |
| TreesDP         | 16    | 🟡 16 ID mismatches                        |
| Tries           | 16    | ⚠️ 2 files with empty outputs              |

---

## ISSUES BY SEVERITY

### 🔴 PRIORITY 1 - CRITICAL (Need Immediate Regeneration)

#### 1. **Greedy** (16 files) - MOST CRITICAL

**Issue**: Only 3-6 tests per problem (need ~38 each)

- GRD-001: 6 tests only
- GRD-002: 6 tests only
- GRD-003: 5 tests only
- GRD-004: 4 tests only
- GRD-005: 3 tests only
- GRD-006 through GRD-016: Similar low counts
- **ALL files also missing `|-` multiline syntax**

**Action Required**: Complete regeneration with proper test count

---

#### 2. **Heaps** (3 files completely empty)

**Issue**: Three files have NO test cases at all

- HEP-008-huffman-merge-limit.yaml: 0 tests
- HEP-009-dynamic-median-of-medians.yaml: 0 tests
- HEP-010-topk-products-index-gap.yaml: 0 tests
- Additional: HEP-002 has empty outputs in some tests

**Action Required**: Generate tests for empty files, fix HEP-002

---

#### 3. **ProbabilisticDS** (16 files)

**Issue**: ALL files missing `problem_id` field entirely

- Files: PDS-001 through PDS-016
- Tests exist (~38 each) but no problem_id field
- Format otherwise correct

**Action Required**: Add problem_id field to all files

---

#### 4. **Queues** (16 files)

**Issue**: ALL files missing `problem_id` field entirely

- Files: QUE-001 through QUE-016
- Tests exist (~38 each) but no problem_id field
- Format otherwise correct

**Action Required**: Add problem_id field to all files

---

#### 5. **SegmentTree** (16 files)

**Issue**: ALL files missing `problem_id` field entirely

- Files: SEG-001 through SEG-016
- Tests exist (~38 each) but no problem_id field
- Format otherwise correct

**Action Required**: Add problem_id field to all files

---

#### 6. **Graphs** (18 files)

**Issues**: Multiple critical problems

- ALL 18 files missing `|-` multiline syntax
- ALL have problem_id mismatches (e.g., file=GRP-001, yaml=GRP_CAMPUS_MAP_BFS)
- Some files have very low test counts:
  - GRP-004: only 9 tests
  - GRP-006: only 11 tests
  - GRP-009: only 10 tests

**Action Required**: Complete regeneration with proper format and IDs

---

#### 7. **GraphsBasics** (12 files)

**Issues**: Format problems across all files

- ALL 12 files missing `|-` multiline syntax
- Some have ID mismatches
- Test counts acceptable (10-15 each)

**Action Required**: Regenerate with proper multiline syntax

---

### 🟡 PRIORITY 2 - HIGH (Need ID/Format Corrections)

#### 1. **Concurrency** (16 files)

**Issues**:

- ALL 16 files have ID mismatches
- Low test counts (3-4 tests each vs expected 38)
- Examples:
  - CON-001: file=CON-001, yaml=CON_PARALLEL_MERGE_RACE\_\_4821
  - CON-002: file=CON-002, yaml=CON_PRODUCER_CONSUMER_OVERFLOW\_\_2847

**Action Required**: Fix IDs and increase test counts

---

#### 2. **DP** (16 files)

**Issue**: Cannot extract ID from filename format

- All 16 files have parsing issues
- Filenames don't follow expected pattern
- Test counts acceptable

**Action Required**: Review filename format and fix IDs

---

#### 3. **GameTheory** (16 files)

**Issue**: ID mismatches in all files

- All 16 files: file ID doesn't match yaml problem_id
- Example: GMT-001 → GMT_PILE_SPLIT_CHOICE\_\_1928
- Test counts good (27-45 tests each)

**Action Required**: Fix problem_id fields to match filenames

---

#### 4. **Geometry** (16 files)

**Issue**: ID mismatches in all files

- All 16 files: file ID doesn't match yaml problem_id
- Example: GEO-001 → GEO_ORIENTATION_TRIPLETS\_\_4821
- Test counts good (40-43 tests each)

**Action Required**: Fix problem_id fields to match filenames

---

#### 5. **NumberTheory** (16 files)

**Issue**: ID mismatches in all files

- All 16 files: file ID doesn't match yaml problem_id
- Example: NUM-001 → NUM_CLASSROOM_GCD_PREFIX_QUERIES\_\_4821
- Test counts acceptable (16-23 tests each)

**Action Required**: Fix problem_id fields to match filenames

---

#### 6. **TreesDP** (16 files)

**Issue**: ID mismatches in all files

- All 16 files: file ID doesn't match yaml problem_id
- Example: TDP-001 → TDP_LCA_BINARY_LIFTING\_\_7291
- Test counts acceptable (22-48 tests each)

**Action Required**: Fix problem_id fields to match filenames

---

#### 7. **Hashing** (1 file)

**Issue**: Single ID mismatch

- HSH-001: file=HSH-001, yaml=HSH_POLYNOMIAL_HASH_PREFIXES\_\_3824
- Test count good (35 tests)

**Action Required**: Fix problem_id field

---

### ⚠️ PRIORITY 3 - MEDIUM (Specific File Fixes)

#### 1. **AdvancedGraphs** (4 files need attention)

- AGR-001: Missing `|-` syntax, ID mismatch
- AGR-003: Empty output in hidden[7]
- AGR-006: Empty output in hidden[22]
- AGR-008: Missing `|-` syntax, ID mismatch
- Other 12 files: Only ID mismatches

---

#### 2. **Arrays** (3 files with empty outputs)

- ARR-004: Empty outputs in hidden[14], [15], [27]
- ARR-005: Missing `|-` syntax
- ARR-007: Empty outputs in hidden[0], [12]
- Other 13 files: Only ID mismatches

---

#### 3. **Bitwise** (4 files missing `|-` syntax)

- BIT-005, BIT-008, BIT-010, BIT-016: Missing `|-` syntax
- Other 13 files: Only ID mismatches

---

#### 4. **LinkedLists** (5 files with empty outputs)

- LNK-001, LNK-002, LNK-006, LNK-007, LNK-010: Various empty outputs
- Other 11 files: Only ID mismatches

---

#### 5. **Strings** (4 files with issues)

- STR-001, STR-004, STR-005, STR-007: Empty outputs or format issues
- Other 12 files: Only ID mismatches

---

#### 6. **Tries** (2 files with empty outputs)

- TRY-003, TRY-016: Empty outputs in some tests
- Other 14 files: Only ID mismatches

---

#### 7. **Stacks** (1 file)

- STK-010: Empty outputs (minor)
- Other 15 files: Perfect

---

## REGENERATION STRATEGY

### Phase 1: Critical Topics (Week 1)

**Order by impact and dependencies**

1. **Greedy** (highest priority - completely inadequate test counts)
   - Regenerate all 16 files with ~38 tests each
   - Add `|-` multiline syntax
2. **Heaps** (empty files)
   - Generate HEP-008, HEP-009, HEP-010
   - Fix HEP-002 empty outputs
3. **Queues, SegmentTree, ProbabilisticDS** (missing problem_id)

   - Batch fix: Add problem_id field to all files
   - Can use script to automate

4. **Graphs** (format + ID issues)

   - Regenerate all 18 files with proper format
   - Fix IDs and test counts

5. **GraphsBasics** (format issues)
   - Regenerate all 12 files with `|-` syntax

---

### Phase 2: High Priority Topics (Week 2)

**Fix ID mismatches and test counts**

1. **Concurrency** - Fix IDs + increase test counts
2. **DP** - Fix filename parsing issues
3. **GameTheory, Geometry, NumberTheory, TreesDP** - Batch fix IDs
4. **Hashing** - Single file fix

---

### Phase 3: Medium Priority Topics (Week 3)

**Targeted fixes for specific files**

1. **AdvancedGraphs** - Fix 4 critical files
2. **Arrays** - Fix 3 files with empty outputs
3. **Bitwise** - Add `|-` to 4 files
4. **LinkedLists** - Fix 5 files with empty outputs
5. **Strings** - Fix 4 files with issues
6. **Tries** - Fix 2 files with empty outputs
7. **Stacks** - Fix STK-010

---

## AUTOMATION OPPORTUNITIES

### Scripts to Create:

1. **`fix_problem_ids.py`**

   - Automatically fix ID mismatches
   - Extract ID from filename and update yaml
   - Use for: GameTheory, Geometry, NumberTheory, TreesDP, Hashing

2. **`add_problem_id_field.py`**

   - Add missing problem_id field based on filename
   - Use for: Queues, SegmentTree, ProbabilisticDS

3. **`add_multiline_syntax.py`**

   - Convert output fields to use `|-` syntax
   - Use for: Graphs, GraphsBasics, Greedy, specific files in other topics

4. **`validate_test_counts.py`**

   - Check all topics have ~38 tests per problem
   - Flag files with fewer than 30 tests

5. **`find_empty_outputs.py`**
   - Scan all yaml files for empty output fields
   - Generate report for manual fixing

---

## SUCCESS METRICS

### Current State:

- ✅ Perfect topics: 4 (Recursion, Sorting, StringsClassic, MathAdvanced)
- ⚠️ Need major work: 7 topics
- 🟡 Need ID fixes: 7 topics
- ⚠️ Need targeted fixes: 9 topics

### Target State (After All Fixes):

- ✅ Perfect topics: 27/27
- ✅ All files with problem_id matching filename
- ✅ All outputs using `|-` multiline syntax
- ✅ All topics with ~38 tests per problem
- ✅ Zero empty output fields
- ✅ 100% yaml parse success rate

---

## ESTIMATED EFFORT

### Time Estimates:

**Phase 1 (Critical)**: ~3-4 days

- Greedy regeneration: 1 day
- Heaps fixes: 0.5 day
- Add problem_id fields: 0.5 day (scripted)
- Graphs regeneration: 1 day
- GraphsBasics regeneration: 0.5 day

**Phase 2 (High Priority)**: ~2-3 days

- Concurrency: 1 day
- DP: 0.5 day
- Batch ID fixes: 1 day (mostly scripted)

**Phase 3 (Medium)**: ~2-3 days

- Targeted file fixes: 2-3 days (reviewing and fixing specific files)

**Total Estimated Time**: 7-10 days of focused work

---

## NEXT IMMEDIATE ACTIONS

### Top 3 Actions to Take Now:

1. **Generate Greedy test cases** (most critical)

   ```bash
   python3 generate_testcases.py Greedy GRD-001 GRD-016
   ```

2. **Create automation scripts**

   - Start with `add_problem_id_field.py` for Queues, SegmentTree, ProbabilisticDS
   - Then `fix_problem_ids.py` for ID mismatches

3. **Fix Heaps empty files**
   - Generate tests for HEP-008, HEP-009, HEP-010
   - Fix HEP-002 empty outputs

---

## CONCLUSION

The audit reveals that while **all 27 topics have testcases directories** (100% coverage), there are **systematic issues** that need addressing:

- **Format consistency**: Missing `|-` syntax in multiple topics
- **ID alignment**: Many topics have problem_id mismatches with filenames
- **Test coverage**: Greedy has critically low test counts
- **Completeness**: 3 files in Heaps are completely empty

The good news: Most issues are **automatable** through scripts, and the fixes can be batched by issue type rather than by topic.

**Recommended approach**: Start with Phase 1 critical topics, create automation scripts for repetitive fixes, then systematically work through the remaining issues.

---

_Generated by comprehensive audit script - See audit_testcases.py for details_
