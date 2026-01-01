#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
    long long minTotalSlack(vector<vector<int>>& meetings, int k, int s) {
        sort(meetings.begin(), meetings.end());
        
        map<int, int> rooms;
        int usedRooms = 0;
        
        long long totalSlack = 0;
        
        for (const auto& m : meetings) {
            int start = m[0];
            int end = m[1];
            
            auto it = rooms.upper_bound(start);
            if (it != rooms.begin()) {
                it--;
                int freeTime = it->first;
                totalSlack += (long long)(start - freeTime);
                
                if (it->second == 1) rooms.erase(it);
                else it->second--;
                
                rooms[end + s]++;
            } else {
                if (usedRooms < k) {
                    usedRooms++;
                    rooms[end + s]++;
                } else {
                    // Should not happen if k is sufficient as per problem constraints/guarantees?
                    // Or maybe we treat it as infinite slack/invalid? The problem implies K is sufficient.
                }
            }
        }
        
        return totalSlack;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k, s;
    if (cin >> n >> k >> s) {
        vector<vector<int>> meetings(n, vector<int>(2));
        for (int i = 0; i < n; i++) {
            cin >> meetings[i][0] >> meetings[i][1];
        }
        
        Solution solution;
        cout << solution.minTotalSlack(meetings, k, s) << "\n";
    }
    return 0;
}
