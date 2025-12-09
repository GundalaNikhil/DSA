# Domain Name Resolution Cache

**Problem ID:** TRIE-006
**Display ID:** 95
**Question Name:** Domain Name Resolution Cache
**Slug:** dns-domain-lookup
**Title:** Domain Name Resolution Cache
**Difficulty:** Medium
**Premium:** No
**Tags:** Trie, String, Design, Hash Table

## Problem Description

Design a DNS (Domain Name System) cache that stores domain-to-IP mappings and supports efficient subdomain lookups. Domain names should be stored in reverse order (from right to left) to enable efficient parent domain matching. For example, "api.example.com" should match both "api.example.com" and wildcard entries for "*.example.com".

## A Simple Scenario (Daily Life Usage)

You're building a DNS resolver for Cloudflare or Google's DNS service (8.8.8.8). When someone visits "blog.techcompany.com", your system needs to quickly find the IP address. If there's no exact match, it should check parent domains like "techcompany.com" or wildcard entries like "*.techcompany.com". This hierarchy mimics how real DNS works - if a specific subdomain isn't found, you check the parent domain. Caching these lookups makes web browsing faster.

## Your Task

Implement the `DNSCache` class:

- `DNSCache()`: Initialize an empty DNS cache
- `addMapping(domain, ipAddress)`: Add a domain-to-IP mapping to the cache
- `addWildcard(parentDomain, ipAddress)`: Add a wildcard mapping where *.parentDomain maps to the IP address
- `resolve(domain)`: Return the IP address for the domain. Check exact matches first, then wildcard matches. Return empty string "" if no match found.

Resolution priority:
1. Exact domain match (e.g., "api.example.com")
2. Wildcard match (e.g., "*.example.com" matches "api.example.com")
3. No match → return ""

## Why is it Important?

This problem teaches you:

- Reverse trie implementation for hierarchical data
- Domain name hierarchy and DNS resolution
- Wildcard pattern matching in tries
- How internet DNS caching works at ISPs and DNS providers

## Examples

### Example 1:

**Input:**
```
["DNSCache", "addMapping", "addMapping", "resolve", "resolve", "resolve"]
[[], ["example.com", "93.184.216.34"], ["api.example.com", "192.0.2.1"], ["example.com"], ["api.example.com"], ["test.example.com"]]
```
**Output:**
```
[null, null, null, "93.184.216.34", "192.0.2.1", ""]
```
**Explanation:**
- Add exact mappings for "example.com" and "api.example.com"
- Resolve "example.com" → exact match found
- Resolve "api.example.com" → exact match found
- Resolve "test.example.com" → no match (no wildcard configured)

### Example 2:

**Input:**
```
["DNSCache", "addMapping", "addWildcard", "resolve", "resolve", "resolve"]
[[], ["google.com", "142.250.185.46"], ["google.com", "192.168.1.1"], ["mail.google.com"], ["drive.google.com"], ["google.com"]]
```
**Output:**
```
[null, null, null, "192.168.1.1", "192.168.1.1", "142.250.185.46"]
```
**Explanation:**
- Add exact mapping for "google.com" → 142.250.185.46
- Add wildcard *.google.com → 192.168.1.1
- Resolve "mail.google.com" → no exact match, wildcard matches → 192.168.1.1
- Resolve "drive.google.com" → wildcard match → 192.168.1.1
- Resolve "google.com" → exact match takes priority → 142.250.185.46

### Example 3:

**Input:**
```
["DNSCache", "addWildcard", "addMapping", "resolve", "resolve"]
[[], ["cdn.cloudflare.net", "104.16.132.229"], ["assets.cdn.cloudflare.net", "104.16.133.229"], ["images.cdn.cloudflare.net"], ["assets.cdn.cloudflare.net"]]
```
**Output:**
```
[null, null, null, "104.16.132.229", "104.16.133.229"]
```
**Explanation:**
- Add wildcard *.cdn.cloudflare.net → 104.16.132.229
- Add exact mapping for "assets.cdn.cloudflare.net" → 104.16.133.229
- Resolve "images.cdn.cloudflare.net" → wildcard match → 104.16.132.229
- Resolve "assets.cdn.cloudflare.net" → exact match (priority) → 104.16.133.229

## Constraints

- 1 <= domain.length <= 100
- domain consists of lowercase English letters, digits, dots '.', and hyphens '-'
- domain follows valid DNS naming conventions
- ipAddress is a valid IPv4 address (e.g., "192.168.1.1")
- At most 10,000 mappings will be added
- At most 50,000 resolve calls will be made
- All operations should be O(L) where L is the length of the domain name

## Asked by Companies

- Cloudflare
- AWS Route53
- Google Cloud DNS
- Akamai
