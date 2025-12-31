#include <iostream>
#include <vector>

using namespace std;

class Solution {
    const int MOD = 1000000007;
public:
    long long rangeSigma(int L, int R) {
        vector<long long> sigma(R + 1, 0);
        
        for (int i = 1; i <= R; i++) {
            for (int j = i; j <= R; j += i) {
                sigma[j] += i;
            }
        }
        
        long long total = 0;
        for (int i = L; i <= R; i++) {
            total = (total + sigma[i]) % MOD;
        }
        
        return total;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int L, R;
    if (cin >> L >> R) {
        Solution solution;
        cout << solution.rangeSigma(L, R) << "\n";
    }
    return 0;
}
