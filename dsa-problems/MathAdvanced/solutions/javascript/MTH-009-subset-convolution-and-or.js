const readline = require("readline");

class Solution {
  subset_convolution_and_or(n, op, A, B) {
    const MOD = 1000000007n;
    const size = 1 << n;
    
    const bigA = A.map(BigInt);
    const bigB = B.map(BigInt);

    function fzt_or(a, invert) {
      for (let i = 0; i < n; i++) {
        for (let mask = 0; mask < size; mask++) {
          if ((mask & (1 << i)) !== 0) {
            const u = a[mask];
            const v = a[mask ^ (1 << i)];
            if (!invert) {
              a[mask] = (u + v) % MOD;
            } else {
              a[mask] = (u - v + MOD) % MOD;
            }
          }
        }
      }
    }

    function fzt_and(a, invert) {
      for (let i = 0; i < n; i++) {
        for (let mask = 0; mask < size; mask++) {
          if ((mask & (1 << i)) === 0) {
            const u = a[mask];
            const v = a[mask ^ (1 << i)];
            if (!invert) {
              a[mask] = (u + v) % MOD;
            } else {
              a[mask] = (u - v + MOD) % MOD;
            }
          }
        }
      }
    }

    if (op === 1) {
      fzt_or(bigA, false);
      fzt_or(bigB, false);
    } else {
      fzt_and(bigA, false);
      fzt_and(bigB, false);
    }

    const bigC = new Array(size);
    for (let i = 0; i < size; i++) {
      bigC[i] = (bigA[i] * bigB[i]) % MOD;
    }

    if (op === 1) {
      fzt_or(bigC, true);
    } else {
      fzt_and(bigC, true);
    }

    return bigC.map(x => Number(x));
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
  const op = parseInt(data[ptr++]);
  const size = 1 << n;
  
  const A = [];
  for(let i=0; i<size; i++) A.push(parseInt(data[ptr++]));
  
  const B = [];
  for(let i=0; i<size; i++) B.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const result = solution.subset_convolution_and_or(n, op, A, B);
  console.log(result.join(" "));
});
