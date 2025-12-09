# Flatten Nested Comment Threads

**Problem ID:** REC-002
**Display ID:** 103
**Question Name:** Comment Thread Flattener
**Slug:** comment-thread-flattener
**Title:** Flatten Nested Comment Threads
**Difficulty:** Medium
**Premium:** No
**Tags:** Recursion, Tree Traversal, Depth-First Search

## Problem Description

You are building a comment system like Reddit or Hacker News. Comments can have replies, and those replies can have their own replies, creating a nested tree structure. Convert this nested comment tree into a flat array where each comment includes its indentation level (depth in the tree).

## A Simple Scenario (Daily Life Usage)

When you browse Reddit or Hacker News, you see comments with visual indentation showing the conversation hierarchy. A top-level comment has depth 0, its direct replies have depth 1, replies to those have depth 2, and so on. Behind the scenes, the nested tree structure needs to be flattened for display, preserving the conversation flow and indentation levels.

## Your Task

Write a recursive function that takes a nested comment structure and returns a flat array of comments, where each comment object includes a `depth` property indicating its nesting level. Process comments in depth-first order (traverse deeply before moving to siblings).

## Why is it Important?

This problem teaches you how to:

- Perform depth-first traversal on tree structures
- Track recursion depth for indentation
- Transform hierarchical data for display
- Understand how discussion platforms organize threads

## Examples

### Example 1:

**Input:**
```javascript
{
  id: 1,
  text: "Great article!",
  replies: [
    {
      id: 2,
      text: "I agree!",
      replies: [
        {
          id: 3,
          text: "Me too!",
          replies: []
        }
      ]
    },
    {
      id: 4,
      text: "Thanks for sharing",
      replies: []
    }
  ]
}
```
**Output:**
```javascript
[
  { id: 1, text: "Great article!", depth: 0 },
  { id: 2, text: "I agree!", depth: 1 },
  { id: 3, text: "Me too!", depth: 2 },
  { id: 4, text: "Thanks for sharing", depth: 1 }
]
```
**Explanation:** DFS traversal processes comment 1, then its first reply (2), then 2's reply (3), then back to 1's second reply (4).

### Example 2:

**Input:**
```javascript
{
  id: 10,
  text: "Root comment",
  replies: []
}
```
**Output:**
```javascript
[
  { id: 10, text: "Root comment", depth: 0 }
]
```
**Explanation:** Single comment with no replies stays at depth 0.

### Example 3:

**Input:**
```javascript
{
  id: 100,
  text: "Hot take",
  replies: [
    {
      id: 101,
      text: "Disagree",
      replies: []
    },
    {
      id: 102,
      text: "Agree",
      replies: []
    },
    {
      id: 103,
      text: "Neutral",
      replies: []
    }
  ]
}
```
**Output:**
```javascript
[
  { id: 100, text: "Hot take", depth: 0 },
  { id: 101, text: "Disagree", depth: 1 },
  { id: 102, text: "Agree", depth: 1 },
  { id: 103, text: "Neutral", depth: 1 }
]
```
**Explanation:** All replies are at depth 1, processed in order.

## Constraints

- 1 ≤ number of comments in tree ≤ 10,000
- 0 ≤ number of replies per comment ≤ 100
- 0 ≤ depth ≤ 20 levels
- Each comment has a unique integer id
- Text is a non-empty string (max 1000 characters)

## Asked by Companies

- Reddit
- Hacker News
- Disqus
- Facebook
- Twitter
- Stack Overflow
