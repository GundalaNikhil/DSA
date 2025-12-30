#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>
using namespace std;

struct Item {
    int value;
    double score;
};

class Solution {
public:
    vector<int> topKWithDecay(vector<pair<int,int>>& events, int now, int D, int k) {
        unordered_map<int, double> scores;
        
        for (auto& p : events) {
            int v = p.first;
            int t = p.second;
            double term = exp(-(double)(now - t) / D);
            scores[v] += term;
        }
        
        vector<Item> items;
        items.reserve(scores.size());
        for (auto& entry : scores) {
            items.push_back({entry.first, entry.second});
        }
        
        // Sort: Descending Score, Ascending Value
        sort(items.begin(), items.end(), [](const Item& a, const Item& b) {
            if (abs(a.score - b.score) > 1e-9) {
                return a.score > b.score;
            }
            return a.value < b.value;
        });
        
        vector<int> result;
        for (int i = 0; i < k && i < items.size(); i++) {
            result.push_back(items[i].value);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<pair<int,int>> events(n);
    for (int i = 0; i < n; i++) cin >> events[i].first >> events[i].second;
    
    int now, D, k;
    cin >> now >> D >> k;

    Solution solution;
    vector<int> result = solution.topKWithDecay(events, now, D, k);
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
