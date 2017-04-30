from distutils.core import setup, Extension
from distutils.command.build import build as _build
import sys

#Define custom build order, so that the python interface module
#created by SWIG is staged in build_py.
class build(_build):
    sub_commands = [('build_ext',     _build.has_ext_modules),
        ('build_py',      _build.has_pure_modules),
        ('build_clib',    _build.has_c_libraries),
        ('build_scripts', _build.has_scripts),
    ]

with open('README.md','r') as fin:
    longdesc = fin.read()

sys.path.insert(0,"./src")

#from pyclblas_gen import gen_output
#with open("src/pyclblas.py","wb") as fout:
#    fout.write(gen_output("src/pyclblas_functions.i"))

pyclblas_swig = Extension('_pyclblas_swig', ['src/pyclblas_swig.i'], libraries=['clBLAS'])

setup(
    name='pyclblas',
    version='0.8.5',
    py_modules=['pyclblas_swig', 'pyclblas'],
    description='Python Bindings for the OpenCL BLAS library (clBLAS)',
    author='Jon Roose',
    author_email='jroose@gmail.com',
    url='https://github.com/jroose/pyclblas',
    ext_modules=[pyclblas_swig],
    requires=['numpy','pyopencl'],
    package_dir={'': 'src'},
    license="Apache 2.0",
    long_description=longdesc,
    cmdclass = {'build':build}
)
