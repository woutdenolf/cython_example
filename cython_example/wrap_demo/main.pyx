cimport main

cpdef hello():
    return main.hello()

cpdef echo(int a):
    return main.echo(a)

cpdef addone(int a):
    return echo(a) + 1
