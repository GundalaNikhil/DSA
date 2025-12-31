const readline = require("readline");

class Solution {
  eulerTour(n, adj, root) {
    const tin = new Int32Array(n);
    const tout = new Int32Array(n);
    let timer = 0;

    // Iterative DFS to avoid stack overflow
    // We need to simulate the post-order processing to set tout
    const stack = [root];
    const parent = new Int32Array(n).fill(-1);
    
    // Iterative DFS to avoid stack overflow for large N
    
    const stackIter = [root];
    const parentMap = new Int32Array(n).fill(-1);
    const childIndex = new Int32Array(n).fill(0); // Index of next child to visit
    
    tin[root] = timer++;
    
    while (stackIter.length > 0) {
        const u = stackIter[stackIter.length - 1];
        const p = parentMap[u];
        const children = adj[u];
        
        let pushedChild = false;
        
        // Find next valid child
        while (childIndex[u] < children.length) {
            const v = children[childIndex[u]];
            childIndex[u]++;
            if (v !== p) {
                parentMap[v] = u;
                tin[v] = timer++;
                stackIter.push(v);
                pushedChild = true;
                break; // Process this child
            }
        }
        
        if (!pushedChild) {
            // All children done, post-order for u
            tout[u] = timer - 1;
            stackIter.pop();
        }
    }

    return [tin, tout];
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
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
    adj[v].push(u);
  }
  const root = parseInt(data[idx++], 10);

  const solution = new Solution();
  const res = solution.eulerTour(n, adj, root);
  console.log(res[0].join(" "));
  console.log(res[1].join(" "));
});
