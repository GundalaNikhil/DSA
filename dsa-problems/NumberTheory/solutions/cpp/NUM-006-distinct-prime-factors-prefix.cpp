#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> buildPrefixDistinct(int N) {
        vector<int> f(N + 1, 0);
        
        for (int i = 2; i <= N; i++) {
            if (f[i] == 0) { // i is prime
                for (int j = i; j <= N; j += i) {
                    f[j]++;
                }
            }
        }
        
        vector<long long> pref(N + 1, 0);
        for (int i = 1; i <= N; i++) {
            pref[i] = pref[i - 1] + f[i];
        }
        
        return pref;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, q;
    if (cin >> N >> q) {
        Solution solution;
        vector<long long> pref = solution.buildPrefixDistinct(N);
        
        for (int i = 0; i < q; i++) {
            int l, r;
            cin >> l >> r;
            cout << pref[r] - pref[l - 1] << "\n";
        }
    }
    return 0;
}
