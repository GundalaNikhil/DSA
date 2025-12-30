#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Point {
    long long num, den;
    int id;
    
    // operator< for "Better" (Smaller)
    bool operator<(const Point& other) const {
        // val1 = num/den, val2 = other.num/other.den
        // num * other.den < other.num * den
        // Use __int128 for safety if needed, but constraints say long long is enough (10^18)
        long long val1 = num * other.den;
        long long val2 = other.num * den;
        if (val1 != val2) return val1 < val2;
        return id < other.id;
    }
};

// Comparator for Max-Heap (we want "Worst" at top, i.e., Largest)
struct MaxHeapComp {
    bool operator()(const Point& a, const Point& b) {
        // Returns true if a < b (so b is at top)
        // We want "Larger" at top.
        // Standard priority_queue is Max-Heap using <.
        // So if a < b, b is considered "larger" and goes to top.
        // Our < defines "Better".
        // We want "Worse" at top.
        // Worse means Larger Dist or Larger ID.
        // So if a is Better than b, a < b.
        // Then b (Worse) is at top. Correct.
        return a < b;
    }
};

class Solution {
public:
    vector<string> processOperations(int k, const vector<vector<string>>& operations) {
        priority_queue<Point, vector<Point>, MaxHeapComp> pq;
        vector<string> results;
        int currentId = 1;
        
        for (const auto& op : operations) {
            if (op[0] == "ADD") {
                long long x = stoll(op[1]);
                long long y = stoll(op[2]);
                long long w = stoll(op[3]);
                Point p = {x * x + y * y, w, currentId++};
                
                if (pq.size() < k) {
                    pq.push(p);
                } else {
                    const Point& top = pq.top();
                    // If p is Better than top (p < top), replace
                    if (p < top) {
                        pq.pop();
                        pq.push(p);
                    }
                }
            } else {
                if (pq.empty()) {
                    results.push_back("EMPTY");
                } else {
                    vector<Point> temp;
                    // Copy heap
                    priority_queue<Point, vector<Point>, MaxHeapComp> copy = pq;
                    while (!copy.empty()) {
                        temp.push_back(copy.top());
                        copy.pop();
                    }
                    // Sort by Better (Ascending)
                    sort(temp.begin(), temp.end());
                    
                    string line = "";
                    for (size_t i = 0; i < temp.size(); i++) {
                        if (i > 0) line += " ";
                        line += to_string(temp[i].id);
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
    
    int q, k;
    if (cin >> q >> k) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "ADD") {
                string x, y, w;
                cin >> x >> y >> w;
                operations.push_back({op, x, y, w});
            } else {
                operations.push_back({op});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(k, operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
