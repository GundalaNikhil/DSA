# Network Traffic Director

**Problem ID:** TRIE-004
**Display ID:** 93
**Question Name:** Network Traffic Director
**Slug:** network-traffic-director
**Title:** Network Traffic Director
**Difficulty:** Hard
**Premium:** No
**Tags:** Trie, String, Bit Manipulation, Design

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Design a network traffic routing system that efficiently determines the best destination server for incoming data packets based on IP address patterns. In modern cloud infrastructure, when a packet arrives at a load balancer, it must quickly decide which backend server cluster should handle the request based on configured routing rules. When multiple routing patterns match, the system should select the most specific pattern to ensure optimal routing.

## A Simple Scenario (Daily Life Usage)

You're building a cloud load balancer for a company's microservices architecture. Your system receives millions of requests per second, and each request needs to be routed to the appropriate backend service based on the client's IP address. For instance, you might route all traffic from "10.5.0.0" through "10.5.255.255" to the "analytics-service", but traffic specifically from "10.5.12.0" through "10.5.12.255" should go to the "premium-analytics-service" instead. The challenge is making this routing decision in microseconds while handling overlapping patterns correctly.

## Your Task

Implement the `NetworkRouter` class:

- `NetworkRouter()`: Initialize an empty routing configuration
- `void addRoute(String ipPattern, int matchBits, String targetServer)`: Configure a routing rule where packets from IPs matching the pattern (using the first matchBits for comparison) should be sent to targetServer
- `String findDestination(String sourceIP)`: Return the targetServer for the most specific matching pattern. Return an empty string "" if no pattern matches

Notes:
- IP addresses are in standard IPv4 format: "W.X.Y.Z" where each octet is 0-255
- matchBits represents how many leading bits must match (similar to network masks)
- When multiple patterns match, choose the one with the highest matchBits value (most specific)

## Why is it Important?

This problem teaches you:

- Building efficient binary trie structures for network operations
- Understanding how IP address matching works in real network systems
- Implementing longest prefix matching algorithms used in production routers
- Working with binary representations and bit-level operations
- Optimizing for both speed and memory in system design problems

## Examples

### Example 1:

**Input:**
```
["NetworkRouter", "addRoute", "addRoute", "findDestination", "findDestination", "findDestination"]
[[], ["10.20.0.0", 16, "service-main"], ["10.20.5.0", 24, "service-premium"], ["10.20.5.100"], ["10.20.8.50"], ["172.16.0.1"]]
```
**Output:**
```
[null, null, null, "service-premium", "service-main", ""]
```
**Explanation:**
- Configure: 10.20.0.0 with 16 matching bits → routes to service-main (covers 10.20.x.x)
- Configure: 10.20.5.0 with 24 matching bits → routes to service-premium (covers 10.20.5.x)
- Query 10.20.5.100: Matches both patterns, but 24-bit match is more specific → "service-premium"
- Query 10.20.8.50: Only matches 16-bit pattern → "service-main"
- Query 172.16.0.1: No matching patterns → ""

### Example 2:

**Input:**
```
["NetworkRouter", "addRoute", "addRoute", "addRoute", "findDestination"]
[[], ["0.0.0.0", 0, "default-cluster"], ["10.0.0.0", 8, "internal-network"], ["10.50.25.0", 24, "analytics-cluster"], ["10.50.25.200"]]
```
**Output:**
```
[null, null, null, null, "analytics-cluster"]
```
**Explanation:**
- 0.0.0.0 with 0 bits matches everything (catch-all default)
- 10.0.0.0 with 8 bits matches all 10.x.x.x addresses
- 10.50.25.0 with 24 bits matches 10.50.25.x addresses
- Query 10.50.25.200 matches all three, most specific is 24-bit → "analytics-cluster"

### Example 3:

**Input:**
```
["NetworkRouter", "addRoute", "addRoute", "addRoute", "findDestination", "findDestination", "findDestination"]
[[], ["192.100.0.0", 16, "region-west"], ["192.100.50.0", 24, "datacenter-A"], ["192.100.50.128", 25, "rack-premium"], ["192.100.50.10"], ["192.100.50.150"], ["192.100.75.1"]]
```
**Output:**
```
[null, null, null, null, "datacenter-A", "rack-premium", "region-west"]
```
**Explanation:**
- 192.100.50.10 matches 16-bit and 24-bit patterns → choose 24-bit "datacenter-A"
- 192.100.50.150 matches all three patterns → choose 25-bit "rack-premium" (most specific)
- 192.100.75.1 only matches 16-bit pattern → "region-west"

## Constraints

- All IP addresses are valid IPv4 addresses in dotted decimal format
- 0 <= matchBits <= 32
- 1 <= targetServer.length <= 60
- At most 15,000 routing rules will be configured
- At most 100,000 routing queries will be performed
- Your solution should handle each query in O(32) = O(1) time

## Asked by Companies

**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.

- Cloud Infrastructure Providers
- Content Delivery Networks (CDN)
- Network Equipment Manufacturers
- Enterprise Load Balancer Companies
- Cybersecurity Firms

---

## Hints

<details>
<summary>Hint 1: Binary Representation</summary>

Think about converting each IP address to its 32-bit binary representation. For example, "192.168.1.1" becomes a 32-bit number. This allows you to compare IPs bit by bit.

</details>

<details>
<summary>Hint 2: Trie Structure</summary>

A binary trie (where each node has at most 2 children: 0 and 1) is perfect for this problem. Each path from root to a node represents a sequence of bits, and you can store the routing target at the appropriate depth.

</details>

<details>
<summary>Hint 3: Longest Prefix Matching</summary>

When searching, traverse the trie following the bits of the query IP. Keep track of the last node that had a routing target stored. This represents the longest (most specific) matching pattern.

</details>

<details>
<summary>Hint 4: IP to Binary Conversion</summary>

To convert an IP "W.X.Y.Z" to binary: combine (W << 24) | (X << 16) | (Y << 8) | Z. Then you can check individual bits using bit shifting and masking.

</details>

---

## Related Topics

- Binary Trie Implementation
- Prefix Matching Algorithms
- CIDR Notation and Subnetting
- Bit Manipulation Techniques
- Network Routing Fundamentals

---

## Difficulty Justification

**Why Hard?**

1. Requires understanding of binary tries (not a common data structure)
2. Involves bit manipulation and binary representations
3. Must handle overlapping patterns correctly (longest prefix matching)
4. Needs to convert between IP string format and binary efficiently
5. Combines multiple concepts: tries, bit operations, and system design

**What makes it achievable?**

- The trie depth is limited to 32 bits (constant)
- IP address format is standardized and predictable
- Clear algorithmic approach once you understand tries
- Each operation has bounded complexity

---

**Disclaimer:** While this problem involves classic computer networking concepts that are part of common computer science knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
