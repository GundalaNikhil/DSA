const readline = require("readline");

class Solution {
  sccCompress(n, adj) {
    const tin = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    const onStack = new Int8Array(n).fill(0);
    const stack = [];
    const sccs = [];
    let timer = 0;

    // Iterative Tarjan using explicit stack
    // Frame: { u, iterIndex }

    const runDFS = (startNode) => {
        const callStack = [{ u: startNode, idx: 0 }];
        tin[startNode] = low[startNode] = timer++;
        stack.push(startNode);
        onStack[startNode] = 1;

        while (callStack.length > 0) {
            const frame = callStack[callStack.length - 1];
            const u = frame.u;

            if (frame.idx < adj[u].length) {
                const v = adj[u][frame.idx];
                frame.idx++;

                if (tin[v] === -1) {
                    tin[v] = low[v] = timer++;
                    stack.push(v);
                    onStack[v] = 1;
                    callStack.push({ u: v, idx: 0 });
                } else if (onStack[v]) {
                    low[u] = Math.min(low[u], tin[v]);
                }
            } else {
                // Post-order
                callStack.pop();
                if (callStack.length > 0) {
                    const p = callStack[callStack.length - 1].u;
                    low[p] = Math.min(low[p], low[u]);
                }

                if (low[u] === tin[u]) {
                    const component = [];
                    while (true) {
                        const v = stack.pop();
                        onStack[v] = 0;
                        component.push(v);
                        if (u === v) break;
                    }
                    sccs.push(component);
                }
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (tin[i] === -1) runDFS(i);
    }

    const k = sccs.length;
    const comp = new Int32Array(n);
    // Assign IDs
    // sccs are found in reverse topological order
    // Reverse sccs to get topological order (Source -> Sink)
    // Though problem doesn't require specific order.
    // Use index.

    // Note: Tarjan's naturally produces reverse topological order of SCCs.
    // sccs[0] is a sink SCC.
    // If we want comp[u] to be somewhat topological, we can assign k-1-i.
    // But simple 0..k-1 is fine.

    for (let i = 0; i < k; i++) {
        for (const node of sccs[i]) {
            comp[node] = i;
        }
    }

    const dagEdges = new Set();
    const edgesList = [];

    for (let u = 0; u < n; u++) {
        for (const v of adj[u]) {
            if (comp[u] !== comp[v]) {
                const key = ``comp[u],`{comp[v]}`;
                if (!dagEdges.has(key)) {
                    dagEdges.add(key);
                    edgesList.push([comp[u], comp[v]]);
                }
            }
        }
    }

    return [k, comp, edgesList];
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
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
  }

  const solution = new Solution();
  const [k, comp, edges] = solution.sccCompress(n, adj);

  const out = [k.toString(), comp.join(" "), edges.length.toString()];
  for (const [a, b] of edges) out.push(``a`{b}`);
  console.log(out.join("\n").trim());
});
