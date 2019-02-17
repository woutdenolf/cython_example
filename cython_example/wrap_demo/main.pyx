# distutils: sources = cython_example/wrap_demo_src/src/hello.c cython_example/wrap_demo_src/src/echo.c
# distutils: include_dirs = cython_example/wrap_demo_src/include

#from cython_example.wrap_demo cimport main
cimport main
cpdef chello():
    return main.hello()
cpdef cecho(int a):
    return main.echo(a)