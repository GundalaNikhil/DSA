#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    long long countCoprimePairs(int N) {
        if (N < 2) return 0;
        
        vector<int> phi(N + 1);
        for (int i = 0; i <= N; i++) phi[i] = i;
        
        for (int i = 2; i <= N; i++) {
            if (phi[i] == i) { // i is prime
                for (int j = i; j <= N; j += i) {
                    phi[j] -= phi[j] / i;
                }
            }
        }
        
        long long total = 0;
        for (int i = 2; i <= N; i++) {
            total += phi[i];
        }
        
        return total;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (cin >> N) {
        Solution solution;
        cout << solution.countCoprimePairs(N) << "\n";
    }
    return 0;
}
