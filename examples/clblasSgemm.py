#!/usr/bin/env python2.7

from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import pyclblas as blas
import time

a_np = np.random.rand(500).astype(np.float32).reshape(50,10)
b_np = np.random.rand(500).astype(np.float32).reshape(10,50)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)
res_np = np.zeros_like(np.dot(a_np, b_np))
res_g = cl.Buffer(ctx, 0, res_np.nbytes)

events = blas.clblasSgemm(
    blas.clblasRowMajor,
    blas.clblasNoTrans,
    blas.clblasNoTrans,
    50, 50, 10,
    1.0,
    a_g, 0, 10,
    b_g, 0, 50,
    0.0, res_g, 0, 50,
    (queue,),
    tuple()
)

#res_np = np.empty_like(a_np)
cl.enqueue_copy(queue, res_np, res_g)
queue.finish()

# Check on CPU with Numpy:
#print(res_np - (a_np + b_np))
print("L2 Norm of (observed-expected):", np.linalg.norm(res_np - np.dot(a_np, b_np)))


