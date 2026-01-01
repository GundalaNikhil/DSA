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
  const remaining = data.slice(idx);

  let t, k, times;

  // If we have exactly n remaining values
  if (remaining.length === n) {
    times = remaining.slice(0, n).map(x => parseInt(x, 10));
    t = 1;  // Default
    k = 1;  // Default
  } else if (remaining.length === n + 2) {
    // First two are t and k
    t = parseInt(remaining[0], 10);
    k = parseInt(remaining[1], 10);
    times = remaining.slice(2, n + 2).map(x => parseInt(x, 10));
  } else {
    // Fallback: assume first two (if present) are t and k
    t = remaining.length > 0 ? parseInt(remaining[0], 10) : 1;
    k = remaining.length > 1 ? parseInt(remaining[1], 10) : 1;
    times = remaining.slice(2, n + 2).map(x => parseInt(x, 10));
  }

  const solution = new Solution();
  const result = solution.rateLimit(times, t, k);
  console.log(result.join(" "));
});
