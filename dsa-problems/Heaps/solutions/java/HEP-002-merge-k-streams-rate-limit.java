import java.util.*;

class Solution {
    static class Element implements Comparable<Element> {
        int val;
        int streamIdx;
        
        public Element(int val, int streamIdx) {
            this.val = val;
            this.streamIdx = streamIdx;
        }
        
        @Override
        public int compareTo(Element other) {
            return Integer.compare(this.val, other.val);
        }
    }
    
    public List<Integer> mergeStreams(List<List<Integer>> streams, int r) {
        PriorityQueue<Element> pq = new PriorityQueue<>();
        int k = streams.size();
        int[] indices = new int[k]; // Current index in each stream
        int[] usage = new int[k];   // Usage in current round
        
        // Initial population
        for (int i = 0; i < k; i++) {
            if (!streams.get(i).isEmpty()) {
                pq.offer(new Element(streams.get(i).get(0), i));
                indices[i]++;
            }
        }
        
        List<Integer> result = new ArrayList<>();
        List<Integer> blocked = new ArrayList<>();
        
        while (!pq.isEmpty()) {
            Element curr = pq.poll();
            result.add(curr.val);
            
            int sIdx = curr.streamIdx;
            usage[sIdx]++;
            
            if (usage[sIdx] < r) {
                // Can still contribute to this round
                if (indices[sIdx] < streams.get(sIdx).size()) {
                    pq.offer(new Element(streams.get(sIdx).get(indices[sIdx]), sIdx));
                    indices[sIdx]++;
                }
            } else {
                // Blocked for this round
                blocked.add(sIdx);
            }
            
            // End of round check
            if (pq.isEmpty() && !blocked.isEmpty()) {
                // Start new round
                for (int idx : blocked) {
                    usage[idx] = 0; // Reset usage
                    if (indices[idx] < streams.get(idx).size()) {
                        pq.offer(new Element(streams.get(idx).get(indices[idx]), idx));
                        indices[idx]++;
                    }
                }
                blocked.clear();
            }
        }
        
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            int r = sc.nextInt();
            List<List<Integer>> streams = new ArrayList<>();
            for (int i = 0; i < k; i++) {
                int m = sc.nextInt();
                List<Integer> stream = new ArrayList<>();
                for (int j = 0; j < m; j++) {
                    stream.add(sc.nextInt());
                }
                streams.add(stream);
            }
            
            Solution solution = new Solution();
            List<Integer> result = solution.mergeStreams(streams, r);
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i));
                if (i < result.size() - 1) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
