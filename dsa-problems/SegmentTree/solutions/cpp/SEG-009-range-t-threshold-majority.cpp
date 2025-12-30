#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <array>

using namespace std;

struct Summary {
    vector<pair<int, int>> candidates;
    static const int K = 40;
    
    void add(int val, int count) {
        for (auto& p : candidates) {
            if (p.first == val) {
                p.second += count;
                return;
            }
        }
        candidates.push_back({val, count});
        if (candidates.size() > K) {
            int minCnt = 2e9;
            for (auto& p : candidates) minCnt = min(minCnt, p.second);
            
            vector<pair<int, int>> next;
            for (auto& p : candidates) {
                p.second -= minCnt;
                if (p.second > 0) next.push_back(p);
            }
            candidates = next;
        }
    }
    
    void merge(const Summary& other) {
        for (const auto& p : other.candidates) {
            add(p.first, p.second);
        }
    }
};

class Solution {
    vector<Summary> tree;
    vector<vector<int>> positions;
    vector<int> idToVal;
    int n;

    void build(const vector<int>& a, int node, int start, int end) {
        if (start == end) {
            tree[node].add(a[start], 1);
        } else {
            int mid = (start + end) / 2;
            build(a, 2 * node + 1, start, mid);
            build(a, 2 * node + 2, mid + 1, end);
            
            tree[node] = Summary(); // Reset
            tree[node].merge(tree[2 * node + 1]);
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    Summary query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return Summary();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Summary s1 = query(2 * node + 1, start, mid, l, r);
        Summary s2 = query(2 * node + 2, mid + 1, end, l, r);
        
        s1.merge(s2);
        return s1;
    }

    int getFreq(int valId, int l, int r) {
        const auto& pos = positions[valId];
        auto it1 = lower_bound(pos.begin(), pos.end(), l);
        auto it2 = upper_bound(pos.begin(), pos.end(), r);
        return distance(it1, it2);
    }

public:
    vector<int> process(const vector<int>& arr, const vector<array<int,3>>& queries) {
        n = arr.size();
        
        // Coordinate Compression
        map<int, int> valToId;
        int idCounter = 0;
        vector<int> mappedArr(n);
        
        for (int x : arr) {
            if (valToId.find(x) == valToId.end()) {
                valToId[x] = idCounter++;
                idToVal.push_back(x);
                positions.push_back({});
            }
        }
        for (int i = 0; i < n; i++) {
            mappedArr[i] = valToId[arr[i]];
            positions[mappedArr[i]].push_back(i);
        }
        
        tree.assign(4 * n, Summary());
        build(mappedArr, 0, 0, n - 1);
        
        vector<int> results;
        for (const auto& q : queries) {
            int l = q[0];
            int r = q[1];
            int t = q[2];
            
            Summary s = query(0, 0, n - 1, l, r);
            vector<int> cands;
            for (auto& p : s.candidates) cands.push_back(p.first);
            for (int i = 0; i < 40; i++) cands.push_back(mappedArr[l + rand() % (r - l + 1)]);
            sort(cands.begin(), cands.end());
            cands.erase(unique(cands.begin(), cands.end()), cands.end());
            
            int bestVal = -1;
            int maxFreq = -1;
            
            for (int valId : cands) {
                int freq = getFreq(valId, l, r);
                if (freq >= t) {
                    int realVal = idToVal[valId];
                    if (freq > maxFreq) {
                        maxFreq = freq;
                        bestVal = realVal;
                    } else if (freq == maxFreq) {
                        if (bestVal == -1 || realVal < bestVal) {
                            bestVal = realVal;
                        }
                    }
                }
            }
            results.push_back(bestVal);
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
    vector<array<int, 3>> queries(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type; // MAJ
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2];
    }
    Solution sol;
    vector<int> results = sol.process(arr, queries);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
