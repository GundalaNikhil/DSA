import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public int weightedMiddleValue(ListNode head) {
        if (head == null) return 0;

        // Pass 1: Calculate total weight
        long totalWeight = 0;
        ListNode curr = head;
        while (curr != null) {
            totalWeight += curr.val;
            curr = curr.next;
        }

        long threshold = (totalWeight + 1) / 2;

        // Pass 2: Find the node
        long currentSum = 0;
        curr = head;
        while (curr != null) {
            currentSum += curr.val;
            if (currentSum >= threshold) {
                return curr.val;
            }
            curr = curr.next;
        }
        return 0; // Should not reach here
    }
}

class Main {
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
        System.out.println(solution.weightedMiddleValue(dummy.next));
        sc.close();
    }
}
