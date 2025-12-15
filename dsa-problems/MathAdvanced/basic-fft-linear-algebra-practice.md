# Original FFT & Linear Algebra Practice Set (14 Questions)

## 1) Polynomial Multiplication via FFT
- Slug: polynomial-multiplication-fft
- Difficulty: Medium
- Problem: Multiply two polynomials with integer coefficients using FFT; return coefficients modulo 1e9+7.
- Constraints: degrees up to 1e5.
- Example:
  - Input: A=[1,2], B=[3,4]
  - Output: [3,10,8]

## 2) Convolution Mod Prime Using NTT
- Slug: convolution-ntt
- Difficulty: Medium
- Problem: Perform convolution under a suitable NTT prime (e.g., 998244353). Handle padding to power of two.
- Constraints: length up to 1e5.
- Example:
  - Input: A=[1,1,1], B=[1,2]
  - Output: [1,3,3,2]

## 3) Inverse Polynomial Mod x^n
- Slug: inverse-polynomial
- Difficulty: Hard
- Problem: Given polynomial P(x) with P[0]!=0 modulo prime, compute Q(x) such that P*Q ≡ 1 mod x^n.
- Constraints: n up to 1e5.
- Hint: Newton iteration with NTT.
- Example:
  - Input: P=[1,1] (1+x), n=3
  - Output: Q=[1,-1,1] (mod prime)

## 4) Multipoint Evaluation
- Slug: multipoint-evaluation
- Difficulty: Hard
- Problem: Given polynomial P and points x_i, compute P(x_i) for all using divide-and-conquer with product tree and remainder tree.
- Constraints: deg P, number of points <= 1e5.
- Example:
  - Input: P=[1,0,1] (x^2+1), points [0,1,2]
  - Output: [1,2,5]

## 5) Lagrange Interpolation Mod Prime
- Slug: lagrange-interpolation-mod
- Difficulty: Medium
- Problem: Given points (x_i,y_i) with distinct x_i, find value of interpolating polynomial at X modulo prime.
- Constraints: k <= 2 * 10^5.
- Example:
  - Input: points (0,1),(1,3), X=2, mod=1e9+7
  - Output: 5

## 6) Determinant via Gaussian Elimination
- Slug: determinant-gaussian
- Difficulty: Medium
- Problem: Compute determinant of an n x n matrix modulo prime using Gaussian elimination with row swaps.
- Constraints: n <= 1000.
- Example:
  - Input: [[1,2],[3,4]] mod 1e9+7
  - Output: -2 mod => 1000000005

## 7) Matrix Exponentiation for Linear Recurrence
- Slug: matrix-exp-linear-recurrence
- Difficulty: Medium
- Problem: Given linear recurrence of order k with coefficients c and initial terms, compute nth term modulo mod via matrix exponentiation.
- Constraints: k <= 50, n <= 10^18.
- Example:
  - Input: Fibonacci c=[1,1], n=5
  - Output: 5

## 8) Fast Walsh-Hadamard Transform (XOR Convolution)
- Slug: fwht-xor-convolution
- Difficulty: Medium
- Problem: Given arrays A,B length power of two, compute XOR convolution using FWHT.
- Constraints: length <= 1<<17.
- Example:
  - Input: A=[1,2], B=[3,4]
  - Output: [1*3+2*4, 1*4+2*3] => [11,10]

## 9) Subset Convolution (AND/OR)
- Slug: subset-convolution-and-or
- Difficulty: Hard
- Problem: Perform subset convolution under bitwise AND or OR using zeta/Möbius transforms.
- Constraints: n<=20 (size 2^n).
- Example:
  - Input: A=[1,1,0,0], B=[0,1,1,0] for OR
  - Output: convolution array of size 4 (provide actual values)

## 10) Berlekamp-Massey Sequence Reconstruction
- Slug: berlekamp-massey
- Difficulty: Hard
- Problem: Given first 2k terms of a linear recurrence, reconstruct minimal recurrence and generate nth term modulo mod.
- Constraints: length <= 4000.
- Example:
  - Input: seq [1,1,2,3,5,8], n=10
  - Output: term 89

## 11) Minimal Polynomial of Matrix (Krylov)
- Slug: minimal-polynomial-matrix
- Difficulty: Hard
- Problem: Compute minimal polynomial of an n x n matrix using Krylov sequence and Berlekamp-Massey on vector sequence.
- Constraints: n<=200.
- Example:
  - Input: 2x2 matrix [[1,1],[0,1]]
  - Output: minimal polynomial (x-1)^2

## 12) Convolution Under Multiple Mods with CRT
- Slug: convolution-multi-mod-crt
- Difficulty: Medium
- Problem: Perform convolution when modulus is not NTT-friendly by combining results from two or three NTT primes via CRT.
- Constraints: length up to 1e5.
- Example:
  - Input: A=[1,2], B=[3,4], mod=1e9+7
  - Output: [3,10,8]

## 13) Fast Inversion of Vandermonde Matrix
- Slug: invert-vandermonde
- Difficulty: Hard
- Problem: Given distinct x_i, invert Vandermonde matrix to solve for coefficients quickly.
- Constraints: n<=2000.
- Example:
  - Input: x=[1,2], y for solving simple system; show inverse [[2,-1],[-1,1]]

## 14) Largest Eigenvalue Power Method
- Slug: largest-eigenvalue-power
- Difficulty: Medium
- Problem: Approximate largest eigenvalue of a real matrix using the power method; discuss convergence.
- Constraints: n<=500.
- Example:
  - Input: matrix [[2,0],[0,1]]
  - Output: approx eigenvalue 2
