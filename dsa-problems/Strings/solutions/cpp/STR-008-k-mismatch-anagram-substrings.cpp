#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
class Solution {
public:
    int countKMismatchAnagrams(string s, string p, int k) {
        int m = p.size();
        int n = s.size();

        if (n < m) return 0;

        // Build pattern frequency
        vector<int> freqP(26, 0);
        for (char c : p) {
            freqP[c - 'a']++;
        }

        // Initialize window frequency
        vector<int> freqWindow(26, 0);
        for (int i = 0; i < m; i++) {
            freqWindow[s[i] - 'a']++;
        }

        auto mismatchCost = [](const vector<int>& fw, const vector<int>& fp) {
            int cost = 0;
            for (int i = 0; i < 26; i++) {
                if (fp[i] > fw[i]) {
                    cost += fp[i] - fw[i];
                }
            }
            return cost;
        };

        int count = 0;

        // Check first window
        if (mismatchCost(freqWindow, freqP) <= k) {
            count++;
        }

        // Slide window
        for (int i = 1; i <= n - m; i++) {
            // Remove leftmost
            freqWindow[s[i - 1] - 'a']--;
            // Add rightmost
            freqWindow[s[i + m - 1] - 'a']++;

            if (mismatchCost(freqWindow, freqP) <= k) {
                count++;
            }
        }

        return count;
    }
};

















int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    string p; cin >> p;
    int k; cin >> k;
    Solution sol;
    cout << sol.countKMismatchAnagrams(s, p, k) << endl;
    return 0;
}
