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
