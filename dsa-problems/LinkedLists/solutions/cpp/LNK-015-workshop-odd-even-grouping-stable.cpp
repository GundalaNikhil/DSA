#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* groupOddEvenStable(ListNode* head) {
        ListNode oddDummy(0);
        ListNode evenDummy(0);
        ListNode* oddTail = &oddDummy;
        ListNode* evenTail = &evenDummy;

        ListNode* curr = head;
        while (curr) {
            if (curr->val % 2 != 0) {
                oddTail->next = curr;
                oddTail = oddTail->next;
            } else {
                evenTail->next = curr;
                evenTail = evenTail->next;
            }
            curr = curr->next;
        }

        evenTail->next = nullptr;
        oddTail->next = evenDummy.next;

        return oddDummy.next;
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

    Solution solution;
    ListNode* res = solution.groupOddEvenStable(dummy.next);
    
    bool first = true;
    while (res) {
        if (!first) cout << " ";
        cout << res->val;
        first = false;
        res = res->next;
    }
    cout << "\n";
    return 0;
}
