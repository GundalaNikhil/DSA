class Solution {
  evalPostfix(tokens, vars) {
    const stack = [];
    const MOD = 1000000007n;
    
    for (const token of tokens) {
      if (vars.has(token)) {
        stack.push(BigInt(vars.get(token)) % MOD);
      } else if (!isNaN(token)) {
        stack.push(BigInt(token) % MOD);
      } else if (token === "DUP") {
        stack.push(stack[stack.length - 1]);
      } else if (token === "SWAP") {
        const a = stack.pop();
        const b = stack.pop();
        stack.push(a);
        stack.push(b);
      } else {
        const b = stack.pop();
        const a = stack.pop();
        let res = 0n;
        
        if (token === "+") {
          res = (a + b) % MOD;
        } else if (token === "-") {
          res = (a - b + MOD) % MOD;
        } else if (token === "*") {
          res = (a * b) % MOD;
        } else if (token === "/") {
          // Integer division (Floor)
          // JS BigInt / is truncation towards 0 (like Java).
          // Python // is floor.
          // If a/b is negative, 
          // Python: -5 // 2 = -3.
          // JS: -5n / 2n = -2n.
          // We need floor.
          // If (a/b) < 0 and a%b != 0, subtract 1?
          // Or strictly follow Python semantics.
          // Helper for floor div
          res = a / b;
          if ((a < 0n) !== (b < 0n) && a % b !== 0n) {
             res -= 1n;
          }
        } else if (token === "%") {
          // Python Modulo
          res = ((a % b) + b) % b;
        }
        stack.push(res);
      }
    }
    return stack[stack.length - 1].toString();
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
  
  const numVars = parseInt(lines[0].trim(), 10);
  const vars = new Map();
  
  for (let i = 1; i <= numVars; i++) {
    const parts = lines[i].trim().split(/\s+/);
    vars.set(parts[0], parseInt(parts[1], 10));
  }
  
  const expr = lines[numVars + 1].trim();
  const tokens = expr.split(/\s+/);
  
  const solution = new Solution();
  console.log(solution.evalPostfix(tokens, vars));
});
