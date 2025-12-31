#include <iostream>
#include <numeric>

using namespace std;

class Solution {
    long long gcd(long long a, long long b) {
        while (b) {
            a %= b;
            swap(a, b);
        }
        return a;
    }

public:
    bool hasInverse(long long a, long long m) {
        return gcd(a, m) == 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (cin >> q) {
        Solution solution;
        for (int i = 0; i < q; i++) {
            long long a, m;
            cin >> a >> m;
            cout << (solution.hasInverse(a, m) ? "true" : "false") << "\n";
        }
    }
    return 0;
}
