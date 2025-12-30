#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    int findFirstIndex(ListNode* head, int target) {
        ListNode* current = head;
        int index = 0;
        while (current != nullptr) {
            if (current->val == target) {
                return index;
            }
            current = current->next;
            index++;
        }
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    ListNode dummy(0);
    ListNode* cur = &dummy;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    
    int target;
    cin >> target;

    Solution solution;
    cout << solution.findFirstIndex(dummy.next, target) << "\n";
    return 0;
}
