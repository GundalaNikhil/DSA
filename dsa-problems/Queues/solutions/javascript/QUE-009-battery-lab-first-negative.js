const readline = require("readline");

class Solution {
  firstNegatives(values, k) {
    const result = [];
    // Using array as queue. For strict O(N), use pointer or linked list.
    // shift() is O(N) in worst case (queue size N).
    // But queue size is bounded by K. Total time O(N*K) worst case if using shift.
    // Let's use pointer for O(1) dequeue.
    
    const queue = []; // Stores indices
    let head = 0;
    
    for (let i = 0; i < values.length; i++) {
      if (values[i] < 0) {
        queue.push(i);
      }
      
      // Remove expired
      if (head < queue.length && queue[head] <= i - k) {
        head++;
      }
      
      if (i >= k - 1) {
        if (head >= queue.length) {
          result.push(0);
        } else {
          result.push(values[queue[head]]);
        }
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
  const k = parseInt(data[idx++], 10);
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.firstNegatives(values, k);
  console.log(result.join(" "));
});
