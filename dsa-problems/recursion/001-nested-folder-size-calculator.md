# Calculate Total Folder Size

**Problem ID:** REC-001
**Display ID:** 102
**Question Name:** Nested Folder Size Calculator
**Slug:** nested-folder-size-calculator
**Title:** Calculate Total Folder Size
**Difficulty:** Easy
**Premium:** No
**Tags:** Recursion, Tree Traversal, File System

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are building a disk space analyzer tool. Given a folder structure represented as a nested object, calculate the total size of a folder including all its subfolders and files. Each folder contains files (with sizes) and may contain other folders.

## A Simple Scenario (Daily Life Usage)

Imagine you're running low on disk space and need to find what's taking up all your storage. Tools like WinDirStat, TreeSize, or macOS Storage Manager recursively scan through folders to calculate total sizes. When you see that "Documents" folder is 50GB, that includes everything nested inside it - your work files, vacation photos in subfolders, and even hidden system files in subdirectories.

## Your Task

Write a recursive function that takes a folder structure and returns the total size in bytes. The folder structure is represented as an object where each folder has a `files` array (each file has a `size` property) and a `subfolders` array (which contains nested folder objects).

## Why is it Important?

This problem teaches you how to:

- Apply recursion to tree-like data structures
- Navigate nested hierarchies efficiently
- Understand how file systems organize data
- Build practical storage analysis tools

## Examples

### Example 1:

**Input:**
```javascript
{
  name: "root",
  files: [
    { name: "doc.txt", size: 100 },
    { name: "photo.jpg", size: 500 }
  ],
  subfolders: [
    {
      name: "work",
      files: [{ name: "report.pdf", size: 300 }],
      subfolders: []
    },
    {
      name: "music",
      files: [{ name: "song.mp3", size: 4000 }],
      subfolders: []
    }
  ]
}
```
**Output:** `4900`
**Explanation:**
- root files: 100 + 500 = 600
- work folder: 300
- music folder: 4000
- Total: 600 + 300 + 4000 = 4900 bytes

### Example 2:

**Input:**
```javascript
{
  name: "documents",
  files: [],
  subfolders: [
    {
      name: "personal",
      files: [{ name: "resume.doc", size: 250 }],
      subfolders: [
        {
          name: "photos",
          files: [{ name: "pic1.png", size: 1000 }],
          subfolders: []
        }
      ]
    }
  ]
}
```
**Output:** `1250`
**Explanation:** The deeply nested structure has 250 + 1000 = 1250 bytes total.

### Example 3:

**Input:**
```javascript
{
  name: "empty",
  files: [],
  subfolders: []
}
```
**Output:** `0`
**Explanation:** An empty folder has 0 bytes.

## Constraints

- 0 ≤ number of files in a folder ≤ 1000
- 0 ≤ number of subfolders ≤ 100
- 0 ≤ file size ≤ 10^9 bytes
- Maximum nesting depth: 50 levels
- Folder and file names are non-empty strings

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Dropbox
- Google Drive
- Box
- OneDrive
- Amazon S3
- Microsoft Azure

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
