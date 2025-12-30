class Solution {
  solve(expr) {
    let postfix = "";
    const ops = [];
    let redundant = 0;
    
    const prec = {
      '+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, '(': 0
    };
    
    let lastType = 0; // 0: Start, 1: Operand, 2: Operator, 3: Open, 4: Close
    
    for (let i = 0; i < expr.length; i++) {
      const c = expr[i];
      
      if (/[A-Z0-9]/.test(c)) {
        if (lastType === 1 || lastType === 4) return "ERROR Invalid syntax 0";
        postfix += c;
        lastType = 1;
      } else if (c === '(') {
        if (lastType === 1 || lastType === 4) return "ERROR Invalid syntax 0";
        ops.push(c);
        lastType = 3;
      } else if (c === ')') {
        if (lastType === 0 || lastType === 2 || lastType === 3) return "ERROR Invalid syntax 0";
        
        let hasOp = false;
        while (ops.length > 0 && ops[ops.length - 1] !== '(') {
          postfix += ops.pop();
          hasOp = true;
        }
        
        if (ops.length === 0) return "ERROR Mismatched parentheses 0";
        ops.pop();
        
        if (!hasOp) redundant++;
        
        lastType = 4;
      } else if (prec.hasOwnProperty(c)) {
        if (lastType === 0 || lastType === 2 || lastType === 3) return "ERROR Invalid syntax 0";
        
        while (ops.length > 0 && ops[ops.length - 1] !== '(' && 
               (prec[ops[ops.length - 1]] > prec[c] || 
               (prec[ops[ops.length - 1]] === prec[c] && c !== '^'))) {
          postfix += ops.pop();
        }
        ops.push(c);
        lastType = 2;
      } else {
        return "ERROR Invalid character 0";
      }
    }
    
    if (lastType === 0 || lastType === 2 || lastType === 3) return "ERROR Invalid syntax 0";
    
    while (ops.length > 0) {
      if (ops[ops.length - 1] === '(') return "ERROR Mismatched parentheses 0";
      postfix += ops.pop();
    }
    
    return `POSTFIX `postfix`{redundant}`;
  }
}
