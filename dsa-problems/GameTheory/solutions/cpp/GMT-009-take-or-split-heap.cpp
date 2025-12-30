#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string takeOrSplit(int n, vector<int>& heaps) {
        long long xorSum = 0;
        for (int x : heaps) {
            xorSum ^= (x - 1);
        }
        return xorSum > 0 ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> heaps(n);
        for (int i = 0; i < n; i++) {
            cin >> heaps[i];
        }
        
        Solution solution;
        cout << solution.takeOrSplit(n, heaps) << "\n";
    }
    return 0;
}
