from distutils.core import setup, Extension
import sys

with open('README.md','r') as fin:
    longdesc = fin.read()

sys.path.insert(0,"./src")

#from pyclblas_gen import gen_output
#with open("src/pyclblas.py","wb") as fout:
#    fout.write(gen_output("src/pyclblas_functions.i"))

pyclblas_swig = Extension('_pyclblas_swig', ['src/pyclblas_swig.i'], libraries=['clBLAS'])

setup(
    name='pyclblas',
    version='0.8.3',
    py_modules=['pyclblas_swig', 'pyclblas'],
    description='Python Bindings for the OpenCL BLAS library (clBLAS)',
    author='Jon Roose',
    author_email='jroose@gmail.com',
    url='https://github.com/jroose/pyclblas',
    ext_modules=[pyclblas_swig],
    requires=['numpy','pyopencl'],
    package_dir={'': 'src'},
    license="Apache 2.0",
    long_description=longdesc
)
