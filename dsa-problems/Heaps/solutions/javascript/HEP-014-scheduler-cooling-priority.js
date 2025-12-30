const readline = require("readline");

class Solution {
  maxPriority(T, cooldown, ids, count, priority) {
    const m = ids.length;
    const tasks = [];
    for (let i = 0; i < m; i++) {
      tasks.push({
        id: ids[i],
        count: count[i],
        priority: BigInt(priority[i]),
        x: count[i]
      });
    }
    
    // 1. Clamp
    const limit = Math.floor((T + cooldown) / (cooldown + 1));
    for (const t of tasks) {
      t.x = Math.min(t.count, limit);
    }
    
    // 2. Schedule Constraint
    while (true) {
      let maxX = 0;
      for (const t of tasks) maxX = Math.max(maxX, t.x);
      
      if (maxX === 0) break;
      
      const atMax = tasks.filter(t => t.x === maxX);
      const required = (maxX - 1) * (cooldown + 1) + atMax.length;
      
      if (required <= T) break;
      
      const allowed = T - (maxX - 1) * (cooldown + 1);
      
      atMax.sort((a, b) => {
        if (a.priority > b.priority) return -1;
        if (a.priority < b.priority) return 1;
        return 0;
      });
      
      for (let i = allowed; i < atMax.length; i++) {
        atMax[i].x--;
      }
    }
    
    // 3. Sum Constraint
    let sumX = 0;
    for (const t of tasks) sumX += t.x;
    
    if (sumX > T) {
      let toRemove = sumX - T;
      tasks.sort((a, b) => {
        if (a.priority < b.priority) return -1;
        if (a.priority > b.priority) return 1;
        return 0;
      });
      
      for (const t of tasks) {
        if (toRemove <= 0) break;
        const rem = Math.min(t.x, toRemove);
        t.x -= rem;
        toRemove -= rem;
      }
    }
    
    let totalScore = 0n;
    for (const t of tasks) {
      totalScore += BigInt(t.x) * t.priority;
    }
    
    return totalScore.toString();
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
  const m = parseInt(data[idx++]);
  const cooldown = parseInt(data[idx++]);
  const T = parseInt(data[idx++]);
  const ids = [];
  const count = [];
  const priority = [];
  for (let i = 0; i < m; i++) {
    ids.push(data[idx++]);
    count.push(parseInt(data[idx++]));
    priority.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  console.log(solution.maxPriority(T, cooldown, ids, count, priority));
});
