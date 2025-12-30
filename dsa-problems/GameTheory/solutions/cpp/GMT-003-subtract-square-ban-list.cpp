#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    string subtractSquareGame(int n, vector<int>& banned) {
        unordered_set<int> bannedSet(banned.begin(), banned.end());
        vector<bool> dp(n + 1, false);
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                int s = j * j;
                if (bannedSet.find(s) == bannedSet.end()) {
                    if (!dp[i - s]) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }
        
        return dp[n] ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k;
    if (cin >> n >> k) {
        vector<int> banned(k);
        for (int i = 0; i < k; i++) {
            cin >> banned[i];
        }
        
        Solution solution;
        cout << solution.subtractSquareGame(n, banned) << "\n";
    }
    return 0;
}
