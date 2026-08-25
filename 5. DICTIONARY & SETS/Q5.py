s = {}

print(type(s))

# {1, 2, 3} → has commas but no colons → set (new syntax)
# {"a": 1} → has colons → dict (original syntax)
# {} → empty, no way to tell which one was intended → defaults to dict, to preserve all the old code that relied on that meaning
# d1 = {}                    # dict (empty)
# d2 = {"x": 1, "y": 2}       # dict (has colons)

# s1 = set()                 # set (empty) — must use the constructor
# s2 = {1, 2, 3}              # set (has commas, no colons)
