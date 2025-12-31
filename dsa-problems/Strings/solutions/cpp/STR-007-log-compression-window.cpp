class Solution {
public:
    string compressWithWindow(string s, int w) {
        if (s.empty()) {
            return "";
        }

        string result;
        int i = 0;
        int n = s.size();

        while (i < n) {
            int start = i;
            char ch = s[i];

            // Count consecutive occurrences
            while (i < n && s[i] == ch) {
                i++;
            }

            int runLength = i - start;

            // Compress if >= threshold
            if (runLength >= w) {
                result += ch;
                result += to_string(runLength);
            } else {
                result.append(runLength, ch);
            }
        }

        return result;
    }
};
