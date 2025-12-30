class Solution {
  eval(tokens, vars) {
    const stack = [];
    const MOD = 1000000007n;
    
    for (const token of tokens) {
      if (vars.has(token)) {
        let val = BigInt(vars.get(token)) % MOD;
        if (val < 0n) val += MOD;
        stack.push(val);
      } else if (!isNaN(token)) {
        let val = BigInt(token) % MOD;
        if (val < 0n) val += MOD;
        stack.push(val);
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
        
        if (token === "+") res = (a + b) % MOD;
        else if (token === "-") res = (a - b + MOD) % MOD;
        else if (token === "*") res = (a * b) % MOD;
        else if (token === "/") res = a / b;
        else if (token === "%") res = a % b;
        
        stack.push(res);
      }
    }
    return Number(stack[stack.length - 1]);
  }
}
