const readline = require("readline");

class Solution {
  eulerTrail(n, edges) {
    const m = edges.length;
    if (m === 0) return [0];

    const inDeg = new Int32Array(n).fill(0);
    const outDeg = new Int32Array(n).fill(0);
    const adj = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
      outDeg[u]++;
      inDeg[v]++;
      adj[u].push(v);
    }

    let startNode = -1;
    let endNode = -1;
    let diffCount = 0;

    for (let i = 0; i < n; i++) {
      if (outDeg[i] === inDeg[i] + 1) {
        if (startNode !== -1) return null;
        startNode = i;
        diffCount++;
      } else if (inDeg[i] === outDeg[i] + 1) {
        if (endNode !== -1) return null;
        endNode = i;
        diffCount++;
      } else if (inDeg[i] !== outDeg[i]) {
        return null;
      }
    }

    if (diffCount === 0) {
      for (let i = 0; i < n; i++) {
        if (outDeg[i] > 0) {
          startNode = i;
          break;
        }
      }
    } else if (diffCount !== 2) {
      return null;
    }

    if (startNode === -1) return null;

    const trail = [];
    // Iterative DFS to avoid stack overflow
    const stack = [startNode];
    
    // Hierholzer's iterative:
    // Maintain current path. If node has edges, push to stack and take edge.
    // If no edges, pop from stack and add to trail.
    
    // stack = [start]
    // while stack:
    //   u = stack[-1]
    //   if adj[u]:
    //     v = adj[u].pop()
    //     stack.push(v)
    //   else:
    //     trail.push(stack.pop())
    
    while (stack.length > 0) {
        const u = stack[stack.length - 1];
        if (adj[u].length > 0) {
            const v = adj[u].pop();
            stack.push(v);
        } else {
            trail.push(stack.pop());
        }
    }

    if (trail.length !== m + 1) return null;

    return trail.reverse();
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
  const trail = solution.eulerTrail(n, edges);
  if (trail === null) {
    console.log("NO");
  } else {
    console.log("YES");
    console.log(trail.join(" "));
  }
});
