import java.util.*;

class Solution {
    public int[] shuttleShiftBlackout(int[] arr, int k, Set<Integer> blackout) {
        List<Integer> validIndices = new ArrayList<>();
        List<Integer> values = new ArrayList<>();
        
        // 1. Extract
        for (int i = 0; i < arr.length; i++) {
            if (!blackout.contains(i)) {
                validIndices.add(i);
                values.add(arr[i]);
            }
        }
        
        if (values.isEmpty()) return arr;
        
        // 2. Rotate
        int count = values.size();
        k = k % count;
        List<Integer> rotatedValues = new ArrayList<>(count);
        // Left rotate: element at i comes from (i + k) % count
        for (int i = 0; i < count; i++) {
            rotatedValues.add(values.get((i + k) % count));
        }
        
        // 3. Write Back
        for (int i = 0; i < count; i++) {
            arr[validIndices.get(i)] = rotatedValues.get(i);
        }
        
        return arr;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        
        int k = sc.nextInt();
        int b = sc.nextInt();
        Set<Integer> blackout = new HashSet<>();
        for (int i = 0; i < b; i++) blackout.add(sc.nextInt());

        Solution solution = new Solution();
        int[] result = solution.shuttleShiftBlackout(arr, k, blackout);
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
