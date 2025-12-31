#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> interleaveQueue(const vector<int>& values) {
        int n = values.size();
        int mid = n / 2;
        vector<int> result(n);
        
        for (int i = 0; i < mid; i++) {
            result[2 * i] = values[i];
            result[2 * i + 1] = values[mid + i];
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
    
        Solution solution;
        vector<int> result = solution.interleaveQueue(values);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
