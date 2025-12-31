#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 31;

public:
    int longestCommonSubstring(string a, string b) {
        int low = 0, high = min(a.length(), b.length());
        int ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            if (check(a, b, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

    bool check(const string& a, const string& b, int len) {
        unordered_set<long long> hashesA;
        long long currentHash = 0;
        long long power = 1;

        // Precompute BASE^(len-1)
        for (int i = 0; i < len - 1; i++) {
            power = (power * BASE) % MOD;
        }

        // Hash A
        for (int i = 0; i < len; i++) {
            currentHash = (currentHash * BASE + a[i]) % MOD;
        }
        hashesA.insert(currentHash);

        for (int i = len; i < a.length(); i++) {
            long long remove = (a[i - len] * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            currentHash = (currentHash * BASE + a[i]) % MOD;
            hashesA.insert(currentHash);
        }

        // Check B
        currentHash = 0;
        for (int i = 0; i < len; i++) {
            currentHash = (currentHash * BASE + b[i]) % MOD;
        }
        if (hashesA.count(currentHash)) return true;

        for (int i = len; i < b.length(); i++) {
            long long remove = (b[i - len] * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            currentHash = (currentHash * BASE + b[i]) % MOD;
            if (hashesA.count(currentHash)) return true;
        }

        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (getline(cin, a) && getline(cin, b)) {
        Solution solution;
        cout << solution.longestCommonSubstring(a, b) << "\n";
    }

    return 0;
}
