#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> mergeStreams(const vector<vector<int>>& streams, int r) {
        int k = streams.size();
        vector<int> indices(k, 0);
        vector<int> usage(k, 0);
        
        // Min-heap: {value, stream_index}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        for (int i = 0; i < k; i++) {
            if (!streams[i].empty()) {
                pq.push({streams[i][0], i});
                indices[i]++;
            }
        }
        
        vector<int> result;
        vector<int> blocked;
        
        while (!pq.empty()) {
            auto [val, sIdx] = pq.top();
            pq.pop();
            result.push_back(val);
            
            usage[sIdx]++;
            
            if (usage[sIdx] < r) {
                if (indices[sIdx] < streams[sIdx].size()) {
                    pq.push({streams[sIdx][indices[sIdx]], sIdx});
                    indices[sIdx]++;
                }
            } else {
                blocked.push_back(sIdx);
            }
            
            if (pq.empty() && !blocked.empty()) {
                for (int idx : blocked) {
                    usage[idx] = 0;
                    if (indices[idx] < streams[idx].size()) {
                        pq.push({streams[idx][indices[idx]], idx});
                        indices[idx]++;
                    }
                }
                blocked.clear();
            }
        }
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int k, r;
    if (cin >> k >> r) {
        vector<vector<int>> streams(k);
        for (int i = 0; i < k; i++) {
            int m;
            cin >> m;
            streams[i].resize(m);
            for (int j = 0; j < m; j++) {
                cin >> streams[i][j];
            }
        }
        
        Solution solution;
        vector<int> result = solution.mergeStreams(streams, r);
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
