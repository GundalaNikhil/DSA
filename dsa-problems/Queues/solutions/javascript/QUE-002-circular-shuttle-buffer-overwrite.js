const readline = require("readline");

class Solution {
  processOperations(k, operations) {
    const buffer = new Int32Array(k);
    let head = 0;
    let tail = 0;
    let count = 0;
    const result = [];
    
    for (const opData of operations) {
      const cmd = opData[0];
      
      if (cmd === "ENQ") {
        if (count === k) {
          result.push("false");
        } else {
          buffer[tail] = parseInt(opData[1], 10);
          tail = (tail + 1) % k;
          count++;
          result.push("true");
        }
      } else if (cmd === "ENQ_OVR") {
        const val = parseInt(opData[1], 10);
        if (count === k) {
          head = (head + 1) % k;
          buffer[tail] = val;
          tail = (tail + 1) % k;
          result.push("overwritten");
        } else {
          buffer[tail] = val;
          tail = (tail + 1) % k;
          count++;
          result.push("true");
        }
      } else if (cmd === "DEQ") {
        if (count === 0) {
          result.push("EMPTY");
        } else {
          result.push(String(buffer[head]));
          head = (head + 1) % k;
          count--;
        }
      } else if (cmd === "FRONT") {
        if (count === 0) result.push("EMPTY");
        else result.push(String(buffer[head]));
      } else if (cmd === "REAR") {
        if (count === 0) result.push("EMPTY");
        else {
          const idx = (tail - 1 + k) % k;
          result.push(String(buffer[idx]));
        }
      } else if (cmd === "ISEMPTY") {
        result.push(count === 0 ? "true" : "false");
      } else if (cmd === "ISFULL") {
        result.push(count === k ? "true" : "false");
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
  const k = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const operations = [];

  for (let i = 0; i < m; i++) {
    const op = data[idx++];
    if (op === "ENQ" || op === "ENQ_OVR") {
      const x = data[idx++];
      operations.push([op, x]);
    } else {
      operations.push([op]);
    }
  }

  const solution = new Solution();
  const result = solution.processOperations(k, operations);
  console.log(result.join("\n"));
});
