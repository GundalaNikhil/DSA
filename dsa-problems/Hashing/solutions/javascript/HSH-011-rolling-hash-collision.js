const readline = require("readline");

class Solution {
  findCollision(B, M, L) {
    const seen = new Map();
    const MOD = BigInt(M);
    const BASE = BigInt(B);
    
    const computeHash = (s) => {
      let h = 0n;
      for (let i = 0; i < s.length; i++) {
        const code = BigInt(s.charCodeAt(i));
        h = (h * BASE + code) % MOD;
      }
      return h;
    };
    
    // Using iterative DFS (stack) to avoid recursion limits if needed
    // But L <= 8 is small enough for recursion.
    
    const dfs = (current) => {
      if (current.length === L) {
        const h = computeHash(current);
        if (seen.has(h)) {
          return [seen.get(h), current];
        }
        seen.set(h, current);
        return null;
      }
      
      for (let i = 97; i <= 122; i++) {
        const char = String.fromCharCode(i);
        const res = dfs(current + char);
        if (res) return res;
      }
      return null;
    };
    
    return dfs("") || ["", ""];
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
  const [B, M, L] = data[0].split(" ").map(Number);

  const solution = new Solution();
  const [s1, s2] = solution.findCollision(B, M, L);

  console.log(s1);
  console.log(s2);
});
