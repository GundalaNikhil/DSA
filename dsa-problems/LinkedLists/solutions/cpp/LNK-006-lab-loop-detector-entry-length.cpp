#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    vector<int> cycleInfo(ListNode* head) {
        if (!head) return {-1, 0, 0};

        ListNode* slow = head;
        ListNode* fast = head;
        bool hasCycle = false;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }

        if (!hasCycle) return {-1, 0, 0};

        ListNode* entry = head;
        int entryIndex = 0;
        while (entry != slow) {
            entry = entry->next;
            slow = slow->next;
            entryIndex++;
        }

        int length = 0;
        int maxVal = INT_MIN;
        ListNode* curr = entry;
        do {
            length++;
            maxVal = max(maxVal, curr->val);
            curr = curr->next;
        } while (curr != entry);

        return {entryIndex, length, maxVal};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    ListNode dummy(0);
    ListNode* cur = &dummy;
    vector<ListNode*> nodes;
    nodes.reserve(n);
    
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        cur->next = new ListNode(v);
        cur = cur->next;
        nodes.push_back(cur);
    }
    
    int pos;
    cin >> pos;
    if (pos >= 0 && n > 0) {
        cur->next = nodes[pos];
    }

    Solution solution;
    vector<int> res = solution.cycleInfo(dummy.next);
    cout << res[0] << " " << res[1] << " " << res[2] << "\n";
    return 0;
}
