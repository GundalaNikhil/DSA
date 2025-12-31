#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

struct Result {
    int sign;
    ListNode* head;
    vector<int> freq;
};

class Solution {
public:
    Result subtractWithFreq(ListNode* a, ListNode* b) {
        int lenA = getLength(a);
        int lenB = getLength(b);
        ListNode *large = a, *small = b;

        if (lenA < lenB) {
            large = b; small = a;
        } else if (lenA == lenB) {
            ListNode *currA = a, *currB = b;
            while (currA && currA->val == currB->val) {
                currA = currA->next;
                currB = currB->next;
            }
            if (!currA) return {0, new ListNode(0), {1,0,0,0,0,0,0,0,0,0}};
            if (currA->val < currB->val) {
                large = b; small = a;
            }
        }

        stack<int> s1, s2;
        ListNode* curr = large;
        while (curr) { s1.push(curr->val); curr = curr->next; }
        curr = small;
        while (curr) { s2.push(curr->val); curr = curr->next; }

        ListNode* head = nullptr;
        int borrow = 0;

        while (!s1.empty()) {
            int v1 = s1.top(); s1.pop();
            int v2 = 0;
            if (!s2.empty()) { v2 = s2.top(); s2.pop(); }

            int diff = v1 - v2 - borrow;
            if (diff < 0) {
                diff += 10;
                borrow = 1;
            } else {
                borrow = 0;
            }

            ListNode* node = new ListNode(diff);
            node->next = head;
            head = node;
        }

        while (head && head->val == 0 && head->next) {
            ListNode* temp = head;
            head = head->next;
            delete temp;
        }

        vector<int> freq(10, 0);
        curr = head;
        while (curr) {
            freq[curr->val]++;
            curr = curr->next;
        }

        return {1, head, freq};
    }

private:
    int getLength(ListNode* head) {
        int len = 0;
        while (head) { len++; head = head->next; }
        return len;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    ListNode dummyA(0);
    ListNode* curA = &dummyA;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        curA->next = new ListNode(v);
        curA = curA->next;
    }
    int m;
    cin >> m;
    ListNode dummyB(0);
    ListNode* curB = &dummyB;
    for (int i = 0; i < m; i++) {
        int v;
        cin >> v;
        curB->next = new ListNode(v);
        curB = curB->next;
    }

    Solution solution;
    Result res = solution.subtractWithFreq(dummyA.next, dummyB.next);
    cout << res.sign << "\n";
    ListNode* out = res.head;
    bool first = true;
    while (out) {
        if (!first) cout << " ";
        cout << out->val;
        first = false;
        out = out->next;
    }
    cout << "\n";
    for (int i = 0; i < 10; i++) {
        cout << res.freq[i] << (i < 9 ? " " : "");
    }
    cout << "\n";
    return 0;
}
