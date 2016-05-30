import pyclblas_swig

from pyclblas_swig import clblasRowMajor
from pyclblas_swig import clblasColumnMajor
from pyclblas_swig import clblasNoTrans
from pyclblas_swig import clblasTrans
from pyclblas_swig import clblasConjTrans
from pyclblas_swig import clblasUpper
from pyclblas_swig import clblasLower
from pyclblas_swig import clblasUnit
from pyclblas_swig import clblasNonUnit
from pyclblas_swig import clblasLeft
from pyclblas_swig import clblasRight


#####CLEANUP CODE#####
import atexit

@atexit.register
def _cleanup():
    pyclblas_swig.shutdown()

def clblasGetVersion():
    """ wraps: `clblasGetVersion <http://clmathlibraries.github.io/clBLAS/group__VERSION.html#ga5b7a3f10272fa76b1cca152eeea78ede>`_

Get the clblas library version info.

:return: Version string as %s.%s.%s % (major, minor, patch)

"""
    return pyclblas_swig.clblasGetVersion()

def clblasSetup():
    """ wraps: `clblasSetup <http://clmathlibraries.github.io/clBLAS/group__INIT.html#gab0c597e62144c27ea6f9c100ee40bb6d>`_

Initialize the clblas library. Must be called before any other clblas API function is invoked. <dl class="section note"> <dt> Note </dt> <dd> This function is not thread-safe. </dd> </dl>


"""
    return pyclblas_swig.clblasSetup()

def clblasTeardown():
    """ wraps: `clblasTeardown <http://clmathlibraries.github.io/clBLAS/group__INIT.html#ga737647d266623bb1aa27043fdaa9298f>`_

Finalize the usage of the clblas library. Frees all memory allocated for different computational kernel and other internal data. <dl class="section note"> <dt> Note </dt> <dd> This function is not thread-safe. </dd> </dl>


"""
    return pyclblas_swig.clblasTeardown()

def clblasCswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasCswap <http://clmathlibraries.github.io/clBLAS/group__SWAP.html#gabd03fadcc12f872eecb0a59a2c5dbde8>`_

interchanges two vectors of complex-float elements.

:param N: Number of elements in vector **X**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasDswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasDswap <http://clmathlibraries.github.io/clBLAS/group__SWAP.html#ga9cb4b5452741d6b8dd34ddd973d296fd>`_

interchanges two vectors of double.

:param N: Number of elements in vector **X**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasSswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasSswap <http://clmathlibraries.github.io/clBLAS/group__SWAP.html#gaa3ce4cbdbe57e82d33ea0ee2c41c5dd1>`_

interchanges two vectors of float.

:param N: Number of elements in vector **X**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasZswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasZswap <http://clmathlibraries.github.io/clBLAS/group__SWAP.html#ga43f1fd6c43cdb1d4084c7d6d036631c8>`_

interchanges two vectors of double-complex elements.

:param N: Number of elements in vector **X**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasCscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasCscal <http://clmathlibraries.github.io/clBLAS/group__SCAL.html#gad12f7c7178428580f0525a71fb4b6d51>`_

Scales a complex-float vector by a complex-float constant. 

* ( X |larr| |alpha| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasDscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasDscal <http://clmathlibraries.github.io/clBLAS/group__SCAL.html#gaa3a11c5c652667f9f15c20bad2d669de>`_

Scales a double vector by a double constant. 

* ( X |larr| |alpha| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasSscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasSscal <http://clmathlibraries.github.io/clBLAS/group__SCAL.html#gaa3d8bf171788d9979d8cbe4969a06dd0>`_

Scales a float vector by a float constant. 

* ( X |larr| |alpha| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasZscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasZscal <http://clmathlibraries.github.io/clBLAS/group__SCAL.html#ga0ee89f07465ca8c945ccdc7d2310577a>`_

Scales a complex-double vector by a complex-double constant. 

* ( X |larr| |alpha| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasCsscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasCsscal <http://clmathlibraries.github.io/clBLAS/group__SSCAL.html#ga11d9baf5f7402fd774f4987b5afe5bcf>`_

Scales a complex-float vector by a float constant. 

* ( X |larr| |alpha| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCsscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasZdscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasZdscal <http://clmathlibraries.github.io/clBLAS/group__SSCAL.html#ga5db19fa2237256c19d567b3a80b01022>`_

Scales a complex-double vector by a double constant. 

* ( X |larr| |alpha| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZdscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasCcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasCcopy <http://clmathlibraries.github.io/clBLAS/group__COPY.html#ga6767ad07243ae19b2617670527219a47>`_

Copies complex-float elements from vector X to vector Y. 

* ( Y |larr| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasDcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasDcopy <http://clmathlibraries.github.io/clBLAS/group__COPY.html#ga358f57842766afd5e51582fd47fbb9d9>`_

Copies double elements from vector X to vector Y. 

* ( Y |larr| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasScopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasScopy <http://clmathlibraries.github.io/clBLAS/group__COPY.html#ga097cbbbf184b626ea420a8f49e66d031>`_

Copies float elements from vector X to vector Y. 

* ( Y |larr| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasScopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasZcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasZcopy <http://clmathlibraries.github.io/clBLAS/group__COPY.html#ga161ee02436143e63b25d1aef7fe0297f>`_

Copies complex-double elements from vector X to vector Y. 

* ( Y |larr| X )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasCaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasCaxpy <http://clmathlibraries.github.io/clBLAS/group__AXPY.html#ga7d3c15344c1844c0b255aaf1a8f1ab1b>`_

Scale vector X of complex-float elements and add to Y. 

* ( Y |larr| |alpha| X + Y )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasDaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasDaxpy <http://clmathlibraries.github.io/clBLAS/group__AXPY.html#gaa8aa08bfce0d20591c403570a28923d1>`_

Scale vector X of double elements and add to Y. 

* ( Y |larr| |alpha| X + Y )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasSaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasSaxpy <http://clmathlibraries.github.io/clBLAS/group__AXPY.html#ga681bfb2ef70dde92ec26d82c80584101>`_

Scale vector X of float elements and add to Y. 

* ( Y |larr| |alpha| X + Y )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasZaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasZaxpy <http://clmathlibraries.github.io/clBLAS/group__AXPY.html#ga93589cdface1d935d8721d182babaea1>`_

Scale vector X of double-complex elements and add to Y. 

* ( Y |larr| |alpha| X + Y )



:param N: Number of elements in vector **X**.
:type N: int [in]
:param alpha: The constant factor for vector **X**.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasCdotc(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasCdotc <http://clmathlibraries.github.io/clBLAS/group__DOT.html#ga4871a408c932ad0f01b0277f2c63439d>`_

dot product of two vectors containing float-complex elements conjugating the first vector

:param N: Number of elements in vector **X**.
:type N: int [in]
:param dotProduct: Buffer object that will contain the dot-product value.
:type dotProduct: pyopencl.Buffer [out]
:param offDP: Offset to dot-product in **dotProduct** buffer object. Counted in elements.
:type offDP: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCdotc(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasCdotu(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasCdotu <http://clmathlibraries.github.io/clBLAS/group__DOT.html#ga986b5776ae55868f866505fa0e75e12a>`_

dot product of two vectors containing float-complex elements

:param N: Number of elements in vector **X**.
:type N: int [in]
:param dotProduct: Buffer object that will contain the dot-product value.
:type dotProduct: pyopencl.Buffer [out]
:param offDP: Offset to dot-product in **dotProduct** buffer object. Counted in elements.
:type offDP: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCdotu(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasDdot(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasDdot <http://clmathlibraries.github.io/clBLAS/group__DOT.html#gaa519db48a934a41734ece5568738507c>`_

dot product of two vectors containing double elements

:param N: Number of elements in vector **X**.
:type N: int [in]
:param dotProduct: Buffer object that will contain the dot-product value.
:type dotProduct: pyopencl.Buffer [out]
:param offDP: Offset to dot-product in **dotProduct** buffer object. Counted in elements.
:type offDP: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDdot(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasSdot(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasSdot <http://clmathlibraries.github.io/clBLAS/group__DOT.html#ga3cb3d1cc132ab3c148126d93cd9cea06>`_

dot product of two vectors containing float elements

:param N: Number of elements in vector **X**.
:type N: int [in]
:param dotProduct: Buffer object that will contain the dot-product value.
:type dotProduct: pyopencl.Buffer [out]
:param offDP: Offset to dot-product in **dotProduct** buffer object. Counted in elements.
:type offDP: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSdot(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasZdotc(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasZdotc <http://clmathlibraries.github.io/clBLAS/group__DOT.html#ga3211c5be047e100189c7c001353067ff>`_

dot product of two vectors containing double-complex elements conjugating the first vector

:param N: Number of elements in vector **X**.
:type N: int [in]
:param dotProduct: Buffer object that will contain the dot-product value.
:type dotProduct: pyopencl.Buffer [out]
:param offDP: Offset to dot-product in **dotProduct** buffer object. Counted in elements.
:type offDP: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZdotc(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasZdotu(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasZdotu <http://clmathlibraries.github.io/clBLAS/group__DOT.html#gaf801191aade608066f1413b6ce55194a>`_

dot product of two vectors containing double-complex elements

:param N: Number of elements in vector **X**.
:type N: int [in]
:param dotProduct: Buffer object that will contain the dot-product value.
:type dotProduct: pyopencl.Buffer [out]
:param offDP: Offset to dot-product in **dotProduct** buffer object. Counted in elements.
:type offDP: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZdotu(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasCrotg(CA, offCA, CB, offCB, C, offC, S, offS, commandQueues, eventWaitList):
    """ wraps: `clblasCrotg <http://clmathlibraries.github.io/clBLAS/group__ROTG.html#gabc546b58516c4beea33b480c021d860b>`_

construct givens plane rotation on float-complex elements

:param CA: Buffer object that contains CA.
:type CA: pyopencl.Buffer [out]
:param offCA: Offset to CA in **CA** buffer object. Counted in elements.
:type offCA: int [in]
:param CB: Buffer object that contains CB.
:type CB: pyopencl.Buffer [out]
:param offCB: Offset to CB in **CB** buffer object. Counted in elements.
:type offCB: int [in]
:param C: Buffer object that contains C. C is real.
:type C: pyopencl.Buffer [out]
:param offC: Offset to C in **C** buffer object. Counted in elements.
:type offC: int [in]
:param S: Buffer object that contains S.
:type S: pyopencl.Buffer [out]
:param offS: Offset to S in **S** buffer object. Counted in elements.
:type offS: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCrotg(CA, offCA, CB, offCB, C, offC, S, offS, commandQueues, eventWaitList)

def clblasDrotg(DA, offDA, DB, offDB, C, offC, S, offS, commandQueues, eventWaitList):
    """ wraps: `clblasDrotg <http://clmathlibraries.github.io/clBLAS/group__ROTG.html#ga8ced299f4f3ae8c85e615a8e3c5c34fc>`_

construct givens plane rotation on double elements

:param DA: Buffer object that contains DA.
:type DA: pyopencl.Buffer [out]
:param offDA: Offset to DA in **DA** buffer object. Counted in elements.
:type offDA: int [in]
:param DB: Buffer object that contains DB.
:type DB: pyopencl.Buffer [out]
:param offDB: Offset to DB in **DB** buffer object. Counted in elements.
:type offDB: int [in]
:param C: Buffer object that contains C.
:type C: pyopencl.Buffer [out]
:param offC: Offset to C in **C** buffer object. Counted in elements.
:type offC: int [in]
:param S: Buffer object that contains S.
:type S: pyopencl.Buffer [out]
:param offS: Offset to S in **S** buffer object. Counted in elements.
:type offS: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDrotg(DA, offDA, DB, offDB, C, offC, S, offS, commandQueues, eventWaitList)

def clblasSrotg(SA, offSA, SB, offSB, C, offC, S, offS, commandQueues, eventWaitList):
    """ wraps: `clblasSrotg <http://clmathlibraries.github.io/clBLAS/group__ROTG.html#ga8b928e9240956547c86c6d4279cc54cb>`_

construct givens plane rotation on float elements

:param SA: Buffer object that contains SA.
:type SA: pyopencl.Buffer [out]
:param offSA: Offset to SA in **SA** buffer object. Counted in elements.
:type offSA: int [in]
:param SB: Buffer object that contains SB.
:type SB: pyopencl.Buffer [out]
:param offSB: Offset to SB in **SB** buffer object. Counted in elements.
:type offSB: int [in]
:param C: Buffer object that contains C.
:type C: pyopencl.Buffer [out]
:param offC: Offset to C in **C** buffer object. Counted in elements.
:type offC: int [in]
:param S: Buffer object that contains S.
:type S: pyopencl.Buffer [out]
:param offS: Offset to S in **S** buffer object. Counted in elements.
:type offS: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSrotg(SA, offSA, SB, offSB, C, offC, S, offS, commandQueues, eventWaitList)

def clblasZrotg(CA, offCA, CB, offCB, C, offC, S, offS, commandQueues, eventWaitList):
    """ wraps: `clblasZrotg <http://clmathlibraries.github.io/clBLAS/group__ROTG.html#gac2eca9bbca7386adc94459d95f82025e>`_

construct givens plane rotation on double-complex elements

:param CA: Buffer object that contains CA.
:type CA: pyopencl.Buffer [out]
:param offCA: Offset to CA in **CA** buffer object. Counted in elements.
:type offCA: int [in]
:param CB: Buffer object that contains CB.
:type CB: pyopencl.Buffer [out]
:param offCB: Offset to CB in **CB** buffer object. Counted in elements.
:type offCB: int [in]
:param C: Buffer object that contains C. C is real.
:type C: pyopencl.Buffer [out]
:param offC: Offset to C in **C** buffer object. Counted in elements.
:type offC: int [in]
:param S: Buffer object that contains S.
:type S: pyopencl.Buffer [out]
:param offS: Offset to S in **S** buffer object. Counted in elements.
:type offS: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZrotg(CA, offCA, CB, offCB, C, offC, S, offS, commandQueues, eventWaitList)

def clblasDrotmg(DD1, offDD1, DD2, offDD2, DX1, offDX1, DY1, offDY1, DPARAM, offDparam, commandQueues, eventWaitList):
    """ wraps: `clblasDrotmg <http://clmathlibraries.github.io/clBLAS/group__ROTMG.html#gae9f743bfef4a17336fbf8912516219c3>`_

construct the modified givens rotation on double elements

:param DD1: Buffer object that contains DD1.
:type DD1: pyopencl.Buffer [out]
:param offDD1: Offset to DD1 in **DD1** buffer object. Counted in elements.
:type offDD1: int [in]
:param DD2: Buffer object that contains DD2.
:type DD2: pyopencl.Buffer [out]
:param offDD2: Offset to DD2 in **DD2** buffer object. Counted in elements.
:type offDD2: int [in]
:param DX1: Buffer object that contains DX1.
:type DX1: pyopencl.Buffer [out]
:param offDX1: Offset to DX1 in **DX1** buffer object. Counted in elements.
:type offDX1: int [in]
:param DY1: Buffer object that contains DY1.
:type DY1: pyopencl.Buffer [in]
:param offDY1: Offset to DY1 in **DY1** buffer object. Counted in elements.
:type offDY1: int [in]
:param DPARAM: Buffer object that contains DPARAM array of minimum length 5 DPARAM(0) = DFLAG DPARAM(1) = DH11 DPARAM(2) = DH21 DPARAM(3) = DH12 DPARAM(4) = DH22.
:type DPARAM: pyopencl.Buffer [out]
:param offDparam: Offset to DPARAM in **DPARAM** buffer object. Counted in elements.
:type offDparam: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDrotmg(DD1, offDD1, DD2, offDD2, DX1, offDX1, DY1, offDY1, DPARAM, offDparam, commandQueues, eventWaitList)

def clblasSrotmg(SD1, offSD1, SD2, offSD2, SX1, offSX1, SY1, offSY1, SPARAM, offSparam, commandQueues, eventWaitList):
    """ wraps: `clblasSrotmg <http://clmathlibraries.github.io/clBLAS/group__ROTMG.html#ga1408f9c9c16a2cd6160bb7d2083dc644>`_

construct the modified givens rotation on float elements

:param SD1: Buffer object that contains SD1.
:type SD1: pyopencl.Buffer [out]
:param offSD1: Offset to SD1 in **SD1** buffer object. Counted in elements.
:type offSD1: int [in]
:param SD2: Buffer object that contains SD2.
:type SD2: pyopencl.Buffer [out]
:param offSD2: Offset to SD2 in **SD2** buffer object. Counted in elements.
:type offSD2: int [in]
:param SX1: Buffer object that contains SX1.
:type SX1: pyopencl.Buffer [out]
:param offSX1: Offset to SX1 in **SX1** buffer object. Counted in elements.
:type offSX1: int [in]
:param SY1: Buffer object that contains SY1.
:type SY1: pyopencl.Buffer [in]
:param offSY1: Offset to SY1 in **SY1** buffer object. Counted in elements.
:type offSY1: int [in]
:param SPARAM: Buffer object that contains SPARAM array of minimum length 5 SPARAM(0) = SFLAG SPARAM(1) = SH11 SPARAM(2) = SH21 SPARAM(3) = SH12 SPARAM(4) = SH22.
:type SPARAM: pyopencl.Buffer [out]
:param offSparam: Offset to SPARAM in **SPARAM** buffer object. Counted in elements.
:type offSparam: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSrotmg(SD1, offSD1, SD2, offSD2, SX1, offSX1, SY1, offSY1, SPARAM, offSparam, commandQueues, eventWaitList)

def clblasCsrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList):
    """ wraps: `clblasCsrot <http://clmathlibraries.github.io/clBLAS/group__ROT.html#ga663e804a23f138d163b4fff8825cac60>`_

applies a plane rotation for float-complex elements

:param N: Number of elements in vector **X** and **Y**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param C: C specifies the cosine, cos. This number is real.
:type C: float [in]
:param S: S specifies the sine, sin. This number is real.
:type S: float [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCsrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList)

def clblasDrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList):
    """ wraps: `clblasDrot <http://clmathlibraries.github.io/clBLAS/group__ROT.html#ga8ede6058ce82f3873a5671e0e20fa995>`_

applies a plane rotation for double elements

:param N: Number of elements in vector **X** and **Y**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param C: C specifies the cosine, cos.
:type C: float [in]
:param S: S specifies the sine, sin.
:type S: float [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList)

def clblasSrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList):
    """ wraps: `clblasSrot <http://clmathlibraries.github.io/clBLAS/group__ROT.html#gaa304aba66a3ac056a2483cb4a46d33ae>`_

applies a plane rotation for float elements

:param N: Number of elements in vector **X** and **Y**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param C: C specifies the cosine, cos.
:type C: float [in]
:param S: S specifies the sine, sin.
:type S: float [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList)

def clblasZdrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList):
    """ wraps: `clblasZdrot <http://clmathlibraries.github.io/clBLAS/group__ROT.html#ga40e24eb11d3a5ec204bb5430291d9398>`_

applies a plane rotation for double-complex elements

:param N: Number of elements in vector **X** and **Y**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param C: C specifies the cosine, cos. This number is real.
:type C: float [in]
:param S: S specifies the sine, sin. This number is real.
:type S: float [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZdrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList)

def clblasDrotm(N, X, offx, incx, Y, offy, incy, DPARAM, offDparam, commandQueues, eventWaitList):
    """ wraps: `clblasDrotm <http://clmathlibraries.github.io/clBLAS/group__ROTM.html#ga66ef211876ccd5ba35f4c1d76139b289>`_

modified givens rotation for double elements

:param N: Number of elements in vector **X** and **Y**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param DPARAM: Buffer object that contains SPARAM array of minimum length 5 DPARAM(1)=DFLAG DPARAM(2)=DH11 DPARAM(3)=DH21 DPARAM(4)=DH12 DPARAM(5)=DH22.
:type DPARAM: pyopencl.Buffer [in]
:param offDparam: Offset of first element of array **DPARAM** in buffer object. Counted in elements.
:type offDparam: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDrotm(N, X, offx, incx, Y, offy, incy, DPARAM, offDparam, commandQueues, eventWaitList)

def clblasSrotm(N, X, offx, incx, Y, offy, incy, SPARAM, offSparam, commandQueues, eventWaitList):
    """ wraps: `clblasSrotm <http://clmathlibraries.github.io/clBLAS/group__ROTM.html#ga13afb13391200f892527019e53986a13>`_

modified givens rotation for float elements

:param N: Number of elements in vector **X** and **Y**.
:type N: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing the vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param SPARAM: Buffer object that contains SPARAM array of minimum length 5 SPARAM(1)=SFLAG SPARAM(2)=SH11 SPARAM(3)=SH21 SPARAM(4)=SH12 SPARAM(5)=SH22.
:type SPARAM: pyopencl.Buffer [in]
:param offSparam: Offset of first element of array **SPARAM** in buffer object. Counted in elements.
:type offSparam: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSrotm(N, X, offx, incx, Y, offy, incy, SPARAM, offSparam, commandQueues, eventWaitList)

def clblasDnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasDnrm2 <http://clmathlibraries.github.io/clBLAS/group__NRM2.html#gaf48d0eadbccb9ca8eb0ebbd2ba25822f>`_

computes the euclidean norm of vector containing double elements NRM2 = sqrt( X' * X )

:param N: Number of elements in vector **X**.
:type N: int [in]
:param NRM2: Buffer object that will contain the NRM2 value.
:type NRM2: pyopencl.Buffer [out]
:param offNRM2: Offset to NRM2 value in **NRM2** buffer object. Counted in elements.
:type offNRM2: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object that can hold minimum of (2*N) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDznrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasDznrm2 <http://clmathlibraries.github.io/clBLAS/group__NRM2.html#ga5bac7b219c072e37b9485229f957d5e0>`_

computes the euclidean norm of vector containing double-complex elements NRM2 = sqrt( X**H * X )

:param N: Number of elements in vector **X**.
:type N: int [in]
:param NRM2: Buffer object that will contain the NRM2 value. Note that the answer of Dznrm2 is a real value.
:type NRM2: pyopencl.Buffer [out]
:param offNRM2: Offset to NRM2 value in **NRM2** buffer object. Counted in elements.
:type offNRM2: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object that can hold minimum of (2*N) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDznrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasScnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasScnrm2 <http://clmathlibraries.github.io/clBLAS/group__NRM2.html#ga5c083d72c8f1e40535e325209ebd27f9>`_

computes the euclidean norm of vector containing float-complex elements NRM2 = sqrt( X**H * X )

:param N: Number of elements in vector **X**.
:type N: int [in]
:param NRM2: Buffer object that will contain the NRM2 value. Note that the answer of Scnrm2 is a real value.
:type NRM2: pyopencl.Buffer [out]
:param offNRM2: Offset to NRM2 value in **NRM2** buffer object. Counted in elements.
:type offNRM2: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object that can hold minimum of (2*N) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasScnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasSnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasSnrm2 <http://clmathlibraries.github.io/clBLAS/group__NRM2.html#gad10a1a63b1fb670eab82017bb30e24da>`_

computes the euclidean norm of vector containing float elements NRM2 = sqrt( X' * X )

:param N: Number of elements in vector **X**.
:type N: int [in]
:param NRM2: Buffer object that will contain the NRM2 value.
:type NRM2: pyopencl.Buffer [out]
:param offNRM2: Offset to NRM2 value in **NRM2** buffer object. Counted in elements.
:type offNRM2: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object that can hold minimum of (2*N) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasiCamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasiCamax <http://clmathlibraries.github.io/clBLAS/group__iAMAX.html#ga63d00e5c0e8cc5dc8f09462e52ab347d>`_

index of max absolute value in a complex float array

:param N: Number of elements in vector **X**.
:type N: int [in]
:param iMax: Buffer object storing the index of first absolute max. The index will be of type unsigned int.
:type iMax: pyopencl.Buffer [out]
:param offiMax: Offset for storing index in the buffer iMax Counted in elements.
:type offiMax: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temprory cl_mem object to store intermediate results It should be able to hold minimum of (2*N) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasiCamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasiDamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasiDamax <http://clmathlibraries.github.io/clBLAS/group__iAMAX.html#gacc4b0ea833914578f12a40696ff472bd>`_

index of max absolute value in a double array

:param N: Number of elements in vector **X**.
:type N: int [in]
:param iMax: Buffer object storing the index of first absolute max. The index will be of type unsigned int.
:type iMax: pyopencl.Buffer [out]
:param offiMax: Offset for storing index in the buffer iMax Counted in elements.
:type offiMax: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temprory cl_mem object to store intermediate results It should be able to hold minimum of (2*N) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasiDamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasiSamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasiSamax <http://clmathlibraries.github.io/clBLAS/group__iAMAX.html#gac4e081772dfa64c68320a9a1f78b7a07>`_

index of max absolute value in a float array

:param N: Number of elements in vector **X**.
:type N: int [in]
:param iMax: Buffer object storing the index of first absolute max. The index will be of type unsigned int.
:type iMax: pyopencl.Buffer [out]
:param offiMax: Offset for storing index in the buffer iMax Counted in elements.
:type offiMax: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temprory cl_mem object to store intermediate results It should be able to hold minimum of (2*N) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasiSamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasiZamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasiZamax <http://clmathlibraries.github.io/clBLAS/group__iAMAX.html#gacebe98820f938c01f4f46cf749e67a54>`_

index of max absolute value in a complex double array

:param N: Number of elements in vector **X**.
:type N: int [in]
:param iMax: Buffer object storing the index of first absolute max. The index will be of type unsigned int.
:type iMax: pyopencl.Buffer [out]
:param offiMax: Offset for storing index in the buffer iMax Counted in elements.
:type offiMax: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temprory cl_mem object to store intermediate results It should be able to hold minimum of (2*N) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasiZamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasDasum <http://clmathlibraries.github.io/clBLAS/group__ASUM.html#ga2871a65e7d53f7b905d6abd3cbdda521>`_

absolute sum of values of a vector containing double elements

:param N: Number of elements in vector **X**.
:type N: int [in]
:param asum: Buffer object that will contain the absoulte sum value.
:type asum: pyopencl.Buffer [out]
:param offAsum: Offset to absoule sum in **asum** buffer object. Counted in elements.
:type offAsum: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDzasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasDzasum <http://clmathlibraries.github.io/clBLAS/group__ASUM.html#gab5e25fa71db7c021194c342aa41c93e5>`_

absolute sum of values of a vector containing double-complex elements

:param N: Number of elements in vector **X**.
:type N: int [in]
:param asum: Buffer object that will contain the absolute sum value.
:type asum: pyopencl.Buffer [out]
:param offAsum: Offset to absolute sum in **asum** buffer object. Counted in elements.
:type offAsum: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDzasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasSasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasSasum <http://clmathlibraries.github.io/clBLAS/group__ASUM.html#ga88e132f215b9830ee2ab19dbe50908f0>`_

absolute sum of values of a vector containing float elements

:param N: Number of elements in vector **X**.
:type N: int [in]
:param asum: Buffer object that will contain the absoule sum value.
:type asum: pyopencl.Buffer [out]
:param offAsum: Offset to absolute sum in **asum** buffer object. Counted in elements.
:type offAsum: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasScasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasScasum <http://clmathlibraries.github.io/clBLAS/group__ASUM.html#gae8a38147c6a1d99b649d279cb0fdb407>`_

absolute sum of values of a vector containing float-complex elements

:param N: Number of elements in vector **X**.
:type N: int [in]
:param asum: Buffer object that will contain the absolute sum value.
:type asum: pyopencl.Buffer [out]
:param offAsum: Offset to absolute sum in **asum** buffer object. Counted in elements.
:type offAsum: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object of minimum size N.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasScasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasCgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasCgemv <http://clmathlibraries.github.io/clBLAS/group__GEMV.html#ga22f1488e4ada5ecea85c366dffffbb0d>`_

Matrix-vector product with a general rectangular matrix and float complex elements. Extended version. Matrix-vector products: 

* ( y |larr| |alpha| A x + |beta| y ) 

* ( y |larr| |alpha| A\ :sup:`T`\ x + |beta| y )



:param order: Row/column order.
:type order: clblasOrder [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param x: Buffer object storing vector **x**.
:type x: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **x** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **x**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of the vector **y**.
:type beta: complex [in]
:param y: Buffer object storing the vector **y**.
:type y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasDgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasDgemv <http://clmathlibraries.github.io/clBLAS/group__GEMV.html#ga6ec9e24c166540d687c0653c2367a829>`_

Matrix-vector product with a general rectangular matrix and double elements. Extended version. Matrix-vector products: 

* ( y |larr| |alpha| A x + |beta| y ) 

* ( y |larr| |alpha| A\ :sup:`T`\ x + |beta| y )



:param order: Row/column order.
:type order: clblasOrder [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param x: Buffer object storing vector **x**.
:type x: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **x** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **x**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of the vector **y**.
:type beta: float [in]
:param y: Buffer object storing the vector **y**.
:type y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasSgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasSgemv <http://clmathlibraries.github.io/clBLAS/group__GEMV.html#gabc2cb7a71197b255ed2a3174fc2e8580>`_

Matrix-vector product with a general rectangular matrix and float elements. Extended version. Matrix-vector products: 

* ( y |larr| |alpha| A x + |beta| y ) 

* ( y |larr| |alpha| A\ :sup:`T`\ x + |beta| y )



:param order: Row/column order.
:type order: clblasOrder [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when the parameter is set to **clblasColumnMajor**.
:type lda: int [in]
:param x: Buffer object storing vector **x**.
:type x: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **x** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **x**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of the vector **y**.
:type beta: float [in]
:param y: Buffer object storing the vector **y**.
:type y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasZgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasZgemv <http://clmathlibraries.github.io/clBLAS/group__GEMV.html#gacf68040cc474f1a0ebef21c62c11e7d2>`_

Matrix-vector product with a general rectangular matrix and double complex elements. Extended version. Matrix-vector products: 

* ( y |larr| |alpha| A x + |beta| y ) 

* ( y |larr| |alpha| A\ :sup:`T`\ x + |beta| y )



:param order: Row/column order.
:type order: clblasOrder [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param x: Buffer object storing vector **x**.
:type x: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **x** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **x**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of the vector **y**.
:type beta: complex [in]
:param y: Buffer object storing the vector **y**.
:type y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasDsymv(order, uplo, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasDsymv <http://clmathlibraries.github.io/clBLAS/group__SYMV.html#gaaaaa79666884be9ef80e037d1280851c>`_

Matrix-vector product with a symmetric matrix and double elements. Matrix-vector products: 

* ( y |larr| |alpha| A x + |beta| y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**. It cannot less than **N**.
:type lda: int [in]
:param x: Buffer object storing vector **x**.
:type x: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **x** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **x**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **y**.
:type beta: float [in]
:param y: Buffer object storing vector **y**.
:type y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDsymv(order, uplo, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasSsymv(order, uplo, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasSsymv <http://clmathlibraries.github.io/clBLAS/group__SYMV.html#gaa0a076ab7bb2c918424c1f5a577e0e42>`_

Matrix-vector product with a symmetric matrix and float elements. Matrix-vector products: 

* ( y |larr| |alpha| A x + |beta| y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**. It cannot less than **N**.
:type lda: int [in]
:param x: Buffer object storing vector **x**.
:type x: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **x** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **x**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **y**.
:type beta: float [in]
:param y: Buffer object storing vector **y**.
:type y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSsymv(order, uplo, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasChemv(order, uplo, N, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasChemv <http://clmathlibraries.github.io/clBLAS/group__HEMV.html#gad02edc212596e6ecd00c647922a8a66a>`_

Matrix-vector product with a hermitian matrix and float-complex elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: complex [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasChemv(order, uplo, N, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasZhemv(order, uplo, N, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasZhemv <http://clmathlibraries.github.io/clBLAS/group__HEMV.html#ga9388229ff62239d8f8ea2eedef2f8af1>`_

Matrix-vector product with a hermitian matrix and double-complex elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: complex [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZhemv(order, uplo, N, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasCtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasCtrmv <http://clmathlibraries.github.io/clBLAS/group__TRMV.html#gad59cbf1c5c61250a0fb8bfadba789037>`_

Matrix-vector product with a triangular matrix and float complex elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasDtrmv <http://clmathlibraries.github.io/clBLAS/group__TRMV.html#gaca35183a87b8562ddc2a5d536b72ec62>`_

Matrix-vector product with a triangular matrix and double elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasStrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasStrmv <http://clmathlibraries.github.io/clBLAS/group__TRMV.html#gadbc52190bf3510e2e2452ad9eb0231fb>`_

Matrix-vector product with a triangular matrix and float elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasStrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasZtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasZtrmv <http://clmathlibraries.github.io/clBLAS/group__TRMV.html#ga1424c90e3abf7b8a33f4a42fb4f56f78>`_

Matrix-vector product with a triangular matrix and double complex elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasCtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasCtrsv <http://clmathlibraries.github.io/clBLAS/group__TRSV.html#ga3bf4841a683582a1971d0861343acb75>`_

solving triangular matrix problems with float-complex elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasDtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasDtrsv <http://clmathlibraries.github.io/clBLAS/group__TRSV.html#gaa1b5e15f7b4f281b0ab15fe5070a8392>`_

solving triangular matrix problems with double elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasStrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasStrsv <http://clmathlibraries.github.io/clBLAS/group__TRSV.html#gac81118a7466fd5bf0a8c9c8aa8ca8b94>`_

solving triangular matrix problems with float elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasStrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasZtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasZtrsv <http://clmathlibraries.github.io/clBLAS/group__TRSV.html#gab04ce87927e30ed59e1b6045d4bea484>`_

solving triangular matrix problems with double-complex elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasDger(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasDger <http://clmathlibraries.github.io/clBLAS/group__GER.html#ga449a136cace1b57b5409d3fc7dac90d5>`_

vector-vector product with double elements and performs the rank 1 operation A Vector-vector products: 

* ( A |larr| |alpha| X Y\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: specifies the scalar alpha.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**. On exit, A is overwritten by the updated matrix.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when the parameter is set to **clblasColumnMajor**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDger(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasSger(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasSger <http://clmathlibraries.github.io/clBLAS/group__GER.html#gaf7f66fa8e62a376c2606223b01b4d33e>`_

vector-vector product with float elements and performs the rank 1 operation A Vector-vector products: 

* ( A |larr| |alpha| X Y\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: specifies the scalar alpha.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**. On exit, A is overwritten by the updated matrix.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when the parameter is set to **clblasColumnMajor**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSger(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasCgeru(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasCgeru <http://clmathlibraries.github.io/clBLAS/group__GERU.html#ga816e54ba610cf074593df2d664dae4cb>`_

vector-vector product with float complex elements and performs the rank 1 operation A Vector-vector products: 

* ( A |larr| |alpha| X Y\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: specifies the scalar alpha.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**. On exit, A is overwritten by the updated matrix.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when the parameter is set to **clblasColumnMajor**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCgeru(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasZgeru(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasZgeru <http://clmathlibraries.github.io/clBLAS/group__GERU.html#ga8819fd184d5cd7fdb9d15f3dc36de533>`_

vector-vector product with double complex elements and performs the rank 1 operation A Vector-vector products: 

* ( A |larr| |alpha| X Y\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: specifies the scalar alpha.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**. On exit, A is overwritten by the updated matrix.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when the parameter is set to **clblasColumnMajor**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZgeru(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasCgerc(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasCgerc <http://clmathlibraries.github.io/clBLAS/group__GERC.html#ga56a5940e875bef708145a5adc7540c9e>`_

vector-vector product with float complex elements and performs the rank 1 operation A Vector-vector products: 

* ( A |larr| |alpha| X Y\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: specifies the scalar alpha.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**. On exit, A is overwritten by the updated matrix.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when the parameter is set to **clblasColumnMajor**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCgerc(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasZgerc(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasZgerc <http://clmathlibraries.github.io/clBLAS/group__GERC.html#ga85e71ec3a57b382e0887a8ec72d240d0>`_

vector-vector product with double complex elements and performs the rank 1 operation A Vector-vector products: 

* ( A |larr| |alpha| X Y\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: specifies the scalar alpha.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**. On exit, A is overwritten by the updated matrix.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when the parameter is set to **clblasColumnMajor**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZgerc(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasDsyr(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasDsyr <http://clmathlibraries.github.io/clBLAS/group__SYR.html#ga8bac6e106ee8dda53d48917f34dec97b>`_

Symmetric rank 1 operation with a general triangular matrix and double elements. Symmetric rank 1 operation: 

* ( A |larr| |alpha| x x\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [out]
:param offa: Offset of first element of matrix **A** in buffer object.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDsyr(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList)

def clblasSsyr(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasSsyr <http://clmathlibraries.github.io/clBLAS/group__SYR.html#gaeb574fbdc1fdbbb4f1d099f8c6d2f0f1>`_

Symmetric rank 1 operation with a general triangular matrix and float elements. Symmetric rank 1 operation: 

* ( A |larr| |alpha| x x\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [out]
:param offa: Offset of first element of matrix **A** in buffer object.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSsyr(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList)

def clblasCher(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasCher <http://clmathlibraries.github.io/clBLAS/group__HER.html#ga684ba5132daf81e5efb687e3a9144100>`_

hermitian rank 1 operation with a general triangular matrix and float-complex elements. hermitian rank 1 operation: 

* ( A |larr| |alpha| X X\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A** (a scalar float value).
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCher(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList)

def clblasZher(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasZher <http://clmathlibraries.github.io/clBLAS/group__HER.html#gad1064fec352eecbf9b35ea1abffa0d25>`_

hermitian rank 1 operation with a general triangular matrix and double-complex elements. hermitian rank 1 operation: 

* ( A |larr| |alpha| X X\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A** (a scalar double value).
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZher(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList)

def clblasDsyr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasDsyr2 <http://clmathlibraries.github.io/clBLAS/group__SYR2.html#gaaf2013281aa5f225c79a001928d1ab71>`_

Symmetric rank 2 operation with a general triangular matrix and double elements. Symmetric rank 2 operation: 

* ( A |larr| |alpha| x y\ :sup:`T`\ + |alpha| y x\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [out]
:param offa: Offset of first element of matrix **A** in buffer object.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDsyr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasSsyr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasSsyr2 <http://clmathlibraries.github.io/clBLAS/group__SYR2.html#ga33866451ca7a0636561a83828acff0f9>`_

Symmetric rank 2 operation with a general triangular matrix and float elements. Symmetric rank 2 operation: 

* ( A |larr| |alpha| x y\ :sup:`T`\ + |alpha| y x\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [out]
:param offa: Offset of first element of matrix **A** in buffer object.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSsyr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasCher2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasCher2 <http://clmathlibraries.github.io/clBLAS/group__HER2.html#ga4113a7d573344651f757dca13025a9e9>`_

Hermitian rank 2 operation with a general triangular matrix and float-compelx elements. Hermitian rank 2 operation: 

* ( A |larr| |alpha| X Y\ :sup:`H`\ + conj{ |alpha| } Y X\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCher2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasZher2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
    """ wraps: `clblasZher2 <http://clmathlibraries.github.io/clBLAS/group__HER2.html#gaf91a79ad8434667abe0c537b2ba89192>`_

Hermitian rank 2 operation with a general triangular matrix and double-compelx elements. Hermitian rank 2 operation: 

* ( A |larr| |alpha| X Y\ :sup:`H`\ + conj{ |alpha| } Y X\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **N**.
:type lda: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZher2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasCtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasCtpmv <http://clmathlibraries.github.io/clBLAS/group__TPMV.html#ga8b55590e7e304acc8b0ce9e07020d78a>`_

Matrix-vector product with a packed triangular matrix and float-complex elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **AP** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **AP** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **AP**.
:type N: int [in]
:param AP: Buffer object storing matrix **AP** in packed format.
:type AP: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **AP**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasDtpmv <http://clmathlibraries.github.io/clBLAS/group__TPMV.html#ga8957d98e5daddc8b3e2849605929ebed>`_

Matrix-vector product with a packed triangular matrix and double elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **AP** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **AP** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **AP**.
:type N: int [in]
:param AP: Buffer object storing matrix **AP** in packed format.
:type AP: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **AP**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasStpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasStpmv <http://clmathlibraries.github.io/clBLAS/group__TPMV.html#gaecafe2c7628d67b93a2d8232210433a6>`_

Matrix-vector product with a packed triangular matrix and float elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **AP** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **AP** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param AP: Buffer object storing matrix **AP** in packed format.
:type AP: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **AP**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasStpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasZtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasZtpmv <http://clmathlibraries.github.io/clBLAS/group__TPMV.html#gab3c492bdddbe4c3c78a8f35b41f54e3a>`_

Matrix-vector product with a packed triangular matrix and double-complex elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **AP** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **AP** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **AP**.
:type N: int [in]
:param AP: Buffer object storing matrix **AP** in packed format.
:type AP: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **AP**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasCtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasCtpsv <http://clmathlibraries.github.io/clBLAS/group__TPSV.html#gab958ceee6960fedd1cced039236b4102>`_

solving triangular packed matrix problems with float complex elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix in packed format. **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList)

def clblasDtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasDtpsv <http://clmathlibraries.github.io/clBLAS/group__TPSV.html#ga1517b6207cbdcc4b820250ba95806665>`_

solving triangular packed matrix problems with double elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix in packed format. **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList)

def clblasStpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasStpsv <http://clmathlibraries.github.io/clBLAS/group__TPSV.html#gab85cc8cc30e89a4a4f631190d532d320>`_

solving triangular packed matrix problems with float elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix in packed format. **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasStpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList)

def clblasZtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasZtpsv <http://clmathlibraries.github.io/clBLAS/group__TPSV.html#ga9827a2b2e45ac638b60da833ee2859ae>`_

solving triangular packed matrix problems with double complex elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in matrix **A**.
:type N: int [in]
:param A: Buffer object storing matrix in packed format. **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList)

def clblasDspmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasDspmv <http://clmathlibraries.github.io/clBLAS/group__SPMV.html#ga8d0216455b03362934ac2acda609f1a2>`_

Matrix-vector product with a symmetric packed-matrix and double elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in matrix **AP**.
:type N: int [in]
:param alpha: The factor of matrix **AP**.
:type alpha: float [in]
:param AP: Buffer object storing matrix **AP**.
:type AP: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **AP**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: float [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDspmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasSspmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasSspmv <http://clmathlibraries.github.io/clBLAS/group__SPMV.html#ga604fd3a102b2b29f92f41e4534b38405>`_

Matrix-vector product with a symmetric packed-matrix and float elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in matrix **AP**.
:type N: int [in]
:param alpha: The factor of matrix **AP**.
:type alpha: float [in]
:param AP: Buffer object storing matrix **AP**.
:type AP: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **AP**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: float [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSspmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasChpmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasChpmv <http://clmathlibraries.github.io/clBLAS/group__HPMV.html#gaa763ee6be9c0fab8fc7f6c534b1ca1d9>`_

Matrix-vector product with a packed hermitian matrix and float-complex elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in matrix **AP**.
:type N: int [in]
:param alpha: The factor of matrix **AP**.
:type alpha: complex [in]
:param AP: Buffer object storing packed matrix **AP**.
:type AP: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **AP**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: complex [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasChpmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasZhpmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasZhpmv <http://clmathlibraries.github.io/clBLAS/group__HPMV.html#gad2ca484bb62e90dc073321709dc5e3fa>`_

Matrix-vector product with a packed hermitian matrix and double-complex elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in matrix **AP**.
:type N: int [in]
:param alpha: The factor of matrix **AP**.
:type alpha: complex [in]
:param AP: Buffer object storing packed matrix **AP**.
:type AP: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **AP**.
:type offa: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: complex [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZhpmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasDspr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList):
    """ wraps: `clblasDspr <http://clmathlibraries.github.io/clBLAS/group__SPR.html#gae627a6d90734a3e6df60d4e93dceaad3>`_

Symmetric rank 1 operation with a general triangular packed-matrix and double elements. Symmetric rank 1 operation: 

* ( A |larr| |alpha| X X\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param AP: Buffer object storing packed-matrix **AP**.
:type AP: pyopencl.Buffer [out]
:param offa: Offset of first element of matrix **AP** in buffer object.
:type offa: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDspr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList)

def clblasSspr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList):
    """ wraps: `clblasSspr <http://clmathlibraries.github.io/clBLAS/group__SPR.html#ga0d90a68dbefa2af95333395549d55251>`_

Symmetric rank 1 operation with a general triangular packed-matrix and float elements. Symmetric rank 1 operation: 

* ( A |larr| |alpha| X X\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param AP: Buffer object storing packed-matrix **AP**.
:type AP: pyopencl.Buffer [out]
:param offa: Offset of first element of matrix **AP** in buffer object.
:type offa: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSspr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList)

def clblasChpr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList):
    """ wraps: `clblasChpr <http://clmathlibraries.github.io/clBLAS/group__HPR.html#ga628703080a9b2bc218273d53ba9b49a9>`_

hermitian rank 1 operation with a general triangular packed-matrix and float-complex elements. hermitian rank 1 operation: 

* ( A |larr| |alpha| X X\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A** (a scalar float value).
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param AP: Buffer object storing matrix **AP**.
:type AP: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **AP**.
:type offa: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasChpr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList)

def clblasZhpr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList):
    """ wraps: `clblasZhpr <http://clmathlibraries.github.io/clBLAS/group__HPR.html#gae692f3e0388f7f3e5a315fd442af789e>`_

hermitian rank 1 operation with a general triangular packed-matrix and double-complex elements. hermitian rank 1 operation: 

* ( A |larr| |alpha| X X\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A** (a scalar float value).
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param AP: Buffer object storing matrix **AP**.
:type AP: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **AP**.
:type offa: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZhpr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList)

def clblasDspr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList):
    """ wraps: `clblasDspr2 <http://clmathlibraries.github.io/clBLAS/group__SPR2.html#gaf80452841c29f564cfaaaf04fbd52323>`_

Symmetric rank 2 operation with a general triangular packed-matrix and double elements. Symmetric rank 2 operation: 

* ( A |larr| |alpha| X Y\ :sup:`T`\ + |alpha| Y X\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param AP: Buffer object storing packed-matrix **AP**.
:type AP: pyopencl.Buffer [out]
:param offa: Offset of first element of matrix **AP** in buffer object.
:type offa: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDspr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList)

def clblasSspr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList):
    """ wraps: `clblasSspr2 <http://clmathlibraries.github.io/clBLAS/group__SPR2.html#ga3cdfb1ef40a2212ffd70de92e6b5002c>`_

Symmetric rank 2 operation with a general triangular packed-matrix and float elements. Symmetric rank 2 operation: 

* ( A |larr| |alpha| X Y\ :sup:`T`\ + |alpha| Y X\ :sup:`T`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset of first element of vector **Y** in buffer object.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param AP: Buffer object storing packed-matrix **AP**.
:type AP: pyopencl.Buffer [out]
:param offa: Offset of first element of matrix **AP** in buffer object.
:type offa: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSspr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList)

def clblasChpr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList):
    """ wraps: `clblasChpr2 <http://clmathlibraries.github.io/clBLAS/group__HPR2.html#ga2af607e07c36182f4aea7594892e2c6d>`_

Hermitian rank 2 operation with a general triangular packed-matrix and float-compelx elements. Hermitian rank 2 operation: 

* ( A |larr| |alpha| X Y\ :sup:`H`\ + conj( alpha ) Y X\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param AP: Buffer object storing packed-matrix **AP**.
:type AP: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **AP**.
:type offa: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasChpr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList)

def clblasZhpr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList):
    """ wraps: `clblasZhpr2 <http://clmathlibraries.github.io/clBLAS/group__HPR2.html#ga3370fdcdd1393fbf4209d1482d771b00>`_

Hermitian rank 2 operation with a general triangular packed-matrix and double-compelx elements. Hermitian rank 2 operation: 

* ( A |larr| |alpha| X Y\ :sup:`H`\ + conj( alpha ) Y X\ :sup:`H`\ + A )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of columns in matrix **A**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset in number of elements for the first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [in]
:param offy: Offset in number of elements for the first element in vector **Y**.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param AP: Buffer object storing packed-matrix **AP**.
:type AP: pyopencl.Buffer [out]
:param offa: Offset in number of elements for the first element in matrix **AP**.
:type offa: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZhpr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList)

def clblasCgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasCgbmv <http://clmathlibraries.github.io/clBLAS/group__GBMV.html#ga5511760f478c859d57a9c720fda7486a>`_

Matrix-vector product with a general rectangular banded matrix and float-complex elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y ) 

* ( Y |larr| |alpha| A\ :sup:`T`\ X + |beta| Y )



:param order: Row/column order.
:type order: clblasOrder [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param M: Number of rows in banded matrix **A**.
:type M: int [in]
:param N: Number of columns in banded matrix **A**.
:type N: int [in]
:param KL: Number of sub-diagonals in banded matrix **A**.
:type KL: int [in]
:param KU: Number of super-diagonals in banded matrix **A**.
:type KU: int [in]
:param alpha: The factor of banded matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing banded matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for the first element in banded matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of banded matrix **A**. It cannot be less than ( **KL** + **KU** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param beta: The factor of the vector **Y**.
:type beta: complex [in]
:param Y: Buffer object storing the vector **y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasDgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasDgbmv <http://clmathlibraries.github.io/clBLAS/group__GBMV.html#ga2b559c78969bee78d0f1b4c1ad9f17ec>`_

Matrix-vector product with a general rectangular banded matrix and double elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y ) 

* ( Y |larr| |alpha| A\ :sup:`T`\ X + |beta| Y )



:param order: Row/column order.
:type order: clblasOrder [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param M: Number of rows in banded matrix **A**.
:type M: int [in]
:param N: Number of columns in banded matrix **A**.
:type N: int [in]
:param KL: Number of sub-diagonals in banded matrix **A**.
:type KL: int [in]
:param KU: Number of super-diagonals in banded matrix **A**.
:type KU: int [in]
:param alpha: The factor of banded matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing banded matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for the first element in banded matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of banded matrix **A**. It cannot be less than ( **KL** + **KU** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param beta: The factor of the vector **Y**.
:type beta: float [in]
:param Y: Buffer object storing the vector **y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasSgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasSgbmv <http://clmathlibraries.github.io/clBLAS/group__GBMV.html#gaa04d900c8d83b97e5646a816b1fac933>`_

Matrix-vector product with a general rectangular banded matrix and float elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y ) 

* ( Y |larr| |alpha| A\ :sup:`T`\ X + |beta| Y )



:param order: Row/column order.
:type order: clblasOrder [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param M: Number of rows in banded matrix **A**.
:type M: int [in]
:param N: Number of columns in banded matrix **A**.
:type N: int [in]
:param KL: Number of sub-diagonals in banded matrix **A**.
:type KL: int [in]
:param KU: Number of super-diagonals in banded matrix **A**.
:type KU: int [in]
:param alpha: The factor of banded matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing banded matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for the first element in banded matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of banded matrix **A**. It cannot be less than ( **KL** + **KU** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param beta: The factor of the vector **Y**.
:type beta: float [in]
:param Y: Buffer object storing the vector **y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasZgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasZgbmv <http://clmathlibraries.github.io/clBLAS/group__GBMV.html#gad82007ef4fd68055eb4f7573361346d6>`_

Matrix-vector product with a general rectangular banded matrix and double-complex elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y ) 

* ( Y |larr| |alpha| A\ :sup:`T`\ X + |beta| Y )



:param order: Row/column order.
:type order: clblasOrder [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param M: Number of rows in banded matrix **A**.
:type M: int [in]
:param N: Number of columns in banded matrix **A**.
:type N: int [in]
:param KL: Number of sub-diagonals in banded matrix **A**.
:type KL: int [in]
:param KU: Number of super-diagonals in banded matrix **A**.
:type KU: int [in]
:param alpha: The factor of banded matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing banded matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for the first element in banded matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of banded matrix **A**. It cannot be less than ( **KL** + **KU** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param beta: The factor of the vector **Y**.
:type beta: complex [in]
:param Y: Buffer object storing the vector **y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of **Y**. Must not be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasCtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasCtbmv <http://clmathlibraries.github.io/clBLAS/group__TBMV.html#ga4e592760b90964d188da3bffa8814961>`_

Matrix-vector product with a triangular banded matrix and float-complex elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in triangular banded matrix **A**.
:type K: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasDtbmv <http://clmathlibraries.github.io/clBLAS/group__TBMV.html#ga72a73e8d67847b699449a94d92fc0762>`_

Matrix-vector product with a triangular banded matrix and double elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in triangular banded matrix **A**.
:type K: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasStbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasStbmv <http://clmathlibraries.github.io/clBLAS/group__TBMV.html#gabfa16c4dda86119486f6f69047b98054>`_

Matrix-vector product with a triangular banded matrix and float elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in triangular banded matrix **A**.
:type K: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasStbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasZtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
    """ wraps: `clblasZtbmv <http://clmathlibraries.github.io/clBLAS/group__TBMV.html#gaf01952e466cf6bb761cc291b2a82aae9>`_

Matrix-vector product with a triangular banded matrix and double-complex elements. Matrix-vector products: 

* ( X |larr| A X ) 

* ( X |larr| A\ :sup:`T`\ X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in triangular banded matrix **A**.
:type K: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param scratchBuff: Temporary cl_mem scratch buffer object which can hold a minimum of (1 + (N-1)*abs(incx)) elements.
:type scratchBuff: pyopencl.Buffer [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDsbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasDsbmv <http://clmathlibraries.github.io/clBLAS/group__SBMV.html#ga5ee7562d914fa80e53e48b7a116ae627>`_

Matrix-vector product with a symmetric banded matrix and double elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in banded matrix **A**.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: float [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDsbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasSsbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasSsbmv <http://clmathlibraries.github.io/clBLAS/group__SBMV.html#gade33d9be70f81d06f295014e088f8fcf>`_

Matrix-vector product with a symmetric banded matrix and float elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in banded matrix **A**.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: float [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSsbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasChbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasChbmv <http://clmathlibraries.github.io/clBLAS/group__HBMV.html#ga41cc199d8297919c3d6ee5c63636b67a>`_

Matrix-vector product with a hermitian banded matrix and float elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in banded matrix **A**.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: complex [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasChbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasZhbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
    """ wraps: `clblasZhbmv <http://clmathlibraries.github.io/clBLAS/group__HBMV.html#gaf0a8116a8dcd71814f9fc1be20cc99f4>`_

Matrix-vector product with a hermitian banded matrix and double elements. Matrix-vector products: 

* ( Y |larr| |alpha| A X + |beta| Y )



:param order: Row/columns order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param N: Number of rows and columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in banded matrix **A**.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [in]
:param offx: Offset of first element of vector **X** in buffer object. Counted in elements.
:type offx: int [in]
:param incx: Increment for the elements of vector **X**. It cannot be zero.
:type incx: int [in]
:param beta: The factor of vector **Y**.
:type beta: complex [in]
:param Y: Buffer object storing vector **Y**.
:type Y: pyopencl.Buffer [out]
:param offy: Offset of first element of vector **Y** in buffer object. Counted in elements.
:type offy: int [in]
:param incy: Increment for the elements of vector **Y**. It cannot be zero.
:type incy: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZhbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasCtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasCtbsv <http://clmathlibraries.github.io/clBLAS/group__TBSV.html#gaef810faf6e624fff42d3bc5c53dae489>`_

solving triangular banded matrix problems with float-complex elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in triangular banded matrix **A**.
:type K: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasDtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasDtbsv <http://clmathlibraries.github.io/clBLAS/group__TBSV.html#ga5e7edcb5f668a94d9f96edcd1a3cd804>`_

solving triangular banded matrix problems with double elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in triangular banded matrix **A**.
:type K: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasStbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasStbsv <http://clmathlibraries.github.io/clBLAS/group__TBSV.html#gadc7262b1bfc4f11f045eff0a5eabee23>`_

solving triangular banded matrix problems with float elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in triangular banded matrix **A**.
:type K: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasStbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasZtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
    """ wraps: `clblasZtbsv <http://clmathlibraries.github.io/clBLAS/group__TBSV.html#gad72c00b6b7135a5c841c9bb2b1b851b7>`_

solving triangular banded matrix problems with double-complex elements. Matrix-vector products: 

* ( A X |larr| X ) 

* ( A\ :sup:`T`\ X |larr| X )



:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param diag: Specify whether matrix **A** is unit triangular.
:type diag: clblasDiag [in]
:param N: Number of rows/columns in banded matrix **A**.
:type N: int [in]
:param K: Number of sub-diagonals/super-diagonals in triangular banded matrix **A**.
:type K: int [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than ( **K** + 1 ).
:type lda: int [in]
:param X: Buffer object storing vector **X**.
:type X: pyopencl.Buffer [out]
:param offx: Offset in number of elements for first element in vector **X**.
:type offx: int [in]
:param incx: Increment for the elements of **X**. Must not be zero.
:type incx: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasCgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasCgemm <http://clmathlibraries.github.io/clBLAS/group__GEMM.html#ga48e1cfff6b71f538618cfd0774e92eef>`_

Matrix-matrix product of general rectangular matrices with float complex elements. Extended version. <dl class="section note"> <dt> Note </dt> <dd> This function is not thread-safe. </dd> </dl> Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B + |beta| C ) 

* ( C |larr| |alpha| A B\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B\ :sup:`T`\ + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param transB: How matrix **B** is to be transposed.
:type transB: clblasTranspose [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param K: Number of columns in matrix **A** and rows in matrix **B**.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasDgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasDgemm <http://clmathlibraries.github.io/clBLAS/group__GEMM.html#ga15b5b2ba7a28915e41f63342c108949b>`_

Matrix-matrix product of general rectangular matrices with double elements. Extended version. <dl class="section note"> <dt> Note </dt> <dd> This function is not thread-safe. </dd> </dl> Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B + |beta| C ) 

* ( C |larr| |alpha| A B\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B\ :sup:`T`\ + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param transB: How matrix **B** is to be transposed.
:type transB: clblasTranspose [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param K: Number of columns in matrix **A** and rows in matrix **B**.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasSgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasSgemm <http://clmathlibraries.github.io/clBLAS/group__GEMM.html#ga29d93e46c106ce34249f21e436ed7102>`_

Matrix-matrix product of general rectangular matrices with float elements. Extended version. <dl class="section note"> <dt> Note </dt> <dd> This function is not thread-safe. </dd> </dl> Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B + |beta| C ) 

* ( C |larr| |alpha| A B\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B\ :sup:`T`\ + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param transB: How matrix **B** is to be transposed.
:type transB: clblasTranspose [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param K: Number of columns in matrix **A** and rows in matrix **B**.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **K** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when the parameter is set to **clblasColumnMajor**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **K** when it is set to **clblasColumnMajor**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajorOrder**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasZgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasZgemm <http://clmathlibraries.github.io/clBLAS/group__GEMM.html#gafd4a1ef1f8a7273005eb32fb6da12e4c>`_

Matrix-matrix product of general rectangular matrices with double complex elements. Exteneded version. <dl class="section note"> <dt> Note </dt> <dd> This function is not thread-safe. </dd> </dl> Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B + |beta| C ) 

* ( C |larr| |alpha| A B\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B\ :sup:`T`\ + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param transB: How matrix **B** is to be transposed.
:type transB: clblasTranspose [in]
:param M: Number of rows in matrix **A**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param K: Number of columns in matrix **A** and rows in matrix **B**.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasCtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
    """ wraps: `clblasCtrmm <http://clmathlibraries.github.io/clBLAS/group__TRMM.html#ga3b4c8d0d6fc5b42ccc35e3ef8bf5733b>`_

Multiplying a matrix by a triangular matrix with float complex elements. Extended version. Matrix-triangular matrix products: 

* ( B |larr| |alpha| A B ) 

* ( B |larr| |alpha| A\ :sup:`T`\ B ) 

* ( B |larr| |alpha| B A ) 

* ( B |larr| |alpha| B A\ :sup:`T`\ )

 where **T** is an upper or lower triangular matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param diag: Specify whether matrix is unit triangular.
:type diag: clblasDiag [in]
:param M: Number of rows in matrix **B**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [out]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasDtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
    """ wraps: `clblasDtrmm <http://clmathlibraries.github.io/clBLAS/group__TRMM.html#gac40593ed2d256a65e957b8a98f843869>`_

Multiplying a matrix by a triangular matrix with double elements. Extended version. Matrix-triangular matrix products: 

* ( B |larr| |alpha| A B ) 

* ( B |larr| |alpha| A\ :sup:`T`\ B ) 

* ( B |larr| |alpha| B A ) 

* ( B |larr| |alpha| B A\ :sup:`T`\ )

 where **T** is an upper or lower triangular matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param diag: Specify whether matrix is unit triangular.
:type diag: clblasDiag [in]
:param M: Number of rows in matrix **B**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [out]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasStrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
    """ wraps: `clblasStrmm <http://clmathlibraries.github.io/clBLAS/group__TRMM.html#ga62d4746230cfe35d46130d58d6d66918>`_

Multiplying a matrix by a triangular matrix with float elements. Extended version. Matrix-triangular matrix products: 

* ( B |larr| |alpha| A B ) 

* ( B |larr| |alpha| A\ :sup:`T`\ B ) 

* ( B |larr| |alpha| B A ) 

* ( B |larr| |alpha| B A\ :sup:`T`\ )

 where **T** is an upper or lower triangular matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param diag: Specify whether matrix is unit triangular.
:type diag: clblasDiag [in]
:param M: Number of rows in matrix **B**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **M** when the **side** parameter is set to **clblasLeft**, or less than **N** when it is set to **clblasRight**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [out]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or not less than **M** when it is set to **clblasColumnMajor**.
:type ldb: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasStrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasZtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
    """ wraps: `clblasZtrmm <http://clmathlibraries.github.io/clBLAS/group__TRMM.html#gad4f14676b00d2c7edac522a4777ebd0e>`_

Multiplying a matrix by a triangular matrix with double complex elements. Extended version. Matrix-triangular matrix products: 

* ( B |larr| |alpha| A B ) 

* ( B |larr| |alpha| A\ :sup:`T`\ B ) 

* ( B |larr| |alpha| B A ) 

* ( B |larr| |alpha| B A\ :sup:`T`\ )

 where **T** is an upper or lower triangular matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param diag: Specify whether matrix is unit triangular.
:type diag: clblasDiag [in]
:param M: Number of rows in matrix **B**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [out]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasCtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
    """ wraps: `clblasCtrsm <http://clmathlibraries.github.io/clBLAS/group__TRSM.html#ga14ab01c2bb58270fd8fa7013c15ff44b>`_

Solving triangular systems of equations with multiple right-hand sides and float complex elements. Extended version. Solving triangular systems of equations: 

* ( B |larr| |alpha| A\ :sup:`-1`\ B ) 

* ( B |larr| |alpha| A^{-T} B ) 

* ( B |larr| |alpha| B A\ :sup:`-1`\ ) 

* ( B |larr| |alpha| B A^{-T} )

 where **T** is an upper or lower triangular matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param diag: Specify whether matrix is unit triangular.
:type diag: clblasDiag [in]
:param M: Number of rows in matrix **B**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [out]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasDtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
    """ wraps: `clblasDtrsm <http://clmathlibraries.github.io/clBLAS/group__TRSM.html#ga5969c2fd6e74889f60ee4afc7259e2c0>`_

Solving triangular systems of equations with multiple right-hand sides and double elements. Extended version. <dl class="section note"> <dt> Note </dt> <dd> This function is not thread-safe. </dd> </dl> Solving triangular systems of equations: 

* ( B |larr| |alpha| A\ :sup:`-1`\ B ) 

* ( B |larr| |alpha| A^{-T} B ) 

* ( B |larr| |alpha| B A\ :sup:`-1`\ ) 

* ( B |larr| |alpha| B A^{-T} )

 where **T** is an upper or lower triangular matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param diag: Specify whether matrix is unit triangular.
:type diag: clblasDiag [in]
:param M: Number of rows in matrix **B**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [out]
:param offB: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasStrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
    """ wraps: `clblasStrsm <http://clmathlibraries.github.io/clBLAS/group__TRSM.html#ga7bc3d6be7e001a5f4e585ab6f63abbff>`_

Solving triangular systems of equations with multiple right-hand sides and float elements. Extended version. <dl class="section note"> <dt> Note </dt> <dd> This function is not thread-safe. </dd> </dl> Solving triangular systems of equations: 

* ( B |larr| |alpha| A\ :sup:`-1`\ B ) 

* ( B |larr| |alpha| A^{-T} B ) 

* ( B |larr| |alpha| B A\ :sup:`-1`\ ) 

* ( B |larr| |alpha| B A^{-T} )

 where **T** is an upper or lower triangular matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param diag: Specify whether matrix is unit triangular.
:type diag: clblasDiag [in]
:param M: Number of rows in matrix **B**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **M** when the **side** parameter is set to **clblasLeft**, or less than **N** when it is set to **clblasRight**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [out]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajor**.
:type ldb: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasStrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasZtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
    """ wraps: `clblasZtrsm <http://clmathlibraries.github.io/clBLAS/group__TRSM.html#ga2dfaa0f5690e064b80217cdd96e494ed>`_

Solving triangular systems of equations with multiple right-hand sides and double complex elements. Extended version. Solving triangular systems of equations: 

* ( B |larr| |alpha| A\ :sup:`-1`\ B ) 

* ( B |larr| |alpha| A^{-T} B ) 

* ( B |larr| |alpha| B A\ :sup:`-1`\ ) 

* ( B |larr| |alpha| B A^{-T} )

 where **T** is an upper or lower triangular matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param diag: Specify whether matrix is unit triangular.
:type diag: clblasDiag [in]
:param M: Number of rows in matrix **B**.
:type M: int [in]
:param N: Number of columns in matrix **B**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [out]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasCsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasCsyrk <http://clmathlibraries.github.io/clBLAS/group__SYRK.html#ga7796e311aa0f99a5317564a8ed313e89>`_

Rank-k update of a symmetric matrix with complex float elements. Extended version. Rank-k updates: 

* ( C |larr| |alpha| A A\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ A + |beta| C )

 where **C** is a symmetric matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrix **A** if it is not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing the matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param beta: The factor of the matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasDsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasDsyrk <http://clmathlibraries.github.io/clBLAS/group__SYRK.html#ga5b7064ab71f4f3a827446c84c6c512a0>`_

Rank-k update of a symmetric matrix with double elements. Extended version. Rank-k updates: 

* ( C |larr| |alpha| A A\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ A + |beta| C )

 where **C** is a symmetric matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrix **A** if it is not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing the matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param beta: The factor of the matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasSsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasSsyrk <http://clmathlibraries.github.io/clBLAS/group__SYRK.html#ga855fe4caf5d558c384ecd8cdde90b82f>`_

Rank-k update of a symmetric matrix with float elements. Extended version. Rank-k updates: 

* ( C |larr| |alpha| A A\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ A + |beta| C )

 where **C** is a symmetric matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrix **A** if it is not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing the matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **K** if **A** is in the row-major format, and less than **N** otherwise.
:type lda: int [in]
:param beta: The factor of the matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matric **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasZsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasZsyrk <http://clmathlibraries.github.io/clBLAS/group__SYRK.html#ga5db94dda44d9ce72d166e217ba4fc270>`_

Rank-k update of a symmetric matrix with complex double elements. Extended version. Rank-k updates: 

* ( C |larr| |alpha| A A\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ A + |beta| C )

 where **C** is a symmetric matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrix **A** if it is not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing the matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param beta: The factor of the matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasCsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasCsyr2k <http://clmathlibraries.github.io/clBLAS/group__SYR2K.html#ga4e1b05eda371a0c092672f6d0ca531d9>`_

Rank-2k update of a symmetric matrix with complex float elements. Extended version. Rank-k updates: 

* ( C |larr| |alpha| A B\ :sup:`T`\ + |alpha| B A\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B + |alpha| B\ :sup:`T`\ A |beta| C )

 where **C** is a symmetric matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transAB: How matrices **A** and **B** is to be transposed.
:type transAB: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrices **A** and **B** if they are not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrices **A** and **B**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasDsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasDsyr2k <http://clmathlibraries.github.io/clBLAS/group__SYR2K.html#gaecbabd3654eb14e5f39fe30cfb6f2e16>`_

Rank-2k update of a symmetric matrix with double elements. Extended version. Rank-k updates: 

* ( C |larr| |alpha| A B\ :sup:`T`\ + |alpha| B A\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B + |alpha| B\ :sup:`T`\ A |beta| C )

 where **C** is a symmetric matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transAB: How matrices **A** and **B** is to be transposed.
:type transAB: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrices **A** and **B** if they are not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrices **A** and **B**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasSsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasSsyr2k <http://clmathlibraries.github.io/clBLAS/group__SYR2K.html#gae485aa188f701b8738582f5170ee3cc3>`_

Rank-2k update of a symmetric matrix with float elements. Extended version. Rank-k updates: 

* ( C |larr| |alpha| A B\ :sup:`T`\ + |alpha| B A\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B + |alpha| B\ :sup:`T`\ A |beta| C )

 where **C** is a symmetric matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transAB: How matrices **A** and **B** is to be transposed.
:type transAB: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrices **A** and **B** if they are not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrices **A** and **B**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **K** if **A** is in the row-major format, and less than **N** otherwise.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less less than **K** if **B** matches to the op( **B** ) matrix in the row-major format, and less than **N** otherwise.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasZsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasZsyr2k <http://clmathlibraries.github.io/clBLAS/group__SYR2K.html#ga078b6914012db7de88785ff06c009c09>`_

Rank-2k update of a symmetric matrix with complex double elements. Extended version. Rank-k updates: 

* ( C |larr| |alpha| A B\ :sup:`T`\ + |alpha| B A\ :sup:`T`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`T`\ B + |alpha| B\ :sup:`T`\ A |beta| C )

 where **C** is a symmetric matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transAB: How matrices **A** and **B** is to be transposed.
:type transAB: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrices **A** and **B** if they are not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrices **A** and **B**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offA: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offA: int [in]
:param lda: Leading dimension of matrix **A**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offB: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offB: int [in]
:param ldb: Leading dimension of matrix **B**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offC: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offC: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasCsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasCsymm <http://clmathlibraries.github.io/clBLAS/group__SYMM.html#ga65007c705039f6b2e53ab43db2bb8c82>`_

Matrix-matrix product of symmetric rectangular matrices with float-complex elements. Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| B A + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param M: Number of rows in matrices **B** and **C**.
:type M: int [in]
:param N: Number of columns in matrices **B** and **C**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **M** when the **side** parameter is set to **clblasLeft**, or less than **N** when the parameter is set to **clblasRight**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offb: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offb: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajor**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offc: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajorOrder**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasDsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasDsymm <http://clmathlibraries.github.io/clBLAS/group__SYMM.html#ga4dc9d222524e4a8f40bde73e9c6c6cd1>`_

Matrix-matrix product of symmetric rectangular matrices with double elements. Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| B A + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param M: Number of rows in matrices **B** and **C**.
:type M: int [in]
:param N: Number of columns in matrices **B** and **C**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **M** when the **side** parameter is set to **clblasLeft**, or less than **N** when the parameter is set to **clblasRight**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offb: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offb: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajor**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offc: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajorOrder**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasDsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasSsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasSsymm <http://clmathlibraries.github.io/clBLAS/group__SYMM.html#ga05b89edae61d4311530d356636f58594>`_

Matrix-matrix product of symmetric rectangular matrices with float elements. Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| B A + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param M: Number of rows in matrices **B** and **C**.
:type M: int [in]
:param N: Number of columns in matrices **B** and **C**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **M** when the **side** parameter is set to **clblasLeft**, or less than **N** when the parameter is set to **clblasRight**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offb: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offb: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajor**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offc: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajorOrder**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasSsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasZsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasZsymm <http://clmathlibraries.github.io/clBLAS/group__SYMM.html#ga13a1d3c000da901eeacae2a44526d45e>`_

Matrix-matrix product of symmetric rectangular matrices with double-complex elements. Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| B A + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param M: Number of rows in matrices **B** and **C**.
:type M: int [in]
:param N: Number of columns in matrices **B** and **C**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **M** when the **side** parameter is set to **clblasLeft**, or less than **N** when the parameter is set to **clblasRight**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offb: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offb: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajor**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offc: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajorOrder**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasChemm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasChemm <http://clmathlibraries.github.io/clBLAS/group__HEMM.html#ga143ba8c1dd56b4c15bfe99af0c73a0c9>`_

Matrix-matrix product of hermitian rectangular matrices with float-complex elements. Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| B A + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param M: Number of rows in matrices **B** and **C**.
:type M: int [in]
:param N: Number of columns in matrices **B** and **C**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **M** when the **side** parameter is set to **clblasLeft**, or less than **N** when the parameter is set to **clblasRight**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offb: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offb: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajor**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offc: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajorOrder**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasChemm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasZhemm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasZhemm <http://clmathlibraries.github.io/clBLAS/group__HEMM.html#ga19e6415ed91f9681724dfd84d33b6a74>`_

Matrix-matrix product of hermitian rectangular matrices with double-complex elements. Matrix-matrix products: 

* ( C |larr| |alpha| A B + |beta| C ) 

* ( C |larr| |alpha| B A + |beta| C )



:param order: Row/column order.
:type order: clblasOrder [in]
:param side: The side of triangular matrix.
:type side: clblasSide [in]
:param uplo: The triangle in matrix being referenced.
:type uplo: clblasUplo [in]
:param M: Number of rows in matrices **B** and **C**.
:type M: int [in]
:param N: Number of columns in matrices **B** and **C**.
:type N: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset of the first element of the matrix **A** in the buffer object. Counted in elements.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **M** when the **side** parameter is set to **clblasLeft**, or less than **N** when the parameter is set to **clblasRight**.
:type lda: int [in]
:param B: Buffer object storing matrix **B**.
:type B: pyopencl.Buffer [in]
:param offb: Offset of the first element of the matrix **B** in the buffer object. Counted in elements.
:type offb: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajor**.
:type ldb: int [in]
:param beta: The factor of matrix **C**.
:type beta: complex [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset of the first element of the matrix **C** in the buffer object. Counted in elements.
:type offc: int [in]
:param ldc: Leading dimension of matrix **C**. It cannot be less than **N** when the **order** parameter is set to **clblasRowMajor**, or less than **M** when it is set to **clblasColumnMajorOrder**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZhemm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasCherk(order, uplo, transA, N, K, alpha, A, offa, lda, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasCherk <http://clmathlibraries.github.io/clBLAS/group__HERK.html#gae36c1bb0eea63739fb980518aacaa845>`_

Rank-k update of a hermitian matrix with float-complex elements. Rank-k updates: 

* ( C |larr| |alpha| A A\ :sup:`H`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`H`\ A + |beta| C )

 where **C** is a hermitian matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrix **A** if it is not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing the matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **K** if **A** is in the row-major format, and less than **N** otherwise.
:type lda: int [in]
:param beta: The factor of the matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset in number of elements for the first element in matrix **C**.
:type offc: int [in]
:param ldc: Leading dimension of matric **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCherk(order, uplo, transA, N, K, alpha, A, offa, lda, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasZherk(order, uplo, transA, N, K, alpha, A, offa, lda, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasZherk <http://clmathlibraries.github.io/clBLAS/group__HERK.html#gad03f4708b471ad0ebdbee35f2e54fb51>`_

Rank-k update of a hermitian matrix with double-complex elements. Rank-k updates: 

* ( C |larr| |alpha| A A\ :sup:`H`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`H`\ A + |beta| C )

 where **C** is a hermitian matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param transA: How matrix **A** is to be transposed.
:type transA: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrix **A** if it is not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: float [in]
:param A: Buffer object storing the matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **K** if **A** is in the row-major format, and less than **N** otherwise.
:type lda: int [in]
:param beta: The factor of the matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset in number of elements for the first element in matrix **C**.
:type offc: int [in]
:param ldc: Leading dimension of matric **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZherk(order, uplo, transA, N, K, alpha, A, offa, lda, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasCher2k(order, uplo, trans, N, K, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasCher2k <http://clmathlibraries.github.io/clBLAS/group__HER2K.html#gad57ea871cab72d51039bf9706bc630ee>`_

Rank-2k update of a hermitian matrix with float-complex elements. Rank-k updates: 

* ( C |larr| |alpha| A B\ :sup:`H`\ + conj( |alpha| ) B A\ :sup:`H`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`H`\ B + conj( |alpha| ) B\ :sup:`H`\ A + |beta| C )

 where **C** is a hermitian matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrix **A** if it is not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing the matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **K** if **A** is in the row-major format, and less than **N** otherwise. Vice-versa for transpose case.
:type lda: int [in]
:param B: Buffer object storing the matrix **B**.
:type B: pyopencl.Buffer [in]
:param offb: Offset in number of elements for the first element in matrix **B**.
:type offb: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **K** if **B** is in the row-major format, and less than **N** otherwise. Vice-versa for transpose case.
:type ldb: int [in]
:param beta: The factor of the matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset in number of elements for the first element in matrix **C**.
:type offc: int [in]
:param ldc: Leading dimension of matric **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasCher2k(order, uplo, trans, N, K, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasZher2k(order, uplo, trans, N, K, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
    """ wraps: `clblasZher2k <http://clmathlibraries.github.io/clBLAS/group__HER2K.html#ga2e416d0f1f22d51f415a35370d332a9e>`_

Rank-2k update of a hermitian matrix with double-complex elements. Rank-k updates: 

* ( C |larr| |alpha| A B\ :sup:`H`\ + conj( |alpha| ) B A\ :sup:`H`\ + |beta| C ) 

* ( C |larr| |alpha| A\ :sup:`H`\ B + conj( |alpha| ) B\ :sup:`H`\ A + |beta| C )

 where **C** is a hermitian matrix.

:param order: Row/column order.
:type order: clblasOrder [in]
:param uplo: The triangle in matrix **C** being referenced.
:type uplo: clblasUplo [in]
:param trans: How matrix **A** is to be transposed.
:type trans: clblasTranspose [in]
:param N: Number of rows and columns in matrix **C**.
:type N: int [in]
:param K: Number of columns of the matrix **A** if it is not transposed, and number of rows otherwise.
:type K: int [in]
:param alpha: The factor of matrix **A**.
:type alpha: complex [in]
:param A: Buffer object storing the matrix **A**.
:type A: pyopencl.Buffer [in]
:param offa: Offset in number of elements for the first element in matrix **A**.
:type offa: int [in]
:param lda: Leading dimension of matrix **A**. It cannot be less than **K** if **A** is in the row-major format, and less than **N** otherwise. Vice-versa for transpose case.
:type lda: int [in]
:param B: Buffer object storing the matrix **B**.
:type B: pyopencl.Buffer [in]
:param offb: Offset in number of elements for the first element in matrix **B**.
:type offb: int [in]
:param ldb: Leading dimension of matrix **B**. It cannot be less than **K** if B is in the row-major format, and less than **N** otherwise. Vice-versa for transpose case.
:type ldb: int [in]
:param beta: The factor of the matrix **C**.
:type beta: float [in]
:param C: Buffer object storing matrix **C**.
:type C: pyopencl.Buffer [out]
:param offc: Offset in number of elements for the first element in matrix **C**.
:type offc: int [in]
:param ldc: Leading dimension of matric **C**. It cannot be less than **N**.
:type ldc: int [in]
:param commandQueues: OpenCL command queues. A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None.
:type commandQueues: pyopencl.CommandQueue [in]
:param eventWaitList: Event wait list. A list, tuple, or single instance of pyopencl.Event. May be None.
:type eventWaitList: pyopencl.Event [in]
:return: A tuple of pyopencl.Event instances, one for each commandQueue supplied.

"""
    return pyclblas_swig.clblasZher2k(order, uplo, trans, N, K, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

