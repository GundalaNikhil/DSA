const readline = require("readline");

class Solution {
  rateLimit(times, t, k) {
    const queue = [];
    let front = 0;
    const result = [];
    
    for (const time of times) {
      while (front < queue.length && queue[front] < time - t) {
        front++;
      }
      
      if (queue.length - front < k) {
        queue.push(time);
        result.push("true");
      } else {
        result.push("false");
      }
    }
    
    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const t = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const times = [];
  for (let i = 0; i < n; i++) {
    times.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.rateLimit(times, t, k);
  console.log(result.join(" "));
});
