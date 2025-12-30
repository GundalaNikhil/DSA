#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    vector<int> smallestRange(const vector<vector<int>>& lists) {
        vector<pair<int, int>> events;
        int k = lists.size();
        vector<int> required(k);
        
        for (int i = 0; i < k; i++) {
            if (lists[i].empty()) return {};
            required[i] = (lists[i].size() == 1) ? 1 : 2;
            for (int val : lists[i]) {
                events.push_back({val, i});
            }
        }
        
        sort(events.begin(), events.end());
        
        vector<int> counts(k, 0);
        int satisfied = 0;
        int left = 0;
        long long minLen = LLONG_MAX;
        vector<int> res;
        
        for (int right = 0; right < events.size(); right++) {
            int listId = events[right].second;
            counts[listId]++;
            
            if (counts[listId] == required[listId]) {
                satisfied++;
            }
            
            while (satisfied == k) {
                int startVal = events[left].first;
                int endVal = events[right].first;
                long long len = (long long)endVal - startVal;
                
                if (len < minLen) {
                    minLen = len;
                    res = {startVal, endVal};
                }
                
                int leftListId = events[left].second;
                if (counts[leftListId] == required[leftListId]) {
                    satisfied--;
                }
                counts[leftListId]--;
                left++;
            }
        }
        
        return res;
    }
};
