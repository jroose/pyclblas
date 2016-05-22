from distutils.core import setup, Extension

with open('README.txt','r') as fin:
    longdesc = fin.read()

setup(
    name='pyclblas',
    version='0.1.0',
    py_modules=['pyclblas_swig', 'pyclblas'],
    description='Python Bindings for the OpenCL BLAS library (clBLAS)',
    author='Jon Roose',
    author_email='jroose@gmail.com',
    url='https://github.com/jroose/pyclblas',
    ext_modules=[Extension('_pyclblas_swig', ['src/pyclblas_swig.i'], libraries=['clBLAS'])],
    requires=['numpy','pyopencl'],
    package_dir={'': 'src'},
    license="Apache 2.0",
    long_description=longdesc
)
