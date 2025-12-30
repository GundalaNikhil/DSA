class Solution {
public:
    bool canRotateToPalindrome(string s) {
        if (s.empty() || s.size() <= 1) return true;

        // Count character frequencies
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Count characters with odd frequency
        int oddCount = 0;
        for (auto& [c, count] : freq) {
            if (count % 2 == 1) {
                oddCount++;
            }
        }

        return oddCount <= 1;
    }
};
