#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> nextTallerWithin(const vector<int>& h, int w) {
        int n = h.size();
        vector<int> result(n, -1);
        stack<int> s; // Stores indices
        
        for (int i = n - 1; i >= 0; i--) {
            while (!s.empty() && h[s.top()] <= h[i]) {
                s.pop();
            }
            
            if (!s.empty()) {
                int j = s.top();
                if (j - i <= w) {
                    result[i] = h[j];
                } else {
                    result[i] = -1;
                }
            }
            
            s.push(i);
        }
        
        return result;
    }
};
