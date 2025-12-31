const readline = require("readline");

class Solution {
  processTemperatureQueries(temps, queries) {
    const n = temps.length;
    // Use BigInt for potentially large values
    const diff = new BigInt64Array(n + 1);
    const results = [];

    for (const q of queries) {
      if (q.type === "add") {
        const xVal = BigInt(q.x);
        diff[q.l] += xVal;
        if (q.r + 1 <= n) {
          diff[q.r + 1] -= xVal;
        }
      } else {
        // Compute prefix sum up to query time
        const P = new BigInt64Array(n + 1);
        let currentAdd = 0n;

        for (let i = 0; i < n; i++) {
          currentAdd += diff[i];
          const finalVal = BigInt(temps[i]) + currentAdd;
          P[i + 1] = P[i] + finalVal;
        }

        results.push(P[q.r + 1] - P[q.l]);
      }
    }

    return results;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const temps = [];
    for (let i = 0; i < n; i++) temps.push(Number(tokens[ptr++]));
    
    const q = Number(tokens[ptr++]);
    const queries = [];
    for (let i = 0; i < q; i++) {
      const type = tokens[ptr++];
      const l = Number(tokens[ptr++]);
      const r = Number(tokens[ptr++]);
      let x = 0;
      if (type === "add") {
        x = Number(tokens[ptr++]);
      }
      queries.push({ type, l, r, x });
    }
    
    const solution = new Solution();
    const result = solution.processTemperatureQueries(temps, queries);
    console.log(result.join("\n"));
});
