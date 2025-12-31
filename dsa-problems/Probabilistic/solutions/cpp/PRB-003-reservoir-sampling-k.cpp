#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> reservoirSample(int n, int k, unsigned long long seed) {
        if (k == 0) return {};
        if (k > n) k = n;

        vector<int> reservoir(k);
        for (int i = 0; i < k; i++) {
            reservoir[i] = i + 1;
        }

        unsigned long long state = seed;

        for (int i = k + 1; i <= n; i++) {
            state = state * 6364136223846793005ULL + 1;

            // Unsigned modulo works correctly in C++
            unsigned long long j = state % i;

            if (j < k) {
                reservoir[j] = i;
            }
        }

        return reservoir;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    unsigned long long seed;
    if (cin >> n >> k >> seed) {
        Solution solution;
        vector<int> res = solution.reservoirSample(n, k, seed);
        for (int i = 0; i < (int)res.size(); i++) {
            if (i) cout << " ";
            cout << res[i];
        }
        cout << "\n";
    }
    return 0;
}
