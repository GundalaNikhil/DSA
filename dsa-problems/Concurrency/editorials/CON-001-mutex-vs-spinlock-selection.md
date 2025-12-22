---
problem_id: CON_LOCK_CHOICE__A9F1
display_id: CON-001
slug: mutex-vs-spinlock-selection
title: "Mutex vs Spinlock Selection"
difficulty: Easy
difficulty_score: 28
topics:
  - Concurrency
  - Locks
  - Performance
tags:
  - concurrency
  - mutex
  - spinlock
  - easy
premium: true
subscription_tier: basic
---

# Mutex vs Spinlock Selection

## What the question is really testing

This problem is not about memorizing “spinlocks are faster” or “mutexes are safer”. It is testing whether you can reason about:

- how long a thread is expected to wait
- what happens to the CPU while waiting (busy-wait vs park)
- what the OS scheduler costs (park/unpark + context switches)
- how oversubscription changes everything (more runnable threads than cores)

If you cannot explain those tradeoffs clearly, you do not actually understand lock selection.

## Key definitions (brutally precise)

- Mutex (sleeping lock): if lock is not available, the OS can park the thread, freeing the CPU for other work. This usually implies context switches and scheduler latency.
- Spinlock (busy-wait): if lock is not available, the thread repeatedly checks until it becomes available. The CPU is occupied doing “nothing useful” while spinning.

## Decision rule of thumb (with the right caveats)

Compare expected wait `w` to critical-section time `cs`:

- Prefer a spinlock when:
  - expected wait is very short (often on the order of tens to a few hundreds of nanoseconds to a few microseconds, depending on platform)
  - the system is not oversubscribed (approximately 1 runnable thread per core for the hot path)
  - the lock holder is running and will release soon (no I/O, no blocking inside the critical section)

- Prefer a mutex when:
  - expected wait is meaningfully larger than the lock holder’s remaining time
  - the system can be oversubscribed (typical servers: yes)
  - the lock holder might be preempted or block (I/O, page fault, sleep, etc.)
  - fairness matters (spinlocks can be very unfair without extra mechanisms)

In other words: spin when the wait is so short that sleeping would cost more than waiting; otherwise sleep.

## Why `w` matters more than `cs`

Students often incorrectly compare only `cs` and ignore contention.

The important quantity is the time you spend *not making progress*:

- A thread that spins for 50µs is burning 50µs of CPU time doing no useful work.
- If you have many contending threads, that wasted CPU time multiplies and can destroy throughput.

So if `w >> cs`, that is the classic “mutex is better” case.

## A clean justification format for interviews

When given numbers, justify like this:

1) “We expect to wait about `w` microseconds per contending thread.”
2) “A spinlock would burn CPU for ~`w` while doing no useful work.”
3) “A mutex can park the thread; the overhead is a context switch and scheduler latency.”
4) “Since `w` is (much larger / much smaller) than the typical park/unpark cost, choose (mutex / spinlock).”
5) “Assumptions: (oversubscription / core count / preemption).”

This avoids hand-wavy answers.

## Walkthrough of the sample

Sample: `cs = 1µs`, `w = 50µs`

- The lock is held briefly, but you expect to wait 50µs due to contention.
- Spinning 50µs per waiter is huge waste unless your system is extremely underutilized.
- Mutex will likely be better because it yields CPU to other runnable threads.

### C++ommon mistakes (what interviewers reject)

- “Spinlocks are always faster.” False. Under contention, they are often worse.
- “Mutexes are always slower.” False. On oversubscribed systems, mutexes often win because they avoid wasting CPU.
- Ignoring preemption: if the lock holder gets preempted, spinners can burn an entire time slice waiting.
- Using spinlocks around code that can block (I/O, sleep, allocation that can stall): that can be catastrophic.

## Takeaway

Pick the tool that minimizes wasted resources under your expected contention model:

- Short waits, running holder, no oversubscription: spinlock can make sense.
- Longer waits or uncertain scheduling: mutex is the safe default.

