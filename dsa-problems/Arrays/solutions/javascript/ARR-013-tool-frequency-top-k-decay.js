const readline = require("readline");

class Solution {
  topKWithDecay(events, now, D, k) {
    const scores = new Map();
    
    for (const [v, t] of events) {
      const term = Math.exp(-(now - t) / D);
      scores.set(v, (scores.get(v) || 0) + term);
    }
    
    const items = [];
    for (const [v, s] of scores.entries()) {
      items.push({ value: v, score: s });
    }
    
    // Sort: Descending Score, Ascending Value
    items.sort((a, b) => {
      if (Math.abs(b.score - a.score) > 1e-9) {
        return b.score - a.score;
      }
      return a.value - b.value;
    });
    
    const result = [];
    for (let i = 0; i < k && i < items.length; i++) {
      result.push(items[i].value);
    }
    return result;
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
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const events = [];
    for (let i = 0; i < n; i++) {
      const v = Number(tokens[ptr++]);
      const t = Number(tokens[ptr++]);
      events.push([v, t]);
    }
    
    const now = Number(tokens[ptr++]);
    const D = Number(tokens[ptr++]);
    const k = Number(tokens[ptr++]);
    
    const solution = new Solution();
    const result = solution.topKWithDecay(events, now, D, k);
    console.log(result.join(" "));
});
