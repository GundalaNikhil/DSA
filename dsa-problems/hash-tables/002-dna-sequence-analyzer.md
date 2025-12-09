# DNA Sequence Analyzer

**Problem ID:** HASH-002
**Display ID:** 37
**Question Name:** DNA Sequence Analyzer
**Slug:** dna-sequence-analyzer
**Title:** Group Anagrams
**Difficulty:** Medium
**Premium:** No
**Tags:** Hash Table, String, Sorting, Array

## Problem Description

Given an array of strings representing DNA sequences, group the sequences that are anagrams of each other. Return the grouped sequences in any order.

## A Simple Scenario (Daily Life Usage)

You're working at a genetics laboratory analyzing DNA samples. Different samples might contain the same nucleotides but in different orders - these are considered similar sequences worth grouping together for analysis. For example, "ATCG" and "CGTA" contain the same genetic material and should be grouped together for comparative study.

## Your Task

Write a function that takes an array of DNA sequence strings and groups all anagrams together. Each group should contain all sequences that are anagrams of each other.

## Why is it Important?

This problem teaches you:

- Hash table key design for grouping
- String sorting and comparison techniques
- Efficient categorization algorithms
- Real-world data organization in bioinformatics

## Examples

### Example 1:

**Input:** `sequences = ["ATCG", "CGTA", "GGCC", "CCGG", "ATGC"]`
**Output:** `[["ATCG", "CGTA"], ["GGCC", "CCGG"], ["ATGC"]]`
**Explanation:** ATCG and CGTA are anagrams, GGCC and CCGG are anagrams, ATGC is unique.

### Example 2:

**Input:** `sequences = ["A"]`
**Output:** `[["A"]]`
**Explanation:** Single sequence forms its own group.

### Example 3:

**Input:** `sequences = ["AAA", "AAA", "BBB"]`
**Output:** `[["AAA", "AAA"], ["BBB"]]`
**Explanation:** Identical sequences are also grouped together.

## Constraints

- 1 ≤ sequences.length ≤ 10,000
- 0 ≤ sequences[i].length ≤ 100
- sequences[i] consists of uppercase English letters only
- Each sequence represents a valid DNA pattern

## Asked by Companies

- 23andMe
- Illumina
- Thermo Fisher
- GenScript
