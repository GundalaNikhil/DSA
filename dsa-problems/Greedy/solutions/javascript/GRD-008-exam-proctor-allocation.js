const readline = require("readline");

class Solution {
  minProctors(n, r, exams) {
    const events = [];
    for (const [start, end] of exams) {
      events.push([start, 1]); // Start
      events.push([end, -1]);  // End
    }
    
    // Sort: Time ascending. If times equal, Start (1) before End (-1).
    events.sort((a, b) => {
      if (a[0] !== b[0]) return a[0] - b[0];
      return b[1] - a[1]; // 1 before -1
    });
    
    let maxOverlap = 0;
    let currentOverlap = 0;
    
    for (const [time, type] of events) {
      currentOverlap += type;
      maxOverlap = Math.max(maxOverlap, currentOverlap);
    }
    
    return Math.ceil(maxOverlap / r);
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
  
  let ptr = 0;
  const [n, r] = data[ptr++].split(" ").map(Number);
  
  const exams = [];
  for (let i = 0; i < n; i++) {
    const [start, end] = data[ptr++].split(" ").map(Number);
    exams.push([start, end]);
  }
  
  const solution = new Solution();
  console.log(solution.minProctors(n, r, exams));
});
