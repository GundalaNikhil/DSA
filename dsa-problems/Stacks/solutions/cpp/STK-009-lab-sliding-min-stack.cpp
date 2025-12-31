#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    vector<int> tree;
    int n = 100005;
    int currentSize = 0;
    vector<int> stackVals;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return INT_MAX;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return min(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
    }

public:
    vector<string> process(const vector<vector<string>>& ops) {
        vector<string> result;
        tree.assign(4 * n, INT_MAX);
        currentSize = 0;
        stackVals.clear();
        
        for (const auto& op : ops) {
            string cmd = op[0];
            if (cmd == "PUSH") {
                int val = stoi(op[1]);
                stackVals.push_back(val);
                update(1, 0, n - 1, currentSize, val);
                currentSize++;
            } else if (cmd == "POP") {
                if (currentSize == 0) {
                    result.push_back("EMPTY");
                } else {
                    result.push_back(to_string(stackVals.back()));
                    stackVals.pop_back();
                    currentSize--;
                }
            } else if (cmd == "MIN") {
                int k = stoi(op[1]);
                if (currentSize < k) {
                    result.push_back("NA");
                } else {
                    int minVal = query(1, 0, n - 1, currentSize - k, currentSize - 1);
                    result.push_back(to_string(minVal));
                }
            }
        }
        return result;
    }
};
