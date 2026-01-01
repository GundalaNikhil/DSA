import java.util.*;

class Solution {
    public long minInversionsAfterSwap(int[] arr) {
        int n = arr.length;
        long best = countInversions(arr.clone());

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;

                long inv = countInversions(arr.clone());
                if (inv < best) {
                    best = inv;
                }

                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }

        return best;
    }

    private long countInversions(int[] arr) {
        int[] temp = new int[arr.length];
        return mergeSort(arr, temp, 0, arr.length - 1);
    }

    private long mergeSort(int[] arr, int[] temp, int left, int right) {
        if (left >= right) {
            return 0;
        }

        int mid = left + (right - left) / 2;
        long inv = mergeSort(arr, temp, left, mid);
        inv += mergeSort(arr, temp, mid + 1, right);
        inv += merge(arr, temp, left, mid, right);
        return inv;
    }

    private long merge(int[] arr, int[] temp, int left, int mid, int right) {
        int i = left;
        int j = mid + 1;
        int k = left;
        long inv = 0;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
                inv += (mid - i + 1);
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        for (i = left; i <= right; i++) {
            arr[i] = temp[i];
        }

        return inv;
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
        System.out.println(solution.minInversionsAfterSwap(arr));
        sc.close();
    }
}
