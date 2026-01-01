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

    int n;
    if (cin >> n) {
        vector<long long> remaining;
        long long val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<long long> times;
        long long t = 1;
        int k = 1;

        // If we have exactly n remaining values
        if ((int)remaining.size() == n) {
            times.assign(remaining.begin(), remaining.end());
            t = 1;
            k = 1;
        } else if ((int)remaining.size() == n + 2) {
            // First two are t and k
            t = remaining[0];
            k = (int)remaining[1];
            times.assign(remaining.begin() + 2, remaining.begin() + n + 2);
        } else {
            // Fallback
            if (!remaining.empty()) {
                t = remaining[0];
            }
            if (remaining.size() > 1) {
                k = (int)remaining[1];
            }
            int start = 2;
            for (int i = start; i < start + n && i < (int)remaining.size(); i++) {
                times.push_back(remaining[i]);
            }
        }

        Solution sol;
        vector<string> results = sol.rateLimit(times, t, k);
        for (int i = 0; i < (int)results.size(); i++) {
            cout << (i ? " " : "") << results[i];
        }
        cout << endl;
    }
    return 0;
}
