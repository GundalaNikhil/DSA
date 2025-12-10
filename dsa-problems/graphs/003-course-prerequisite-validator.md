# Course Prerequisite Validator

**Problem ID:** GRP-003
**Display ID:** 50
**Question Name:** Course Prerequisite Validator
**Slug:** course-prerequisite-validator
**Title:** Course Schedule
**Difficulty:** Medium
**Premium:** No
**Tags:** Graph, Topological Sort, Depth-First Search

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You have numCourses to take, labeled 0 to numCourses-1. Some courses have prerequisites. Can you finish all courses?

## A Simple Scenario (Daily Life Usage)

To take "Advanced Programming" (course 1), you must first complete "Intro to Programming" (course 0). Prerequisites: [[1,0]] means course 1 requires course 0. If there's a circular dependency (course 1 needs 0, course 0 needs 1), you can't complete either! This validates your college course plan.

## Your Task

Return true if you can finish all courses (no circular dependencies), false otherwise.

## Why is it Important?

This problem teaches you:

- Cycle detection in directed graphs
- Topological sorting
- Dependency resolution
- Course planning logic

## Examples

### Example 1:

**Input:** `numCourses = 2, prerequisites = [[1,0]]`
**Output:** `true`
**Explanation:** Take course 0, then course 1.

### Example 2:

**Input:** `numCourses = 2, prerequisites = [[1,0], [0,1]]`
**Output:** `false`
**Explanation:** Circular dependency: course 1 needs 0, course 0 needs 1.

### Example 3:

**Input:** `numCourses = 3, prerequisites = [[1,0], [2,1]]`
**Output:** `true`
**Explanation:** Take courses in order: 0 → 1 → 2.

## Constraints

- 1 ≤ numCourses ≤ 2000
- 0 ≤ prerequisites.length ≤ 5000
- prerequisites[i].length == 2
- All prerequisite pairs are unique

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Coursera
- Udemy
- Khan Academy
- edX

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
