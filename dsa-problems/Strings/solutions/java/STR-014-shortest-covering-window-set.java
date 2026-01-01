class Solution {
    public Object[] shortestCoveringWindow(String[] arr, Set<String> T) {
        if (arr == null || arr.length == 0 || T == null || T.isEmpty()) {
            return new Object[]{0, new String[]{}};
        }

        Map<String, Integer> required = new HashMap<>();
        for (String s : T) {
            required.put(s, 1);
        }

        Map<String, Integer> windowCounts = new HashMap<>();
        int left = 0, formed = 0;
        int minLen = Integer.MAX_VALUE;
        int resultLeft = 0, resultRight = 0;

        for (int right = 0; right < arr.length; right++) {
            String s = arr[right];
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

                String leftS = arr[left];
                windowCounts.put(leftS, windowCounts.get(leftS) - 1);
                if (required.containsKey(leftS) && windowCounts.get(leftS) == 0) {
                    formed--;
                }

                left++;
            }
        }

        if (minLen == Integer.MAX_VALUE) {
            return new Object[]{0, new String[]{}};
        }

        String[] resultWindow = new String[minLen];
        System.arraycopy(arr, resultLeft, resultWindow, 0, minLen);
        return new Object[]{minLen, resultWindow};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr_n = sc.nextInt();
        List<String> arr = new ArrayList<>();
        for(int i=0; i<arr_n; i++) arr.add(sc.next());
        Solution sol = new Solution();
        List<String> res = sol.shortestCoveringWindow(arr, T);
        for(String out_s : res) System.out.println(out_s);
        if(res.isEmpty()) System.out.println("NONE");
        sc.close();
    }
}
