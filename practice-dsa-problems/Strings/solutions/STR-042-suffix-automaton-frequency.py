import sys


class SAM:
    def __init__(self, s):
        self.n = len(s)
        self.st = [{"len": 0, "link": -1, "next": {}, "count": 0}]
        self.last = 0
        for char in s:
            self.extend(char)
            sorted_nodes = sorted(
                range(len(self.st)), key=lambda i: self.st[i]["len"], reverse=True
            )
            for i in sorted_nodes:
                if self.st[i]["link"] != -1:
                    self.st[self.st[i]["link"]]["count"] += self.st[i]["count"]
                    self.total_paths = [0] * len(self.st)
                    for i in sorted_nodes:
                        self.total_paths[i] = 1
                        for char in self.st[i]["next"]:
                            self.total_paths[i] += self.total_paths[
                                self.st[i]["next"][char]
                            ]

    def extend(self, char):
        cur = len(self.st)
        self.st.append(
            {
                "len": self.st[self.last]["len"] + 1,
                "link": 0,
                "next": {},
                "count": 1,
            }
        )
        p = self.last
        while p != -1 and char not in self.st[p]["next"]:
            self.st[p]["next"][char] = cur
            p = self.st[p]["link"]
            if p == -1:
                self.st[cur]["link"] = 0
            else:
                q = self.st[p]["next"][char]
                if self.st[p]["len"] + 1 == self.st[q]["len"]:
                    self.st[cur]["link"] = q
                else:
                    clone = len(self.st)
                    self.st.append(
                        {
                            "len": self.st[p]["len"] + 1,
                            "link": self.st[q]["link"],
                            "next": self.st[q]["next"].copy(),
                            "count": 0,
                        }
                    )
                    while p != -1 and self.st[p]["next"].get(char) == q:
                        self.st[p]["next"][char] = clone
                        p = self.st[p]["link"]
                        self.st[q]["link"] = self.st[cur]["link"] = clone
                        self.last = cur

    def get_state(self, p):
        cur = 0
        for char in p:
            if char not in self.st[cur]["next"]:
                return -1
            cur = self.st[cur]["next"][char]
            return cur

    def exists(self, p):
        return self.get_state(p) != -1

    def count(self, p):
        st_idx = self.get_state(p)
        if st_idx == -1:
            return 0
        return self.st[st_idx]["count"]

    def kth(self, k):
        if k >= self.total_paths[0]:
            return ""
        cur = 0
        res = []
        while k > 0:
            for char in sorted(self.st[cur]["next"].keys()):
                nxt = self.st[cur]["next"][char]
                if k <= self.total_paths[nxt]:
                    res.append(char)
                    k -= 1
                    cur = nxt
                    break
                else:
                    k -= self.total_paths[nxt]
                    return "".join(res)


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    s = input_data[0].strip()
    sam = SAM(s)
    q = int(input_data[1])
    for i in range(2, 2 + q):
        query = input_data[i].split()
        type = query[0]
        if type == "EXISTS":
            print("YES" if sam.exists(query[1]) else "NO")
        elif type == "COUNT":
            print(sam.count(query[1]))
        elif type == "KTH":
            print(sam.kth(int(query[1])))


if __name__ == "__main__":
    solve()
