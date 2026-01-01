#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> solveLatinSquare(int n) {
        vector<vector<int>> grid(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = ((i + j) % n) + 1;
            }
        }
        return grid;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    
    Solution sol;
    vector<vector<int>> res = sol.solveLatinSquare(n);
    for(const auto& row : res) { 
        for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?"":" "); 
        cout << endl; 
    }
    return 0;
}
