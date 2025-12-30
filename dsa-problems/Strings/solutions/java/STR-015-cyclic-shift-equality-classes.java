class Solution {
    public int cyclicShiftEquivalenceClasses(List<String> strings) {
        Set<String> canonicalSet = new HashSet<>();

        for (String s : strings) {
            String canonical = minimalRotation(s);
            canonicalSet.add(canonical);
        }

        return canonicalSet.size();
    }

    private String minimalRotation(String s) {
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

        return s.substring(k) + s.substring(0, k);
    }
}
