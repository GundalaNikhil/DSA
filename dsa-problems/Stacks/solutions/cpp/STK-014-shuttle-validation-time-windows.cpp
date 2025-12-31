#include <vector>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    bool validate(const vector<int>& push, const vector<long long>& pushT, const vector<int>& pop, const vector<long long>& popT,
                  const unordered_map<int,long long>& windows, const unordered_set<int>& priority) {
        int n = push.size();
        stack<int> s;
        stack<long long> timeStack;
        stack<int> minPriorityStack;
        
        int j = 0;
        for (int i = 0; i < n; i++) {
            int val = push[i];
            long long time = pushT[i];
            
            s.push(val);
            timeStack.push(time);
            
            int currentMin = minPriorityStack.empty() ? INT_MAX : minPriorityStack.top();
            if (priority.count(val)) {
                currentMin = min(currentMin, val);
            }
            minPriorityStack.push(currentMin);
            
            while (!s.empty() && j < n && s.top() == pop[j]) {
                int poppedVal = s.top(); s.pop();
                long long pushedTime = timeStack.top(); timeStack.pop();
                minPriorityStack.pop();
                
                long long poppedTime = popT[j];
                
                // Check Time
                if (windows.count(poppedVal)) {
                    if (poppedTime - pushedTime > windows.at(poppedVal)) {
                        return false;
                    }
                }
                
                // Check Priority
                if (!priority.count(poppedVal)) {
                    int minP = minPriorityStack.empty() ? INT_MAX : minPriorityStack.top();
                    if (poppedVal > minP) {
                        return false;
                    }
                }
                
                j++;
            }
        }
        
        return s.empty();
    }
};
