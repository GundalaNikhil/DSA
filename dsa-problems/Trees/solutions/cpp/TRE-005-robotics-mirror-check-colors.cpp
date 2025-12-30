#include <iostream>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

class Solution {
    bool checkMirror(int u, int v, const vector<int>& values, const vector<int>& left, const vector<int>& right) {
        if (u == -1 && v == -1) return true;
        if (u == -1 || v == -1) return false;
        if (values[u] != values[v]) return false;
        return checkMirror(left[u], right[v], values, left, right) &&
               checkMirror(right[u], left[v], values, left, right);
    }

public:
    bool mirrorCheck(int n, const vector<int>& values, const vector<int>& colors,
                     const vector<int>& left, const vector<int>& right) {
        if (n == 0) return true;
        
        if (left[0] == -1 && right[0] == -1) return true;
        if (!checkMirror(left[0], right[0], values, left, right)) return false;
        
        // Color Check
        queue<int> qL, qR;
        qL.push(left[0]);
        qR.push(right[0]);
        
        while (!qL.empty() && !qR.empty()) {
            if (qL.size() != qR.size()) return false;
            
            int size = qL.size();
            long long sumL = 0;
            for (int i = 0; i < size; i++) {
                int u = qL.front(); qL.pop();
                sumL += colors[u];
                if (left[u] != -1) qL.push(left[u]);
                if (right[u] != -1) qL.push(right[u]);
            }
            
            long long sumR = 0;
            for (int i = 0; i < size; i++) {
                int v = qR.front(); qR.pop();
                sumR += colors[v];
                if (left[v] != -1) qR.push(left[v]);
                if (right[v] != -1) qR.push(right[v]);
            }
            
            if (sumL != sumR) return false;
        }
        
        return qL.empty() && qR.empty();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), colors(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> colors[i] >> left[i] >> right[i];
    }

    Solution solution;
    cout << (solution.mirrorCheck(n, values, colors, left, right) ? "true" : "false") << "\n";
    return 0;
}
