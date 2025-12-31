#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Node {
    int val;
    int queueIndex;
    
    // Min-heap: greater value means lower priority
    bool operator>(const Node& other) const {
        return val > other.val;
    }
};

class Solution {
public:
    vector<int> mergeQueues(vector<vector<int>>& queues) {
        priority_queue<Node, vector<Node>, greater<Node>> pq;
        vector<int> indices(queues.size(), 0);
        
        for (int i = 0; i < queues.size(); i++) {
            if (!queues[i].empty()) {
                pq.push({queues[i][0], i});
            }
        }
        
        vector<int> result;
        int lastVal = -1;
        int count = 0;
        
        while (!pq.empty()) {
            Node best = pq.top();
            pq.pop();
            
            if (!result.empty() && best.val == lastVal && count == 2) {
                // Blocked
                vector<Node> temp;
                temp.push_back(best);
                
                bool found = false;
                while (!pq.empty()) {
                    Node next = pq.top();
                    pq.pop();
                    if (next.val != lastVal) {
                        // Found valid
                        result.push_back(next.val);
                        lastVal = next.val;
                        count = 1;
                        
                        indices[next.queueIndex]++;
                        if (indices[next.queueIndex] < queues[next.queueIndex].size()) {
                            pq.push({queues[next.queueIndex][indices[next.queueIndex]], next.queueIndex});
                        }
                        found = true;
                        break;
                    } else {
                        temp.push_back(next);
                    }
                }
                
                // Push back temp
                for (const auto& node : temp) {
                    pq.push(node);
                }
                
                if (!found) break; // Deadlock
                
            } else {
                // Valid
                result.push_back(best.val);
                if (!result.empty() && best.val == lastVal) {
                    count++;
                } else {
                    lastVal = best.val;
                    count = 1;
                }
                
                indices[best.queueIndex]++;
                if (indices[best.queueIndex] < queues[best.queueIndex].size()) {
                    pq.push({queues[best.queueIndex][indices[best.queueIndex]], best.queueIndex});
                }
            }
        }
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    vector<vector<int>> queues(k);
    for (int i = 0; i < k; i++) {
        int len;
        cin >> len;
        queues[i].resize(len);
        for (int j = 0; j < len; j++) {
            cin >> queues[i][j];
        }
    }

    Solution solution;
    vector<int> result = solution.mergeQueues(queues);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << "\n";

    return 0;
}
