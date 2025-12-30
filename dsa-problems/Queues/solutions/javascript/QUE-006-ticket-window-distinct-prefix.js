const readline = require("readline");

class Solution {
  firstNonRepeating(s) {
    const count = new Map();
    // Using a simple array as queue. For strict O(N), use a linked-list queue or pointer.
    // Given constraints and JS engine optimizations, array.shift() might be acceptable 
    // but technically O(N). Let's use a pointer approach for O(1) dequeue.
    
    const queue = [];
    let head = 0;
    const result = [];
    
    for (const char of s) {
      count.set(char, (count.get(char) || 0) + 1);
      queue.push(char);
      
      while (head < queue.length && count.get(queue[head]) > 1) {
        head++;
      }
      
      if (head >= queue.length) {
        result.push("#");
      } else {
        result.push(queue[head]);
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
  const s = data[0];
  const solution = new Solution();
  const result = solution.firstNonRepeating(s);
  console.log(result.join(" "));
});
