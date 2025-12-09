# Count All Subordinates

**Problem ID:** REC-004
**Display ID:** 105
**Question Name:** Organizational Reporting Chain
**Slug:** organizational-reporting-chain
**Title:** Count All Subordinates
**Difficulty:** Easy
**Premium:** No
**Tags:** Recursion, Tree Traversal, Graph

## Problem Description

You are building an HR analytics tool for a company. Given an organizational chart where each employee can manage other employees, calculate the total number of people reporting to a specific manager, including both direct reports and indirect reports (reports of reports, and so on).

## A Simple Scenario (Daily Life Usage)

In a company, a CEO might have 5 VPs reporting directly to them, but each VP manages directors, who manage managers, who manage individual contributors. When HR needs to know the "span of control" for the CEO, they don't just count the 5 VPs - they count everyone in the entire organization. If a VP is being promoted, HR needs to quickly calculate how many total employees will be affected by the transition.

## Your Task

Write a recursive function that takes an employee object (with a `directReports` array containing their direct reports) and returns the total count of all employees reporting to them, directly or indirectly. Don't count the manager themselves.

## Why is it Important?

This problem teaches you how to:

- Apply recursion to organizational hierarchies
- Count nodes in a tree structure
- Understand reporting relationships in companies
- Build HR analytics and org chart tools

## Examples

### Example 1:

**Input:**
```javascript
{
  name: "Alice (CEO)",
  directReports: [
    {
      name: "Bob (VP)",
      directReports: [
        {
          name: "Charlie (Manager)",
          directReports: []
        },
        {
          name: "Diana (Manager)",
          directReports: []
        }
      ]
    },
    {
      name: "Eve (VP)",
      directReports: [
        {
          name: "Frank (Manager)",
          directReports: []
        }
      ]
    }
  ]
}
```
**Output:** `5`
**Explanation:**
- Direct reports: Bob, Eve (2 people)
- Bob's reports: Charlie, Diana (2 people)
- Eve's reports: Frank (1 person)
- Total: 2 + 2 + 1 = 5 subordinates

### Example 2:

**Input:**
```javascript
{
  name: "Manager",
  directReports: []
}
```
**Output:** `0`
**Explanation:** No one reports to this person.

### Example 3:

**Input:**
```javascript
{
  name: "Director",
  directReports: [
    {
      name: "Team Lead A",
      directReports: [
        { name: "Dev 1", directReports: [] },
        { name: "Dev 2", directReports: [] },
        { name: "Dev 3", directReports: [] }
      ]
    },
    {
      name: "Team Lead B",
      directReports: [
        { name: "Dev 4", directReports: [] },
        { name: "Dev 5", directReports: [] }
      ]
    }
  ]
}
```
**Output:** `7`
**Explanation:**
- Direct reports: Team Lead A, Team Lead B (2)
- Team Lead A's reports: Dev 1, 2, 3 (3)
- Team Lead B's reports: Dev 4, 5 (2)
- Total: 2 + 3 + 2 = 7 subordinates

### Example 4:

**Input:**
```javascript
{
  name: "Senior Manager",
  directReports: [
    {
      name: "Junior Manager",
      directReports: [
        {
          name: "Intern Coordinator",
          directReports: [
            { name: "Intern 1", directReports: [] },
            { name: "Intern 2", directReports: [] }
          ]
        }
      ]
    }
  ]
}
```
**Output:** `4`
**Explanation:** Deep hierarchy: 1 + 1 + 2 = 4 total subordinates across all levels.

## Constraints

- 0 ≤ number of direct reports per person ≤ 50
- 1 ≤ total employees in tree ≤ 10,000
- 0 ≤ organizational depth ≤ 15 levels
- Each employee has a unique name
- No circular reporting relationships (tree structure)

## Asked by Companies

- Workday
- SAP
- Oracle (PeopleSoft)
- BambooHR
- ADP
- LinkedIn
- Microsoft (Teams/Delve)
