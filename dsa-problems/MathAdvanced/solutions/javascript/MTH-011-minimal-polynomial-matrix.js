const readline = require("readline");

class Solution {
  minimal_polynomial_matrix(n, MOD, matrix) {
    const P = BigInt(MOD);
    const N = n;
    
    const mat = matrix.map(row => row.map(BigInt));

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

    function berlekampMassey(s) {
      let C = [1n];
      let B = [1n];
      let L = 0;
      let b = 1;
      let b_delta = 1n;

      for (let i = 0; i < s.length; i++) {
        let delta = s[i];
        for (let j = 1; j < C.length; j++) {
          delta = (delta + C[j] * s[i - j]) % P;
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
      return C;
    }

    // Random vectors u and v
    const u = new Array(N).fill(0n).map(() => BigInt(Math.floor(Math.random() * MOD)));
    const v = new Array(N).fill(0n).map(() => BigInt(Math.floor(Math.random() * MOD)));
    
    const seq = [];
    let currV = [...v];
    
    for(let k=0; k < 2*N + 2; k++) {
        let val = 0n;
        for(let i=0; i<N; i++) val = (val + u[i] * currV[i]) % P;
        seq.push(val);
        
        const nextV = new Array(N).fill(0n);
        for(let r=0; r<N; r++) {
            for(let c=0; c<N; c++) {
                nextV[r] = (nextV[r] + mat[r][c] * currV[c]) % P;
            }
        }
        currV = nextV;
    }
    
    const C = berlekampMassey(seq);
    const d = C.length - 1;
    const res = [];
    res.push(d);
    for(let i=d; i>=0; i--) res.push(Number(C[i]));
    
    return res;
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
  
  const n = parseInt(data[ptr++]);
  const MOD = parseInt(data[ptr++]);
  
  const matrix = [];
  for(let i=0; i<n; i++) {
      const row = [];
      for(let j=0; j<n; j++) row.push(parseInt(data[ptr++]));
      matrix.push(row);
  }
  
  const solution = new Solution();
  const result = solution.minimal_polynomial_matrix(n, MOD, matrix);
  
  console.log(result[0]);
  console.log(result.slice(1).join(" "));
});
