#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int countUnsafe(vector<int>& d) {
        int count = 0;
        int n = d.size();
        for (int i = 0; i < n - 1; i++) {
            if (d[i+1] > d[i]) {
                count++;
            }
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> d(n);
    for (int i = 0; i < n; i++) {
        cin >> d[i];
    }
    
    Solution sol;
    cout << sol.countUnsafe(d) << endl;
    
    return 0;
}
