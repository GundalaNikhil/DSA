class Solution {
  allOrderings(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    const indegree = Array(n).fill(0);
    
    for (const [u, v] of edges) {
      adj[u].push(v);
      indegree[v]++;
    }

    const results = [];
    const visited = Array(n).fill(false);

    const backtrack = (path) => {
      if (path.length === n) {
        results.push([...path]);
        return;
      }

      for (let i = 0; i < n; i++) {
        if (!visited[i] && indegree[i] === 0) {
          visited[i] = true;
          path.push(i);
          for (const neighbor of adj[i]) {
            indegree[neighbor]--;
          }

          backtrack(path);

          for (const neighbor of adj[i]) {
            indegree[neighbor]++;
          }
          path.pop();
          visited[i] = false;
        }
      }
    };

    backtrack([]);
    return results;
  }
}
