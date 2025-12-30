#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<long long> computePrefixHashes(string s, long long B, long long M) {
        vector<long long> hashes;
        hashes.reserve(s.length());

        long long currentHash = 0;

        for (char c : s) {
            // (currentHash * B) can exceed 2^63-1 if M is large (~10^18)
            // But constraints say M <= 10^9 + 7, so long long is safe.
            currentHash = (currentHash * B + c) % M;
            hashes.push_back(currentHash);
        }

        return hashes;
    }
};

int main() {
    // Fast I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    long long B, M;

    if (getline(cin, s)) {
        if (cin >> B >> M) {
            Solution solution;
            vector<long long> result = solution.computePrefixHashes(s, B, M);

            for (int i = 0; i < result.size(); i++) {
                cout << result[i];
                if (i < result.size() - 1) cout << " ";
            }
            cout << "\n";
        }
    }

    return 0;
}
