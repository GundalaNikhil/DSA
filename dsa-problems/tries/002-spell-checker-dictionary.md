# Word Spelling Validator

**Problem ID:** TRIE-002
**Display ID:** 91
**Question Name:** Word Spelling Validator
**Slug:** spell-checker-dictionary
**Title:** Word Spelling Validator
**Difficulty:** Easy
**Premium:** No
**Tags:** Trie, String, Design, Hash Table

## Problem Description

Build a spell checker that can validate whether words are spelled correctly and suggest adding new words to the dictionary. The system should efficiently check if a word exists in the dictionary.

## A Simple Scenario (Daily Life Usage)

You're writing an email in Gmail or composing a document in Microsoft Word. As you type, the spell checker needs to instantly verify if each word you write is in the dictionary. If you type "recieve", it should detect it's not a valid word (the correct spelling is "receive"). The system needs to be fast enough to check words in real-time as you type.

## Your Task

Implement the `SpellChecker` class:

- `SpellChecker()`: Initialize an empty dictionary
- `addWord(word)`: Add a word to the dictionary
- `checkSpelling(word)`: Return `true` if the word exists in the dictionary (exact match, case-insensitive), otherwise return `false`
- `searchPrefix(prefix)`: Return `true` if any word in the dictionary starts with the given prefix (case-insensitive), otherwise return `false`

## Why is it Important?

This problem teaches you:

- Basic trie data structure implementation
- Efficient word lookup operations
- Prefix matching for autocomplete features
- Case-insensitive string comparison in data structures

## Examples

### Example 1:

**Input:**
```
["SpellChecker", "addWord", "addWord", "checkSpelling", "checkSpelling", "checkSpelling"]
[[], ["hello"], ["world"], ["Hello"], ["goodbye"], ["WORLD"]]
```
**Output:**
```
[null, null, null, true, false, true]
```
**Explanation:**
- Add "hello" to dictionary
- Add "world" to dictionary
- "Hello" exists (case-insensitive match) → true
- "goodbye" doesn't exist → false
- "WORLD" exists (case-insensitive match) → true

### Example 2:

**Input:**
```
["SpellChecker", "addWord", "addWord", "searchPrefix", "searchPrefix", "checkSpelling"]
[[], ["application"], ["apple"], ["app"], ["ban"], ["app"]]
```
**Output:**
```
[null, null, null, true, false, false]
```
**Explanation:**
- Add "application" and "apple"
- "app" is a prefix of both words → true
- "ban" is not a prefix of any word → false
- "app" is not a complete word in dictionary → false

### Example 3:

**Input:**
```
["SpellChecker", "addWord", "checkSpelling", "addWord", "checkSpelling"]
[[], ["programming"], ["program"], ["program"], ["program"]]
```
**Output:**
```
[null, null, false, null, true]
```
**Explanation:**
- Add "programming"
- "program" is a prefix but not a complete word → false
- Add "program" as a complete word
- "program" now exists → true

## Constraints

- 1 <= word.length, prefix.length <= 200
- word and prefix consist of lowercase and uppercase English letters
- At most 30,000 calls will be made to addWord, checkSpelling, and searchPrefix
- All operations should be performed in O(L) time where L is the length of the word

## Asked by Companies

- Grammarly
- Microsoft
- Google
- Apple
