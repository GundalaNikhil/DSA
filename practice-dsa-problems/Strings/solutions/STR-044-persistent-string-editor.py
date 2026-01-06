import sys
import random


class Node:
    def __init__(self, char, priority=None):
        self.char = char
        self.priority = priority if priority is not None else random.random()
        self.left = None
        self.right = None
        self.size = 1


def get_size(node):
    return node.size if node else 0


def update_size(node):
    if node:
        node.size = 1 + get_size(node.left) + get_size(node.right)


def copy_node(node):
    if not node:
        return None
    new_node = Node(node.char, node.priority)
    new_node.left = node.left
    new_node.right = node.right
    new_node.size = node.size
    return new_node


def split(node, k):
    if not node:
        return None, None
    new_node = copy_node(node)
    left_size = get_size(new_node.left)
    if left_size < k:
        new_node.right, r = split(new_node.right, k - left_size - 1)
        update_size(new_node)
        return new_node, r
    else:
        l, new_node.left = split(new_node.left, k)
        update_size(new_node)
        return l, new_node


def merge(l, r):
    if not l or not r:
        return copy_node(l or r)
    if l.priority > r.priority:
        new_node = copy_node(l)
        new_node.right = merge(new_node.right, r)
        update_size(new_node)
        return new_node
    else:
        new_node = copy_node(r)
        new_node.left = merge(l, new_node.left)
        update_size(new_node)
        return new_node


def get_string(node, res):
    if not node:
        return
    get_string(node.left, res)
    res.append(node.char)
    get_string(node.right, res)


class PersistentEditor:
    def __init__(self):
        self.versions = [None]

    def append(self, v, char):
        root = self.versions[v]
        new_root = merge(root, Node(char))
        self.versions.append(new_root)

    def delete_last(self, v):
        root = self.versions[v]
        sz = get_size(root)
        if sz == 0:
            self.versions.append(None)
        else:
            new_root, _ = split(root, sz - 1)
            self.versions.append(new_root)

    def replace(self, v, i, char):
        root = self.versions[v]
        l, mid_r = split(root, i)
        _, r = split(mid_r, 1)
        new_root = merge(merge(l, Node(char)), r)
        self.versions.append(new_root)

    def substring(self, v, i, j):
        root = self.versions[v]
        _, mid_r = split(root, i)
        mid, _ = split(mid_r, j - i + 1)
        self.versions.append(mid)

    def print_version(self, v):
        res = []
        get_string(self.versions[v], res)
        print("".join(res))


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    q = int(input_data[0])
    editor = PersistentEditor()
    for i in range(1, 1 + q):
        line = input_data[i].split()
        cmd = line[0]
        v = int(line[1])
        if cmd == "APPEND":
            editor.append(v, line[2])
        elif cmd == "DELETE_LAST":
            editor.delete_last(v)
        elif cmd == "REPLACE":
            editor.replace(v, int(line[2]), line[3])
        elif cmd == "SUBSTRING":
            editor.substring(v, int(line[2]), int(line[3]))
        elif cmd == "PRINT":
            editor.print_version(v)


if __name__ == "__main__":
    solve()
