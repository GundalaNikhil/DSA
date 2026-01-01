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
    int longestChunkedDecomposition(string s, int L) {
        int n = s.size();
        int left = 0, right = n - 1;
        int chunks = 0;

        while (left < right) {
            bool matched = false;
            int maxLen = min(L, (right - left + 1) / 2);

            for (int len = 1; len <= maxLen; len++) {
                string leftChunk = s.substr(left, len);
                string rightChunk = s.substr(right - len + 1, len);

                if (leftChunk == rightChunk) {
                    chunks += 2;
                    left += len;
                    right -= len;
                    matched = true;
                    break;
                }
            }

            if (!matched) {
                break;
            }
        }

        // Add middle chunk if exists
        if (left <= right) {
            chunks++;
        }

        return chunks;
    }
};

















int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int L; cin >> L;
    Solution sol;
    cout << sol.longestChunkedDecomposition(s, L) << endl;
    return 0;
}
