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
