#include <iostream>
class Solution {
public:
    int cyclicShiftEquivalenceClasses(vector<string>& strings) {
        unordered_set<string> canonicalSet;

        for (const string& s : strings) {
            string canonical = minimalRotation(s);
            canonicalSet.insert(canonical);
        }

        return canonicalSet.size();
    }

private:
    string minimalRotation(const string& s) {
        string doubled = s + s;
        int n = s.size();
        vector<int> failure(2 * n, -1);
        int k = 0;

        for (int j = 1; j < 2 * n; j++) {
            int i = failure[j - k - 1];
            while (i != -1 && doubled[j] != doubled[k + i + 1]) {
                if (doubled[j] < doubled[k + i + 1]) {
                    k = j - i - 1;
                }
                i = failure[i];
            }

            if (doubled[j] != doubled[k + i + 1]) {
                if (doubled[j] < doubled[k + i + 1]) {
                    k = j;
                }
                failure[j - k] = -1;
            } else {
                failure[j - k] = i + 1;
            }
        }

        return s.substr(k) + s.substr(0, k);
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int strings_n; cin >> strings_n; vector<string> strings(strings_n); for(int i=0; i<strings_n; i++) cin >> strings[i];
    Solution sol;
    cout << sol.cyclicShiftEquivalenceClasses(strings) << endl;
    return 0;
}
