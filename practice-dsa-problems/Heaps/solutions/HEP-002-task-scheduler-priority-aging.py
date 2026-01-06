import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    cap = int(input_data[ptr])
    ptr += 1
    tasks = []
    for i in range(1, n + 1):
        cnt = int(input_data[ptr])
        ptr += 1
        cool = int(input_data[ptr])
        ptr += 1
        dead = int(input_data[ptr])
        ptr += 1
        base = int(input_data[ptr])
        ptr += 1
        tasks.append(
            {
                "cnt": cnt,
                "cool": cool,
                "dead": dead,
                "base": base,
                "id": i,
                "last": -(10**18),
                "age": 0,
            }
        )
        t = 1
        available = []
        cooling = []
        for i in range(n):
            heapq.heappush(
                available,
                (
                    -(tasks[i]["base"] + tasks[i]["age"]),
                    tasks[i]["dead"],
                    tasks[i]["id"],
                    i,
                ),
            )
            tasks_left = sum(tasks[i]["cnt"] for i in range(n))
            while tasks_left > 0:
                while cooling and cooling[0][0] <= t:
                    _, idx = heapq.heappop(cooling)
                    heapq.heappush(
                        available,
                        (
                            -(tasks[idx]["base"] + tasks[idx]["age"]),
                            tasks[idx]["dead"],
                            tasks[idx]["id"],
                            idx,
                        ),
                    )
                    if available:
                        pri, dead, tid, idx = heapq.heappop(available)
                        tasks[idx]["cnt"] -= 1
                        tasks[idx]["last"] = t
                        tasks_left -= 1
                        if tasks[idx]["cnt"] > 0:
                            heapq.heappush(cooling, (t + tasks[idx]["cool"] + 1, idx))
                            t += 1
                        else:
                            for i in range(n):
                                if tasks[i]["cnt"] > 0 and t > tasks[i]["dead"]:
                                    tasks[i]["age"] = min(cap, tasks[i]["age"] + 1)
                                    if cooling:
                                        next_t = cooling[0][0]
                                        idle_ticks = next_t - t
                                        for _ in range(idle_ticks):
                                            for i in range(n):
                                                if (
                                                    tasks[i]["cnt"] > 0
                                                    and t > tasks[i]["dead"]
                                                ):
                                                    tasks[i]["age"] = min(
                                                        cap, tasks[i]["age"] + 1
                                                    )
                                                    t += 1
                                                    if cooling and cooling[0][0] <= t:
                                                        break
                                                else:
                                                    t += 1
                                                    print(t - 1)


if __name__ == "__main__":
    solve()
