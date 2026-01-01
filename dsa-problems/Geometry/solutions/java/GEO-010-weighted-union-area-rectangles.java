import java.util.*;

class Main {
    public static long solve(int n, int targetW, int[][] rects) {
        if (n == 0) return 0;
        
        List<Integer> xCoords = new ArrayList<>();
        List<Integer> yCoords = new ArrayList<>();
        for (int[] r : rects) {
            xCoords.add(r[0]);
            xCoords.add(r[2]);
            yCoords.add(r[1]);
            yCoords.add(r[3]);
        }
        Collections.sort(xCoords);
        Collections.sort(yCoords);
        
        List<Integer> ux = new ArrayList<>();
        if (!xCoords.isEmpty()) ux.add(xCoords.get(0));
        for (int i = 1; i < xCoords.size(); i++) if (!xCoords.get(i).equals(xCoords.get(i-1))) ux.add(xCoords.get(i));
        
        List<Integer> uy = new ArrayList<>();
        if (!yCoords.isEmpty()) uy.add(yCoords.get(0));
        for (int i = 1; i < yCoords.size(); i++) if (!yCoords.get(i).equals(yCoords.get(i-1))) uy.add(yCoords.get(i));
        
        long totalArea = 0;
        for (int i = 0; i < ux.size() - 1; i++) {
            long dx = (long)ux.get(i + 1) - ux.get(i);
            if (dx <= 0) continue;
            
            long[] yWeights = new long[uy.size() - 1];
            for (int[] r : rects) {
                if (r[0] <= ux.get(i) && r[2] >= ux.get(i+1)) {
                    for (int j = 0; j < uy.size() - 1; j++) {
                        if (r[1] <= uy.get(j) && r[3] >= uy.get(j+1)) {
                            yWeights[j] += r[4];
                        }
                    }
                }
            }
            
            long dyCovered = 0;
            for (int j = 0; j < uy.size() - 1; j++) {
                if (yWeights[j] >= targetW) {
                    dyCovered += (long)uy.get(j+1) - uy.get(j);
                }
            }
            totalArea += dx * dyCovered;
        }
        return totalArea;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int targetW = sc.nextInt();
        int[][] rects = new int[n][5];
        for (int i = 0; i < n; i++) {
            rects[i][0] = sc.nextInt();
            rects[i][1] = sc.nextInt();
            rects[i][2] = sc.nextInt();
            rects[i][3] = sc.nextInt();
            rects[i][4] = sc.nextInt();
        }
        System.out.println(solve(n, targetW, rects));
        sc.close();
    }
}
