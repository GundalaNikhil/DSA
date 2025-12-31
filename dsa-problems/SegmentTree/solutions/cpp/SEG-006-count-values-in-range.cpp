#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> process(const vector<int>& inputArr, const vector<vector<string>>& ops) {
        vector<int> arr = inputArr;
        int n = arr.size();
        int blockSize = sqrt(n * log2(n + 1)) + 1;
        if (blockSize < 50) blockSize = 50;
        
        int numBlocks = (n + blockSize - 1) / blockSize;
        vector<vector<int>> blocks(numBlocks);
        
        for (int i = 0; i < n; i++) {
            blocks[i / blockSize].push_back(arr[i]);
        }
        for (auto& b : blocks) sort(b.begin(), b.end());
        
        vector<int> results;
        
        for (const auto& op : ops) {
            if (op[0] == "SET") {
                int idx = stoi(op[1]);
                int val = stoi(op[2]);
                int oldVal = arr[idx];
                arr[idx] = val;
                
                auto& block = blocks[idx / blockSize];
                auto it = lower_bound(block.begin(), block.end(), oldVal);
                block.erase(it);
                auto it2 = upper_bound(block.begin(), block.end(), val);
                block.insert(it2, val);
                
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                int x = stoi(op[3]);
                int y = stoi(op[4]);
                
                int count = 0;
                int startBlock = l / blockSize;
                int endBlock = r / blockSize;
                
                if (startBlock == endBlock) {
                    for (int i = l; i <= r; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                } else {
                    for (int i = l; i < (startBlock + 1) * blockSize; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                    for (int i = startBlock + 1; i < endBlock; i++) {
                        const auto& b = blocks[i];
                        auto upper = upper_bound(b.begin(), b.end(), y);
                        auto lower = lower_bound(b.begin(), b.end(), x);
                        count += distance(lower, upper);
                    }
                    for (int i = endBlock * blockSize; i <= r; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                }
                results.push_back(count);
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        if (type == "SET") {
            string i_str, x_str;
            cin >> i_str >> x_str;
            ops[i] = {type, i_str, x_str};
        } else {
            string l_str, r_str, x_str, y_str;
            cin >> l_str >> r_str >> x_str >> y_str;
            ops[i] = {type, l_str, r_str, x_str, y_str};
        }
    }
    Solution sol;
    vector<int> results = sol.process(arr, ops);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
