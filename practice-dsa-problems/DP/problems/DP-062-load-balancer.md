# DP-062: Load Balancer DP

## Problem Statement

You have `s` servers and `n` requests in order. Request `i` has size `w_i`. Server `j` has capacity `cap_j` and latency cost `lat_j`. If a request assigned to server `j` causes total assigned load to exceed `cap_j`, you pay an overload penalty `P` for that request.

Minimize total latency plus overload penalties.

## Input Format

- First line: integers `n`, `s`, `P`
- Second line: `n` integers: request sizes
- Third line: `s` integers: capacities
- Fourth line: `s` integers: latencies

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= n <= 60`
- `1 <= s <= 4`
- `0 <= P <= 10^6`
- `0 <= sizes, capacities, latencies <= 50`

## Clarifying Notes

- Each request must be assigned to exactly one server.
- Total load per server is cumulative over all requests.

## Example Input

```
3 2 5
2 3 4
4 5
1 2
```

## Example Output

```
9
```
