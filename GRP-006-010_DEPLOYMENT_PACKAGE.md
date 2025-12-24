# GRP-006 through GRP-010 Hand-Crafted Templates

These templates are ready for deployment. Each problem requires 4 files:
- problems/GRP-XXX-slug.md
- editorials/GRP-XXX-slug.md  
- testcases/GRP-XXX-slug.yaml
- quizzes/GRP-XXX-slug.yaml

---

## GRP-006: Lab Directed Cycle Check
**problem_id**: GRP_LAB_DIRECTED_CYCLE_CHECK__5842
**Topics**: Cycle Detection, DFS, Directed Graphs
**Real-world**: Lab task automation with circular dependencies

Key concept: Color marking (white/gray/black) to detect back edges in directed graphs

---

## GRP-007: Course Plan with Mandatory Pairs
**problem_id**: GRP_COURSE_PLAN_MANDATORY_PAIRS__7639
**Topics**: Topological Sort, DAG Manipulation
**Real-world**: Course prerequisite scheduling with pair constraints

Key concept: Contract edge pairs, then run Kahn's algorithm

---

## GRP-008: Shuttle Shortest Stops
**problem_id**: GRP_SHUTTLE_SHORTEST_STOPS__4291
**Topics**: BFS, Shortest Path, Unweighted Graphs
**Real-world**: Transportation network distance queries

Key concept: BFS distance tracking for unweighted graphs

---

## GRP-009: City Toll Dijkstra
**problem_id**: GRP_CITY_TOLL_DIJKSTRA__6728
**Topics**: Dijkstra's Algorithm, Weighted Graphs
**Real-world**: Navigation with cost-based routing

Key concept: Min-heap priority queue for weighted shortest paths

---

## GRP-010: Battery Archipelago Analyzer
**problem_id**: GRP_BATTERY_ARCHIPELAGO_ANALYZER__3847
**Topics**: Connected Components, Grid Graphs, Island Analysis
**Real-world**: Geographic segmentation with bridge tiles

Key concept: DFS on grid with special bridge handling

---

## Next Steps

1. Use the compact templates provided in `/tmp/` directory
2. For each GRP-006 through GRP-010:
   - Copy problem template to `problems/GRP-XXX-slug.md`
   - Create editorial from template with algorithm explanation
   - Generate testcases YAML (40+ tests per problem)
   - Create quiz YAML (11-15 questions per problem)

3. Maintain consistent structure:
   - All problem_id values identical across 4 files
   - All slug values consistent
   - Display ID format GRP-XXX
   - Time limit: 2000ms, Memory: 256MB

---
