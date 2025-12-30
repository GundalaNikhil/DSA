#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* mergeByParity(ListNode* l1, ListNode* l2) {
        ListNode evenDummy(0);
        ListNode oddDummy(0);
        ListNode* evenTail = &evenDummy;
        ListNode* oddTail = &oddDummy;

        ListNode* curr = l1;
        while (curr) {
            if (curr->val % 2 == 0) {
                evenTail->next = curr;
                evenTail = evenTail->next;
            } else {
                oddTail->next = curr;
                oddTail = oddTail->next;
            }
            curr = curr->next;
        }

        curr = l2;
        while (curr) {
            if (curr->val % 2 == 0) {
                evenTail->next = curr;
                evenTail = evenTail->next;
            } else {
                oddTail->next = curr;
                oddTail = oddTail->next;
            }
            curr = curr->next;
        }

        oddTail->next = nullptr;
        evenTail->next = oddDummy.next;

        return evenDummy.next;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    ListNode d1(0);
    ListNode* c1 = &d1;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        c1->next = new ListNode(v);
        c1 = c1->next;
    }
    
    int m;
    cin >> m;
    ListNode d2(0);
    ListNode* c2 = &d2;
    for (int i = 0; i < m; i++) {
        int v;
        cin >> v;
        c2->next = new ListNode(v);
        c2 = c2->next;
    }

    Solution solution;
    ListNode* res = solution.mergeByParity(d1.next, d2.next);
    
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
