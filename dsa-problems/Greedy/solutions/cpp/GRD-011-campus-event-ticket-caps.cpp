#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maxTickets(int n, vector<pair<int,int>>& requests) {
        // Sort by deadline (second element)
        sort(requests.begin(), requests.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
            return a.second < b.second;
        });
        
        priority_queue<int, vector<int>, greater<int>> pq;
        long long total = 0;
        
        for (const auto& req : requests) {
            int quantity = req.first;
            int deadline = req.second;
            
            pq.push(quantity);
            total += quantity;
            
            if (pq.size() > deadline) {
                total -= pq.top();
                pq.pop();
            }
        }
        
        return total;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<int,int>> requests(n);
    for (int i = 0; i < n; i++) {
        cin >> requests[i].first >> requests[i].second;
    }

    Solution solution;
    cout << solution.maxTickets(n, requests) << "\n";

    return 0;
}
