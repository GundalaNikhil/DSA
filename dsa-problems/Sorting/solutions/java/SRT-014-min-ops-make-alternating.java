import java.util.*;

class Solution {
    public int minChanges(int[] arr) {
        int n = arr.length;
        if (n <= 1) return 0;
        
        Map<Integer, Integer> evenCounts = new HashMap<>();
        Map<Integer, Integer> oddCounts = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                evenCounts.put(arr[i], evenCounts.getOrDefault(arr[i], 0) + 1);
            } else {
                oddCounts.put(arr[i], oddCounts.getOrDefault(arr[i], 0) + 1);
            }
        }
        
        int[] topEven = getTopTwo(evenCounts);
        int[] topOdd = getTopTwo(oddCounts);
        
        int e1Val = topEven[0], e1Count = topEven[1];
        int e2Val = topEven[2], e2Count = topEven[3];
        int o1Val = topOdd[0], o1Count = topOdd[1];
        int o2Val = topOdd[2], o2Count = topOdd[3];
        
        if (e1Val != o1Val) {
            return n - (e1Count + o1Count);
        } else {
            int option1 = n - (e1Count + o2Count);
            int option2 = n - (e2Count + o1Count);
            return Math.min(option1, option2);
        }
    }
    
    private int[] getTopTwo(Map<Integer, Integer> counts) {
        int firstVal = -1, firstCount = 0;
        int secondVal = -1, secondCount = 0;
        
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            int val = entry.getKey();
            int count = entry.getValue();
            
            if (count > firstCount) {
                secondCount = firstCount;
                secondVal = firstVal;
                firstCount = count;
                firstVal = val;
            } else if (count > secondCount) {
                secondCount = count;
                secondVal = val;
            }
        }
        return new int[]{firstVal, firstCount, secondVal, secondCount};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.minChanges(arr));
        sc.close();
    }
}
