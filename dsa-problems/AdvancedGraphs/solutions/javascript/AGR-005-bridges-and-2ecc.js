const readline = require("readline");

class Solution {
  bridgesAndComponents(n, edges) {
    const m = edges.length;
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < m; i++) {
      const [u, v] = edges[i];
      adj[u].push({ to: v, idx: i });
      adj[v].push({ to: u, idx: i });
    }

    const tin = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    const bridgeFlags = new Int8Array(m).fill(0);
    let timer = 0;

    // Use iterative DFS to avoid stack overflow
    const parentEdge = new Int32Array(n).fill(-1);
    const stack = [];
    
    // Recursive is cleaner for logic, but JS stack is small.
    // N=200,000 requires iterative.
    
    // Iterative DFS for Bridges
    // We need to process node in post-order to update low-link.
    // Stack stores {u, iter_index}
    
    const visited = new Int8Array(n).fill(0);
    
    const runDFS = (startNode) => {
        const stack = [startNode];
        const iterIndex = new Int32Array(n).fill(0);
        visited[startNode] = 1;
        tin[startNode] = low[startNode] = timer++;
        
        while (stack.length > 0) {
            const u = stack[stack.length - 1];
            const children = adj[u];
            
            if (iterIndex[u] < children.length) {
                const { to: v, idx } = children[iterIndex[u]];
                iterIndex[u]++;
                
                if (idx === parentEdge[u]) continue;
                
                if (visited[v]) {
                    low[u] = Math.min(low[u], tin[v]);
                } else {
                    visited[v] = 1;
                    tin[v] = low[v] = timer++;
                    parentEdge[v] = idx;
                    stack.push(v);
                }
            } else {
                // Post-order processing
                stack.pop();
                if (parentEdge[u] !== -1) {
                    // We came from some parent via parentEdge[u]
                    // We need to find who is the parent node.
                    // But simpler: we need to update parent's low.
                    // In iterative DFS, parent is now at top of stack (if stack not empty)
                    if (stack.length > 0) {
                        const p = stack[stack.length - 1];
                        low[p] = Math.min(low[p], low[u]);
                        if (low[u] > tin[p]) {
                            bridgeFlags[parentEdge[u]] = 1;
                        }
                    }
                }
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (!visited[i]) runDFS(i);
    }

    // Components
    const comp = new Int32Array(n).fill(0);
    let compCount = 0;
    
    const runCompDFS = (startNode, c) => {
        const stack = [startNode];
        comp[startNode] = c;
        while(stack.length > 0) {
            const u = stack.pop();
            for(const {to: v, idx} of adj[u]) {
                if(bridgeFlags[idx]) continue;
                if(comp[v] === 0) {
                    comp[v] = c;
                    stack.push(v);
                }
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (comp[i] === 0) {
            compCount++;
            runCompDFS(i, compCount);
        }
    }

    return [bridgeFlags, comp];
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
  const m = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const [bridgeFlags, comp] = solution.bridgesAndComponents(n, edges);
  
  let bridgeCount = 0;
  for (let i = 0; i < m; i++) bridgeCount += bridgeFlags[i];
  
  const out = [bridgeCount.toString()];
  for (let i = 0; i < m; i++) {
    if (bridgeFlags[i]) out.push(``edges[i][0]`{edges[i][1]}`);
  }
  out.push(comp.join(" "));
  console.log(out.join("\n"));
});
