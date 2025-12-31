#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> firstNegatives(const vector<int>& values, int k) {
        int n = values.size();
        vector<int> result;
        deque<int> q; // Stores indices
        
        for (int i = 0; i < n; i++) {
            if (values[i] < 0) {
                q.push_back(i);
            }
            
            if (!q.empty() && q.front() <= i - k) {
                q.pop_front();
            }
            
            if (i >= k - 1) {
                if (q.empty()) {
                    result.push_back(0);
                } else {
                    result.push_back(values[q.front()]);
                }
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        vector<int> values(n);
        for (int i = 0; i < n; i++) {
            cin >> values[i];
        }
    
        Solution solution;
        vector<int> result = solution.firstNegatives(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
