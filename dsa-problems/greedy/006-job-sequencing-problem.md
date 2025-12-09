# Maximum Profit Job Scheduling

**Problem ID:** GRDY-006
**Display ID:** 83
**Question Name:** Job Sequencing Problem
**Slug:** job-sequencing-problem
**Title:** Maximum Profit Job Scheduling
**Difficulty:** Hard
**Premium:** No
**Tags:** Greedy, Sorting, Union Find, Dynamic Programming

## Problem Description

You are given a list of jobs where each job has a deadline and a profit. Each job takes 1 unit of time to complete, and only one job can be scheduled at a time. A job is completed if it is finished before or on its deadline. Find the maximum profit you can earn by scheduling jobs optimally.

Each job is represented as `[jobId, deadline, profit]`.

## A Simple Scenario (Daily Life Usage)

Imagine you're a freelancer on platforms like Upwork or Fiverr with multiple job offers. Each job has a deadline (days from now) and pays different amounts. You can only work on one job per day. To maximize your income, you need to strategically choose which jobs to accept and when to complete them. For example, if you have a 2-day job paying $100 and a 1-day job paying $50, you'd do the $50 job on day 1 and the $100 job on day 2 to earn $150 total.

## Your Task

Write a function that takes an array of jobs (each with a deadline and profit) and returns the maximum profit you can achieve by optimally scheduling the jobs.

## Why is it Important?

This problem teaches you how to:

- Apply greedy algorithms to scheduling optimization
- Use sorting strategies for decision-making
- Implement slot allocation techniques
- Handle deadline constraints in scheduling
- Understand tradeoffs between different greedy approaches
- Apply disjoint set (Union Find) for advanced optimization

## Examples

### Example 1:

**Input:** `jobs = [[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]`
**Output:** `60`
**Explanation:**
- Sort by profit: [3, 4, 1, 2]
- Schedule job 3 (profit 40) at deadline 1
- Schedule job 4 (profit 30) cannot fit (deadline 1 taken)
- Schedule job 1 (profit 20) at any slot ≤ 4, choose slot 2
- Schedule job 2 (profit 10) cannot fit (deadline 1 taken)
Maximum profit = 40 + 20 = 60

### Example 2:

**Input:** `jobs = [[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]`
**Output:** `127`
**Explanation:**
- Schedule job 1 (profit 100) at slot 2
- Schedule job 3 (profit 27) at slot 1
Maximum profit = 100 + 27 = 127

### Example 3:

**Input:** `jobs = [[1, 1, 50], [2, 2, 60], [3, 3, 20], [4, 2, 30]]`
**Output:** `140`
**Explanation:** Schedule jobs 1, 2, and 4 for profit 50+60+30 = 140.

## Constraints

- 1 ≤ jobs.length ≤ 10^5
- 1 ≤ deadline ≤ 10^5
- 1 ≤ profit ≤ 10^5

## Asked by Companies

- Upwork
- Fiverr
- Freelancer
- Toptal
