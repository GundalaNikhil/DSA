#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

class Solution {
    vector<long long> bit;
    int n;
    long long mod;

    void add(int idx, long long val) {
        idx++; // 1-based
        for (; idx <= n; idx += idx & -idx) {
            bit[idx] = (bit[idx] + val) % mod;
            if (bit[idx] < 0) bit[idx] += mod;
        }
    }

    long long query(int idx) {
        idx++;
        long long sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum = (sum + bit[idx]) % mod;
        }
        return sum;
    }

public:
    vector<long long> process(const vector<int>& arr, long long mod, const vector<vector<string>>& ops) {
        this->n = arr.size();
        this->mod = mod;
        bit.assign(n + 1, 0);

        // Build BIT
        for (int i = 0; i < n; i++) {
            add(i, (long long)arr[i] % mod);
        }

        vector<long long> currentArr(n);
        for(int i=0; i<n; i++) currentArr[i] = (long long)arr[i] % mod;

        stack<pair<int, long long>> history;
        vector<long long> results;

        for (const auto& op : ops) {
            if (op[0] == "UPDATE") {
                int idx = stoi(op[1]);
                long long val = stoll(op[2]) % mod;
                if (val < 0) val += mod;

                long long oldVal = currentArr[idx];
                history.push({idx, oldVal});

                long long diff = (val - oldVal) % mod;
                if (diff < 0) diff += mod;

                add(idx, diff);
                currentArr[idx] = val;

            } else if (op[0] == "QUERY") {
                int l = stoi(op[1]);
                int r = stoi(op[2]);

                long long res = (query(r) - query(l - 1)) % mod;
                if (res < 0) res += mod;
                results.push_back(res);

            } else if (op[0] == "UNDO") {
                int k = stoi(op[1]);
                while (k > 0 && !history.empty()) {
                    auto last = history.top();
                    history.pop();
                    int idx = last.first;
                    long long oldVal = last.second;

                    long long currentVal = currentArr[idx];
                    long long diff = (oldVal - currentVal) % mod;
                    if (diff < 0) diff += mod;

                    add(idx, diff);
                    currentArr[idx] = oldVal;
                    k--;
                }
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    long long mod;
    if (!(cin >> n >> q >> mod)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        if (type == "UNDO") {
            string k;
            cin >> k;
            ops[i] = {type, k};
        } else {
            string a, b;
            cin >> a >> b;
            ops[i] = {type, a, b};
        }
    }
    Solution sol;
    vector<long long> results = sol.process(arr, mod, ops);
    for (long long res : results) {
        cout << res << "\n";
    }
    return 0;
}
