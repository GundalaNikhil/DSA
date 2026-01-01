import java.util.*;

class Solution {
    public Object[] shortestCoveringWindow(List<String> arr, Set<String> T) {
        if (arr == null || arr.isEmpty() || T == null || T.isEmpty()) {
            return new Object[]{0, new ArrayList<>()};
        }

        Map<String, Integer> required = new HashMap<>();
        for (String s : T) {
            required.put(s, 1);
        }

        Map<String, Integer> windowCounts = new HashMap<>();
        int left = 0, formed = 0;
        int minLen = Integer.MAX_VALUE;
        int resultLeft = 0, resultRight = 0;

        for (int right = 0; right < arr.size(); right++) {
            String s = arr.get(right);
            windowCounts.put(s, windowCounts.getOrDefault(s, 0) + 1);

            if (required.containsKey(s) && windowCounts.get(s) == 1) {
                formed++;
            }

            while (formed == T.size() && left <= right) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    resultLeft = left;
                    resultRight = right;
                }

                String leftS = arr.get(left);
                windowCounts.put(leftS, windowCounts.get(leftS) - 1);
                if (required.containsKey(leftS) && windowCounts.get(leftS) == 0) {
                    formed--;
                }

                left++;
            }
        }

        if (minLen == Integer.MAX_VALUE) {
            return new Object[]{0, new ArrayList<>()};
        }

        List<String> resultWindow = new ArrayList<>();
        for (int i = resultLeft; i <= resultRight; i++) {
            resultWindow.add(arr.get(i));
        }
        return new Object[]{minLen, resultWindow};
    }
}




class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr_n = sc.nextInt();
        List<String> arr = new ArrayList<>();
        for(int i=0; i<arr_n; i++) arr.add(sc.next());
        int T_n = sc.nextInt();
        Set<String> T = new HashSet<>();
        for(int i=0; i<T_n; i++) T.add(sc.next());
        Solution sol = new Solution();
        Object[] res = sol.shortestCoveringWindow(arr, T);
        System.out.println(res[0]);
        @SuppressWarnings("unchecked")
        List<String> list = (List<String>)res[1];
        for(String s : list) System.out.println(s);
        if(list.isEmpty()) System.out.println("NONE");
        sc.close();
    }
}
