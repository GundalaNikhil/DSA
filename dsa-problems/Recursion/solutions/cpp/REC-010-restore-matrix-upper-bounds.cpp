#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int> rowSums, vector<int> colSums, const vector<vector<int>>& bounds) {
        int R = rowSums.size();
        int C = colSums.size();
        vector<vector<int>> matrix(R, vector<int>(C));
        
        if (backtrack(0, 0, rowSums, colSums, bounds, matrix)) {
            return matrix;
        }
        return {};
    }

private:
    bool backtrack(int r, int c, vector<int>& rowSums, vector<int>& colSums, const vector<vector<int>>& bounds, vector<vector<int>>& matrix) {
        int R = rowSums.size();
        int C = colSums.size();

        if (r == R) {
            for (int x : colSums) if (x != 0) return false;
            return true;
        }

        int nextR = (c == C - 1) ? r + 1 : r;
        int nextC = (c == C - 1) ? 0 : c + 1;

        if (c == C - 1) {
            int val = rowSums[r];
            if (val >= 0 && val <= bounds[r][c] && val <= colSums[c]) {
                matrix[r][c] = val;
                rowSums[r] -= val;
                colSums[c] -= val;
                if (backtrack(nextR, nextC, rowSums, colSums, bounds, matrix)) return true;
                rowSums[r] += val;
                colSums[c] += val;
            }
            return false;
        }

        int maxVal = min({bounds[r][c], rowSums[r], colSums[c]});

        for (int val = maxVal; val >= 0; val--) {
            matrix[r][c] = val;
            rowSums[r] -= val;
            colSums[c] -= val;
            if (backtrack(nextR, nextC, rowSums, colSums, bounds, matrix)) return true;
            rowSums[r] += val;
            colSums[c] += val;
        }

        return false;
    }
};






int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int rowSums_n; cin >> rowSums_n; vector<int> rowSums(rowSums_n); for(int i=0; i<rowSums_n; i++) cin >> rowSums[i];
    int colSums_n; cin >> colSums_n; vector<int> colSums(colSums_n); for(int i=0; i<colSums_n; i++) cin >> colSums[i];
    int bounds_r, bounds_c; cin >> bounds_r >> bounds_c; vector<vector<int>> bounds(bounds_r, vector<int>(bounds_c)); for(int i=0; i<bounds_r; i++) for(int j=0; j<bounds_c; j++) cin >> bounds[i][j];
    Solution sol;
    vector<vector<int>> res = sol.restoreMatrix(rowSums, colSums, bounds); for(const auto& row : res) { for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?"":" "); cout << endl; }
    return 0;
}
