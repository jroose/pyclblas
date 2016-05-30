#!/usr/bin/env python

import pyopencl as cl
import pyclblas
import scipy.linalg.blas
import numpy as np
import random
import sys
import inspect
import itertools

def randval(dtype):
    if dtype in (np.float32, np.float64):
        return random.random()
    elif dtype in (np.complex64, np.complex128):
        return complex(random.random(), random.random())
    else:
        raise NotImplementedError("randval(dtype=" + str(dtype)+")")

def randmat(shape, dtype):
    if dtype in (np.float32, np.float64):
        return (np.random.rand(*shape).astype(dtype))
    elif dtype in (np.complex64, np.complex128):
        r=np.random.rand(*shape).astype(dtype)
        i=np.random.rand(*shape).astype(dtype)
        r += i * 1j

        return (r)
    else:
        raise NotImplementedError("randmat(shape, dtype=" + str(dtype)+")")


def gemm(queue, dtype, scale):
    M = 4 * scale
    N = 3 * scale
    K = 5 * scale

    #alpha = randval(dtype)
    #beta = randval(dtype)
    A = randmat((M,K), dtype)
    B = randmat((K,N), dtype)
    C = randmat((M,N), dtype)

    ret = []
    for transA in (False, True):
        for transB in (False, True):
            if transA:
                tA = np.ascontiguousarray(A.T)
            else:
                tA = A

            if transB:
                tB = np.ascontiguousarray(B.T)
            else:
                tB = B

            for alpha_type in (int, long, float, complex):
                if (alpha_type is complex) and (dtype not in (np.complex64, np.complex128)):
                    continue

                if (alpha_type is complex) or (dtype not in (np.complex64, np.complex128)):
                    alpha = alpha_type(randval(dtype) * 3)
                    beta = alpha_type(randval(dtype) * 3)
                else:
                    alpha = alpha_type(randval(np.float64) * 3)
                    beta = alpha_type(randval(np.float64) * 3)


                clargsin = (
                    pyclblas.clblasRowMajor,
                    (pyclblas.clblasNoTrans, pyclblas.clblasTrans)[transA],
                    (pyclblas.clblasNoTrans, pyclblas.clblasTrans)[transB],
                    M,N,K,
                    alpha,
                    tA, 0, tA.shape[1],
                    tB, 0, tB.shape[1],
                    beta,
                    C, 0, C.shape[1],
                    queue,
                    None
                )

                clargsout = (C,)

                blasargsin = (
                    alpha, tA, tB,
                    beta, C,
                    transA, transB, True
                )

                blasargsout = (C,)

                ret.append((clargsin, clargsout, blasargsin, blasargsout))

    return ret

def gemv(queue, dtype, scale):
    M = 4 * scale
    N = 3 * scale

    A = randmat((M,N), dtype)

    offA = 0
    offx = 0
    incx = 1
    offy = 0
    incy = 1

    ret = []
    for transA in (False, True):
        if transA:
            tA = np.ascontiguousarray(A.T)
        else:
            tA = A

        for offx, offy, incx, incy in itertools.product((0,1,2,11), (0,1,2,11), (1,2,3,11), (1,2,3,11)):
            X = randmat((N * incx + offx,), dtype)
            Y = randmat((M * incy + offy,), dtype)

            for alpha_type in (int, long, float, complex):
                if (alpha_type is complex) and (dtype not in (np.complex64, np.complex128)):
                    continue

                if (alpha_type is complex) or (dtype not in (np.complex64, np.complex128)):
                    alpha = alpha_type(randval(dtype) * 3)
                    beta = alpha_type(randval(dtype) * 3)
                else:
                    alpha = alpha_type(randval(np.float64) * 3)
                    beta = alpha_type(randval(np.float64) * 3)

                clargsin = (
                    pyclblas.clblasRowMajor,
                    (pyclblas.clblasNoTrans, pyclblas.clblasTrans)[transA],
                    tA.shape[0], tA.shape[1],
                    alpha,
                    tA, offA, tA.shape[-1],
                    X, offx, incx,
                    beta,
                    Y, offy, incy,
                    queue,
                    None
                )

                clargsout = (Y,)

                blasargsin = (
                    alpha, tA, X, beta, Y,
                    offx, incx, offy, incy,
                    transA, True
                )

                blasargsout = (Y,)

                ret.append((clargsin, clargsout, blasargsin, blasargsout))

    return ret

def axpy(queue, dtype, scale):
    N = 100 * scale

    ret = []

    for offx in (0,1,2,3,10):
        for offy in (0,1,2,5,10):
            for incx in (1,2,3,4):
                for incy in (1,2,3,4):
                    for alpha_type in (int, long, float, complex):
                        if alpha_type in (int, long, float):
                            alpha = alpha_type(offx + offy)
                        elif alpha_type is complex:
                            if dtype not in (np.complex64, np.complex128):
                                continue
                            alpha = complex(offx, offy)
                        X = randmat((N*incx+offx,), dtype)
                        Y = randmat((N*incy+offy,), dtype)

                        clargsin = (
                            N,
                            alpha,
                            X, offx, incx,
                            Y, offy, incy,
                            queue,
                            None
                        )

                        clargsout = (Y,)

                        blasargsin = (
                            X, Y, N, alpha, 
                            offx, incx,
                            offy, incy
                        )

                        blasargsout = (Y,)

                        ret.append((clargsin, clargsout, blasargsin, blasargsout))

    return ret
    

class TestPyCLBLAS:
    typechars = {
        np.float32: "S",
        np.float64: "D",
        np.complex64: "C",
        np.complex128: "Z"
    }

    dtypes = {
        "S":np.float32,
        "D":np.float64,
        "C":np.complex64,
        "Z":np.complex128
    }

    cases = [
        ("SDCZ", "gemv"),
        ("SDCZ", "gemm"),
        ("SDCZ", "axpy")
    ]

    @classmethod
    def setupClass(cls):
        cls.context = cl.create_some_context()
        cls.queue = cl.CommandQueue(cls.context)

    @classmethod
    def teardownAll(cls):
        cls.context = None
        cls.queue = None

    def clmat(self, val):
        ret = cl.Buffer(self.context, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=val)
        return ret

    def runtest(self, clfunc, clargsin, clargsout, spfunc, spargsin, spargsout):
        clargs = tuple(self.clmat(x) if isinstance(x, np.ndarray) else x for x in clargsin)
        clargs = zip(clargsin, clargs)
        spargs = tuple(np.asfortranarray(x) if isinstance(x, np.ndarray) else x for x in spargsin)
        spargs = zip(spargsin, spargs)

        def lookup(pairs, x):
            for x0, x1 in pairs:
                if x0 is x:
                    return x1
            return None
        
        try:
            clfunc(*[x[1] for x in clargs])
            self.queue.finish()
            spfunc(*[x[1] for x in spargs])

            for cla, spa in zip(clargsout, spargsout):
                clout = lookup(clargs, cla)
                assert isinstance(clout, cl.Buffer)
                cl.enqueue_copy(self.queue, cla, clout)
                spa = lookup(spargs, spa)
                assert isinstance(spa, np.ndarray)
                self.queue.finish()

                assert np.linalg.norm(cla - spa) <= np.linalg.norm(spa) * 0.01
        except:
            args, varargs, keywords, defaults = inspect.getargspec(clfunc)

            it = 0
            print clfunc.func_name
            for x in clargs:
                if isinstance(x[1], cl.Buffer):
                    print it, args[it], x[1], type(x[1]), x[0].shape, x[0].dtype, x[0].nbytes, x[1].size
                else:
                    print it, args[it], x[1], type(x[1])
                it += 1
            print

            raise

    
    def test_generator(self):
        for ctypes, family in self.cases:
            for ctype in ctypes:
                clblas_name = "clblas%s%s" % (ctype.upper(), family.lower())
                spblas_name = "%s%s" % (ctype.lower(), family.lower())

                for scale in (1,10,30):
                    for clin, clout, spin, spout in globals()[family.lower()](self.queue, self.dtypes[ctype], scale):
                        yield (self.runtest, getattr(pyclblas, clblas_name), clin, clout, getattr(scipy.linalg.blas, spblas_name), spin, spout)
