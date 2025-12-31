#include <iostream>
#include <vector>
#include <string>
#include <deque>

using namespace std;

class Solution {
public:
    vector<string> rateLimit(const vector<long long>& times, long long t, int k) {
        deque<long long> q;
        vector<string> result;
        result.reserve(times.size());
        
        for (long long time : times) {
            // Remove expired requests
            while (!q.empty() && q.front() < time - t) {
                q.pop_front();
            }
            
            if (q.size() < k) {
                q.push_back(time);
                result.push_back("true");
            } else {
                result.push_back("false");
            }
        }
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k;
    long long t;
    if (cin >> n >> t >> k) {
        vector<long long> times(n);
        for (int i = 0; i < n; i++) cin >> times[i];
        
        Solution sol;
        vector<string> results = sol.rateLimit(times, t, k);
        for (int i = 0; i < (int)results.size(); i++) {
            cout << (i ? " " : "") << results[i];
        }
        cout << endl;
    }
    return 0;
}
