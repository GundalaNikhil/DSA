import java.util.*;

class Solution {
    public List<List<String>> ladders(String start, String end, List<String> dict) {
        Set<String> dictSet = new HashSet<>(dict);
        dictSet.add(start);
        dictSet.add(end); // Ensure end is in dict for graph building
        
        // Build adjacency list with constraints
        Map<String, List<String>> adj = new HashMap<>();
        for (String w : dictSet) {
            adj.put(w, new ArrayList<>());
        }
        
        List<String> words = new ArrayList<>(dictSet);
        for (int i = 0; i < words.size(); i++) {
            for (int j = i + 1; j < words.size(); j++) {
                String w1 = words.get(i);
                String w2 = words.get(j);
                if (isOneDiff(w1, w2) && isAlternating(w1, w2)) {
                    adj.get(w1).add(w2);
                    adj.get(w2).add(w1);
                }
            }
        }
        
        // BFS
        Map<String, Integer> dist = new HashMap<>();
        Map<String, List<String>> parents = new HashMap<>();
        Queue<String> q = new LinkedList<>();
        
        q.offer(start);
        dist.put(start, 0);
        
        boolean found = false;
        
        while (!q.isEmpty()) {
            int size = q.size();
            Set<String> currentLevelVisited = new HashSet<>();
            
            for (int i = 0; i < size; i++) {
                String curr = q.poll();
                if (curr.equals(end)) found = true;
                
                int curDist = dist.get(curr);
                
                for (String neighbor : adj.getOrDefault(curr, new ArrayList<>())) {
                    if (!dist.containsKey(neighbor)) {
                        // Not visited yet
                        if (currentLevelVisited.add(neighbor)) {
                            dist.put(neighbor, curDist + 1);
                            q.offer(neighbor);
                        }
                        parents.computeIfAbsent(neighbor, k -> new ArrayList<>()).add(curr);
                    } else if (dist.get(neighbor) == curDist + 1) {
                        // Visited in this level (another shortest path)
                        parents.computeIfAbsent(neighbor, k -> new ArrayList<>()).add(curr);
                    }
                }
            }
            if (found) break;
        }
        
        List<List<String>> results = new ArrayList<>();
        if (found) {
            List<String> path = new ArrayList<>();
            path.add(end);
            backtrack(end, start, parents, path, results);
        }
        
        // Sort results for consistent output if needed (problem doesn't specify order, but usually lexicographical or any)
        // The problem output example shows sorted paths.
        results.sort((a, b) -> {
            for(int i=0; i<a.size(); i++) {
                if(!a.get(i).equals(b.get(i))) return a.get(i).compareTo(b.get(i));
            }
            return 0;
        });
        
        return results;
    }
    
    private void backtrack(String curr, String start, Map<String, List<String>> parents, List<String> path, List<List<String>> results) {
        if (curr.equals(start)) {
            List<String> fullPath = new ArrayList<>(path);
            Collections.reverse(fullPath);
            results.add(fullPath);
            return;
        }
        
        for (String p : parents.getOrDefault(curr, new ArrayList<>())) {
            path.add(p);
            backtrack(p, start, parents, path, results);
            path.remove(path.size() - 1);
        }
    }
    
    private boolean isOneDiff(String a, String b) {
        if (a.length() != b.length()) return false;
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) diff++;
            if (diff > 1) return false;
        }
        return diff == 1;
    }
    
    private boolean isAlternating(String a, String b) {
        return isVowel(a.charAt(0)) != isVowel(b.charAt(0));
    }
    
    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) != -1;
    }
}
