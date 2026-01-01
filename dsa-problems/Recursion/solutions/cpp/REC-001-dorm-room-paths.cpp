#include <iostream>
#include <vector>
using namespace std;

class Solution {
    vector<vector<long long>> memo;
public:
    long long countPaths(int r, int c) {
        memo.assign(r, vector<long long>(c, -1));
        return helper(r - 1, c - 1);
    }

    long long helper(int r, int c) {
        if (r == 0 && c == 0) return 1;
        if (r < 0 || c < 0) return 0;
        
        if (memo[r][c] != -1) return memo[r][c];
        
        return memo[r][c] = helper(r - 1, c) + helper(r, c - 1);
    }
};






int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r; cin >> r;
    int c; cin >> c;
    Solution sol;
    cout << sol.countPaths(r, c) << endl;
    return 0;
}
