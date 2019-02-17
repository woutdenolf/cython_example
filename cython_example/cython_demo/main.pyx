#cimport main

cpdef hello():
    return 42

cpdef echo(int a):
    return a

cpdef addone(int a):
    return echo(a) + 1
