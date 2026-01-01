import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public int[] cycleInfo(ListNode head) {
        if (head == null) return new int[]{-1, 0, 0};

        ListNode slow = head;
        ListNode fast = head;
        boolean hasCycle = false;

        // Phase 1: Detect Cycle
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }

        if (!hasCycle) return new int[]{-1, 0, 0};

        // Phase 2: Find Entry
        ListNode entry = head;
        int entryIndex = 0;
        while (entry != slow) {
            entry = entry.next;
            slow = slow.next;
            entryIndex++;
        }

        // Phase 3: Cycle Stats
        int length = 0;
        int maxVal = Integer.MIN_VALUE;
        ListNode curr = entry;
        do {
            length++;
            maxVal = Math.max(maxVal, curr.val);
            curr = curr.next;
        } while (curr != entry);

        return new int[]{entryIndex, length, maxVal};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        ListNode[] nodes = new ListNode[n];
        for (int i = 0; i < n; i++) {
            cur.next = new ListNode(sc.nextInt());
            cur = cur.next;
            nodes[i] = cur;
        }
        
        int pos = sc.nextInt();
        if (pos >= 0 && n > 0) {
            cur.next = nodes[pos];
        }

        Solution solution = new Solution();
        int[] res = solution.cycleInfo(dummy.next);
        System.out.println(res[0] + " " + res[1] + " " + res[2]);
        sc.close();
    }
}
