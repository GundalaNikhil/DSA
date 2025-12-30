#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
    vector<int> memo; // 0: unknown, 1: Win, 2: Loss

    bool canWin(int n) {
        if (memo[n] != 0) return memo[n] == 1;

        bool canReachLosing = false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                int d1 = i;
                if (!canWin(d1)) {
                    canReachLosing = true;
                    break;
                }
                int d2 = n / i;
                if (d2 < n) {
                    if (!canWin(d2)) {
                        canReachLosing = true;
                        break;
                    }
                }
            }
        }

        memo[n] = canReachLosing ? 1 : 2;
        return canReachLosing;
    }

public:
    string divisorGame(int n) {
        memo.assign(n + 1, 0);
        return canWin(n) ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (cin >> n) {
        Solution solution;
        cout << solution.divisorGame(n) << "\n";
    }
    return 0;
}
