#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    int memo[20][20][20][20];
    vector<vector<int>> mat;
    int N, M;
    bool visited[20][20][20][20];

    int solve(int r1, int r2, int c1, int c2) {
        if (r1 == r2 && c1 == c2) return mat[r1][c1];
        if (visited[r1][r2][c1][c2]) return memo[r1][r2][c1][c2];

        int movesMade = (N - (r2 - r1 + 1)) + (M - (c2 - c1 + 1));
        bool isMax = (movesMade % 2 == 0);

        int res;
        if (isMax) {
            res = INT_MIN;
            if (r1 < r2) {
                res = max(res, solve(r1 + 1, r2, c1, c2));
                res = max(res, solve(r1, r2 - 1, c1, c2));
            }
            if (c1 < c2) {
                res = max(res, solve(r1, r2, c1 + 1, c2));
                res = max(res, solve(r1, r2, c1, c2 - 1));
            }
        } else {
            res = INT_MAX;
            if (r1 < r2) {
                res = min(res, solve(r1 + 1, r2, c1, c2));
                res = min(res, solve(r1, r2 - 1, c1, c2));
            }
            if (c1 < c2) {
                res = min(res, solve(r1, r2, c1 + 1, c2));
                res = min(res, solve(r1, r2, c1, c2 - 1));
            }
        }

        visited[r1][r2][c1][c2] = true;
        return memo[r1][r2][c1][c2] = res;
    }

public:
    int matrixGame(int n, int m, vector<vector<int>>& matrix) {
        N = n;
        M = m;
        mat = matrix;
        // Initialize visited
        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                for(int k=0; k<m; ++k)
                    for(int l=0; l<m; ++l)
                        visited[i][j][k][l] = false;
                        
        return solve(0, n - 1, 0, m - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (cin >> n >> m) {
        vector<vector<int>> matrix(n, vector<int>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> matrix[i][j];
            }
        }
        
        Solution solution;
        cout << solution.matrixGame(n, m, matrix) << "\n";
    }
    return 0;
}
