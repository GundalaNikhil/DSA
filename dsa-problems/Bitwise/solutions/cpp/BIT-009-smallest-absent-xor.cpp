#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long smallestAbsentXor(vector<int>& a) {
        vector<int> basis(32, 0);
        
        for (int x : a) {
            for (int i = 30; i >= 0; i--) {
                if ((x >> i) & 1) {
                    if (basis[i] == 0) {
                        basis[i] = x;
                        break;
                    }
                    x ^= basis[i];
                }
            }
        }
        
        for (int i = 0; i <= 30; i++) {
            if (basis[i] == 0) {
                return (1LL << i);
            }
        }
        return (1LL << 31);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    cout << solution.smallestAbsentXor(a) << "\n";
    return 0;
}
