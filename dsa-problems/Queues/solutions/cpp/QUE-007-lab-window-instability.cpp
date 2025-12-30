#include <iostream>
#include <vector>
#include <deque>
#include <set>

using namespace std;

class Solution {
public:
    vector<long long> windowInstability(const vector<int>& values, int k) {
        int n = values.size();
        vector<long long> result;
        deque<int> minD, maxD;
        
        // Use multiset for median (simplest in C++ as it supports deletion)
        // Two multisets: small (max), large (min)
        multiset<int> small, large;
        
        auto balance = [&]() {
            while (small.size() > large.size() + 1) {
                large.insert(*small.rbegin());
                small.erase(prev(small.end()));
            }
            while (large.size() > small.size()) {
                small.insert(*large.begin());
                large.erase(large.begin());
            }
        };
        
        auto add = [&](int val) {
            small.insert(val);
            large.insert(*small.rbegin());
            small.erase(prev(small.end()));
            balance();
        };
        
        auto remove = [&](int val) {
            auto it = small.find(val);
            if (it != small.end()) {
                small.erase(it);
            } else {
                large.erase(large.find(val));
            }
            balance();
        };
        
        for (int i = 0; i < n; i++) {
            // Min/Max Deques
            while (!minD.empty() && minD.front() <= i - k) minD.pop_front();
            while (!minD.empty() && values[minD.back()] >= values[i]) minD.pop_back();
            minD.push_back(i);
            
            while (!maxD.empty() && maxD.front() <= i - k) maxD.pop_front();
            while (!maxD.empty() && values[maxD.back()] <= values[i]) maxD.pop_back();
            maxD.push_back(i);
            
            // Median
            add(values[i]);
            if (i >= k) remove(values[i - k]);
            
            if (i >= k - 1) {
                int minVal = values[minD.front()];
                int maxVal = values[maxD.front()];
                int med = *small.rbegin();
                if (med == 0) result.push_back(0);
                else {
                    long long diff = (long long)maxVal - minVal;
                    long long instability = diff / med;
                    if (diff % med != 0 && ((diff ^ med) < 0)) {
                        instability--;
                    }
                    result.push_back(instability);
                }
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        vector<int> values(n);
        for (int i = 0; i < n; i++) {
            cin >> values[i];
        }
    
        Solution solution;
        vector<long long> result = solution.windowInstability(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
