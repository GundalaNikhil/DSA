import heapq
import yaml
import random
import math
from pathlib import Path

# --- Reference Solvers ---

def solve_grd001(n, trips, da, db):
    inf = float('inf')
    cost_a = 0 if (da[0] <= trips[0][0] and trips[0][1] <= da[1]) else inf
    cost_b = 0 if (db[0] <= trips[0][0] and trips[0][1] <= db[1]) else inf
    for i in range(1, n):
        na, nb = inf, inf
        if da[0] <= trips[i][0] and trips[i][1] <= da[1]: na = min(cost_a, cost_b + 1)
        if db[0] <= trips[i][0] and trips[i][1] <= db[1]: nb = min(cost_b, cost_a + 1)
        cost_a, cost_b = na, nb
    res = min(cost_a, cost_b)
    return res if res != inf else -1

def solve_grd002(k, m, q):
    pq = [-x for x in q if x > 0]; heapq.heapify(pq)
    total = sum(q); fulfilled = min(m, total); to_dist = fulfilled
    while to_dist > 0 and pq:
        mx = -heapq.heappop(pq) - 1; to_dist -= 1
        if mx > 0: heapq.heappush(pq, -mx)
    return f"{fulfilled} {k - len(pq)}"

def solve_grd003(n, d, stalls):
    stalls.sort(key=lambda x: x[1])
    count, last_end = 0, -2 * 10**18
    for s, e in stalls:
        if s - last_end >= d: count += 1; last_end = e
    return count

def solve_grd004(n, t, caps):
    if sum(caps) < t: return -1
    caps.sort(reverse=True); cur = 0
    for i, c in enumerate(caps):
        cur += c
        if cur >= t: return i
    return -1

def solve_grd005(n, h, shifts):
    total_l = sum(s[0] for s in shifts)
    if total_l >= h: return 0
    return (h - total_l) * min(s[1] for s in shifts)

def solve_grd006(n, t, w, q):
    pq = [(-q[i], w[i]) for i in range(n)]; heapq.heapify(pq)
    while len(pq) > 1:
        nq1, w1 = heapq.heappop(pq); nq2, w2 = heapq.heappop(pq)
        q1, q2 = -nq1, -nq2
        new_q = min(q1, q2) - 1
        if new_q < t: return -1
        new_w = w1 + w2 - math.floor(0.1 * min(w1, w2))
        heapq.heappush(pq, (-new_q, new_w))
    return int(pq[0][1])

def solve_grd007(n, h, m, existing):
    par = list(range(n))
    def fnd(i):
        if par[i] == i: return i
        par[i] = fnd(par[i]); return par[i]
    def uni(i, j):
        ri, rj = fnd(i), fnd(j)
        if ri != rj: par[ri] = rj; return True
        return False
    comps = n
    for u, v in existing:
        if 0 <= u < n and 0 <= v < n:
            if uni(u, v): comps -= 1
    if comps == 1: return 0
    edges = []
    sh = sorted([(h[i], i) for i in range(n)])
    for k in range(n-1): edges.append((abs(sh[k][0] - sh[k+1][0]), sh[k][1], sh[k+1][1]))
    edges.sort(); cost = 0
    for c, u, v in edges:
        if uni(u, v):
            cost += c; comps -= 1
            if comps == 1: break
    return cost

def solve_grd008(n, r, ex):
    ev = []
    for s, e in ex: ev.append((s, 1)); ev.append((e, -1))
    ev.sort(key=lambda x: (x[0], -x[1]))
    mx, cur = 0, 0
    for _, tp in ev: cur += tp; mx = max(mx, cur)
    return (mx + r - 1) // r

def solve_grd009(n, gain, cost):
    def check(s_idx):
        f, mc, u = 0, 0, False
        for i in range(n):
            idx = (s_idx + i) % n; f += gain[idx]; mc = max(mc, cost[idx]); f -= cost[idx]
            if f < 0:
                if not u: f += mc; u = True
                if f < 0: return False
        return True
    
    total_gain, total_cost, max_cost = sum(gain), sum(cost), max(cost)
    if total_gain + max_cost < total_cost: return -1
    
    # Try classic candidate first
    diff = [gain[i] - cost[i] for i in range(n)]
    cur, mn, cand = 0, 0, 0
    for i in range(n):
        cur += diff[i]
        if cur < mn: mn = cur; cand = (i + 1) % n
    if check(cand): return cand
    
    # If small N, try all
    if n <= 1000:
        for i in range(n):
            if check(i): return i
    else:
        # For large N, try 100 random starts
        for _ in range(100):
            s = random.randint(0, n-1)
            if check(s): return s
    return -1

def solve_grd010(k, queues):
    res = []
    pq = [] 
    idx_list = [0] * k
    for i, q in enumerate(queues):
        if q: heapq.heappush(pq, (q[0], i))
    lv, ct = None, 0
    while pq:
        v, qi = heapq.heappop(pq)
        if res and v == lv and ct == 2:
            if not pq: break
            tmp = [(v, qi)]
            v2, q2 = heapq.heappop(pq)
            while v2 == lv:
                tmp.append((v2, q2))
                if not pq: v2 = None; break
                v2, q2 = heapq.heappop(pq)
            if v2 is None: break
            res.append(v2); lv, ct = v2, 1
            idx_list[q2] += 1
            if idx_list[q2] < len(queues[q2]): heapq.heappush(pq, (queues[q2][idx_list[q2]], q2))
            for x in tmp: heapq.heappush(pq, x)
        else:
            res.append(v)
            if v == lv: ct += 1
            else: lv, ct = v, 1
            idx_list[qi] += 1
            if idx_list[qi] < len(queues[qi]): heapq.heappush(pq, (queues[qi][idx_list[qi]], qi))
    return " ".join(map(str, res))

def solve_grd011(n, req):
    req.sort(key=lambda x: x[1]); pq = []
    for q, d in req:
        heapq.heappush(pq, q)
        if len(pq) > d: heapq.heappop(pq)
    return sum(pq)

def solve_grd012(n, k, tasks):
    pq = [(-p, -ct, nm) for nm, ct, p in tasks]; heapq.heapify(pq)
    cd = []; t, comp, tot = 0, 0, sum(x[1] for x in tasks)
    while comp < tot:
        t += 1
        ready = []
        while cd and cd[0][0] <= t:
            ready.append(heapq.heappop(cd))
        for _, p, c, nm in ready: heapq.heappush(pq, (p, c, nm))
        if pq:
            np, nc, nm = heapq.heappop(pq); comp += 1
            for i in range(len(cd)):
                if -cd[i][1] < -np: cd[i] = (t + k + 1, cd[i][1], cd[i][2], cd[i][3])
            heapq.heapify(cd)
            if nc + 1 < 0: heapq.heappush(cd, (t + k + 1, np, nc + 1, nm))
    return t

def solve_grd013(r, caps, ref):
    p = sum(caps) - len(ref)
    if p <= 0: return 0
    for i in range(r):
        p -= caps[i]
        if p <= 0: return i + 1
    return r

def solve_grd014(n, b, v):
    v.sort(); c, cur = 0, 0
    for x in v:
        if cur + x <= b: cur += x; c += 1
        else: break
    return c

def solve_grd015(k, t, batches):
    f = {}; res = []
    for b in batches:
        for x in b: f[x] = f.get(x, 0) + 1
        v = []
        for x, c in f.items():
            if c <= t: v.extend([x] * c)
        if not v: res.append("NA")
        else:
            v.sort(); nv = len(v)
            if nv % 2 == 1: res.append(str(v[nv // 2]))
            else: res.append(str((v[nv // 2 - 1] + v[nv // 2]) // 2))
    return " ".join(res)

def solve_grd016(n, trips):
    trips.sort(key=lambda x: (x[0] + x[1], x[0])); cur, tot = 0, 0
    for s, d in trips:
        tot += max(0, cur - s)
        cur += d
    return tot

# --- Generator ---

def save(fname, data):
    root = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Greedy/testcases")
    with open(root / f"{fname}.yaml", 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def generate_all():
    root = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Greedy/testcases")
    p_meta = [
        ("GRD-001-campus-shuttle-driver-swaps", "GRD_CAMPUS_SHUTTLE_DRIVER_SWAPS__3847"),
        ("GRD-002-lab-kit-distribution", "GRD_LAB_KIT_DISTRIBUTION__5291"),
        ("GRD-003-festival-stall-placement", "GRD_FESTIVAL_STALL_PLACEMENT__7146"),
        ("GRD-004-library-power-backup", "GRD_LIBRARY_POWER_BACKUP__4928"),
        ("GRD-005-shuttle-overtime-minimizer", "GRD_SHUTTLE_OVERTIME_MINIMIZER__6381"),
        ("GRD-006-robotics-component-bundling-loss-quality", "GRD_ROBOTICS_COMPONENT_BUNDLING__7259"),
        ("GRD-007-campus-wifi-expansion", "GRD_CAMPUS_WIFI_EXPANSION__4892"),
        ("GRD-008-exam-proctor-allocation", "GRD_EXAM_PROCTOR_ALLOCATION__3517"),
        ("GRD-009-shuttle-refuel-with-refund", "GRD_SHUTTLE_REFUEL_WITH_REFUND__6724"),
        ("GRD-010-library-merge-queues", "GRD_LIBRARY_MERGE_QUEUES__8135"),
        ("GRD-011-campus-event-ticket-caps", "GRD_CAMPUS_EVENT_TICKET_CAPS__5864"),
        ("GRD-012-workshop-task-cooldown-priority", "GRD_WORKSHOP_TASK_COOLDOWN_PRIORITY__7539"),
        ("GRD-013-auditorium-seat-refunds", "GRD_AUDITORIUM_SEAT_REFUNDS__2841"),
        ("GRD-014-festival-bandwidth-split", "GRD_FESTIVAL_BANDWIDTH_SPLIT__9163"),
        ("GRD-015-robotics-median-after-batches-stale", "GRD_ROBOTICS_MEDIAN_BATCHES_STALE__4276"),
        ("GRD-016-shuttle-schedule-delay-minimizer", "GRD_SHUTTLE_SCHEDULE_DELAY_MINIMIZER__8457")
    ]

    for idx, (fname, pid) in enumerate(p_meta):
        num = idx + 1
        data = {'problem_id': pid, 'samples': [], 'public': [], 'hidden': []}
        
        # 1 Sample
        if num == 1: smp = {'input': "3\n1 3\n4 6\n7 9\n1 8\n3 10", 'output': '1'}
        elif num == 2: smp = {'input': "3 4\n3 1 2", 'output': solve_grd002(3, 4, [3, 1, 2])}
        elif num == 3: smp = {'input': "3 2\n0 2\n1 4\n5 6", 'output': str(solve_grd003(3, 2, [[0,2],[1,4],[5,6]]))}
        elif num == 4: smp = {'input': "3 7\n3 5 2", 'output': str(solve_grd004(3, 7, [3,5,2]))}
        elif num == 5: smp = {'input': "2 8\n4 3\n2 1", 'output': str(solve_grd005(2, 8, [[4,3],[2,1]]))}
        elif num == 6: smp = {'input': "3 5\n4 3 2\n10 8 6", 'output': str(solve_grd006(3, 5, [4,3,2], [10,8,6]))}
        elif num == 7: smp = {'input': "3\n5 1 9\n0", 'output': str(solve_grd007(3, [5,1,9], 0, []))}
        elif num == 8: smp = {'input': "3 2\n0 10\n5 7\n6 9", 'output': str(solve_grd008(3, 2, [[0,10],[5,7],[6,9]]))}
        elif num == 9: smp = {'input': "3\n1 4 2\n3 2 3", 'output': '1'}
        elif num == 10: smp = {'input': "3\n3 1 1 1\n2 1 2\n1 2", 'output': "1 1 1 2 2"}
        elif num == 11: smp = {'input': "3\n3 1\n5 3\n2 2", 'output': '7'}
        elif num == 12: smp = {'input': "2 1\nA 3 2\nB 2 1", 'output': '7'}
        elif num == 13: smp = {'input': "3 3\n5 4 3\n3 1\n3 2\n2 1", 'output': '2'}
        elif num == 14: smp = {'input': "3 7\n5 2 4", 'output': '2'}
        elif num == 15: smp = {'input': "3 2\n3 5 5 1\n2 5 3\n2 8 9", 'output': "5 3 6"}
        elif num == 16: smp = {'input': "2\n0 3\n1 2", 'output': '2'}
        data['samples'].append(smp)

        # 9 Public and 30 Hidden
        for test_idx in range(2, 41):
            category = 'public' if test_idx <= 10 else 'hidden'
            n_max = 50 if category == 'public' else 1000
            if num == 1:
                n = random.randint(1, n_max)
                tr = []; c = 0
                for _ in range(n): tr.append((c + random.randint(1, 5), c + random.randint(6, 10))); c = tr[-1][1]
                da = (0, random.randint(c//2, c*2)); db = (0, random.randint(c//2, c*2))
                inp = f"{n}\n" + "\n".join(f"{x[0]} {x[1]}" for x in tr) + f"\n{da[0]} {da[1]}\n{db[0]} {db[1]}"
                out = str(solve_grd001(n, tr, da, db))
            elif num == 2:
                k, m = random.randint(5, n_max), random.randint(10, n_max*5)
                q = [random.randint(0, m//k*2) for _ in range(k)]
                inp = f"{k} {m}\n{' '.join(map(str, q))}"
                out = solve_grd002(k, m, q)
            elif num == 3:
                n, d = random.randint(5, n_max), random.randint(1, 20)
                st = []
                for _ in range(n):
                    s = random.randint(0, n*10)
                    st.append([s, s + random.randint(1, 10)])
                inp = f"{n} {d}\n" + "\n".join(f"{x[0]} {x[1]}" for x in st)
                out = str(solve_grd003(n, d, st))
            elif num == 4:
                n, t = random.randint(5, n_max), random.randint(1, n_max*50)
                c = [random.randint(1, 100) for _ in range(n)]
                inp = f"{n} {t}\n{' '.join(map(str, c))}"
                out = str(solve_grd004(n, t, c))
            elif num == 5:
                n, h = random.randint(5, n_max), random.randint(10, n_max*100)
                s = [[random.randint(0, 100), random.randint(1, 50)] for _ in range(n)]
                inp = f"{n} {h}\n" + "\n".join(f"{x[0]} {x[1]}" for x in s)
                out = str(solve_grd005(n, h, s))
            elif num == 6:
                n, t = random.randint(2, 50 if category == 'public' else 200), random.randint(0, 10)
                w = [random.randint(1, 100) for _ in range(n)]
                q = [random.randint(t + n, t + n + 10) for _ in range(n)]
                inp = f"{n} {t}\n{' '.join(map(str, w))}\n{' '.join(map(str, q))}"
                out = str(solve_grd006(n, t, w, q))
            elif num == 7:
                n = random.randint(2, n_max)
                h = [random.randint(0, 10**6) for _ in range(n)]
                m = random.randint(0, n//2)
                e = []
                for _ in range(m): e.append([random.randint(0, n-1), random.randint(0, n-1)])
                inp = f"{n}\n{' '.join(map(str, h))}\n{m}\n" + "\n".join(f"{u} {v}" for u, v in e)
                out = str(solve_grd007(n, h, m, e))
            elif num == 8:
                n, r = random.randint(5, n_max), random.randint(1, 10)
                ex = []
                for _ in range(n):
                    s = random.randint(0, 1000)
                    ex.append([s, s + random.randint(1, 100)])
                inp = f"{n} {r}\n" + "\n".join(f"{x[0]} {x[1]}" for x in ex)
                out = str(solve_grd008(n, r, ex))
            elif num == 9:
                n = random.randint(3, n_max)
                g = [random.randint(0, 100) for _ in range(n)]
                c = [random.randint(0, 100) for _ in range(n)]
                inp = f"{n}\n{' '.join(map(str, g))}\n{' '.join(map(str, c))}"
                out = str(solve_grd009(n, g, c))
            elif num == 10:
                k = random.randint(2, 10)
                qs = []
                for _ in range(k):
                    l = random.randint(1, 20)
                    q = sorted([random.randint(1, 5) for _ in range(l)])
                    qs.append(q)
                inp = f"{k}\n" + "\n".join(f"{len(q)} {' '.join(map(str, q))}" for q in qs)
                out = solve_grd010(k, qs)
            elif num == 11:
                n = random.randint(5, n_max)
                rq = [[random.randint(1, 100), random.randint(1, n)] for _ in range(n)]
                inp = f"{n}\n" + "\n".join(f"{x[0]} {x[1]}" for x in rq)
                out = str(solve_grd011(n, rq))
            elif num == 12:
                n, k = random.randint(2, 26), random.randint(0, 5)
                ts = []
                for i in range(n):
                    nm = chr(ord('A') + i)
                    ts.append((nm, random.randint(1, 10), random.randint(1, 3)))
                inp = f"{n} {k}\n" + "\n".join(f"{x[1]} {x[2]} {x[3]}" if False else f"{x[0]} {x[1]} {x[2]}" for x in ts)
                out = str(solve_grd012(n, k, ts))
            elif num == 13:
                r, n = random.randint(1, n_max), random.randint(0, 100)
                cps = [random.randint(1, 10) for _ in range(r)]
                tot_p = sum(cps)
                n = min(n, tot_p) # No more refunds than people
                refs = []
                temp_occ = list(cps)
                for _ in range(n):
                    row = random.randint(1, r)
                    while temp_occ[row-1] == 0: row = random.randint(1, r)
                    refs.append((row, temp_occ[row-1]))
                    temp_occ[row-1] -= 1
                inp = f"{r} {n}\n{' '.join(map(str, cps))}\n" + "\n".join(f"{x[0]} {x[1]}" for x in refs)
                out = str(solve_grd013(r, cps, refs))
            elif num == 14:
                n, b = random.randint(5, n_max), random.randint(10, n_max*50)
                v = [random.randint(1, 100) for _ in range(n)]
                inp = f"{n} {b}\n{' '.join(map(str, v))}"
                out = str(solve_grd014(n, b, v))
            elif num == 15:
                k, t = random.randint(1, 10), random.randint(1, 5)
                bths = []
                for _ in range(k):
                    m = random.randint(1, 10)
                    bths.append([random.randint(1, 10) for _ in range(m)])
                inp = f"{k} {t}\n" + "\n".join(f"{len(b)} {' '.join(map(str, b))}" for b in bths)
                out = solve_grd015(k, t, bths)
            elif num == 16:
                n = random.randint(1, n_max)
                tr = [[random.randint(0, 100), random.randint(1, 50)] for _ in range(n)]
                inp = f"{n}\n" + "\n".join(f"{x[0]} {x[1]}" for x in tr)
                out = str(solve_grd016(n, tr))
            
            data[category].append({'input': inp, 'output': out})
        
        save(fname, data)

if __name__ == "__main__":
    generate_all()
    print("All Greedy test cases (40 per file) regenerated!")
