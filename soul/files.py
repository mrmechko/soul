"""
A bunch functions that would make my life easier
"""

import os, re

def ls(p=".", pattern=".*", depth=0):
    # 1. If it is a file, return a list containing the file
    # 2. If it is a directory return all contents to depth 
    # 3. Filter results by pattern
    cands = []
    if os.path.isfile(p):
        cands = [p]
    elif os.path.isdir(p):
        cands = os.listdir(p)
        cands = [c for c in cands if re.match(pattern, c)]
        while depth > 0:
            depth = depth - 1
            cands = sum([ls(c, pattern, depth) for c in cands], [])
            cands = [c for c in cands if re.match(pattern, c)]
    else:
        return []
    return cands

