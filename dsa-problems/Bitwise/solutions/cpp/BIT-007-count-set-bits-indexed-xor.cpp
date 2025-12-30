#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long countSetBitsIndexedXor(vector<int>& a) {
        long long total = 0;
        for (int i = 0; i < a.size(); i++) {
            // __builtin_popcount is a GCC/Clang intrinsic.
            // For standard C++20, use <bit> std::popcount
            total += __builtin_popcount(i ^ a[i]);
        }
        return total;
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
    cout << solution.countSetBitsIndexedXor(a) << "\n";
    return 0;
}
