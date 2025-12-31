const readline = require("readline");

class Solution {
  processCommands(commands) {
    // Using a simple array with an index pointer for O(1) amortized dequeue
    // Or a proper Linked List implementation.
    // For simplicity in JS, we can use an array but shift() is O(N).
    // However, for competitive programming in JS, usually a custom Queue is needed
    // or we assume N is small enough.
    // Let's implement a pointer-based queue for O(1).
    
    const queue = [];
    let head = 0;
    const result = [];
    
    for (const cmd of commands) {
      const op = cmd[0];
      if (op === "ENQUEUE") {
        queue.push(cmd[1]);
      } else if (op === "DEQUEUE") {
        if (head >= queue.length) {
          result.push("EMPTY");
        } else {
          result.push(queue[head]);
          head++;
        }
      } else if (op === "FRONT") {
        if (head >= queue.length) {
          result.push("EMPTY");
        } else {
          result.push(queue[head]);
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
  const m = parseInt(data[idx++], 10);
  const commands = [];

  for (let i = 0; i < m; i++) {
    const op = data[idx++];
    if (op === "ENQUEUE") {
      const x = data[idx++];
      commands.push([op, x]);
    } else {
      commands.push([op]);
    }
  }

  const solution = new Solution();
  const result = solution.processCommands(commands);
  console.log(result.join("\n"));
});
