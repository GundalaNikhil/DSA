# Longest Prefix IP Routing

**Problem ID:** TRIE-004
**Display ID:** 93
**Question Name:** Longest Prefix IP Routing
**Slug:** ip-address-router
**Title:** Longest Prefix IP Routing
**Difficulty:** Hard
**Premium:** No
**Tags:** Trie, String, Bit Manipulation, Design

## Problem Description

Design an IP routing table that efficiently finds the longest matching prefix for a given IP address. When a packet arrives at a router, it needs to determine which network interface to forward it to based on the destination IP address. Multiple routing rules may match, but the most specific (longest prefix) should be selected.

## A Simple Scenario (Daily Life Usage)

You're configuring a network router at a company like Cisco. The router has multiple network interfaces and needs to decide where to send each data packet. For example, if you have routes for "192.168.0.0/16" (general company network) and "192.168.1.0/24" (engineering subnet), a packet destined for "192.168.1.50" should match the more specific "/24" route, not the broader "/16" route. This ensures packets take the optimal path through the network.

## Your Task

Implement the `IPRouter` class:

- `IPRouter()`: Initialize an empty routing table
- `addRoute(ipPrefix, prefixLength, nextHop)`: Add a routing rule where packets matching the IP prefix with the given prefix length should be forwarded to nextHop
- `route(destinationIP)`: Return the nextHop for the longest matching prefix. If no route matches, return empty string ""

IP addresses are represented as strings in dotted decimal notation (e.g., "192.168.1.1").
Prefix length is in CIDR notation (e.g., 24 means the first 24 bits must match).

## Why is it Important?

This problem teaches you:

- Binary trie implementation for IP routing
- Longest prefix matching algorithm used in real routers
- Converting IP addresses to binary representation
- CIDR notation and subnet masking
- How internet routing works at a fundamental level

## Examples

### Example 1:

**Input:**
```
["IPRouter", "addRoute", "addRoute", "route", "route", "route"]
[[], ["192.168.0.0", 16, "Interface-A"], ["192.168.1.0", 24, "Interface-B"], ["192.168.1.50"], ["192.168.2.10"], ["10.0.0.1"]]
```
**Output:**
```
[null, null, null, "Interface-B", "Interface-A", ""]
```
**Explanation:**
- Add route: 192.168.0.0/16 → Interface-A (matches 192.168.x.x)
- Add route: 192.168.1.0/24 → Interface-B (matches 192.168.1.x)
- 192.168.1.50 matches both routes, but /24 is longer → Interface-B
- 192.168.2.10 only matches /16 route → Interface-A
- 10.0.0.1 matches no routes → ""

### Example 2:

**Input:**
```
["IPRouter", "addRoute", "addRoute", "addRoute", "route"]
[[], ["0.0.0.0", 0, "Default-Gateway"], ["10.0.0.0", 8, "Private-Network"], ["10.1.1.0", 24, "Engineering"], ["10.1.1.100"]]
```
**Output:**
```
[null, null, null, null, "Engineering"]
```
**Explanation:**
- 0.0.0.0/0 matches everything (default route)
- 10.0.0.0/8 matches all 10.x.x.x addresses
- 10.1.1.0/24 matches 10.1.1.x addresses
- 10.1.1.100 matches all three, but /24 is most specific → Engineering

### Example 3:

**Input:**
```
["IPRouter", "addRoute", "addRoute", "route", "route"]
[[], ["172.16.0.0", 12, "Corp-Network"], ["172.16.5.0", 24, "Marketing"], ["172.16.5.50"], ["172.20.1.1"]]
```
**Output:**
```
[null, null, null, "Marketing", "Corp-Network"]
```
**Explanation:**
- 172.16.5.50 matches both routes → choose Marketing (longer prefix)
- 172.20.1.1 matches only Corp-Network (/12 covers 172.16-31.x.x)

## Constraints

- IP addresses are valid IPv4 addresses in dotted decimal notation
- 0 <= prefixLength <= 32
- 1 <= nextHop.length <= 50
- At most 10,000 routes will be added
- At most 50,000 route lookups will be performed
- Routing decisions must be O(32) = O(1) time complexity

## Asked by Companies

- Cisco
- Juniper
- Arista
- Cloudflare
