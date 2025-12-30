import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Result {
    ListNode head;
    int reversedGroups;
    long sum;
    Result(ListNode head, int reversedGroups, long sum) {
        this.head = head;
        this.reversedGroups = reversedGroups;
        this.sum = sum;
    }
}

class Solution {
    public Result reverseFromOffset(ListNode head, int k, int s) {
        if (head == null || k <= 1) return new Result(head, 0, 0L);

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        // Move to s-1
        for (int i = 0; i < s - 1; i++) {
            if (prev.next == null) return new Result(head, 0, 0L);
            prev = prev.next;
        }

        int groups = 0;
        long totalSum = 0;

        while (true) {
            // Probe k steps
            ListNode probe = prev;
            for (int i = 0; i < k; i++) {
                probe = probe.next;
                if (probe == null) return new Result(dummy.next, groups, totalSum);
            }

            // Reverse k nodes
            ListNode tail = prev.next;
            ListNode curr = tail.next;
            long groupSum = tail.val;
            
            for (int i = 1; i < k; i++) {
                groupSum += curr.val;
                ListNode temp = curr.next;
                curr.next = prev.next;
                prev.next = curr;
                tail.next = temp;
                curr = temp;
            }
            
            groups++;
            totalSum += groupSum;
            prev = tail; // Move prev to end of reversed group
        }
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
        
        int k = sc.nextInt();
        int s = sc.nextInt();

        Solution solution = new Solution();
        Result res = solution.reverseFromOffset(dummy.next, k, s);
        
        ListNode out = res.head;
        boolean first = true;
        while (out != null) {
            if (!first) System.out.print(" ");
            System.out.print(out.val);
            first = false;
            out = out.next;
        }
        System.out.println();
        System.out.println(res.reversedGroups);
        System.out.println(res.sum);
        sc.close();
    }
}
