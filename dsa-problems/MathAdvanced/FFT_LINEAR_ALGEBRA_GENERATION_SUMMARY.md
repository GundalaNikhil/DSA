# FFT & Linear Algebra Problems Generation Summary

## Overview

Successfully generated **14 problem files** for the MathAdvanced topic covering FFT (Fast Fourier Transform) and Linear Algebra algorithms.

## Problems Created

### 1. MTH-001: Polynomial Multiplication via FFT

- **Difficulty**: Medium (55)
- **Topics**: FFT, Polynomial Multiplication
- **Description**: Multiply two polynomials using FFT algorithm
- **Key Concepts**: FFT, O((n+m)log(n+m)) complexity

### 2. MTH-002: Convolution Mod Prime Using NTT

- **Difficulty**: Medium (58)
- **Topics**: NTT, Convolution
- **Description**: Compute convolution using Number Theoretic Transform
- **Key Concepts**: NTT, Prime 998244353, Modular arithmetic

### 3. MTH-003: Inverse Polynomial Mod x^n

- **Difficulty**: Hard (72)
- **Topics**: Polynomial Inverse, Newton Iteration
- **Description**: Find inverse polynomial using Newton iteration
- **Key Concepts**: Newton method, Modular inverse, NTT

### 4. MTH-004: Multipoint Evaluation

- **Difficulty**: Hard (75)
- **Topics**: Polynomial Evaluation, Divide and Conquer
- **Description**: Evaluate polynomial at multiple points efficiently
- **Key Concepts**: Product tree, Remainder tree, O(n log² n)

### 5. MTH-005: Lagrange Interpolation Mod Prime

- **Difficulty**: Medium (60)
- **Topics**: Interpolation, Polynomial
- **Description**: Find interpolating polynomial value at query point
- **Key Concepts**: Lagrange formula, Modular arithmetic

### 6. MTH-006: Determinant via Gaussian Elimination

- **Difficulty**: Medium (55)
- **Topics**: Linear Algebra, Determinant
- **Description**: Compute matrix determinant using Gaussian elimination
- **Key Concepts**: Row reduction, Partial pivoting, O(n³)

### 7. MTH-007: Matrix Exponentiation for Linear Recurrence

- **Difficulty**: Medium (58)
- **Topics**: Matrix Exponentiation, Recurrence
- **Description**: Solve linear recurrence using fast matrix power
- **Key Concepts**: Fibonacci-like sequences, O(k³ log n)

### 8. MTH-008: Fast Walsh-Hadamard Transform (XOR Convolution)

- **Difficulty**: Medium (62)
- **Topics**: FWHT, XOR Convolution
- **Description**: Compute XOR convolution using FWHT
- **Key Concepts**: Walsh-Hadamard transform, XOR operation

### 9. MTH-009: Subset Convolution (AND/OR)

- **Difficulty**: Hard (78)
- **Topics**: Subset Convolution, Transforms
- **Description**: Perform subset convolution with AND/OR operations
- **Key Concepts**: Zeta transform, Möbius transform, O(2^n × n²)

### 10. MTH-010: Berlekamp-Massey Sequence Reconstruction

- **Difficulty**: Hard (80)
- **Topics**: Linear Recurrence, Algorithm
- **Description**: Reconstruct minimal recurrence from sequence
- **Key Concepts**: Berlekamp-Massey algorithm, Cryptography

### 11. MTH-011: Minimal Polynomial of Matrix (Krylov)

- **Difficulty**: Hard (82)
- **Topics**: Matrix Theory, Krylov Sequence
- **Description**: Find minimal polynomial using Krylov method
- **Key Concepts**: Krylov sequence, Berlekamp-Massey, Matrix theory

### 12. MTH-012: Convolution Under Multiple Mods with CRT

- **Difficulty**: Medium (65)
- **Topics**: CRT, Multi-modular Arithmetic
- **Description**: Compute convolution for non-NTT-friendly modulus
- **Key Concepts**: Chinese Remainder Theorem, Multiple primes

### 13. MTH-013: Fast Inversion of Vandermonde Matrix

- **Difficulty**: Hard (76)
- **Topics**: Vandermonde Matrix, Matrix Inversion
- **Description**: Efficiently invert Vandermonde matrix
- **Key Concepts**: Lagrange basis, O(n²) with FFT

### 14. MTH-014: Largest Eigenvalue Power Method

- **Difficulty**: Medium (58)
- **Topics**: Eigenvalues, Iterative Methods
- **Description**: Approximate largest eigenvalue using power iteration
- **Key Concepts**: Power method, Convergence, Iterative algorithm

## Difficulty Distribution

- **Medium**: 8 problems (55-65 difficulty)
- **Hard**: 6 problems (72-82 difficulty)

## Topics Covered

### FFT & Polynomial Algorithms

- Fast Fourier Transform (FFT)
- Number Theoretic Transform (NTT)
- Polynomial multiplication
- Polynomial inverse
- Multipoint evaluation
- Lagrange interpolation

### Transform Algorithms

- Fast Walsh-Hadamard Transform (FWHT)
- Zeta Transform
- Möbius Transform
- XOR/AND/OR convolutions

### Linear Algebra

- Matrix operations
- Determinant computation
- Matrix exponentiation
- Eigenvalue approximation
- Vandermonde matrices
- Krylov sequences

### Advanced Techniques

- Newton iteration
- Berlekamp-Massey algorithm
- Chinese Remainder Theorem
- Divide and conquer
- Power method

## File Structure

All files follow the Universal DSA Generation Prompt structure:

```
MathAdvanced/
├── problems/
│   ├── MTH-001-polynomial-multiplication-fft.md
│   ├── MTH-002-convolution-ntt.md
│   ├── MTH-003-inverse-polynomial.md
│   ├── MTH-004-multipoint-evaluation.md
│   ├── MTH-005-lagrange-interpolation-mod.md
│   ├── MTH-006-determinant-gaussian.md
│   ├── MTH-007-matrix-exp-linear-recurrence.md
│   ├── MTH-008-fwht-xor-convolution.md
│   ├── MTH-009-subset-convolution-and-or.md
│   ├── MTH-010-berlekamp-massey.md
│   ├── MTH-011-minimal-polynomial-matrix.md
│   ├── MTH-012-convolution-multi-mod-crt.md
│   ├── MTH-013-invert-vandermonde.md
│   └── MTH-014-largest-eigenvalue-power.md
```

## Features Included

✅ **Frontmatter**: Complete metadata with problem_id, difficulty, topics, tags
✅ **Problem Statement**: Clear description with constraints
✅ **Input/Output Format**: Detailed specifications
✅ **Example**: Concrete example with explanation
✅ **Notes**: Implementation tips and complexity analysis
✅ **Solution Templates**: All 4 languages (Java, Python, C++, JavaScript)
✅ **Image References**: Placeholders for visualizations
✅ **Related Topics**: Cross-references

## Next Steps

To complete the problem set, you need to create:

1. **Editorial Files** (14 files)

   - Location: `MathAdvanced/editorials/MTH-XXX-[slug].md`
   - Content: 500-750 lines with detailed explanations

2. **Test Cases** (14 files)

   - Location: `MathAdvanced/testcases/MTH-XXX-[slug].yaml`
   - Content: samples (2), public (3), hidden (35+)

3. **Quiz Files** (14 files)

   - Location: `MathAdvanced/quizzes/MTH-XXX-[slug].yaml`
   - Content: PRQ (5-7) and EDQ (6-8) questions

4. **Image READMEs** (14 files, optional)
   - Location: `MathAdvanced/images/MTH-XXX/README.md`
   - Content: Image generation prompts

## Quality Checklist

### Problem Files ✅

- [x] All 14 problems created
- [x] Frontmatter has 12 required fields
- [x] time_limit: 2000 and memory_limit: 256 included
- [x] Single example per problem
- [x] All 4 language templates included
- [x] Clear constraints and notes
- [x] Image references included
- [x] 150-250 lines per file

### Consistency ✅

- [x] Display IDs: MTH-001 through MTH-014
- [x] Problem IDs follow format: MTH\_[DESCRIPTION]\_\_[4_DIGITS]
- [x] Slugs are kebab-case
- [x] All files follow Universal DSA Generation Prompt

## Commands Used

```bash
# Generated problems 004-014 using Python script
cd /Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced
python3 generate_fft_problems.py

# Manually created problems 001-003
# MTH-001: Polynomial Multiplication via FFT
# MTH-002: Convolution Mod Prime Using NTT
# MTH-003: Inverse Polynomial Mod x^n
```

## Summary

Successfully created **14 comprehensive problem files** for FFT & Linear Algebra topics in the MathAdvanced category. All problems follow the Universal DSA Generation Prompt structure with complete metadata, examples, constraints, and solution templates in 4 programming languages.

---

**Status**: ✅ Problem Files Complete (14/14)
**Next**: Create Editorial, Test Cases, and Quiz files
**Date**: December 20, 2025
