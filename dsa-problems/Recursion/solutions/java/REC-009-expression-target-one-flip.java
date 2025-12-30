import java.util.*;

class Solution {
    public List<String> expressions(String s, long target, int maxOps) {
        List<String> result = new ArrayList<>();
        backtrack(0, 0, 0, false, "", s, target, maxOps, result);
        Collections.sort(result);
        return result;
    }

    private void backtrack(int index, long currentVal, int opsCount, boolean flipUsed, String expr, 
                           String s, long target, int maxOps, List<String> result) {
        if (index == s.length()) {
            if (currentVal == target) {
                result.add(expr);
            }
            return;
        }

        for (int i = index; i < s.length(); i++) {
            // Leading zero check
            if (i > index && s.charAt(index) == '0') break;

            String sub = s.substring(index, i + 1);
            long val = Long.parseLong(sub);

            if (index == 0) {
                // First term
                // Option 1: Normal
                backtrack(i + 1, val, 0, flipUsed, sub, s, target, maxOps, result);
                
                // Option 2: Flip (if not used yet, which is always true at start)
                // Unary flip at start: "-123"
                if (!flipUsed) {
                    backtrack(i + 1, -val, 0, true, "-" + sub, s, target, maxOps, result);
                }
            } else {
                if (opsCount < maxOps) {
                    // Operator +
                    // Normal
                    backtrack(i + 1, currentVal + val, opsCount + 1, flipUsed, expr + "+" + sub, s, target, maxOps, result);
                    // Flip
                    if (!flipUsed) {
                        backtrack(i + 1, currentVal - val, opsCount + 1, true, expr + "+-" + sub, s, target, maxOps, result);
                    }

                    // Operator -
                    // Normal
                    backtrack(i + 1, currentVal - val, opsCount + 1, flipUsed, expr + "-" + sub, s, target, maxOps, result);
                    // Flip
                    if (!flipUsed) {
                        backtrack(i + 1, currentVal + val, opsCount + 1, true, expr + "--" + sub, s, target, maxOps, result);
                    }
                }
            }
        }
    }
}
