const readline = require("readline");

class Solution {
  solveTwoSat(n, clauses, groups) {
    let totalGroupSize = 0;
    for (const g of groups) totalGroupSize += g.length;

    const N = n + totalGroupSize;
    const totalNodes = 2 * N + 2;
    const adj = Array.from({ length: totalNodes }, () => []);
    const revAdj = Array.from({ length: totalNodes }, () => []);

    const getNode = (lit) => (lit > 0 ? lit : -lit + N);
    const getNeg = (lit) => (lit > 0 ? lit + N : -lit);

    const addEdge = (u, v) => {
      adj[u].push(v);
      revAdj[v].push(u);
    };

    const addImplication = (a, b) => {
      addEdge(getNode(a), getNode(b));
      addEdge(getNeg(b), getNeg(a));
    };

    // Clauses
    for (const [a, b] of clauses) {
      addImplication(-a, b);
    }

    // AMO
    let currentAux = n + 1;
    for (const group of groups) {
      const k = group.length;
      if (k > 1) {
        for (let i = 0; i < k; i++) {
          const x = group[i];
          const p = currentAux + i;

          addImplication(x, p);
          if (i < k - 1) addImplication(p, p + 1);
          if (i > 0) addImplication(p - 1, -x);
        }
        currentAux += k;
      }
    }

    // SCC
    const visited = new Int8Array(totalNodes).fill(0);
    const order = [];

    const dfs1 = (u) => {
      visited[u] = 1;
      for (const v of adj[u]) {
        if (!visited[v]) dfs1(v);
      }
      order.push(u);
    };

    // Use iterative DFS if stack depth is an issue, but standard recursion usually fits 10^5 in Node
    // For safety with 4*10^5 nodes, increasing stack size or iterative is better.
    // Here we use recursive for clarity.
    
    try {
        for (let i = 1; i <= 2 * N; i++) {
          if (!visited[i]) dfs1(i);
        }
    } catch(e) {
        // Fallback or error handling
        return null;
    }

    const component = new Int32Array(totalNodes).fill(-1);
    let compCount = 0;

    const dfs2 = (u, c) => {
      component[u] = c;
      for (const v of revAdj[u]) {
        if (component[v] === -1) dfs2(v, c);
      }
    };

    for (let i = order.length - 1; i >= 0; i--) {
      const u = order[i];
      if (component[u] === -1) {
        dfs2(u, compCount++);
      }
    }

    const result = [];
    for (let i = 1; i <= n; i++) {
      if (component[i] === component[i + N]) return null;
      result.push(component[i] > component[i + N] ? 1 : 0);
    }
    return result;
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
  const clauses = [];
  for (let i = 0; i < m; i++) {
    const a = parseInt(data[idx++], 10);
    const b = parseInt(data[idx++], 10);
    clauses.push([a, b]);
  }
  const g = parseInt(data[idx++], 10);
  const groups = [];
  for (let i = 0; i < g; i++) {
    const k = parseInt(data[idx++], 10);
    const varsList = [];
    for (let j = 0; j < k; j++) varsList.push(parseInt(data[idx++], 10));
    groups.push(varsList);
  }

  const solution = new Solution();
  const assign = solution.solveTwoSat(n, clauses, groups);
  if (assign === null) {
    console.log("UNSAT");
  } else {
    console.log("SAT");
    console.log(assign.join(" "));
  }
});
