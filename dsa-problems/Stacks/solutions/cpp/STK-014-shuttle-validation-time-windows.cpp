#include <iostream>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <climits>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool validate(vector<int>& push, vector<int>& pushT,
                 vector<int>& pop, vector<int>& popT,
                 map<int, int>& windows, set<int>& priority) {
        
        stack<int> st;
        stack<int> timeStack;
        stack<int> minPriorityStack;
        
        int j = 0;
        int n = push.size();
        
        for (int i = 0; i < n; i++) {
            int val = push[i];
            int t = pushT[i];
            
            st.push(val);
            timeStack.push(t);
            
            int currentMin = minPriorityStack.empty() ? INT_MAX : minPriorityStack.top();
            if (priority.count(val)) {
                currentMin = min(currentMin, val);
            }
            minPriorityStack.push(currentMin);
            
            while (!st.empty() && j < n && st.top() == pop[j]) {
                int poppedVal = st.top(); st.pop();
                int pushedTime = timeStack.top(); timeStack.pop();
                minPriorityStack.pop();
                
                int poppedTime = popT[j];
                
                // Check Time Window
                if (windows.count(poppedVal)) {
                    if (poppedTime - pushedTime > windows[poppedVal]) {
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
        
        return st.empty();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int numPush;
    if (!(cin >> numPush)) return 0;
    
    vector<int> push(numPush);
    vector<int> pushT(numPush);
    for (int i = 0; i < numPush; i++) {
        cin >> push[i] >> pushT[i];
    }
    
    int numPop;
    cin >> numPop;
    vector<int> pop(numPop);
    vector<int> popT(numPop);
    for (int i = 0; i < numPop; i++) {
        cin >> pop[i] >> popT[i];
    }
    
    int numWindows;
    cin >> numWindows;
    map<int, int> windows;
    for (int i = 0; i < numWindows; i++) {
        int k, v;
        cin >> k >> v;
        windows[k] = v;
    }
    
    int numPriority;
    cin >> numPriority;
    set<int> priority;
    for (int i = 0; i < numPriority; i++) {
        int val;
        cin >> val;
        priority.insert(val);
    }
    
    Solution sol;
    cout << (sol.validate(push, pushT, pop, popT, windows, priority) ? "YES" : "NO") << endl;
    
    return 0;
}
