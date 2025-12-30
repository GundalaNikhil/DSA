const readline = require("readline");

class Solution {
  maxOverlap(x1, y1, x2, y2) {
    const n = x1.length;
    let ys = new Set();
    for (let i = 0; i < n; i++) {
      ys.add(y1[i]);
      ys.add(y2[i]);
    }
    const sortedYs = Array.from(ys).sort((a, b) => a - b);
    const yMap = new Map();
    for (let i = 0; i < sortedYs.length; i++) {
      yMap.set(sortedYs[i], i);
    }
    
    const events = [];
    for (let i = 0; i < n; i++) {
      events.push({ x: x1[i], type: 1, l: yMap.get(y1[i]), r: yMap.get(y2[i]) });
      events.push({ x: x2[i], type: -1, l: yMap.get(y1[i]), r: yMap.get(y2[i]) });
    }
    
    events.sort((a, b) => a.x - b.x);
    
    const segN = sortedYs.length - 1;
    if (segN <= 0) return 0;
    
    const add = new Int32Array(4 * segN).fill(0);
    const mx = new Int32Array(4 * segN).fill(0);
    
    const update = (node, l, r, ql, qr, val) => {
      if (qr <= l || r <= ql) return;
      if (ql <= l && r <= qr) {
        add[node] += val;
        mx[node] += val;
        return;
      }
      const mid = Math.floor((l + r) / 2);
      update(node * 2, l, mid, ql, qr, val);
      update(node * 2 + 1, mid, r, ql, qr, val);
      mx[node] = add[node] + Math.max(mx[node * 2], mx[node * 2 + 1]);
    };
    
    let ans = 0;
    for (const e of events) {
      update(1, 0, segN, e.l, e.r, e.type);
      ans = Math.max(ans, mx[1]);
    }
    
    return ans;
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
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  
  const x1 = [], y1 = [], x2 = [], y2 = [];
  for (let i = 0; i < n; i++) x1.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) y1.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) x2.push(parseInt(data[ptr++], 10));
  for (let i = 0; i < n; i++) y2.push(parseInt(data[ptr++], 10));
  
  const solution = new Solution();
  console.log(solution.maxOverlap(x1, y1, x2, y2));
});
