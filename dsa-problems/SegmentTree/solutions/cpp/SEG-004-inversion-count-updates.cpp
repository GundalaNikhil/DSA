#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
    long long mergeSort(vector<int>& arr, int l, int r) {
        if (l >= r) return 0;
        int mid = (l + r) / 2;
        long long count = mergeSort(arr, l, mid) + mergeSort(arr, mid + 1, r);
        
        vector<int> temp;
        temp.reserve(r - l + 1);
        int i = l, j = mid + 1;
        while (i <= mid && j <= r) {
            if (arr[i] <= arr[j]) {
                temp.push_back(arr[i++]);
            } else {
                temp.push_back(arr[j++]);
                count += (mid - i + 1);
            }
        }
        while (i <= mid) temp.push_back(arr[i++]);
        while (j <= r) temp.push_back(arr[j++]);
        for (int k = 0; k < temp.size(); k++) arr[l + k] = temp[k];
        return count;
    }

public:
    vector<long long> process(const vector<int>& inputArr, const vector<pair<int,int>>& updates) {
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
        
        vector<int> tempArr = arr;
        long long currentInversions = mergeSort(tempArr, 0, n - 1);
        
        vector<long long> results;
        results.reserve(updates.size());
        
        for (const auto& up : updates) {
            int idx = up.first;
            int val = up.second;
            int oldVal = arr[idx];
            
            if (val == oldVal) {
                results.push_back(currentInversions);
                continue;
            }
            
            int bIdx = idx / blockSize;
            
            // Remove oldVal
            // Left blocks
            for (int i = 0; i < bIdx; i++) {
                auto& b = blocks[i];
                auto it = upper_bound(b.begin(), b.end(), oldVal);
                currentInversions -= distance(it, b.end());
            }
            // Same block left
            int start = bIdx * blockSize;
            for (int i = start; i < idx; i++) {
                if (arr[i] > oldVal) currentInversions--;
            }
            // Same block right
            int end = min((bIdx + 1) * blockSize, n);
            for (int i = idx + 1; i < end; i++) {
                if (arr[i] < oldVal) currentInversions--;
            }
            // Right blocks
            for (int i = bIdx + 1; i < numBlocks; i++) {
                auto& b = blocks[i];
                auto it = lower_bound(b.begin(), b.end(), oldVal);
                currentInversions -= distance(b.begin(), it);
            }
            
            // Update
            arr[idx] = val;
            auto& block = blocks[bIdx];
            auto itRemoval = lower_bound(block.begin(), block.end(), oldVal);
            block.erase(itRemoval);
            auto itInsertion = lower_bound(block.begin(), block.end(), val);
            block.insert(itInsertion, val);
            
            // Add val
            // Left blocks
            for (int i = 0; i < bIdx; i++) {
                auto& b = blocks[i];
                auto it = upper_bound(b.begin(), b.end(), val);
                currentInversions += distance(it, b.end());
            }
            // Same block left
            for (int i = start; i < idx; i++) {
                if (arr[i] > val) currentInversions++;
            }
            // Same block right
            for (int i = idx + 1; i < end; i++) {
                if (arr[i] < val) currentInversions++;
            }
            // Right blocks
            for (int i = bIdx + 1; i < numBlocks; i++) {
                auto& b = blocks[i];
                auto it = lower_bound(b.begin(), b.end(), val);
                currentInversions += distance(b.begin(), it);
            }
            
            results.push_back(currentInversions);
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
    vector<pair<int, int>> updates(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type; // SET
        cin >> updates[i].first >> updates[i].second;
    }
    Solution sol;
    vector<long long> results = sol.process(arr, updates);
    for (long long res : results) {
        cout << res << "\n";
    }
    return 0;
}
