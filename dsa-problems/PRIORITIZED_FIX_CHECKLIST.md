# PRIORITIZED FIX CHECKLIST

**Quick reference for fixing test cases in priority order**

---

## 🔴 IMMEDIATE ACTION REQUIRED (Do First)

### 1. Greedy - Complete Regeneration ⚡ MOST URGENT

**Issue**: Only 3-6 tests per file (need ~38)
**Files**: ALL 16 files (GRD-001 through GRD-016)
**Action**:

```bash
# Regenerate all Greedy test cases
python3 generate_testcases.py Greedy GRD-001 GRD-016
```

**Estimated Time**: 1 day

---

### 2. Heaps - Empty Files

**Issue**: 3 files have ZERO tests
**Files**:

- [ ] HEP-008-huffman-merge-limit.yaml
- [ ] HEP-009-dynamic-median-of-medians.yaml
- [ ] HEP-010-topk-products-index-gap.yaml
- [ ] HEP-002 (fix empty outputs)

**Action**:

```bash
# Generate missing test cases
python3 generate_testcases.py Heaps HEP-008 HEP-010
# Manually fix HEP-002 empty outputs
```

**Estimated Time**: 4 hours

---

### 3. Queues - Missing problem_id Field

**Issue**: ALL 16 files missing problem_id
**Files**: QUE-001 through QUE-016
**Action**:

```bash
# Create automation script
python3 add_problem_id_field.py Queues
```

**Script needed**: `add_problem_id_field.py` (create once, reuse)
**Estimated Time**: 2 hours (including script creation)

---

### 4. SegmentTree - Missing problem_id Field

**Issue**: ALL 16 files missing problem_id
**Files**: SEG-001 through SEG-016
**Action**:

```bash
python3 add_problem_id_field.py SegmentTree
```

**Estimated Time**: 30 minutes (reuse script from Queues)

---

### 5. ProbabilisticDS - Missing problem_id Field

**Issue**: ALL 16 files missing problem_id
**Files**: PDS-001 through PDS-016
**Action**:

```bash
python3 add_problem_id_field.py ProbabilisticDS
```

**Estimated Time**: 30 minutes (reuse script)

---

### 6. Graphs - Complete Regeneration

**Issue**: Missing `|-` syntax + ID mismatches + low test counts
**Files**: ALL 18 files (GRP-001 through GRP-018)
**Action**:

```bash
python3 generate_testcases.py Graphs GRP-001 GRP-018
```

**Estimated Time**: 1 day

---

### 7. GraphsBasics - Missing `|-` Syntax

**Issue**: ALL 12 files missing multiline syntax
**Files**: GRB-001 through GRB-012
**Action**:

```bash
# Option 1: Regenerate
python3 generate_testcases.py GraphsBasics GRB-001 GRB-012

# Option 2: Fix in place (if test content is good)
python3 add_multiline_syntax.py GraphsBasics
```

**Estimated Time**: 4-6 hours

---

## 🟡 HIGH PRIORITY (Do Next)

### 8. Concurrency - ID Mismatches + Low Test Counts

**Issue**: All 16 files have ID mismatches and only 3-4 tests each
**Files**: CON-001 through CON-016
**Action**:

```bash
# Regenerate to fix both issues
python3 generate_testcases.py Concurrency CON-001 CON-016
```

**Estimated Time**: 1 day

---

### 9. GameTheory - ID Mismatches

**Issue**: problem_id doesn't match filename
**Files**: GMT-001 through GMT-016 (16 files)
**Example**: File `GMT-001`, yaml has `GMT_PILE_SPLIT_CHOICE__1928`
**Action**:

```bash
python3 fix_problem_ids.py GameTheory
```

**Script needed**: `fix_problem_ids.py`
**Estimated Time**: 1 hour (including script)

---

### 10. Geometry - ID Mismatches

**Issue**: problem_id doesn't match filename
**Files**: GEO-001 through GEO-016 (16 files)
**Action**:

```bash
python3 fix_problem_ids.py Geometry
```

**Estimated Time**: 30 minutes (reuse script)

---

### 11. NumberTheory - ID Mismatches

**Issue**: problem_id doesn't match filename
**Files**: NUM-001 through NUM-016 (16 files)
**Action**:

```bash
python3 fix_problem_ids.py NumberTheory
```

**Estimated Time**: 30 minutes (reuse script)

---

### 12. TreesDP - ID Mismatches

**Issue**: problem_id doesn't match filename
**Files**: TDP-001 through TDP-016 (16 files)
**Action**:

```bash
python3 fix_problem_ids.py TreesDP
```

**Estimated Time**: 30 minutes (reuse script)

---

### 13. DP - Filename Format Issues

**Issue**: Cannot extract ID from filename
**Files**: DP-001 through DP-016 (16 files)
**Action**: Review filenames and problem structure
**Estimated Time**: 2-3 hours

---

### 14. Hashing - Single ID Mismatch

**Issue**: 1 file with ID mismatch
**Files**:

- [ ] HSH-001-polynomial-hash-prefixes.yaml
      **Action**: Manually fix or use script
      **Estimated Time**: 15 minutes

---

## ⚠️ MEDIUM PRIORITY (Fix When Available)

### 15. AdvancedGraphs - Specific File Issues

**Files**:

- [ ] AGR-001 (missing `|-`, ID mismatch)
- [ ] AGR-003 (empty output hidden[7])
- [ ] AGR-006 (empty output hidden[22])
- [ ] AGR-008 (missing `|-`, ID mismatch)
- [ ] AGR-002 through AGR-016 (ID mismatches only - 12 files)

**Action**: Fix empty outputs manually, use scripts for IDs
**Estimated Time**: 2-3 hours

---

### 16. Arrays - Empty Outputs

**Files**:

- [ ] ARR-004 (empty: hidden[14], [15], [27])
- [ ] ARR-005 (missing `|-`)
- [ ] ARR-007 (empty: hidden[0], [12])
- [ ] Others (ID mismatches only)

**Action**: Regenerate problem cases or fix manually
**Estimated Time**: 2 hours

---

### 17. Bitwise - Missing `|-` Syntax

**Files**:

- [ ] BIT-005
- [ ] BIT-008
- [ ] BIT-010
- [ ] BIT-016
- [ ] Others (ID mismatches only)

**Action**:

```bash
python3 add_multiline_syntax.py Bitwise --files BIT-005 BIT-008 BIT-010 BIT-016
```

**Estimated Time**: 1 hour

---

### 18. LinkedLists - Empty Outputs

**Files**:

- [ ] LNK-001
- [ ] LNK-002
- [ ] LNK-006
- [ ] LNK-007
- [ ] LNK-010
- [ ] Others (ID mismatches only)

**Action**: Regenerate or fix manually
**Estimated Time**: 2 hours

---

### 19. Strings - Various Issues

**Files**:

- [ ] STR-001 (empty outputs)
- [ ] STR-004 (format issues)
- [ ] STR-005 (empty outputs)
- [ ] STR-007 (empty outputs)
- [ ] Others (ID mismatches only)

**Action**: Regenerate or fix manually
**Estimated Time**: 2 hours

---

### 20. Tries - Empty Outputs

**Files**:

- [ ] TRY-003 (empty outputs)
- [ ] TRY-016 (empty outputs)
- [ ] Others (ID mismatches only)

**Action**: Regenerate or fix manually
**Estimated Time**: 1 hour

---

### 21. Stacks - Minor Issue

**Files**:

- [ ] STK-010 (empty outputs)
- [ ] All others perfect ✅

**Action**: Quick manual fix
**Estimated Time**: 30 minutes

---

## ✅ PERFECT (No Action Needed)

- **Recursion** (16 files) ✅
- **Sorting** (16 files) ✅
- **StringsClassic** (16 files) ✅
- **MathAdvanced** (14 files) ✅
- **Stacks** (15/16 files) ✅
- **Probabilistic** (16 files) ✅

---

## AUTOMATION SCRIPTS TO CREATE

### Priority Order:

1. **`add_problem_id_field.py`** ⚡ Most impactful
   - Add missing problem_id field
   - Use for: Queues, SegmentTree, ProbabilisticDS
2. **`fix_problem_ids.py`** ⚡ High impact

   - Fix ID mismatches between filename and yaml
   - Use for: GameTheory, Geometry, NumberTheory, TreesDP, Hashing, etc.

3. **`add_multiline_syntax.py`**

   - Convert output fields to `|-` syntax
   - Use for: GraphsBasics, Bitwise specific files

4. **`find_empty_outputs.py`**

   - Scan for empty output fields
   - Generate repair list

5. **`validate_test_counts.py`**
   - Check test counts across all topics
   - Flag files with <30 tests

---

## PROGRESS TRACKING

### Week 1: Critical Issues

- [ ] Greedy regenerated (16 files)
- [ ] Heaps empty files fixed (3 files)
- [ ] Queues problem_id added (16 files)
- [ ] SegmentTree problem_id added (16 files)
- [ ] ProbabilisticDS problem_id added (16 files)
- [ ] Graphs regenerated (18 files)
- [ ] GraphsBasics regenerated (12 files)

**Total**: 97 files fixed

---

### Week 2: High Priority

- [ ] Concurrency regenerated (16 files)
- [ ] GameTheory IDs fixed (16 files)
- [ ] Geometry IDs fixed (16 files)
- [ ] NumberTheory IDs fixed (16 files)
- [ ] TreesDP IDs fixed (16 files)
- [ ] DP reviewed and fixed (16 files)
- [ ] Hashing ID fixed (1 file)

**Total**: 97 files fixed

---

### Week 3: Medium Priority

- [ ] AdvancedGraphs fixes (16 files)
- [ ] Arrays fixes (16 files)
- [ ] Bitwise fixes (17 files)
- [ ] LinkedLists fixes (16 files)
- [ ] Strings fixes (16 files)
- [ ] Tries fixes (16 files)
- [ ] Stacks fix (1 file)

**Total**: 98 files fixed

---

## GRAND TOTAL

**Files needing fixes**: ~292 files
**Perfect files**: ~139 files
**Success rate after fixes**: 431/431 (100%)

---

## QUICK START COMMAND

To begin fixing immediately:

```bash
# 1. Start with Greedy (most critical)
python3 generate_testcases.py Greedy GRD-001 GRD-016

# 2. While that runs, create automation script
cat > add_problem_id_field.py << 'EOF'
#!/usr/bin/env python3
import os
import sys
import yaml

def add_problem_id(topic, file_id):
    # Extract ID from filename and add to yaml
    # Implementation here
    pass

if __name__ == "__main__":
    topic = sys.argv[1]
    # Run for all files in topic
EOF

# 3. Fix missing problem_id fields
python3 add_problem_id_field.py Queues
python3 add_problem_id_field.py SegmentTree
python3 add_problem_id_field.py ProbabilisticDS

# 4. Fix Heaps empty files
python3 generate_testcases.py Heaps HEP-008 HEP-010

# Continue with remaining priorities...
```

---

_Last Updated: After comprehensive audit_
_See COMPREHENSIVE_AUDIT_REPORT.md for detailed analysis_
