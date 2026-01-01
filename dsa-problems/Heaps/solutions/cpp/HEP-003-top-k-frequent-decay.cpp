#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

struct State {
    double count;
    int last_update;
    int version;
};

struct Entry {
    double count;
    string key;
    int version;
};

struct Cmp {
    bool operator()(const Entry& a, const Entry& b) const {
        if (abs(a.count - b.count) > 1e-9) {
            return a.count < b.count; // Max heap by count
        }
        return a.key > b.key; // Lexicographically smaller key
    }
};

class Solution {
public:
    vector<string> processOperations(int d, int k, const vector<vector<string>>& operations) {
        unordered_map<string, State> map;
        priority_queue<Entry, vector<Entry>, Cmp> pq;
        vector<string> results;
        
        for (const auto& op : operations) {
            if (op[0] == "ADD") {
                string key = op[1];
                int t = stoi(op[2]);
                
                double current_count = 0.0;
                if (map.find(key) != map.end()) {
                    State& s = map[key];
                    if (t >= s.last_update) {
                        int steps = (t - s.last_update) / d;
                        if (steps > 0) {
                            s.count *= pow(0.5, steps);
                        }
                    }
                    current_count = s.count;
                }
                
                double new_count = current_count + 1.0;
                int new_ver = (map.count(key) ? map[key].version + 1 : 1);
                
                State newState;
                newState.count = new_count;
                newState.last_update = t;
                newState.version = new_ver;
                map[key] = newState;
                
                pq.push({new_count, key, new_ver});
                
            } else {
                int t = stoi(op[1]);
                vector<string> top_k;
                vector<Entry> temp_back;
                
                while (top_k.size() < k && !pq.empty()) {
                    Entry e = pq.top();
                    pq.pop();
                    
                    if (map.find(e.key) == map.end() || map[e.key].version != e.version) {
                        continue;
                    }
                    
                    State& s = map[e.key];
                    int steps = 0;
                    if (t >= s.last_update) {
                        steps = (t - s.last_update) / d;
                    }
                    
                    if (steps > 0) {
                        s.count *= pow(0.5, steps);
                        s.last_update += steps * d;
                        s.version++;
                        
                        pq.push({s.count, e.key, s.version});
                    } else {
                        top_k.push_back(e.key);
                        temp_back.push_back(e);
                    }
                }
                
                if (top_k.empty()) {
                    results.push_back("EMPTY");
                } else {
                    string line = "";
                    for (int i = 0; i < top_k.size(); i++) {
                        if (i > 0) line += " ";
                        line += top_k[i];
                    }
                    results.push_back(line);
                }
                
                for (const auto& e : temp_back) {
                    pq.push(e);
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
