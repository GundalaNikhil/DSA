const readline = require("readline");

class Solution {
  blockingTokens(n, edges, u, v) {
    const adj = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of edges) {
      adj[a].push(b);
    }

    // memo[u][v]: 0=unknown, 1=losing, 2=winning
    const memo = Array.from({ length: n + 1 }, () => new Int8Array(n + 1));

    const canWin = (currU, currV) => {
      if (memo[currU][currV] !== 0) return memo[currU][currV] === 2;

      let canReachLosing = false;

      // Try moving u
      for (const nextU of adj[currU]) {
        if (nextU === currV) continue;
        if (!canWin(nextU, currV)) {
          canReachLosing = true;
          break;
        }
      }

      // Try moving v
      if (!canReachLosing) {
        for (const nextV of adj[currV]) {
          if (nextV === currU) continue;
          if (!canWin(currU, nextV)) {
            canReachLosing = true;
            break;
          }
        }
      }

      memo[currU][currV] = canReachLosing ? 2 : 1;
      return canReachLosing;
    };

    return canWin(u, v) ? "First" : "Second";
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
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  const m = parseInt(flatData[idx++]);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
      edges.push([parseInt(flatData[idx++]), parseInt(flatData[idx++])]);
  }
  const u = parseInt(flatData[idx++]);
  const v = parseInt(flatData[idx++]);

  const solution = new Solution();
  console.log(solution.blockingTokens(n, edges, u, v));
});
