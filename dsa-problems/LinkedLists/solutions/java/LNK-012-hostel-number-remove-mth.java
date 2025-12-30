import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode removeMth(ListNode head, int M) {
        if (M <= 0) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;

        // Move to the (M-1)th node
        for (int i = 0; i < M - 1; i++) {
            if (curr == null) return head; // Out of bounds
            curr = curr.next;
        }

        // Check if M-th node exists
        if (curr != null && curr.next != null) {
            curr.next = curr.next.next;
        }

        return dummy.next;
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
        int M = sc.nextInt();

        Solution solution = new Solution();
        ListNode res = solution.removeMth(dummy.next, M);
        
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
