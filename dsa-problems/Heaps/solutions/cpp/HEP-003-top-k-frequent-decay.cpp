#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>
#include <queue>

using namespace std;

struct State {
    double count;
    int bucket;
    double score;
    int version;
};

struct Entry {
    string key;
    double score;
    int version;
};

struct Cmp {
    bool operator()(const Entry& a, const Entry& b) const {
        if (a.score == b.score) return a.key > b.key;
        return a.score < b.score;
    }
};

class Solution {
public:
    vector<string> processOperations(int d, int k, const vector<vector<string>>& operations) {
        unordered_map<string, State> map;
        priority_queue<Entry, vector<Entry>, Cmp> pq;
        vector<string> results;
        const double LN2 = log(2.0);
        
        for (const auto& op : operations) {
            if (op[0] == "ADD") {
                string key = op[1];
                int t = stoi(op[2]);

                int bucket = t / d;
                State state;
                auto it = map.find(key);
                if (it == map.end()) {
                    state.count = 0.0;
                    state.bucket = bucket;
                    state.version = 0;
                } else {
                    state = it->second;
                    if (bucket > state.bucket) {
                        int diff = bucket - state.bucket;
                        state.count *= pow(0.5, diff);
                    }
                }
                state.count += 1.0;
                state.bucket = bucket;
                state.score = log(state.count) + state.bucket * LN2;
                state.version++;
                map[key] = state;
                pq.push({key, state.score, state.version});
            } else {
                vector<Entry> used;
                vector<string> out;
                while (!pq.empty() && (int)out.size() < k) {
                    Entry e = pq.top();
                    pq.pop();
                    auto it = map.find(e.key);
                    if (it == map.end() || it->second.version != e.version) {
                        continue;
                    }
                    out.push_back(e.key);
                    used.push_back(e);
                }
                for (const auto& e : used) pq.push(e);
                if (out.empty()) {
                    results.push_back("EMPTY");
                } else {
                    string line;
                    for (int i = 0; i < (int)out.size(); i++) {
                        if (i) line += " ";
                        line += out[i];
                    }
                    results.push_back(line);
                }
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q, d, k;
    if (cin >> q >> d >> k) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "ADD") {
                string key, t;
                cin >> key >> t;
                operations.push_back({op, key, t});
            } else {
                string t;
                cin >> t;
                operations.push_back({op, t});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(d, k, operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
