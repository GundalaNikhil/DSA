# Emergency Room Triage

**Problem ID:** HEAP-001
**Display ID:** 84
**Question Name:** Emergency Room Triage
**Slug:** emergency-room-triage
**Title:** Find K Most Critical Patients
**Difficulty:** Medium
**Premium:** No
**Tags:** Heap, Priority Queue, Sorting

## Problem Description

You are building a triage system for a hospital emergency room. Patients arrive with different severity levels, and you need to efficiently identify the K most critical patients who should be treated first. Each patient has a severity score (1-10, where 10 is most critical), an arrival timestamp, and a patient ID.

## A Simple Scenario (Daily Life Usage)

Imagine you're the head nurse in a busy ER. Multiple patients are waiting, each with varying degrees of injury or illness. A severe car accident victim (severity 9) should be treated before someone with a minor cut (severity 2), regardless of arrival time. However, if two patients have the same severity, the one who arrived first gets priority. You need a system that quickly identifies the most critical cases.

## Your Task

Write a function that takes an array of patient records and returns the K most critical patients who should be treated immediately. Each patient is represented as:
- `patientId`: unique identifier (string)
- `severity`: critical level from 1-10 (integer)
- `arrivalTime`: timestamp when patient arrived (integer)

Return the K patients with the highest severity. If severities are equal, prioritize by earliest arrival time.

## Why is it Important?

This problem teaches you:

- Implementing and using max heaps for priority-based selection
- Handling multi-criteria sorting (severity first, then time)
- Efficient top-K element extraction
- Real-world healthcare system optimization
- Time complexity analysis with heaps (O(n log k) vs O(n log n))

## Examples

### Example 1:

**Input:**
```
patients = [
  {patientId: "P001", severity: 5, arrivalTime: 100},
  {patientId: "P002", severity: 9, arrivalTime: 105},
  {patientId: "P003", severity: 3, arrivalTime: 110},
  {patientId: "P004", severity: 9, arrivalTime: 102},
  {patientId: "P005", severity: 7, arrivalTime: 115}
]
k = 2
```

**Output:**
```
[
  {patientId: "P004", severity: 9, arrivalTime: 102},
  {patientId: "P002", severity: 9, arrivalTime: 105}
]
```

**Explanation:** Both P004 and P002 have severity 9 (highest). P004 arrived first (102 vs 105), so gets top priority.

### Example 2:

**Input:**
```
patients = [
  {patientId: "P101", severity: 4, arrivalTime: 200},
  {patientId: "P102", severity: 6, arrivalTime: 201},
  {patientId: "P103", severity: 8, arrivalTime: 202},
  {patientId: "P104", severity: 5, arrivalTime: 203}
]
k = 3
```

**Output:**
```
[
  {patientId: "P103", severity: 8, arrivalTime: 202},
  {patientId: "P102", severity: 6, arrivalTime: 201},
  {patientId: "P104", severity: 5, arrivalTime: 203}
]
```

**Explanation:** Top 3 by severity are P103 (8), P102 (6), and P104 (5).

### Example 3:

**Input:**
```
patients = [
  {patientId: "P201", severity: 10, arrivalTime: 300}
]
k = 1
```

**Output:**
```
[
  {patientId: "P201", severity: 10, arrivalTime: 300}
]
```

**Explanation:** Only one patient, so they are the most critical by default.

## Constraints

- 1 ≤ patients.length ≤ 10^4
- 1 ≤ k ≤ patients.length
- 1 ≤ severity ≤ 10
- 0 ≤ arrivalTime ≤ 10^6
- All patientIds are unique
- All arrivalTimes are unique

## Asked by Companies

- Epic Systems
- Cerner
- Allscripts
- athenahealth
