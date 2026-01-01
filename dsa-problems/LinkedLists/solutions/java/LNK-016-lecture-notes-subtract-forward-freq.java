import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Result {
    int sign;
    ListNode head;
    int[] freq;
    Result(int sign, ListNode head, int[] freq) {
        this.sign = sign;
        this.head = head;
        this.freq = freq;
    }
}

class Solution {
    public Result subtractWithFreq(ListNode a, ListNode b) {
        // 1. Compare to find larger
        int lenA = getLength(a);
        int lenB = getLength(b);
        ListNode large = a, small = b;
        
        if (lenA < lenB) {
            large = b; small = a;
        } else if (lenA == lenB) {
            ListNode currA = a, currB = b;
            while (currA != null && currA.val == currB.val) {
                currA = currA.next;
                currB = currB.next;
            }
            if (currA == null) return new Result(0, new ListNode(0), new int[]{1,0,0,0,0,0,0,0,0,0}); // Equal
            if (currA.val < currB.val) {
                large = b; small = a;
            }
        }

        // 2. Use Stacks
        Deque<Integer> s1 = new ArrayDeque<>();
        Deque<Integer> s2 = new ArrayDeque<>();
        
        ListNode curr = large;
        while (curr != null) { s1.push(curr.val); curr = curr.next; }
        curr = small;
        while (curr != null) { s2.push(curr.val); curr = curr.next; }

        // 3. Subtract
        ListNode head = null;
        int borrow = 0;
        int[] freq = new int[10];

        while (!s1.isEmpty()) {
            int v1 = s1.pop();
            int v2 = s2.isEmpty() ? 0 : s2.pop();
            
            int diff = v1 - v2 - borrow;
            if (diff < 0) {
                diff += 10;
                borrow = 1;
            } else {
                borrow = 0;
            }
            
            ListNode node = new ListNode(diff);
            node.next = head;
            head = node;
        }

        // 4. Remove leading zeros
        while (head != null && head.val == 0 && head.next != null) {
            head = head.next;
        }

        // 5. Count Freq
        curr = head;
        while (curr != null) {
            freq[curr.val]++;
            curr = curr.next;
        }

        return new Result(1, head, freq);
    }

    private int getLength(ListNode head) {
        int len = 0;
        while (head != null) { len++; head = head.next; }
        return len;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        ListNode dummyA = new ListNode(0);
        ListNode curA = dummyA;
        for (int i = 0; i < n; i++) {
            curA.next = new ListNode(sc.nextInt());
            curA = curA.next;
        }
        int m = sc.nextInt();
        ListNode dummyB = new ListNode(0);
        ListNode curB = dummyB;
        for (int i = 0; i < m; i++) {
            curB.next = new ListNode(sc.nextInt());
            curB = curB.next;
        }

        Solution solution = new Solution();
        Result res = solution.subtractWithFreq(dummyA.next, dummyB.next);
        System.out.println(res.sign);
        ListNode out = res.head;
        boolean first = true;
        while (out != null) {
            if (!first) System.out.print(" ");
            System.out.print(out.val);
            first = false;
            out = out.next;
        }
        System.out.println();
        for (int i = 0; i < 10; i++) {
            System.out.print(res.freq[i] + (i < 9 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
