#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> swapQueues(const vector<int>& q1, const vector<int>& q2) {
        return {q2, q1};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> q1(n), q2(n);
        for (int i = 0; i < n; i++) cin >> q1[i];
        for (int i = 0; i < n; i++) cin >> q2[i];
        
        Solution sol;
        vector<vector<int>> result = sol.swapQueues(q1, q2);
        for (const auto& resArr : result) {
            for (int i = 0; i < n; i++) {
                cout << (i ? " " : "") << resArr[i];
            }
            cout << endl;
        }
    }
    return 0;
}
