#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> spans(const vector<int>& demand) {
        int n = demand.size();
        vector<int> result(n);
        stack<int> s; // Stores indices
        
        for (int i = 0; i < n; i++) {
            while (!s.empty() && demand[s.top()] < demand[i]) {
                s.pop();
            }
            
            int prevIdx = s.empty() ? -1 : s.top();
            result[i] = i - prevIdx - 1;
            
            s.push(i);
        }
        return result;
    }
};
