#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    long long intersectionSum(ListNode* headA, ListNode* headB) {
        int lenA = getLength(headA);
        int lenB = getLength(headB);

        ListNode* ptrA = headA;
        ListNode* ptrB = headB;

        while (lenA > lenB) {
            ptrA = ptrA->next;
            lenA--;
        }
        while (lenB > lenA) {
            ptrB = ptrB->next;
            lenB--;
        }

        while (ptrA != ptrB) {
            ptrA = ptrA->next;
            ptrB = ptrB->next;
        }

        if (!ptrA) return 0;

        long long sum = 0;
        while (ptrA) {
            sum += ptrA->val;
            ptrA = ptrA->next;
        }
        return sum;
    }

private:
    int getLength(ListNode* head) {
        int len = 0;
        while (head) {
            len++;
            head = head->next;
        }
        return len;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    ListNode dummyA(0);
    ListNode* curA = &dummyA;
    vector<ListNode*> nodesA;
    nodesA.reserve(n);
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        curA->next = new ListNode(v);
        curA = curA->next;
        nodesA.push_back(curA);
    }
    
    ListNode dummyB(0);
    ListNode* curB = &dummyB;
    vector<ListNode*> nodesB;
    nodesB.reserve(m);
    for (int i = 0; i < m; i++) {
        int v;
        cin >> v;
        curB->next = new ListNode(v);
        curB = curB->next;
        nodesB.push_back(curB);
    }
    
    int ia, ib;
    cin >> ia >> ib;
    if (ia >= 0 && ib >= 0 && n > 0 && m > 0) {
        nodesB[ib]->next = nodesA[ia];
    }

    Solution solution;
    cout << solution.intersectionSum(dummyA.next, dummyB.next) << "\n";
    return 0;
}
