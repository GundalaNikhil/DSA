#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> secondMinimums(const vector<int>& values, int k) {
        int n = values.size();
        vector<int> result;
        multiset<int> window;
        
        for (int i = 0; i < n; i++) {
            window.insert(values[i]);
            if (i >= k) {
                window.erase(window.find(values[i - k]));
            }
            
            if (i >= k - 1) {
                if (k == 1) {
                    result.push_back(*window.begin());
                } else {
                    auto it = window.begin();
                    it++; // Move to second
                    result.push_back(*it);
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
        vector<int> result = solution.secondMinimums(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
