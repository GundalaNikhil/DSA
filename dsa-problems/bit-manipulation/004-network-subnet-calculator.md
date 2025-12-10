# IP Address Subnet Matching

**Problem ID:** BIT-004
**Display ID:** 99
**Question Name:** IP Address Subnet Matching
**Slug:** network-subnet-calculator
**Title:** IP Address Subnet Matching
**Difficulty:** Medium
**Premium:** No
**Tags:** Bit Manipulation, Networking, Bitwise AND

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Implement a network subnet calculator to determine if an IP address belongs to a specific subnet using CIDR notation. An IPv4 address is represented as a 32-bit integer, and a subnet is defined by a base IP and a prefix length (number of network bits). Use bitwise operations to check if an IP matches the subnet.

## A Simple Scenario (Daily Life Usage)

You're configuring a firewall at a company. Your internal network is `192.168.1.0/24`, meaning the first 24 bits identify the network. When someone at IP `192.168.1.50` tries to access resources, your firewall checks: does this IP belong to our subnet? Using a subnet mask (first 24 bits all 1s), you AND both the base IP and the incoming IP with the mask. They match! Access granted. But `192.168.2.50` doesn't match - access denied.

## Your Task

Implement the following functions:
- `ipBelongsToSubnet(ip, subnetBase, prefixLength)`: Check if an IP belongs to a subnet
- `createSubnetMask(prefixLength)`: Create a subnet mask from prefix length
- `getNetworkAddress(ip, prefixLength)`: Get the network address for an IP
- `getBroadcastAddress(subnetBase, prefixLength)`: Get the broadcast address for a subnet
- `countUsableHosts(prefixLength)`: Count usable host addresses in a subnet

Where:
- `ip` and `subnetBase` are 32-bit integers representing IPv4 addresses
- `prefixLength` is an integer from 0 to 32 representing network bits

## Why is it Important?

This problem teaches you how to:

- Apply bitwise AND for network masking
- Use left shifts to create subnet masks
- Understand CIDR notation and subnetting
- Work with IP address binary representations
- Solve real networking problems
- Optimize network security checks

## Examples

### Example 1:

**Input:** `ip = 3232235826 (192.168.1.50), subnetBase = 3232235776 (192.168.1.0), prefixLength = 24`
**Output:** `true`
**Explanation:**
- Subnet mask for /24: 0xFFFFFF00 (first 24 bits are 1)
- ip & mask = 3232235776
- subnetBase & mask = 3232235776
- They match, so IP is in subnet

### Example 2:

**Input:** `ip = 3232236082 (192.168.2.50), subnetBase = 3232235776 (192.168.1.0), prefixLength = 24`
**Output:** `false`
**Explanation:**
- ip & mask = 3232236032 (192.168.2.0)
- subnetBase & mask = 3232235776 (192.168.1.0)
- Different networks, so IP is not in subnet

### Example 3:

**Input:** `prefixLength = 24, operation = "createSubnetMask"`
**Output:** `4294967040` (0xFFFFFF00 in decimal)
**Explanation:** /24 means first 24 bits are 1: 11111111.11111111.11111111.00000000

### Example 4:

**Input:** `ip = 3232235826 (192.168.1.50), prefixLength = 24, operation = "getNetworkAddress"`
**Output:** `3232235776` (192.168.1.0)
**Explanation:** AND with subnet mask gives network address.

### Example 5:

**Input:** `subnetBase = 3232235776 (192.168.1.0), prefixLength = 24, operation = "getBroadcastAddress"`
**Output:** `3232236031` (192.168.1.255)
**Explanation:** Network address OR with inverted mask gives broadcast address.

### Example 6:

**Input:** `prefixLength = 24, operation = "countUsableHosts"`
**Output:** `254`
**Explanation:** /24 has 2^(32-24) = 256 addresses. Subtract 2 (network and broadcast) = 254 usable hosts.

### Example 7:

**Input:** `ip = 167772162 (10.0.0.2), subnetBase = 167772160 (10.0.0.0), prefixLength = 30`
**Output:** `true`
**Explanation:** /30 subnet has only 4 addresses (10.0.0.0 to 10.0.0.3). IP 10.0.0.2 is within range.

## Constraints

- 0 ≤ ip, subnetBase ≤ 2^32 - 1
- 0 ≤ prefixLength ≤ 32
- All operations should run in O(1) time
- Use only bitwise operations
- IPs are represented as 32-bit unsigned integers

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Cisco
- Palo Alto Networks
- Fortinet
- AWS

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
