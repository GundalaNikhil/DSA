---
problem_id: HEP_PROJECT_SELECTION_RISK_BUDGET__2917
display_id: HEP-013
slug: project-selection-risk-budget
title: "Project Selection with Risk Budget"
difficulty: Medium
difficulty_score: 60
topics:
  - Heaps
  - Greedy
  - Finance
tags:
  - heaps
  - greedy
  - risk-budget
  - medium
premium: true
subscription_tier: basic
---

# HEP-013: Project Selection with Risk Budget

## 📋 Problem Summary

You have `n` projects, each with:
- `cost`: Minimum capital required to start.
- `profit`: Capital gained after completion.
- `risk`: Risk incurred.

You start with initial capital `C` and risk budget `R`.
You can select at most `k` projects.
Constraints to select a project:
1. `current_capital >= cost`
2. `current_risk + risk <= R`

Goal: Maximize final capital.
Note: Capital increases by `profit`. Risk increases by `risk`.

## 🌍 Real-World Scenario

**Scenario Title:** Venture Capital Investment

A VC firm has a fund `C` and a strict risk tolerance `R`.
- Startups pitch for funding (`cost`).
- If successful, they return `profit`.
- Each investment adds exposure (`risk`) to the portfolio.
- The firm wants to reinvest returns into new startups to maximize the fund's value after `k` rounds of investment, without exceeding the risk limit.

![Real-World Application](../images/HEP-013/real-world-scenario.png)

## Detailed Explanation

### Key Idea

This is the IPO selection pattern with an extra risk budget.
- Capital only increases, so once a project is affordable by cost, it stays
  affordable.
- Remaining risk only decreases, so a project that is too risky now will never
  become feasible later.

We sort projects by cost and maintain a max-heap by profit for the projects that
are currently affordable. For each selection, we pop the most profitable project
that fits the remaining risk budget.

### Example

Input:
```
3 2 1 3
1 2 1
2 2 2
3 5 2
```
- Start: capital=1, remaining risk=3.
- Pick project 1 (cost 1, profit 2, risk 1): capital=3, remaining risk=2.
- Projects 2 and 3 are affordable; pick project 3 (profit 5, risk 2).
- Final capital = 8.

### Algorithm

1. Sort projects by cost ascending.
2. Max-heap by profit for all projects with `cost <= current capital`.
3. Repeat up to `k` times:
   - Push all newly affordable projects into the heap.
   - Pop from the heap until you find a project with `risk <= remaining risk`.
     If none exist, stop.
   - Take the project: `capital += profit`, `remaining risk -= risk`.
4. Return the final capital.

### Time Complexity

- **O(N log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-013/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 2 1 3
1 2 1
2 2 2
3 5 2
```
Sorted by cost: P1 (1,2,1), P2 (2,2,2), P3 (3,5,2).

1. **Step 1:**
   - Affordable: P1.
   - Pick P1. Capital = 3, Remaining risk = 2.
2. **Step 2:**
   - Affordable: P2, P3.
   - Pick P3 (profit 5, risk 2).
   - Capital = 8, Remaining risk = 0.

**Result:** 8.

## ✅ Proof of Correctness

### Invariant
- The set of cost-affordable projects only grows as capital increases, so every
  project is pushed to the heap at most once.
- Remaining risk only decreases. If a project is too risky now, it will never
  become feasible later, so discarding it is safe.
- Choosing the feasible project with maximum profit maximizes the next capital
  and cannot reduce future affordability.

## 💡 Interview Extensions

- **Extension 1:** Capital consumed?
  - *Answer:* Then it becomes Knapsack-like (Cost/Profit trade-off).
- **Extension 2:** Risk decreases?
  - *Answer:* Then valid set grows.

### Common Mistakes to Avoid

1. **Risk Check Timing**
   - ❌ Wrong: Checking risk only when adding to heap.
   - ✅ Correct: Check risk when popping, because budget decreases.
2. **Capital Consumption**
   - ❌ Wrong: Subtracting cost from capital.
   - ✅ Correct: Capital only increases.

## Related Concepts

- **Greedy:** Standard approach.
