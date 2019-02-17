import os
from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

PROJECT = 'cython_example'
VERSION = '0.0.1a0'


def project_module(*args):
    return '.'.join((PROJECT,)+args)


def project_path(*args):
    return os.path.join(PROJECT, *args)

extensions = []
extension_paths = []

ext = Extension(
        project_module('wrap_demo'),
        [project_path('wrap_demo', 'main.pyx')
         project_path('wrap_demo_src', 'src', 'hello.c'),
         project_path('wrap_demo_src', 'src', 'echo.c')],
        include_dirs=[project_path('wrap_demo_src', 'include')]
    )
#extensions.append(ext)
#extension_paths.append(project_path('wrap_demo'))

ext = Extension(
        project_module('cython_demo'),
        [project_path('cython_demo', 'main.pyx')]
    )
#extensions.append(ext)
#extension_paths.append(project_path('cython_demo'))

ext = Extension(
        project_module('fib'),
        [project_path('cython_demo', 'fib.pyx')]
    )
extensions.append(ext)


setup_requires = ["cython"]
setup(
    name=PROJECT,
    version=VERSION,
    description='Cython test project',
    url="https://github.com/woutdenolf/cython_example",
    author="Wout De Nolf",
    author_email="woutdenolf@users.sf.net",
    setup_requires=setup_requires,
    packages=find_packages(),
    package_data={
        project_module('wrap_demo'): ['*.pxd'],
    },
    ext_modules=cythonize(extensions,
                          include_path=extension_paths),
    zip_safe=False,
    test_suite=project_module('tests', 'test_all', 'test_suite')
)
