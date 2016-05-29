#!/usr/bin/env python2.7

from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import pyclblas as blas
import time

#Select a problem size
M = 5000
K = 1000
N = 5000
total_flops = M*K*(2*N+3)
measure_transfer = True #Whether to include memory transfers in performance calculations

#Select device
ctx = cl.create_some_context()

#Generate input data
a_np = np.random.rand(M*K).astype(np.float32).reshape(M,K)
b_np = np.random.rand(K*N).astype(np.float32).reshape(K,N)
res_np = np.zeros((M,N)).astype(np.float32)
exp_np = np.copy(res_np)

cl_start_time = time.time()

#Create a compute queue
queue = cl.CommandQueue(ctx)

#Copy memory onto the device
a_g = cl.Buffer(ctx, cl.mem_flags.READ_WRITE, a_np.nbytes)
b_g = cl.Buffer(ctx, cl.mem_flags.READ_WRITE, b_np.nbytes)
res_g = cl.Buffer(ctx, 0, res_np.nbytes)
cl.enqueue_copy(queue, a_g, a_np)
cl.enqueue_copy(queue, b_g, b_np)

if not measure_transfer:
    queue.finish()
    cl_start_time = time.time()

#Perform a matrix-matrix multiply using GEMM
events = blas.clblasSgemm(
    blas.clblasRowMajor,
    blas.clblasNoTrans,
    blas.clblasNoTrans,
    M, N, K,
    1.0,
    a_g, 0, K,
    b_g, 0, N,
    0.0, res_g, 0, N,
    (queue,),
    None
)

#Copy the result back to host memory
if not measure_transfer:
    queue.finish()
    cl_end_time = time.time()
    cl.enqueue_copy(queue, res_np, res_g)
    queue.finish()
else:
    cl.enqueue_copy(queue, res_np, res_g)
    queue.finish()
    cl_end_time = time.time()

print("OpenCL time: %f" % (cl_end_time-cl_start_time))
print("OpenCL GFLOPS: %f" % (total_flops / (cl_end_time-cl_start_time) / (1024 ** 3)))

#Check reuslt with Numpy:
np_start_time = time.time()
np.dot(a_np, b_np, out=exp_np)
np_end_time = time.time()
print("Numpy time: %f" % (np_end_time-np_start_time))
print("Numpy GFLOPS: %f" % (total_flops / (np_end_time-np_start_time) / (1024 ** 3)))

#Results
print("Total speedup: %5.5gx" % ((np_end_time-np_start_time)/(cl_end_time-cl_start_time)))
print("L2 Norm of (observed-expected):", np.linalg.norm(res_np - exp_np))
