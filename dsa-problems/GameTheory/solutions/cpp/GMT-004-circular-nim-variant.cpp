#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

class Solution {
    map<vector<int>, string> memo;
    set<vector<int>> visiting;

public:
    string circularNim(int n, vector<int>& piles) {
        return solve(n, piles, 0);
    }

    string solve(int n, vector<int>& piles, int depth) {
        if (depth > 50) return "Draw";
        if (memo.count(piles)) return memo[piles];
        if (visiting.count(piles)) return "Draw";

        visiting.insert(piles);
        bool canReachLoss = false;
        bool canReachDraw = false;
        bool hasMoves = false;

        for (int i = 0; i < n; i++) {
            if (piles[i] > 0) {
                for (int k = 1; k <= piles[i]; k++) {
                    hasMoves = true;
                    piles[i] -= k;
                    piles[(i - 1 + n) % n]++;
                    piles[(i + 1) % n]++;

                    string res = solve(n, piles, depth + 1);
                    
                    piles[(i + 1) % n]--;
                    piles[(i - 1 + n) % n]--;
                    piles[i] += k;

                    if (res == "Second") {
                        canReachLoss = true;
                        break;
                    }
                    if (res == "Draw") {
                        canReachDraw = true;
                    }
                }
                if (canReachLoss) break;
            }
        }

        visiting.erase(piles);
        string result;
        if (canReachLoss) result = "First";
        else if (!hasMoves) result = "Second";
        else if (canReachDraw) result = "Draw";
        else result = "Second";

        return memo[piles] = result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> piles(n);
        for (int i = 0; i < n; i++) {
            cin >> piles[i];
        }
        
        Solution solution;
        cout << solution.circularNim(n, piles) << "\n";
    }
    return 0;
}
