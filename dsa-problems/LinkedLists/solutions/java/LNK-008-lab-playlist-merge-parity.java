import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode mergeByParity(ListNode l1, ListNode l2) {
        ListNode evenDummy = new ListNode(0);
        ListNode oddDummy = new ListNode(0);
        ListNode evenTail = evenDummy;
        ListNode oddTail = oddDummy;

        // Process List 1
        ListNode curr = l1;
        while (curr != null) {
            if (curr.val % 2 == 0) {
                evenTail.next = curr;
                evenTail = evenTail.next;
            } else {
                oddTail.next = curr;
                oddTail = oddTail.next;
            }
            curr = curr.next;
        }

        // Process List 2
        curr = l2;
        while (curr != null) {
            if (curr.val % 2 == 0) {
                evenTail.next = curr;
                evenTail = evenTail.next;
            } else {
                oddTail.next = curr;
                oddTail = oddTail.next;
            }
            curr = curr.next;
        }

        // Connect lists
        oddTail.next = null; // Terminate odd list
        evenTail.next = oddDummy.next; // Connect even tail to odd head

        return evenDummy.next;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        ListNode d1 = new ListNode(0);
        ListNode c1 = d1;
        for (int i = 0; i < n; i++) {
            c1.next = new ListNode(sc.nextInt());
            c1 = c1.next;
        }
        
        int m = sc.nextInt();
        ListNode d2 = new ListNode(0);
        ListNode c2 = d2;
        for (int i = 0; i < m; i++) {
            c2.next = new ListNode(sc.nextInt());
            c2 = c2.next;
        }

        Solution solution = new Solution();
        ListNode res = solution.mergeByParity(d1.next, d2.next);
        
        boolean first = true;
        while (res != null) {
            if (!first) System.out.print(" ");
            System.out.print(res.val);
            first = false;
            res = res.next;
        }
        System.out.println();
        sc.close();
    }
}
