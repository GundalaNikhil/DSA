#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

class Solution {
public:
    string pileSplitGame(int n) {
        if (n == 0) return "Second";
        vector<int> g(n + 1, 0);
        
        for (int i = 3; i <= n; i++) {
            unordered_set<int> reachable;
            for (int j = 1; 2 * j < i; j++) {
                reachable.insert(g[j] ^ g[i - j]);
            }
            
            int mex = 0;
            while (reachable.count(mex)) {
                mex++;
            }
            g[i] = mex;
        }
        
        return g[n] > 0 ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (cin >> n) {
        Solution solution;
        cout << solution.pileSplitGame(n) << "\n";
    }
    return 0;
}
