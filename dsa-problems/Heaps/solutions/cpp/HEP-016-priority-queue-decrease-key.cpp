#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

struct Node {
    string id;
    long long value;
};

class Solution {
    vector<Node> heap;
    unordered_map<string, int> pos;
    
    bool less(int i, int j) {
        if (heap[i].value != heap[j].value) {
            return heap[i].value < heap[j].value;
        }
        return heap[i].id < heap[j].id;
    }
    
    void swapNodes(int i, int j) {
        swap(heap[i], heap[j]);
        pos[heap[i].id] = i;
        pos[heap[j].id] = j;
    }
    
    void bubbleUp(int k) {
        while (k > 0) {
            int p = (k - 1) / 2;
            if (less(k, p)) {
                swapNodes(k, p);
                k = p;
            } else {
                break;
            }
        }
    }
    
    void bubbleDown(int k) {
        int n = heap.size();
        while (true) {
            int left = 2 * k + 1;
            if (left >= n) break;
            int child = left;
            int right = left + 1;
            if (right < n && less(right, left)) {
                child = right;
            }
            if (less(child, k)) {
                swapNodes(k, child);
                k = child;
            } else {
                break;
            }
        }
    }

public:
    vector<string> processOperations(const vector<vector<string>>& operations) {
        vector<string> results;
        heap.clear();
        pos.clear();
        
        for (const auto& op : operations) {
            if (op[0] == "INSERT") {
                string id = op[1];
                long long val = stoll(op[2]);
                heap.push_back({id, val});
                pos[id] = heap.size() - 1;
                bubbleUp(heap.size() - 1);
            } else if (op[0] == "DECREASE") {
                string id = op[1];
                long long delta = stoll(op[2]);
                if (pos.count(id)) {
                    int idx = pos[id];
                    heap[idx].value -= delta;
                    bubbleUp(idx);
                }
            } else if (op[0] == "EXTRACT") {
                if (heap.empty()) {
                    results.push_back("EMPTY");
                } else {
                    Node minNode = heap[0];
                    results.push_back(to_string(minNode.value) + " " + minNode.id);
                    
                    pos.erase(minNode.id);
                    Node last = heap.back();
                    heap.pop_back();
                    
                    if (!heap.empty()) {
                        heap[0] = last;
                        pos[last.id] = 0;
                        bubbleDown(0);
                    }
                }
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q;
    if (cin >> q) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "INSERT") {
                string id, val;
                cin >> id >> val;
                operations.push_back({op, id, val});
            } else if (op == "DECREASE") {
                string id, delta;
                cin >> id >> delta;
                operations.push_back({op, id, delta});
            } else {
                operations.push_back({op});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
