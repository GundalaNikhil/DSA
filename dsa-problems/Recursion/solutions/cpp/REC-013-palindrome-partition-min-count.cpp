#include <vector>
#include <string>
#include <climits>

using namespace std;

class Solution {
public:
    vector<vector<string>> minPalindromePartitions(const string& s, int L) {
        int n = s.length();
        vector<vector<bool>> isPal(n, vector<bool>(n, false));
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                if (s[i] == s[j]) {
                    if (len <= 2 || isPal[i + 1][j - 1]) {
                        isPal[i][j] = true;
                    }
                }
            }
        }

        vector<vector<string>> results;
        int minCount = INT_MAX;
        vector<string> current;
        
        backtrack(0, s, L, isPal, current, results, minCount);
        return results;
    }

private:
    void backtrack(int start, const string& s, int L, const vector<vector<bool>>& isPal, 
                   vector<string>& current, vector<vector<string>>& results, int& minCount) {
        if (start == s.length()) {
            if ((int)current.size() < minCount) {
                minCount = current.size();
                results.clear();
                results.push_back(current);
            } else if ((int)current.size() == minCount) {
                results.push_back(current);
            }
            return;
        }

        if ((int)current.size() >= minCount) return;

        for (int end = start; end < s.length(); end++) {
            if (end - start + 1 > L) break;
            if (isPal[start][end]) {
                current.push_back(s.substr(start, end - start + 1));
                backtrack(end + 1, s, L, isPal, current, results, minCount);
                current.pop_back();
            }
        }
    }
};
