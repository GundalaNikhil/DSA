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
    pair<int, vector<string>> shortestCoveringWindow(vector<string>& arr, unordered_set<string>& T) {
        if (arr.empty() || T.empty()) {
            return {0, {}};
        }

        unordered_map<string, int> required;
        for (const string& s : T) {
            required[s] = 1;
        }

        unordered_map<string, int> windowCounts;
        int left = 0, formed = 0;
        int minLen = INT_MAX;
        int resultLeft = 0, resultRight = 0;

        for (int right = 0; right < arr.size(); right++) {
            string s = arr[right];
            windowCounts[s]++;

            if (required.count(s) && windowCounts[s] == 1) {
                formed++;
            }

            while (formed == (int)T.size() && left <= right) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    resultLeft = left;
                    resultRight = right;
                }

                string leftS = arr[left];
                windowCounts[leftS]--;
                if (required.count(leftS) && windowCounts[leftS] == 0) {
                    formed--;
                }

                left++;
            }
        }

        if (minLen == INT_MAX) {
            return {0, {}};
        }

        vector<string> resultWindow(arr.begin() + resultLeft, arr.begin() + resultRight + 1);
        return {minLen, resultWindow};
    }
};

















int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int arr_n; cin >> arr_n; vector<string> arr(arr_n); for(int i=0; i<arr_n; i++) cin >> arr[i];
    int T_n; cin >> T_n; unordered_set<string> T; for(int i=0; i<T_n; i++) { string s; cin >> s; T.insert(s); }
    Solution sol;
    pair<int, vector<string>> res = sol.shortestCoveringWindow(arr, T); cout << res.first << endl; for(const string& s : res.second) cout << s << endl; if(res.second.empty()) cout << "NONE" << endl;
    return 0;
}
