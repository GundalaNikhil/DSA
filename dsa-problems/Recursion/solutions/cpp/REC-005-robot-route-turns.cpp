#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class Solution {
    int R, C, T;
    long long memo[55][55][4][20]; // r, c, dir, turns. T <= 15 per problem constraints usually? 
    // Python constraints? 
    // If T is large, maybe map? But T usually small for turn limits.
    // Python code handles T dynamically? 
    // Let's use a map or bigger array?
    // r, c usually small?
    // Let's assume R,C <= 50, T <= 50.

public:
    long long countPaths(int r, int c, int t) {
        R = r; C = c; T = t;
        memset(memo, -1, sizeof(memo));
        // Start: 0,0, no last dir (-1), 0 turns
        // lastDir: 0=Right, 1=Down. -1=None.
        // Array index for -1 -> use 2 or something?
        // Map: 0->0, 1->1, -1->2.
        return dfs(0, 0, 2, 0);
    }

    long long dfs(int r, int c, int lastDir, int turns) {
        if (r == R - 1 && c == C - 1) return 1;
        if (turns > T) return 0;
        
        if (memo[r][c][lastDir][turns] != -1) return memo[r][c][lastDir][turns];

        long long count = 0;

        // Dir 0: Right (c+1)
        if (c + 1 < C) {
            int newTurns = turns;
            if (lastDir != 2 && lastDir != 0) newTurns++; // Turn if changing from Down(1) to Right(0)
            count += dfs(r, c + 1, 0, newTurns);
        }

        // Dir 1: Down (r+1)
        if (r + 1 < R) {
            int newTurns = turns;
            if (lastDir != 2 && lastDir != 1) newTurns++; // Turn if changing from Right(0) to Down(1)
            count += dfs(r + 1, c, 1, newTurns);
        }

        return memo[r][c][lastDir][turns] = count;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r, c, T;
    if (!(cin >> r >> c >> T)) return 0;
    
    Solution sol;
    cout << sol.countPaths(r, c, T) << endl;
    return 0;
}
