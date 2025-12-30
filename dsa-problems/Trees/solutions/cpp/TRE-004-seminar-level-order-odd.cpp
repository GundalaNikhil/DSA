#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<vector<int>> oddDepthLevels(int n, const vector<int>& left,
                                       const vector<int>& right, const vector<int>& values) {
        vector<vector<int>> result;
        if (n == 0) return result;
        
        queue<int> q;
        q.push(0);
        int depth = 0;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> currentLevel;
            bool isOdd = (depth % 2 != 0);
            
            for (int i = 0; i < size; i++) {
                int u = q.front();
                q.pop();
                
                if (isOdd) {
                    currentLevel.push_back(values[u]);
                }
                
                if (left[u] != -1) q.push(left[u]);
                if (right[u] != -1) q.push(right[u]);
            }
            
            if (isOdd) {
                result.push_back(currentLevel);
            }
            depth++;
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    if (n == 0) {
        cout << "\n";
        return 0;
    }

    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<vector<int>> levels = solution.oddDepthLevels(n, left, right, values);
    if (levels.empty()) {
        cout << "\n";
    } else {
        for (int i = 0; i < (int)levels.size(); i++) {
            for (int j = 0; j < (int)levels[i].size(); j++) {
                if (j) cout << ' ';
                cout << levels[i][j];
            }
            if (i + 1 < (int)levels.size()) cout << "\n";
        }
    }
    return 0;
}
