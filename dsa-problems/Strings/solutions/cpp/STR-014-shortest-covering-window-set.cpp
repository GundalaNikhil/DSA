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
