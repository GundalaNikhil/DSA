#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
    bool found = false;

    void checkRightChain(int u, long long turnLeftSum, const unordered_set<long long>& prefixes,
                         const vector<long long>& values, const vector<int>& right, long long target) {
        long long currentRightSum = 0;
        int curr = u;
        while (curr != -1 && !found) {
            currentRightSum += values[curr];
            long long needed = turnLeftSum + currentRightSum - target;
            if (prefixes.count(needed)) {
                found = true;
                return;
            }
            curr = right[curr];
        }
    }

    void dfs(int u, long long currentLeftSum, unordered_set<long long>& prefixes,
             const vector<long long>& values, const vector<int>& left, const vector<int>& right,
             long long target, bool isStart) {
        if (u == -1 || found) return;

        long long val = values[u];
        long long nextSum = currentLeftSum + val;

        if (!isStart) {
            checkRightChain(right[u], nextSum, prefixes, values, right, target);
        }
        if (found) return;

        prefixes.insert(currentLeftSum);
        dfs(left[u], nextSum, prefixes, values, left, right, target, false);
        prefixes.erase(currentLeftSum);

        if (found) return;

        // Start new chain for right child
        unordered_set<long long> newPrefixes;
        dfs(right[u], 0, newPrefixes, values, left, right, target, true);
    }

public:
    bool hasOneTurnPath(int n, const vector<long long>& values,
                        const vector<int>& left, const vector<int>& right, long long target) {
        if (n == 0) return false;
        found = false;
        unordered_set<long long> prefixes;
        dfs(0, 0, prefixes, values, left, right, target, true);
        return found;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> values(n);
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }
    long long target;
    cin >> target;

    Solution solution;
    cout << (solution.hasOneTurnPath(n, values, left, right, target) ? "true" : "false") << "\n";
    return 0;
}
