#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    vector<int> bit;
    int n;

    void update(int idx, int val) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += val;
    }

    int query(int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx) sum += bit[idx];
        return sum;
    }

public:
    vector<int> sortWithSwaps(const vector<int>& arr, long long S) {
        n = arr.size();
        queue<int> q0, q1, q2;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0) q0.push(i);
            else if (arr[i] == 1) q1.push(i);
            else q2.push(i);
        }

        bit.assign(n + 1, 0);
        for (int i = 0; i < n; i++) update(i + 1, 1);

        vector<int> res;
        res.reserve(n);

        for (int i = 0; i < n; i++) {
            int idx0 = q0.empty() ? -1 : q0.front();
            int idx1 = q1.empty() ? -1 : q1.front();
            int idx2 = q2.empty() ? -1 : q2.front();

            long long cost0 = (idx0 != -1) ? query(idx0) : LLONG_MAX;
            long long cost1 = (idx1 != -1) ? query(idx1) : LLONG_MAX;

            if (cost0 <= S) {
                S -= cost0;
                res.push_back(0);
                q0.pop();
                update(idx0 + 1, -1);
            } else if (cost1 <= S) {
                S -= cost1;
                res.push_back(1);
                q1.pop();
                update(idx1 + 1, -1);
            } else {
                int minIdx = INT_MAX;
                if (idx0 != -1) minIdx = min(minIdx, idx0);
                if (idx1 != -1) minIdx = min(minIdx, idx1);
                if (idx2 != -1) minIdx = min(minIdx, idx2);

                if (idx0 != -1 && minIdx == idx0) {
                    res.push_back(0); q0.pop(); update(idx0 + 1, -1);
                } else if (idx1 != -1 && minIdx == idx1) {
                    res.push_back(1); q1.pop(); update(idx1 + 1, -1);
                } else {
                    res.push_back(2); q2.pop(); update(idx2 + 1, -1);
                }
            }
        }
        return res;
    }
};
