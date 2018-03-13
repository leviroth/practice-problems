def to_tuple(s):
    return tuple(int(c) for c in s)


def make_set(l):
    return {to_tuple(s) for s in l}


def advance(state, position, forward=True):
    change = 1 if forward else -1
    new_val = (state[position] + change) % 10
    mutable = list(state)
    mutable[position] = new_val
    return tuple(mutable)


def neighbors(state):
    for forward in (True, False):
        for position in range(4):
            yield advance(state, position, forward)


def solve(deadends, target):
    target = to_tuple(target)
    start = to_tuple("0000")
    deadends = make_set(deadends)

    frontier = [start]
    visited = {start}
    level = 0

    while frontier:
        new = []
        for state in frontier:
            if state in deadends:
                continue
            if state == target:
                return level
            for neighbor in neighbors(state):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new.append(neighbor)
        level += 1
        frontier = new

    return -1


class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        return solve(deadends, target)
