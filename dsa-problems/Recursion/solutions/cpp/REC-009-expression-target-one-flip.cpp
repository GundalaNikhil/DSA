#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> expressions(string s, long long target, int maxOps) {
        vector<string> result;
        backtrack(0, 0, 0, false, "", s, target, maxOps, result);
        sort(result.begin(), result.end());
        return result;
    }

private:
    void backtrack(int index, long long currentVal, int opsCount, bool flipUsed, string expr, 
                   const string& s, long long target, int maxOps, vector<string>& result) {
        if (index == s.length()) {
            if (currentVal == target) {
                result.push_back(expr);
            }
            return;
        }

        for (int i = index; i < s.length(); i++) {
            if (i > index && s[index] == '0') break;

            string sub = s.substr(index, i - index + 1);
            long long val = stoll(sub);

            if (index == 0) {
                // First term
                backtrack(i + 1, val, 0, flipUsed, sub, s, target, maxOps, result);
                if (!flipUsed) {
                    backtrack(i + 1, -val, 0, true, "-" + sub, s, target, maxOps, result);
                }
            } else {
                if (opsCount < maxOps) {
                    // +
                    backtrack(i + 1, currentVal + val, opsCount + 1, flipUsed, expr + "+" + sub, s, target, maxOps, result);
                    if (!flipUsed) {
                        backtrack(i + 1, currentVal - val, opsCount + 1, true, expr + "+-" + sub, s, target, maxOps, result);
                    }

                    // -
                    backtrack(i + 1, currentVal - val, opsCount + 1, flipUsed, expr + "-" + sub, s, target, maxOps, result);
                    if (!flipUsed) {
                        backtrack(i + 1, currentVal + val, opsCount + 1, true, expr + "--" + sub, s, target, maxOps, result);
                    }
                }
            }
        }
    }
};
