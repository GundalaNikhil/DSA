#include <iostream>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> reverseFirstK(const vector<int>& values, int k) {
        queue<int> q;
        for (int v : values) q.push(v);
        
        stack<int> s;
        
        // 1. Dequeue first K and push to stack
        for (int i = 0; i < k; i++) {
            s.push(q.front());
            q.pop();
        }
        
        // 2. Pop from stack and enqueue
        while (!s.empty()) {
            q.push(s.top());
            s.pop();
        }
        
        // 3. Rotate remaining N-K elements
        int n = values.size();
        for (int i = 0; i < n - k; i++) {
            q.push(q.front());
            q.pop();
        }
        
        vector<int> result;
        while (!q.empty()) {
            result.push_back(q.front());
            q.pop();
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> values(n);
        for (int i = 0; i < n; i++) {
            cin >> values[i];
        }
        int k;
        cin >> k;
    
        Solution solution;
        vector<int> result = solution.reverseFirstK(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
