# Deep Object Value Finder

**Problem ID:** REC-003
**Display ID:** 104
**Question Name:** JSON Config Parser
**Slug:** json-config-parser
**Title:** Deep Object Value Finder
**Difficulty:** Medium
**Premium:** No
**Tags:** Recursion, Object Traversal, String Parsing

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are building a configuration management system. Given a nested JSON-like object (configuration file) and a dot-notation path string (like "database.connection.host"), recursively find and return the value at that path. Return null if the path doesn't exist.

## A Simple Scenario (Daily Life Usage)

Modern applications use nested configuration files (JSON, YAML, etc.) to manage settings. Tools like Terraform, Docker Compose, and Kubernetes need to extract specific values from deeply nested configs. For example, getting "server.security.ssl.enabled" from a config file that has multiple levels of nesting. Rather than manually navigating each level, a recursive parser can follow the path and retrieve the value.

## Your Task

Write a recursive function that takes a nested object and a dot-notation path string, then returns the value at that path. If any key in the path doesn't exist, return null. Handle nested objects of any depth.

## Why is it Important?

This problem teaches you how to:

- Parse and process path strings recursively
- Navigate nested object structures dynamically
- Handle missing keys gracefully
- Build configuration management utilities

## Examples

### Example 1:

**Input:**
```javascript
config = {
  database: {
    host: "localhost",
    port: 5432,
    credentials: {
      username: "admin",
      password: "secret123"
    }
  },
  cache: {
    enabled: true
  }
}
path = "database.credentials.username"
```
**Output:** `"admin"`
**Explanation:** Follow the path: database → credentials → username = "admin"

### Example 2:

**Input:**
```javascript
config = {
  server: {
    name: "prod-server-01",
    region: "us-east-1"
  }
}
path = "server.security.firewall"
```
**Output:** `null`
**Explanation:** "security" doesn't exist under "server", so return null.

### Example 3:

**Input:**
```javascript
config = {
  app: {
    version: "2.1.0",
    features: {
      auth: {
        oauth: {
          providers: ["google", "github", "microsoft"]
        }
      }
    }
  }
}
path = "app.features.auth.oauth.providers"
```
**Output:** `["google", "github", "microsoft"]`
**Explanation:** Successfully navigates through 5 levels to find the array.

### Example 4:

**Input:**
```javascript
config = {
  api: {
    timeout: 30
  }
}
path = "api.timeout"
```
**Output:** `30`
**Explanation:** Simple two-level path returns the number 30.

### Example 5:

**Input:**
```javascript
config = {
  settings: {
    theme: "dark"
  }
}
path = "settings"
```
**Output:** `{ theme: "dark" }`
**Explanation:** Path points to an object, so return the entire object.

## Constraints

- 1 ≤ object depth ≤ 20 levels
- 1 ≤ path length ≤ 100 characters
- Path contains only alphanumeric characters and dots
- Object keys are non-empty strings
- Values can be: string, number, boolean, array, object, or null
- No circular references in the object

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- HashiCorp
- Docker
- Kubernetes
- Terraform
- AWS (CloudFormation)
- Google Cloud
- Ansible

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
