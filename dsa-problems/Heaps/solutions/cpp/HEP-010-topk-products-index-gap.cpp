#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

struct Node {
    long long val;
    int r, c;
    int dir;
    
    bool operator<(const Node& other) const {
        return val < other.val; // Max heap
    }
};

class Solution {
    void tryAdd(priority_queue<Node>& pq, set<pair<int,int>>& visited, const vector<long long>& A, const vector<long long>& B, int r, int c, int dir, int d) {
        if (r >= 0 && r < A.size() && c >= 0 && c < B.size()) {
            if (abs(r - c) >= d) {
                if (visited.find({r, c}) == visited.end()) {
                    visited.insert({r, c});
                    pq.push({A[r] * B[c], r, c, dir});
                }
            }
        }
    }
    
public:
    vector<long long> topKProducts(const vector<long long>& A, const vector<long long>& B, int k, int d) {
        int n = A.size();
        int m = B.size();
        priority_queue<Node> pq;
        set<pair<int,int>> visited;
        
        // TL
        if (d < n) tryAdd(pq, visited, A, B, d, 0, 1, d);
        if (d < m && d > 0) tryAdd(pq, visited, A, B, 0, d, 1, d);
        else if (d == 0) tryAdd(pq, visited, A, B, 0, 0, 1, d);
        
        // BR
        if (d < n) {
            int startI = n - 1;
            int startJ = min(m - 1, n - 1 - d);
            if (startJ >= 0) tryAdd(pq, visited, A, B, startI, startJ, -1, d);
        }
        if (d < m && d > 0) {
            int startJ = m - 1;
            int startI = min(n - 1, m - 1 - d);
            if (startI >= 0) tryAdd(pq, visited, A, B, startI, startJ, -1, d);
        }
        
        vector<long long> res;
        while (k > 0 && !pq.empty()) {
            Node node = pq.top();
            pq.pop();
            res.push_back(node.val);
            k--;
            
            if (node.dir == 1) {
                tryAdd(pq, visited, A, B, node.r + 1, node.c, 1, d);
                tryAdd(pq, visited, A, B, node.r, node.c + 1, 1, d);
            } else {
                tryAdd(pq, visited, A, B, node.r - 1, node.c, -1, d);
                tryAdd(pq, visited, A, B, node.r, node.c - 1, -1, d);
            }
        }
        
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m, k, d;
    if (cin >> n >> m >> k >> d) {
        vector<long long> A(n), B(m);
        for (int i = 0; i < n; i++) cin >> A[i];
        for (int i = 0; i < m; i++) cin >> B[i];
        
        Solution solution;
        vector<long long> result = solution.topKProducts(A, B, k, d);
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
