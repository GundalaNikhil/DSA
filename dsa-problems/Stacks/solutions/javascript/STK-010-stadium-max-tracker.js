class Solution {
  process(ops) {
    const result = [];
    const mainStack = [];
    const maxStack = [];
    
    for (const op of ops) {
      const cmd = op[0];
      
      if (cmd === "PUSH") {
        const val = parseInt(op[1], 10);
        mainStack.push(val);
        if (maxStack.length === 0 || val >= maxStack[maxStack.length - 1]) {
          maxStack.push(val);
        }
      } else if (cmd === "POP") {
        if (mainStack.length === 0) {
          result.push("EMPTY");
        } else {
          const val = mainStack.pop();
          result.push(val.toString());
          if (val === maxStack[maxStack.length - 1]) {
            maxStack.pop();
          }
        }
      } else if (cmd === "TOP") {
        if (mainStack.length === 0) {
          result.push("EMPTY");
        } else {
          result.push(mainStack[mainStack.length - 1].toString());
        }
      } else if (cmd === "GETMAX") {
        if (mainStack.length === 0) {
          result.push("EMPTY");
        } else {
          result.push(maxStack[maxStack.length - 1].toString());
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

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  if (lines.length === 0) return;
  
  const m = parseInt(lines[0].trim(), 10);
  const ops = [];
  
  for (let i = 1; i <= m; i++) { // Read m lines
    if (i < lines.length) {
      ops.push(lines[i].trim().split(/\s+/));
    }
  }
  
  const solution = new Solution();
  const res = solution.process(ops);
  console.log(res.join("\n"));
});
