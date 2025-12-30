const readline = require("readline");

class Solution {
  maxDiameterAfterRemoval(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u);
    }

    const height = new Int32Array(n);
    const diam = new Int32Array(n);
    const upHeight = new Int32Array(n);
    const upDiam = new Int32Array(n);
    let maxDiam = 0;

    const dfs1 = (u, p) => {
      let maxH1 = -1, maxH2 = -1;
      let maxD = 0;

      for (const v of adj[u]) {
        if (v === p) continue;
        dfs1(v, u);
        maxD = Math.max(maxD, diam[v]);
        if (height[v] > maxH1) {
          maxH2 = maxH1;
          maxH1 = height[v];
        } else if (height[v] > maxH2) {
          maxH2 = height[v];
        }
      }

      height[u] = 1 + maxH1;
      diam[u] = Math.max(maxD, (maxH1 + 1) + (maxH2 + 1));
    };

    const dfs2 = (u, p) => {
      if (p !== -1) {
        maxDiam = Math.max(maxDiam, Math.max(diam[u], upDiam[u]));
      }

      const lens = [];
      const diams = [];
      
      if (p !== -1) {
        lens.push(upHeight[u]);
        diams.push(upDiam[u]);
      } else {
        lens.push(-1);
        diams.push(0);
      }

      for (const v of adj[u]) {
        if (v !== p) {
          lens.push(height[v] + 1);
          diams.push(diam[v]);
        }
      }

      // Sort descending
      lens.sort((a, b) => b - a);
      diams.sort((a, b) => b - a);
      
      while (lens.length < 3) lens.push(-1);
      while (diams.length < 2) diams.push(0);

      for (const v of adj[u]) {
        if (v === p) continue;
        
        const vLen = height[v] + 1;
        const vDiam = diam[v];

        let bestLen = lens[0] === vLen ? lens[1] : lens[0];
        upHeight[v] = 1 + bestLen;

        let bestDiam = diams[0] === vDiam ? diams[1] : diams[0];
        
        let path = 0;
        if (lens[0] === vLen) {
            path = lens[1] + lens[2];
        } else if (lens[1] === vLen) {
            path = lens[0] + lens[2];
        } else {
            path = lens[0] + lens[1];
        }

        upDiam[v] = Math.max(bestDiam, path);
        dfs2(v, u);
      }
    };

    dfs1(0, -1);
    dfs2(0, -1);

    return maxDiam;
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
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.maxDiameterAfterRemoval(n, edges).toString());
});
