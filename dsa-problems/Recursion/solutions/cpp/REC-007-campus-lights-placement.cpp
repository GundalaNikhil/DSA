#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> placeLights(int n, int k, int d) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(0, 0, n, k, d, current, result);
        return result;
    }

private:
    void backtrack(int start_pos, int lights_placed, int n, int k, int d, vector<int>& current, vector<vector<int>>& result) {
        if (lights_placed == k) {
            result.push_back(current);
            return;
        }

        // Pruning
        int remaining_lights = k - lights_placed;
        int remaining_positions = n - start_pos;
        if (remaining_positions < remaining_lights) return;

        for (int pos = start_pos; pos < n; ++pos) {
            // Check constraint
            if (current.empty() || pos - current.back() >= d) {
                current.push_back(pos);
                // Python: backtrack(pos + 1, ...)
                // But wait, the constraint check handles 'd'.
                // Python loop iterates pos.
                // Constraint `pos - last >= d`.
                // If I place at pos, next recurse must start at pos + 1?
                // Python calls `backtrack(pos + 1, ...)`
                // AND relies on `if not current or pos - current[-1] >= d` check in loop.
                // Correct.
                backtrack(pos + 1, lights_placed + 1, n, k, d, current, result);
                current.pop_back();
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, k, d;
    if (!(cin >> n >> k >> d)) return 0;
    
    Solution sol;
    vector<vector<int>> res = sol.placeLights(n, k, d);
    
    if (res.empty()) {
        cout << "NONE" << endl;
    } else {
        for(const auto& row : res) { 
            for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?"":" "); 
            cout << endl; 
        }
    }
    return 0;
}
