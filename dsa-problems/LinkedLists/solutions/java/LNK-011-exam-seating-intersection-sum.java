import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public long intersectionSum(ListNode headA, ListNode headB) {
        int lenA = getLength(headA);
        int lenB = getLength(headB);

        ListNode ptrA = headA;
        ListNode ptrB = headB;

        // Align pointers
        while (lenA > lenB) {
            ptrA = ptrA.next;
            lenA--;
        }
        while (lenB > lenA) {
            ptrB = ptrB.next;
            lenB--;
        }

        // Find intersection
        while (ptrA != ptrB) {
            ptrA = ptrA.next;
            ptrB = ptrB.next;
        }

        // ptrA is now intersection or null
        if (ptrA == null) return 0;

        // Sum suffix
        long sum = 0;
        while (ptrA != null) {
            sum += ptrA.val;
            ptrA = ptrA.next;
        }
        return sum;
    }

    private int getLength(ListNode head) {
        int len = 0;
        while (head != null) {
            len++;
            head = head.next;
        }
        return len;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        ListNode dummyA = new ListNode(0);
        ListNode curA = dummyA;
        ListNode[] nodesA = new ListNode[n];
        for (int i = 0; i < n; i++) {
            curA.next = new ListNode(sc.nextInt());
            curA = curA.next;
            nodesA[i] = curA;
        }
        
        ListNode dummyB = new ListNode(0);
        ListNode curB = dummyB;
        ListNode[] nodesB = new ListNode[m];
        for (int i = 0; i < m; i++) {
            curB.next = new ListNode(sc.nextInt());
            curB = curB.next;
            nodesB[i] = curB;
        }
        
        int ia = sc.nextInt();
        int ib = sc.nextInt();
        if (ia >= 0 && ib >= 0 && n > 0 && m > 0) {
            nodesB[ib].next = nodesA[ia];
        }

        Solution solution = new Solution();
        System.out.println(solution.intersectionSum(dummyA.next, dummyB.next));
        sc.close();
    }
}
