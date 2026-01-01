class Solution {
  process(ops) {
    const result = [];
    const stack = [];
    
    for (const op of ops) {
      const command = op[0];
      
      if (command === "PUSH") {
        stack.push(op[1]);
      } else if (command === "POP") {
        if (stack.length === 0) {
          result.push("EMPTY");
        } else {
          result.push(stack.pop());
        }
      } else if (command === "TOP") {
        if (stack.length === 0) {
          result.push("EMPTY");
        } else {
          result.push(stack[stack.length - 1]);
        }
      }
    }
    return result;
  }
}

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const m = parseInt(data[idx++], 10);
  const ops = [];
  for (let i = 0; i < m; i++) {
    const op = data[idx++];
    if (op === "PUSH") {
      ops.push([op, data[idx++]]);
    } else {
      ops.push([op]);
    }
  }

  const solution = new Solution();
  const out = solution.process(ops);
  console.log(out.join("\n"));
});
