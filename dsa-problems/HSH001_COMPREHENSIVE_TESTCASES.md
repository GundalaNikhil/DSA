# HSH-001: Polynomial Hash of Prefixes - Comprehensive Test Cases

**Status:** ✅ **COMPLETE & VERIFIED**  
**Date:** December 24, 2025  
**Total Test Cases:** 35  
**Pass Rate:** 100%

---

## 📊 Test Case Distribution

Following the Universal Test Case Generation Framework **exactly**:

| Category    | Count  | Description                                    |
| ----------- | ------ | ---------------------------------------------- |
| **Samples** | 3      | Sample test cases from problem description     |
| **Public**  | 5      | Basic scenarios visible to users for debugging |
| **Hidden**  | 27     | Comprehensive coverage not visible to users    |
| **TOTAL**   | **35** | Target range: 30-40 ✅                         |

### Hidden Test Cases Breakdown

| Subcategory            | Count | Coverage                                             |
| ---------------------- | ----- | ---------------------------------------------------- |
| **Edge Cases**         | 5     | Min/max ASCII, all same, alternating, sequences      |
| **Boundary Cases**     | 5     | Min/max base (B), small/large M, collision potential |
| **Special Constraint** | 5     | Palindromes, patterns, prime lengths, power-of-2     |
| **Normal Cases**       | 8     | Real words, varied inputs, typical scenarios         |
| **Stress Cases**       | 4     | 300-1000 character strings, worst-case               |

---

## ✅ Sample Test Cases (3)

### Sample 1: Basic Example

```yaml
input: |-
  abc
  911382323 1000000007
output: |-
  97 404084813 983030434
```

**Coverage:** Standard example from editorial

### Sample 2: Single Character

```yaml
input: |-
  a
  31 1000000007
output: |-
  97
```

**Coverage:** Minimum length edge case

### Sample 3: Short Word

```yaml
input: |-
  test
  31 1000000007
output: |-
  116 3697 114722 3556498
```

**Coverage:** Typical short input

---

## 👁️ Public Test Cases (5)

### Public 1: Maximum ASCII Character

```yaml
input: |-
  z
  31 1000000007
output: |-
  122
```

### Public 2: Repeated Character

```yaml
input: |-
  aa
  31 1000000007
output: |-
  97 3104
```

### Public 3: Common Word

```yaml
input: |-
  hello
  911382323 1000000007
output: |-
  104 783761035 755042784 629378853 78982331
```

### Public 4: Palindrome

```yaml
input: |-
  aba
  31 1000000007
output: |-
  97 3105 96352
```

### Public 5: Sequential Characters

```yaml
input: |-
  abcde
  911382323 1000000007
output: |-
  97 404084813 983030434 247202404 631633300
```

---

## 🔒 Hidden Test Cases (27)

### Edge Cases (5)

1. **All minimum ASCII (10 chars):** `aaaaaaaaaa` with B=31
2. **All maximum ASCII (10 chars):** `zzzzzzzzzz` with B=31
3. **Alternating pattern:** `ababababab` with large B
4. **Sequential alphabet:** `abcdefghijklmnopqrst` with B=31
5. **Reverse sequence:** `zyxwvutsrq` with large B

### Boundary Cases (5)

1. **Minimum base:** `binary` with B=2
2. **Small base:** `decimal` with B=10
3. **Large base:** `large` with B=999999937 (close to M)
4. **Small modulus:** `collision` with M=1000003 (tests collision)
5. **Prime base:** `prime` with B=53

### Special Constraint Cases (5)

1. **Palindrome:** `racecar` with large B
2. **Repeated pattern:** `abcabcabcabc` with B=31
3. **Power of 2 length:** 16 'a's with large B
4. **Prime length:** `thequickbrown` (13 chars) with B=31
5. **Alternative modulus:** `hashing` with M=1000000009

### Normal Cases (8)

1. **algorithm** - Technical term
2. **function** - Programming term
3. **beautiful** - Mixed vowels/consonants
4. **programming** - Medium length
5. **football** - Double letters
6. **abcdefghij** - All unique
7. **banana** - Repeated substrings
8. **database** - Technical term

### Stress Cases (4)

1. **300 characters:** `abc` repeated 100 times
2. **500 characters:** `ab` repeated 250 times
3. **1000 characters:** `a` repeated 1000 times
4. **988 characters:** Alphabet repeated 38 times

---

## 🎯 Coverage Analysis

### ✅ What's Covered

- ✅ Minimum length (1 character)
- ✅ Maximum ASCII values ('z')
- ✅ Minimum ASCII values ('a')
- ✅ All same characters
- ✅ Alternating patterns
- ✅ Sequential patterns
- ✅ Palindromes
- ✅ Repeated patterns
- ✅ Minimum base (B=2)
- ✅ Maximum base (B=999999937)
- ✅ Small modulus (M=1000003)
- ✅ Alternative modulus (M=1000000009)
- ✅ Common bases (31, 53, 911382323)
- ✅ Power-of-2 lengths
- ✅ Prime lengths
- ✅ Stress tests up to 1000 characters
- ✅ Collision potential scenarios
- ✅ Real English words
- ✅ Technical terms

### ❌ Negative Test Cases

**Not applicable** for this problem - all valid strings produce valid hash outputs. No "impossible" or "no solution" scenarios exist.

---

## 🧪 Verification Results

```bash
./test_python.sh Hashing HSH-001
```

**Result:**

```
HSH-001: ✅ 35/35
Pass Rate: 100.0%
🎉 ALL 35 TESTS PASSED!
```

### Editorial Fix Applied

Fixed Python input reading in editorial:

```python
def main():
    lines = sys.stdin.read().strip().split('\n')
    s = lines[0]
    B, M = map(int, lines[1].split())
    result = compute_prefix_hashes(s, B, M)
    print(' '.join(map(str, result)))
```

---

## 📝 Format Compliance

All test cases follow **exact** YAML format from Universal Prompt:

```yaml
problem_id: HSH_POLYNOMIAL_HASH_PREFIXES__3824
samples:
  - input: |-
      line1
      line2
    output: |-
      result
```

✅ Uses `|-` for multi-line preservation  
✅ Proper indentation (2/4/6 spaces)  
✅ No trailing newlines  
✅ Valid YAML syntax

---

## 🚀 Production Ready

This test suite is **ready for deployment** with:

- ✅ 35 comprehensive test cases
- ✅ 100% pass rate across all categories
- ✅ Proper format and syntax
- ✅ Edge/boundary/stress coverage
- ✅ Real-world scenario testing
- ✅ Verified against editorial solution

---

## 📚 Next Steps

1. Test with other languages:

   ```bash
   ./test_cpp.sh Hashing HSH-001
   ./test_java.sh Hashing HSH-001
   ./test_javascript.sh Hashing HSH-001
   ```

2. Deploy to Judge0 platform

3. Replicate this approach for remaining 15 Hashing problems

---

**Generated:** December 24, 2025  
**Framework:** Universal Test Case Generation Prompt  
**Status:** ✅ **PRODUCTION READY**
