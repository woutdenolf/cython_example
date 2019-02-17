import os
from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

PROJECT = 'cython_example'
VERSION = '0.0.1a'


def project_module(*args):
    return '.'.join((PROJECT,)+args)


def project_path(*args):
    return os.path.join(PROJECT, *args)


extensions = [
    Extension(
        project_module('wrap_demo'),
        [project_path('wrap_demo', 'main.pyx')],
        include_dirs=[project_path('wrap_demo_src', 'include')]
    ),
]

setup_requires = ["cython"]
setup(
    name=PROJECT,
    version=VERSION,
    url="https://github.com/woutdenolf/cython_example",
    author="Wout De Nolf",
    author_email="woutdenolf@users.sf.net",
    setup_requires=setup_requires,
    packages=find_packages(),
    package_data={
        project_module('wrap_demo'): ['*.pxd'],
    },
    ext_modules=cythonize(extensions,
                          include_path=[project_path('wrap_demo')]),
    test_suite=project_module('tests', 'test_all', 'test_suite')
)
