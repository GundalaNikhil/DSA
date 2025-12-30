import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode groupOddEvenStable(ListNode head) {
        ListNode oddDummy = new ListNode(0);
        ListNode evenDummy = new ListNode(0);
        ListNode oddTail = oddDummy;
        ListNode evenTail = evenDummy;

        ListNode curr = head;
        while (curr != null) {
            if (curr.val % 2 != 0) {
                oddTail.next = curr;
                oddTail = oddTail.next;
            } else {
                evenTail.next = curr;
                evenTail = evenTail.next;
            }
            curr = curr.next;
        }

        evenTail.next = null; // Terminate even list
        oddTail.next = evenDummy.next; // Connect odd to even

        return oddDummy.next;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int i = 0; i < n; i++) {
            cur.next = new ListNode(sc.nextInt());
            cur = cur.next;
        }

        Solution solution = new Solution();
        ListNode res = solution.groupOddEvenStable(dummy.next);
        
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
