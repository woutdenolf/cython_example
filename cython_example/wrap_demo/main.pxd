cdef extern from "hello.h":
    int hello()
cdef extern from "echo.h":
    int echo(int)