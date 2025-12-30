#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> buildDeque(const vector<int>& values) {
        vector<int> result;
        int n = values.size();
        result.reserve(n);
        
        int left = 0;
        int right = n - 1;
        
        while (left <= right) {
            result.push_back(values[left]);
            if (left != right) {
                result.push_back(values[right]);
            }
            left++;
            right--;
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
        for (int i = 0; i < n; i++) cin >> values[i];
        
        Solution sol;
        vector<int> result = sol.buildDeque(values);
        for (int i = 0; i < (int)result.size(); i++) {
            cout << (i ? " " : "") << result[i];
        }
        cout << endl;
    }
    return 0;
}
