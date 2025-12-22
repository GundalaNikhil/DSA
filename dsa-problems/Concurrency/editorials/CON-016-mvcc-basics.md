---
problem_id: CON_MVCC_BASICS__A20E
display_id: CON-016
slug: mvcc-basics
title: "Multiversion Concurrency Control (MVCC) Basics"
difficulty: Medium
difficulty_score: 58
topics:
  - Concurrency
  - Databases
  - MVCC
  - Transactions
tags:
  - concurrency
  - mvcc
  - transactions
  - isolation
  - medium
premium: true
subscription_tier: basic
---

# Multiversion Concurrency Control (MVCC) Basics

## Problem summary

MVCC (Multi-Version Concurrency Control) allows:

- readers to read without blocking writers
- writers to write without blocking readers (mostly)

It does this by storing multiple versions of a record and deciding which version is visible to each transaction.

## What metadata exists per row/version

Most MVCC systems store something like:

- `created_by` (transaction id or commit timestamp)
- `deleted_by` (transaction id or commit timestamp), optional
- pointer to previous/next version (version chain)

Some systems use commit timestamps, some use transaction IDs plus commit lists. The concept is the same: each version has a “validity interval”.

## Snapshot reads (visibility rules)

When transaction `T` starts, it gets a snapshot:

- a read timestamp `ts` (or a set of visible committed transactions)

A version is visible to `T` if:

- it was created by a transaction committed before `T`’s snapshot, and
- it was not deleted by a transaction committed before `T`’s snapshot

So `T` sees a consistent point-in-time view, even while other transactions commit new versions.

This is why readers do not block writers: readers just follow version chains.

## Writes (creating new versions)

When `T` updates row `X`:

- it creates a new version `X'` linked to old version
- it typically locks the row for writing (or uses a write-intent marker)

Other transactions’ reads:

- still see the old version if their snapshot predates `T`’s commit
- see the new version if their snapshot is after `T`’s commit

So the same logical row can have multiple physical versions.

## Write-write conflicts

MVCC does not magically allow two writers to update the same row simultaneously without coordination.

Typical rule:

- first writer obtains the write lock / write-intent

Many databases use “first-committer-wins”:

- if two concurrent transactions attempt to update the same row, one will abort at commit time if it detects the row was updated since its snapshot.

This is often called a serialization failure.

## Garbage collection (vacuum)

Old versions cannot be kept forever:

- they consume space
- they lengthen version chains

Systems reclaim versions that are no longer visible to any active transaction:

- If the oldest active snapshot is newer than a version’s deletion, the version is safe to remove.

This is why long-running transactions can cause “bloat”: they prevent garbage collection.

## What interviewers expect

- You can explain “read snapshot sees old version”.
- You say writers create new versions and handle write-write conflicts by locking or aborting.
- You mention old versions are garbage-collected once no snapshots need them.

