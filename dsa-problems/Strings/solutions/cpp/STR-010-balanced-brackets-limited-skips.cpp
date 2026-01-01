#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
class Solution {
public:
    bool canBalanceWithSkips(string s, int k) {
        int balance = 0;
        int skipsUsed = 0;

        for (char c : s) {
            if (c == '(') {
                balance++;
            } else {  // c == ')'
                balance--;
                if (balance < 0) {
                    // Need to skip this ')'
                    skipsUsed++;
                    balance = 0;
                }
            }
        }

        // Remaining balance are unmatched '('
        int totalSkipsNeeded = skipsUsed + balance;
        return totalSkipsNeeded <= k;
    }
};

















int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int k; cin >> k;
    Solution sol;
    cout << (sol.canBalanceWithSkips(s, k) ? "true" : "false") << endl;
    return 0;
}
