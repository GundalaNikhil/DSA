class Solution {
  expressions(s, target, maxOps) {
    const results = [];
    const n = s.length;

    const backtrack = (index, currentVal, opsCount, flipUsed, currentExpr) => {
      if (index === n) {
        if (currentVal === target) {
          results.push(currentExpr);
        }
        return;
      }

      for (let i = index; i < n; i++) {
        if (i > index && s[index] === '0') break;

        const sub = s.substring(index, i + 1);
        const val = parseInt(sub, 10);

        if (index === 0) {
          // First term
          backtrack(i + 1, val, 0, flipUsed, sub);
          if (!flipUsed) {
            backtrack(i + 1, -val, 0, true, "-" + sub);
          }
        } else {
          if (opsCount < maxOps) {
            // +
            backtrack(i + 1, currentVal + val, opsCount + 1, flipUsed, currentExpr + "+" + sub);
            if (!flipUsed) {
              backtrack(i + 1, currentVal - val, opsCount + 1, true, currentExpr + "+-" + sub);
            }

            // -
            backtrack(i + 1, currentVal - val, opsCount + 1, flipUsed, currentExpr + "-" + sub);
            if (!flipUsed) {
              backtrack(i + 1, currentVal + val, opsCount + 1, true, currentExpr + "--" + sub);
            }
          }
        }
      }
    };

    backtrack(0, 0, 0, false, "");
    return results.sort();
  }
}
