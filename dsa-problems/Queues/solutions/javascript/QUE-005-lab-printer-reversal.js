const readline = require("readline");

class Solution {
  reverseFirstK(values, k) {
    // Using array methods to simulate Queue/Stack for clarity
    const queue = [...values]; // Copy
    const stack = [];
    
    // 1. Dequeue first K
    for (let i = 0; i < k; i++) {
      stack.push(queue.shift());
    }
    
    // 2. Pop and Enqueue
    while (stack.length > 0) {
      queue.push(stack.pop());
    }
    
    // 3. Rotate remaining N-K
    const n = values.length;
    for (let i = 0; i < n - k; i++) {
      queue.push(queue.shift());
    }
    
    return queue;
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
  const result = solution.reverseFirstK(values, k);
  console.log(result.join(" "));
});
