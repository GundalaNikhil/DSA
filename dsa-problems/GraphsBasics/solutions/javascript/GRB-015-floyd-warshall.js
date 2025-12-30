const readline = require("readline");

class Solution {
  floydWarshall(dist) {
    const n = dist.length;
    const INF = 1e15; // Safe large number

    // Preprocess
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (i !== j && dist[i][j] === -1) {
          dist[i][j] = INF;
        }
      }
    }

    for (let k = 0; k < n; k++) {
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
          if (dist[i][k] !== INF && dist[k][j] !== INF) {
            if (dist[i][k] + dist[k][j] < dist[i][j]) {
              dist[i][j] = dist[i][k] + dist[k][j];
            }
          }
        }
      }
    }

    // Negative Cycle Check
    for (let i = 0; i < n; i++) {
      if (dist[i][i] < 0) return null;
    }

    // Postprocess
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (dist[i][j] >= INF / 2) {
          dist[i][j] = -1;
        }
      }
    }

    return dist;
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
  const dist = Array.from({ length: n }, () => new Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dist[i][j] = parseInt(data[idx++], 10);
    }
  }

  const solution = new Solution();
  const ans = solution.floydWarshall(dist);
  if (ans === null) {
    console.log("NEGATIVE CYCLE");
  } else {
    const out = [];
    for (let i = 0; i < n; i++) {
      out.push(ans[i].join(" "));
    }
    console.log(out.join("\n"));
  }
});
