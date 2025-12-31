class Solution {
public:
    string minimalUniqueRotation(string s) {
        int n = s.size();

        // Booth's algorithm
        int minIdx = boothMinimalRotationIndex(s);
        string minRotation = s.substr(minIdx) + s.substr(0, minIdx);

        // Check if same as original
        if (minRotation == s) {
            return s;
        } else {
            return minRotation;
        }
    }

private:
    int boothMinimalRotationIndex(const string& s) {
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

        return k;
    }
};
