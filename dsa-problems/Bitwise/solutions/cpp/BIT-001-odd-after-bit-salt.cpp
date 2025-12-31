#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long oddAfterBitSalt(vector<int>& a, int salt) {
        long long result = 0;
        for (int x : a) {
            result ^= (x ^ salt);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int salt;
    cin >> salt;
    
    Solution solution;
    cout << solution.oddAfterBitSalt(a, salt) << "\n";
    return 0;
}
