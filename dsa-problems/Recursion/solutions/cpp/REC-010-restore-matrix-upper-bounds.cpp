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
