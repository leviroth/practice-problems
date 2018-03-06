def solve(s):
    counts = {}
    for c in s:
        count = counts.setdefault(c, 0)
        counts[c] = count + 1
    for i, c in enumerate(s):
        if counts[c] == 1:
            return i
    return -1


def solve2(s):
    seen = set()
    idx = -1
    for i in range(len(s) - 1, -1, -1):
        c = s[i]
        if c in seen:
            idx = -1
        else:
            idx = i
        seen.add(c)
    return idx
