const readline = require("readline");

class Solution {
  processQueueOperations(operations) {
    const queue = [];
    let total = 0;

    for (const opData of operations) {
      const cmd = opData[0];

      if (cmd === "ENQUEUE") {
        queue.push(parseInt(opData[1], 10));

      } else if (cmd === "DEQUEUE") {
        if (queue.length > 0) {
          queue.shift();
        }

      } else if (cmd === "FRONT") {
        // Just read
      } else if (cmd === "REAR") {
        // Just read
      } else if (cmd === "SIZE") {
        total += queue.length;

      } else if (cmd === "ISEMPTY") {
        // Just read
      }
    }

    return String(total);
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
  const operations = [];

  for (let i = 0; i < m; i++) {
    const op = data[idx++];
    if (op === "ENQUEUE") {
      const val = data[idx++];
      operations.push([op, val]);
    } else {
      operations.push([op]);
    }
  }

  const solution = new Solution();
  const result = solution.processQueueOperations(operations);
  console.log(result);
});
