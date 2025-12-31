#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> spans(const vector<int>& counts) {
        int n = counts.size();
        vector<int> result(n);
        stack<int> s;
        
        for (int i = 0; i < n; i++) {
            while (!s.empty() && counts[s.top()] < counts[i]) {
                s.pop();
            }
            
            if (s.empty()) {
                result[i] = i + 1;
            } else {
                result[i] = i - s.top();
            }
            
            s.push(i);
        }
        return result;
    }
};
