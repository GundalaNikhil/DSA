class Solution {
public:
    int minimalDeleteKPeriodic(string s, int k) {
        int n = s.size();
        int deletions = 0;

        for (int pos = 0; pos < k; pos++) {
            unordered_map<char, int> freq;

            // Count frequency at positions pos, pos+k, pos+2k, ...
            for (int i = pos; i < n; i += k) {
                freq[s[i]]++;
            }

            // Keep most frequent, delete others
            if (!freq.empty()) {
                int maxFreq = 0;
                int totalAtPos = 0;
                for (auto& [c, f] : freq) {
                    maxFreq = max(maxFreq, f);
                    totalAtPos += f;
                }
                deletions += totalAtPos - maxFreq;
            }
        }

        return deletions;
    }
};
