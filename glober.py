from os import listdir
from os.path import isfile, join
import copy
#from fnmatch import fnmatch

def check(x, pattern):
    m = len(x)
    n = len(pattern)
    f = [[False]*n for _ in range(m)]
    if x[0] == pattern[0] or pattern[0] == '*' or pattern[0] =='?':
        f[0][0] = True
    for j in range(1,n):
        if pattern[j] == '*':
            f[0][j] = f[0][j-1]
    for i in range(1,m):
        if pattern[0] == '*':
            f[i][0] = True
    for i in range(1,m):
        for j in range(1,n):
            if pattern[j] == '*':
                f[i][j] = f[i-1][j] or f[i][j-1]
            elif pattern[j] == '?':
                f[i][j] = f[i-1][j-1]
            else:
                if x[i] == pattern[j]:
                    f[i][j] = f[i-1][j-1]
    return f[m-1][n-1]

def search(path, pattern):
    '''
    path: str
    f: str
    '''
    dirs = listdir(path)
    onlyfiles = [f for f in dirs if isfile(join(path, f))]
    res = []
    for x in onlyfiles:
        if check(x, pattern) == True:
            res.append(x)
    return res