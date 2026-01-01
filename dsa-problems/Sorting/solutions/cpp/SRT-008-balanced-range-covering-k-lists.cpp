#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    vector<vector<int>> lists;
    lists.reserve(k);
    for (int i = 0; i < k; i++) {
        int m;
        cin >> m;
        vector<int> list(m);
        for (int j = 0; j < m; j++) {
            cin >> list[j];
        }
        lists.push_back(list);
    }
    Solution solution;
    vector<int> result = solution.smallestRange(lists);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        cout << result[0] << " " << result[1] << "\n";
    }
    return 0;
}
