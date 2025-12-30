#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> rotateQueue(const vector<int>& values, long long k) {
        int n = values.size();
        if (n == 0) return {};
        
        int rotations = k % n;
        if (rotations == 0) return values;
        
        vector<int> result;
        result.reserve(n);
        
        // Append second part
        for (int i = rotations; i < n; i++) {
            result.push_back(values[i]);
        }
        // Append first part
        for (int i = 0; i < rotations; i++) {
            result.push_back(values[i]);
        }
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> values(n);
        for (int i = 0; i < n; i++) {
            cin >> values[i];
        }
        long long k;
        cin >> k;
    
        Solution solution;
        vector<int> result = solution.rotateQueue(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
