#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Query {
    string type;
    int l, r;
    long long x;
};

class Solution {
public:
    vector<long long> processTemperatureQueries(vector<int>& temps, vector<Query>& queries) {
        int n = temps.size();
        vector<long long> diff(n + 1, 0);
        vector<Query*> sumQueries;
        
        // 1. Process Updates
        for (auto& q : queries) {
            if (q.type == "add") {
                diff[q.l] += q.x;
                if (q.r + 1 < n) {
                    diff[q.r + 1] -= q.x;
                }
            } else {
                sumQueries.push_back(&q);
            }
        }
        
        // 2. Reconstruct & Build Prefix
        vector<long long> P(n + 1, 0);
        long long currentAdd = 0;
        
        for (int i = 0; i < n; i++) {
            currentAdd += diff[i];
            long long finalVal = temps[i] + currentAdd;
            P[i + 1] = P[i] + finalVal;
        }
        
        // 3. Answer Sums
        vector<long long> results;
        results.reserve(sumQueries.size());
        for (auto* q : sumQueries) {
            results.push_back(P[q->r + 1] - P[q->l]);
        }
        
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> temps(n);
    for (int i = 0; i < n; i++) cin >> temps[i];
    
    int q;
    cin >> q;
    vector<Query> queries;
    queries.reserve(q);
    
    for (int i = 0; i < q; i++) {
        Query query;
        cin >> query.type >> query.l >> query.r;
        if (query.type == "add") cin >> query.x;
        else query.x = 0;
        queries.push_back(query);
    }

    Solution solution;
    vector<long long> result = solution.processTemperatureQueries(temps, queries);
    
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
