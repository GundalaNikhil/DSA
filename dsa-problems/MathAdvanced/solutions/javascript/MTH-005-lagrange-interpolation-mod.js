const readline = require("readline");

class Solution {
  lagrange_interpolation_mod(k, X, MOD, points) {
    const P = BigInt(MOD);
    const X_val = BigInt(X);
    
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

    function modInverse(n) {
      return power(n, P - 2n);
    }

    let ans = 0n;

    for (let i = 0; i < k; i++) {
      const xi = BigInt(points[i][0]);
      const yi = BigInt(points[i][1]);

      let num = 1n;
      let den = 1n;

      for (let j = 0; j < k; j++) {
        if (i === j) continue;
        const xj = BigInt(points[j][0]);

        num = (num * (X_val - xj + P)) % P;
        den = (den * (xi - xj + P)) % P;
      }

      let term = (yi * num) % P;
      term = (term * modInverse(den)) % P;
      ans = (ans + term) % P;
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
  
  const k = parseInt(data[ptr++]);
  const X = parseInt(data[ptr++]);
  const MOD = parseInt(data[ptr++]);
  
  const points = [];
  for(let i=0; i<k; i++) {
      points.push([parseInt(data[ptr++]), parseInt(data[ptr++])]);
  }
  
  const solution = new Solution();
  console.log(solution.lagrange_interpolation_mod(k, X, MOD, points));
});
