const readline = require("readline");

class Solution {
  articulationAndBcc(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u);
    }

    const tin = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    let timer = 0;
    const aps = new Set();
    const bccs = [];
    const stack = [];

    // Iterative DFS is hard for Tarjan's because we need to process after returning.
    // Given N=200,000, recursion can overflow.
    // However, implementing iterative Tarjan is complex.
    // Use a custom stack to simulate recursion.

    // Frame: { u, p, iterIndex, children }

    const runDFS = (startNode) => {
        const callStack = [{ u: startNode, p: -1, idx: 0, children: 0 }];
        tin[startNode] = low[startNode] = timer++;

        while (callStack.length > 0) {
            const frame = callStack[callStack.length - 1];
            const u = frame.u;
            const p = frame.p;

            if (frame.idx < adj[u].length) {
                const v = adj[u][frame.idx];
                frame.idx++;

                if (v === p) continue;

                if (tin[v] !== -1) {
                    low[u] = Math.min(low[u], tin[v]);
                    if (tin[v] < tin[u]) {
                        stack.push([u, v]);
                    }
                } else {
                    stack.push([u, v]);
                    frame.children++;
                    // Push new frame
                    tin[v] = low[v] = timer++;
                    callStack.push({ u: v, p: u, idx: 0, children: 0 });
                }
            } else {
                // Post-order
                callStack.pop();
                if (p !== -1) {
                    // Update parent
                    const parentFrame = callStack[callStack.length - 1];
                    low[p] = Math.min(low[p], low[u]);

                    if (low[u] >= tin[p]) {
                        aps.add(p);
                        const bcc = new Set();
                        while (stack.length > 0) {
                            const edge = stack.pop();
                            bcc.add(edge[0]);
                            bcc.add(edge[1]);
                            if (edge[0] === p && edge[1] === u) break;
                        }
                        bccs.push(Array.from(bcc));
                    }
                } else {
                    // Root
                    if (frame.children > 1) {
                        aps.add(startNode);
                    }
                }
            }
        }
    };

    for (let i = 0; i < n; i++) {
        if (tin[i] === -1) {
            runDFS(i);
            if (stack.length > 0) {
                const bcc = new Set();
                while (stack.length > 0) {
                    const edge = stack.pop();
                    bcc.add(edge[0]);
                    bcc.add(edge[1]);
                }
                bccs.push(Array.from(bcc));
            }
        }
    }

    const sortedAps = Array.from(aps).sort((a, b) => a - b);
    return [sortedAps, bccs];
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
  const [aps, bccs] = solution.articulationAndBcc(n, edges);

  const out = [aps.length.toString()];
  if (aps.length > 0) out.push(aps.join(" "));
  else out.push("");

  out.push(bccs.length.toString());
  for (const b of bccs) {
    out.push(``b.length`{b.join(" ")}`.trim());
  }

  // Handle empty line logic for aps
  if (aps.length === 0) {
      // out has ["0", "", "numBCC", ...]
      // join("\n") gives "0\n\nnumBCC..."
      // This is correct.
  }

  console.log(out.join("\n").trim());
});
