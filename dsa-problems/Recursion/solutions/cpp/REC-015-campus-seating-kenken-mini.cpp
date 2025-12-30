#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
    int grid[4][4];
    struct Cage {
        int target;
        char op;
        vector<pair<int,int>> cells;
    };
    vector<Cage> cageList;
    int cageMap[4][4];

public:
    vector<vector<int>> solveKenKen(const vector<vector<int>>& cages) {
        // Parse cages
        cageList.clear();
        for (int i = 0; i < cages.size(); i++) {
            Cage c;
            c.target = cages[i][0];
            c.op = (char)cages[i][1];
            int len = cages[i][2];
            for (int j = 0; j < len; j++) {
                int r = cages[i][3 + 2 * j];
                int col = cages[i][4 + 2 * j];
                c.cells.push_back({r, col});
                cageMap[r][col] = i;
            }
            cageList.push_back(c);
        }

        for(int i=0; i<4; i++) fill(grid[i], grid[i]+4, 0);

        if (backtrack(0, 0)) {
            vector<vector<int>> res(4, vector<int>(4));
            for(int i=0; i<4; i++)
                for(int j=0; j<4; j++) res[i][j] = grid[i][j];
            return res;
        }
        return {};
    }

    bool backtrack(int r, int c) {
        if (r == 4) return true;

        int nextR = (c == 3) ? r + 1 : r;
        int nextC = (c == 3) ? 0 : c + 1;

        for (int v = 1; v <= 4; v++) {
            if (isValid(r, c, v)) {
                grid[r][c] = v;
                if (checkCage(r, c)) {
                    if (backtrack(nextR, nextC)) return true;
                }
                grid[r][c] = 0;
            }
        }
        return false;
    }

    bool isValid(int r, int c, int v) {
        for (int j = 0; j < 4; j++) if (grid[r][j] == v) return false;
        for (int i = 0; i < 4; i++) if (grid[i][c] == v) return false;
        return true;
    }

    bool checkCage(int r, int c) {
        int idx = cageMap[r][c];
        const Cage& cage = cageList[idx];
        
        vector<int> vals;
        for (auto& p : cage.cells) {
            if (grid[p.first][p.second] == 0) return true; // Not full
            vals.push_back(grid[p.first][p.second]);
        }

        if (cage.op == '+') {
            int sum = 0;
            for (int x : vals) sum += x;
            return sum == cage.target;
        } else if (cage.op == '*') {
            int prod = 1;
            for (int x : vals) prod *= x;
            return prod == cage.target;
        } else if (cage.op == '-') {
            return abs(vals[0] - vals[1]) == cage.target;
        } else if (cage.op == '/') {
            int a = vals[0], b = vals[1];
            return (a % b == 0 && a / b == cage.target) || (b % a == 0 && b / a == cage.target);
        } else if (cage.op == '=') {
            return vals[0] == cage.target;
        }
        return false;
    }
};
