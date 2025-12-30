#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* head = nullptr;
    ListNode* tail = nullptr;

    void pushBack(int value) {
        ListNode* newNode = new ListNode(value);
        if (!head) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    vector<int> toArray() {
        vector<int> result;
        ListNode* current = head;
        while (current) {
            result.push_back(current->val);
            current = current->next;
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    string dummy;
    getline(cin, dummy);

    Solution solution;
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        if (line.rfind("push_back", 0) == 0) {
            stringstream ss(line);
            string op;
            int value;
            ss >> op >> value;
            solution.pushBack(value);
        } else {
            vector<int> arr = solution.toArray();
            for (int j = 0; j < (int)arr.size(); j++) {
                if (j) cout << " ";
                cout << arr[j];
            }
            cout << "\n";
        }
    }
    return 0;
}
