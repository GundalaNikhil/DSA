#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string kthMissingString(const vector<string>& insertedList, int L, int k) {
        unordered_set<string> inserted(insertedList.begin(), insertedList.end());
        vector<string> allStrings;

        for (char c = 'a'; c <= 'z'; c++) {
            string prefix(1, c);
            if (L >= 1 && inserted.find(prefix) == inserted.end()) {
                allStrings.push_back(prefix);
            }
            for (int length = 2; length <= L; length++) {
                generateCombinations(prefix, length - 1, inserted, allStrings);
            }
        }

        if (k <= static_cast<int>(allStrings.size())) {
            return allStrings[k - 1];
        }
        return "";
    }

private:
    void generateCombinations(const string& prefix, int remaining,
                              const unordered_set<string>& inserted,
                              vector<string>& result) {
        if (remaining == 0) {
            if (inserted.find(prefix) == inserted.end()) {
                result.push_back(prefix);
            }
            return;
        }
        for (char c = 'a'; c <= 'z'; c++) {
            generateCombinations(prefix + c, remaining - 1, inserted, result);
        }
    }
};

int main() {
    int n, L, k;
    if (!(cin >> n >> L >> k)) {
        return 0;
    }

    vector<string> inserted(n);
    for (int i = 0; i < n; i++) {
        cin >> inserted[i];
    }

    Solution solution;
    string result = solution.kthMissingString(inserted, L, k);

    cout << result << '\n';
    return 0;
}
