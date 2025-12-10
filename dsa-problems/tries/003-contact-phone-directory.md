# Phone Directory Search

**Problem ID:** TRIE-003
**Display ID:** 92
**Question Name:** Phone Directory Search
**Slug:** contact-phone-directory
**Title:** Phone Directory Search
**Difficulty:** Medium
**Premium:** No
**Tags:** Trie, String, Design, Array

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Design a phone directory system that allows users to search for contacts by typing a prefix of either their name or phone number. The system should return all matching contacts sorted alphabetically by name.

## A Simple Scenario (Daily Life Usage)

You're using your iPhone or Android phone to find a contact. When you type "joh" in the search bar, it should show "John Smith", "Johnny Appleseed", and "Johnson Mike". Similarly, if you type "555", it should show all contacts whose phone numbers start with "555". This makes finding contacts quick and intuitive, especially when you have hundreds of contacts saved.

## Your Task

Implement the `PhoneDirectory` class:

- `PhoneDirectory()`: Initialize an empty phone directory
- `addContact(name, phoneNumber)`: Add a contact with the given name and phone number. Names are case-insensitive and unique.
- `searchByName(prefix)`: Return a list of all contact names that start with the given prefix (case-insensitive), sorted alphabetically
- `searchByNumber(prefix)`: Return a list of all contact names whose phone numbers start with the given prefix, sorted alphabetically by name

## Why is it Important?

This problem teaches you:

- Building multiple tries for different search criteria
- Implementing dual-index search systems
- Handling both alphabetic and numeric data in tries
- Real-world contact management algorithms used in smartphones

## Examples

### Example 1:

**Input:**
```
["PhoneDirectory", "addContact", "addContact", "addContact", "searchByName", "searchByName"]
[[], ["Alice", "1234567890"], ["Bob", "5551234567"], ["Alice Johnson", "9876543210"], ["ali"], ["bob"]]
```
**Output:**
```
[null, null, null, null, ["Alice", "Alice Johnson"], ["Bob"]]
```
**Explanation:**
- Add three contacts
- Search "ali" → matches "Alice" and "Alice Johnson"
- Search "bob" → matches "Bob"

### Example 2:

**Input:**
```
["PhoneDirectory", "addContact", "addContact", "addContact", "searchByNumber", "searchByNumber"]
[[], ["Charlie", "5551234567"], ["David", "5559876543"], ["Emma", "1234567890"], ["555"], ["123"]]
```
**Output:**
```
[null, null, null, null, ["Charlie", "David"], ["Emma"]]
```
**Explanation:**
- Add three contacts
- Search by number "555" → Charlie and David both have numbers starting with 555
- Search by number "123" → only Emma's number starts with 123

### Example 3:

**Input:**
```
["PhoneDirectory", "addContact", "addContact", "searchByName", "searchByNumber"]
[[], ["John Smith", "4155551234"], ["Johnny Appleseed", "4155559876"], ["john"], ["415"]]
```
**Output:**
```
[null, null, null, ["John Smith", "Johnny Appleseed"], ["John Smith", "Johnny Appleseed"]]
```
**Explanation:**
- Both contacts start with "john"
- Both phone numbers start with "415" (San Francisco area code)
- Results are sorted alphabetically: John Smith before Johnny Appleseed

## Constraints

- 1 <= name.length <= 50
- phoneNumber.length == 10 (standard US phone format)
- phoneNumber consists only of digits
- name consists of English letters and spaces
- 1 <= prefix.length <= 50 for name searches
- 1 <= prefix.length <= 10 for number searches
- At most 10,000 contacts will be added
- At most 5,000 searches will be performed
- Names are unique (case-insensitive)

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Apple
- Samsung
- Google
- WhatsApp

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
