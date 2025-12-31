#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

struct Block {
    vector<long long> sorted;
    long long lazy;
};

class Solution {
    vector<long long> arr;
    vector<Block> blocks;
    int blockSize;
    int n;

    void update(int l, int r, long long x) {
        int startBlock = l / blockSize;
        int endBlock = r / blockSize;

        if (startBlock == endBlock) {
            partialUpdate(startBlock, l, r, x);
        } else {
            partialUpdate(startBlock, l, (startBlock + 1) * blockSize - 1, x);
            for (int i = startBlock + 1; i < endBlock; i++) {
                blocks[i].lazy += x;
            }
            partialUpdate(endBlock, endBlock * blockSize, r, x);
        }
    }

    void partialUpdate(int bIdx, int l, int r, long long x) {
        Block& b = blocks[bIdx];
        int start = bIdx * blockSize;
        int end = min(n, start + blockSize);

        if (b.lazy != 0) {
            for (int i = start; i < end; i++) arr[i] += b.lazy;
            b.lazy = 0;
        }

        for (int i = l; i <= r; i++) arr[i] += x;

        b.sorted.clear();
        for (int i = start; i < end; i++) b.sorted.push_back(arr[i]);
        sort(b.sorted.begin(), b.sorted.end());
    }

    int countLessEqual(int l, int r, long long val) {
        int count = 0;
        int startBlock = l / blockSize;
        int endBlock = r / blockSize;

        if (startBlock == endBlock) {
            long long lazy = blocks[startBlock].lazy;
            for (int i = l; i <= r; i++) {
                if (arr[i] + lazy <= val) count++;
            }
        } else {
            long long lazyStart = blocks[startBlock].lazy;
            for (int i = l; i < (startBlock + 1) * blockSize; i++) {
                if (arr[i] + lazyStart <= val) count++;
            }

            for (int i = startBlock + 1; i < endBlock; i++) {
                long long target = val - blocks[i].lazy;
                auto it = upper_bound(blocks[i].sorted.begin(), blocks[i].sorted.end(), target);
                count += distance(blocks[i].sorted.begin(), it);
            }

            long long lazyEnd = blocks[endBlock].lazy;
            for (int i = endBlock * blockSize; i <= r; i++) {
                if (arr[i] + lazyEnd <= val) count++;
            }
        }
        return count;
    }

public:
    vector<long long> process(const vector<long long>& inputArr, const vector<vector<string>>& ops) {
        arr = inputArr;
        n = arr.size();
        blockSize = sqrt(n * log2(n + 1)) + 1;
        if (blockSize < 100) blockSize = 100;

        int numBlocks = (n + blockSize - 1) / blockSize;
        blocks.assign(numBlocks, Block());

        for (int i = 0; i < numBlocks; i++) {
            int start = i * blockSize;
            int end = min(n, start + blockSize);
            blocks[i].lazy = 0;
            for (int j = start; j < end; j++) {
                blocks[i].sorted.push_back(arr[j]);
            }
            sort(blocks[i].sorted.begin(), blocks[i].sorted.end());
        }

        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "ADD") {
                update(stoi(op[1]), stoi(op[2]), stoll(op[3]));
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                int k = stoi(op[3]);
                
                long long low = -2e14, high = 2e14;
                long long ans = high;
                
                while (low <= high) {
                    long long mid = low + (high - low) / 2;
                    if (countLessEqual(l, r, mid) >= k) {
                        ans = mid;
                        high = mid - 1;
                    } else {
                        low = mid + 1;
                    }
                }
                results.push_back(ans);
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
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        string a, b, c;
        cin >> a >> b >> c;
        ops[i] = {type, a, b, c};
    }
    Solution sol;
    vector<long long> results = sol.process(arr, ops);
    for (long long res : results) {
        cout << res << "\n";
    }
    return 0;
}
