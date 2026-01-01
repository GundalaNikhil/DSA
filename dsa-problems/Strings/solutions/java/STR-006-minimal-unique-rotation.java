class Solution {
    public String minimalUniqueRotation(String s) {
        int n = s.length();

        // Booth's algorithm
        int minIdx = boothMinimalRotationIndex(s);
        String minRotation = s.substring(minIdx) + s.substring(0, minIdx);

        // Check if same as original
        if (minRotation.equals(s)) {
            return s;
        } else {
            return minRotation;
        }
    }

    private int boothMinimalRotationIndex(String s) {
        String doubled = s + s;
        int n = s.length();
        int[] failure = new int[2 * n];
        Arrays.fill(failure, -1);
        int k = 0;

        for (int j = 1; j < 2 * n; j++) {
            int i = failure[j - k - 1];
            while (i != -1 && doubled.charAt(j) != doubled.charAt(k + i + 1)) {
                if (doubled.charAt(j) < doubled.charAt(k + i + 1)) {
                    k = j - i - 1;
                }
                i = failure[i];
            }

            if (doubled.charAt(j) != doubled.charAt(k + i + 1)) {
                if (doubled.charAt(j) < doubled.charAt(k + i + 1)) {
                    k = j;
                }
                failure[j - k] = -1;
            } else {
                failure[j - k] = i + 1;
            }
        }

        return k;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        Solution sol = new Solution();
        System.out.println(sol.minimalUniqueRotation(s));
        sc.close();
    }
}
