const readline = require("readline");

class Solution {
  berlekamp_massey(m, n, MOD, S) {
    const P = BigInt(MOD);
    const N = BigInt(n);
    const Seq = S.map(BigInt);

    function power(base, exp) {
      let res = 1n;
      base %= P;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % P;
        base = (base * base) % P;
        exp /= 2n;
      }
      return res;
    }

    function modInverse(x) {
      return power(x, P - 2n);
    }

    let C = [1n];
    let B = [1n];
    let L = 0;
    let b = 1;
    let b_delta = 1n;

    for (let i = 0; i < m; i++) {
      let delta = Seq[i];
      for (let j = 1; j < C.length; j++) {
        delta = (delta + C[j] * Seq[i - j]) % P;
      }

      if (delta === 0n) {
        b++;
        continue;
      }

      const T = [...C];
      const factor = (delta * modInverse(b_delta)) % P;

      while (C.length < B.length + b) C.push(0n);
      for (let j = 0; j < B.length; j++) {
        const val = (B[j] * factor) % P;
        const idx = j + b;
        C[idx] = (C[idx] - val + P) % P;
      }

      if (2 * L <= i) {
        L = i + 1 - L;
        B = T;
        b_delta = delta;
        b = 1;
      } else {
        b++;
      }
    }

    const K = C.length - 1;
    if (K === 0) return 0;

    const Rec = [];
    for (let i = 0; i < K; i++) {
      Rec.push((P - C[i + 1]) % P);
    }

    if (N < BigInt(m)) return Number(Seq[Number(N)]);

    function combine(A, B_poly) {
      const prod = new Array(2 * K).fill(0n);
      for (let i = 0; i < A.length; i++) {
        for (let j = 0; j < B_poly.length; j++) {
          prod[i + j] = (prod[i + j] + A[i] * B_poly[j]) % P;
        }
      }

      for (let i = prod.length - 1; i >= K; i--) {
        const factor = prod[i];
        if (factor === 0n) continue;
        for (let j = 0; j < K; j++) {
          const target = i - 1 - j;
          prod[target] = (prod[target] + factor * Rec[j]) % P;
        }
      }
      return prod.slice(0, K);
    }

    let res = new Array(K).fill(0n);
    res[0] = 1n;

    let base = new Array(K).fill(0n);
    if (K > 1) base[1] = 1n;
    else base[0] = Rec[0];

    let exp = N;
    while (exp > 0n) {
      if (exp % 2n === 1n) res = combine(res, base);
      base = combine(base, base);
      exp /= 2n;
    }

    let ans = 0n;
    for (let i = 0; i < K; i++) {
      ans = (ans + res[i] * Seq[i]) % P;
    }

    return Number(ans);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let ptr = 0;
  
  const m = parseInt(data[ptr++]);
  const n = BigInt(data[ptr++]);
  
  const S = [];
  for(let i=0; i<m; i++) S.push(parseInt(data[ptr++]));
  
  const MOD = parseInt(data[ptr++]);
  
  const solution = new Solution();
  console.log(solution.berlekamp_massey(m, n, MOD, S));
});
