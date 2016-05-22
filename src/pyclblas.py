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

def clblasGetVersion(major, minor, patch):
    return pyclblas_swig.clblasGetVersion(major, minor, patch)

def clblasSetup():
    return pyclblas_swig.clblasSetup()

def clblasTeardown():
    return pyclblas_swig.clblasTeardown()

def clblasSswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasDswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasCswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasZswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZswap(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasSscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasDscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasCscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasZscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasCsscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCsscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasZdscal(N, alpha, X, offx, incx, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZdscal(N, alpha, X, offx, incx, commandQueues, eventWaitList)

def clblasScopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasScopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasDcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasCcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasZcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZcopy(N, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasSaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasDaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasCaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasZaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZaxpy(N, alpha, X, offx, incx, Y, offy, incy, commandQueues, eventWaitList)

def clblasSdot(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSdot(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasDdot(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDdot(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasCdotu(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCdotu(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasZdotu(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZdotu(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasCdotc(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCdotc(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasZdotc(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZdotc(N, dotProduct, offDP, X, offx, incx, Y, offy, incy, scratchBuff, commandQueues, eventWaitList)

def clblasSrotg(SA, offSA, SB, offSB, C, offC, S, offS, commandQueues, eventWaitList):
	"""	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSrotg(SA, offSA, SB, offSB, C, offC, S, offS, commandQueues, eventWaitList)

def clblasDrotg(DA, offDA, DB, offDB, C, offC, S, offS, commandQueues, eventWaitList):
	"""	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDrotg(DA, offDA, DB, offDB, C, offC, S, offS, commandQueues, eventWaitList)

def clblasCrotg(CA, offCA, CB, offCB, C, offC, S, offS, commandQueues, eventWaitList):
	"""	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCrotg(CA, offCA, CB, offCB, C, offC, S, offS, commandQueues, eventWaitList)

def clblasZrotg(CA, offCA, CB, offCB, C, offC, S, offS, commandQueues, eventWaitList):
	"""	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZrotg(CA, offCA, CB, offCB, C, offC, S, offS, commandQueues, eventWaitList)

def clblasSrotmg(SD1, offSD1, SD2, offSD2, SX1, offSX1, SY1, offSY1, SPARAM, offSparam, commandQueues, eventWaitList):
	"""	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSrotmg(SD1, offSD1, SD2, offSD2, SX1, offSX1, SY1, offSY1, SPARAM, offSparam, commandQueues, eventWaitList)

def clblasDrotmg(DD1, offDD1, DD2, offDD2, DX1, offDX1, DY1, offDY1, DPARAM, offDparam, commandQueues, eventWaitList):
	"""	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDrotmg(DD1, offDD1, DD2, offDD2, DX1, offDX1, DY1, offDY1, DPARAM, offDparam, commandQueues, eventWaitList)

def clblasSrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList)

def clblasDrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList)

def clblasCsrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCsrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList)

def clblasZdrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZdrot(N, X, offx, incx, Y, offy, incy, C, S, commandQueues, eventWaitList)

def clblasSrotm(N, X, offx, incx, Y, offy, incy, SPARAM, offSparam, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSrotm(N, X, offx, incx, Y, offy, incy, SPARAM, offSparam, commandQueues, eventWaitList)

def clblasDrotm(N, X, offx, incx, Y, offy, incy, DPARAM, offDparam, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDrotm(N, X, offx, incx, Y, offy, incy, DPARAM, offDparam, commandQueues, eventWaitList)

def clblasSnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasScnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasScnrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDznrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDznrm2(N, NRM2, offNRM2, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasiSamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasiSamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasiDamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasiDamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasiCamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasiCamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasiZamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasiZamax(N, iMax, offiMax, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasSasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasScasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasScasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDzasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDzasum(N, asum, offAsum, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasSgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasDgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasCgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasZgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZgemv(order, transA, M, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasSsymv(order, uplo, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSsymv(order, uplo, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasDsymv(order, uplo, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDsymv(order, uplo, N, alpha, A, offA, lda, x, offx, incx, beta, y, offy, incy, commandQueues, eventWaitList)

def clblasChemv(order, uplo, N, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasChemv(order, uplo, N, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasZhemv(order, uplo, N, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZhemv(order, uplo, N, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasStrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasStrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasCtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasZtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZtrmv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasStrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasStrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasDtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasCtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasZtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZtrsv(order, uplo, trans, diag, N, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasSger(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSger(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasDger(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDger(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasCgeru(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCgeru(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasZgeru(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZgeru(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasCgerc(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCgerc(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasZgerc(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZgerc(order, M, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasSsyr(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSsyr(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList)

def clblasDsyr(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDsyr(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList)

def clblasCher(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCher(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList)

def clblasZher(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZher(order, uplo, N, alpha, X, offx, incx, A, offa, lda, commandQueues, eventWaitList)

def clblasSsyr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSsyr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasDsyr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDsyr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasCher2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCher2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasZher2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param A: Buffer object storing matrix A
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZher2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, A, offa, lda, commandQueues, eventWaitList)

def clblasStpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasStpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasCtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasZtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZtpmv(order, uplo, trans, diag, N, AP, offa, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasStpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasStpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList)

def clblasDtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList)

def clblasCtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList)

def clblasZtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZtpsv(order, uplo, trans, diag, N, A, offa, X, offx, incx, commandQueues, eventWaitList)

def clblasSspmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSspmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasDspmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDspmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasChpmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasChpmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasZhpmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZhpmv(order, uplo, N, alpha, AP, offa, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasSspr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSspr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList)

def clblasDspr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDspr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList)

def clblasChpr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasChpr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList)

def clblasZhpr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZhpr(order, uplo, N, alpha, X, offx, incx, AP, offa, commandQueues, eventWaitList)

def clblasSspr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSspr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList)

def clblasDspr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDspr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList)

def clblasChpr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasChpr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList)

def clblasZhpr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZhpr2(order, uplo, N, alpha, X, offx, incx, Y, offy, incy, AP, offa, commandQueues, eventWaitList)

def clblasSgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasDgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasCgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasZgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZgbmv(order, trans, M, N, KL, KU, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasStbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasStbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasDtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasCtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasZtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZtbmv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, scratchBuff, commandQueues, eventWaitList)

def clblasSsbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSsbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasDsbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDsbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasChbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasChbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasZhbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZhbmv(order, uplo, N, K, alpha, A, offa, lda, X, offx, incx, beta, Y, offy, incy, commandQueues, eventWaitList)

def clblasStbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasStbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasDtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasCtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasZtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZtbsv(order, uplo, trans, diag, N, K, A, offa, lda, X, offx, incx, commandQueues, eventWaitList)

def clblasSgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param transB: How matrix B is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasDgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param transB: How matrix B is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasCgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param transB: How matrix B is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasZgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param transB: How matrix B is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZgemm(order, transA, transB, M, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasStrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param B: Buffer object storing matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasStrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasDtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param B: Buffer object storing matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasCtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param B: Buffer object storing matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasZtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param B: Buffer object storing matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZtrmm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasStrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param B: Buffer object storing matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasStrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasDtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param B: Buffer object storing matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasCtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param B: Buffer object storing matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasZtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param B: Buffer object storing matrix B
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZtrsm(order, side, uplo, transA, diag, M, N, alpha, A, offA, lda, B, offB, ldb, commandQueues, eventWaitList)

def clblasSsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasDsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasCsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasZsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZsyrk(order, uplo, transA, N, K, alpha, A, offA, lda, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasSsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasDsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasCsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasZsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZsyr2k(order, uplo, transAB, N, K, alpha, A, offA, lda, B, offB, ldb, beta, C, offC, ldc, commandQueues, eventWaitList)

def clblasSsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasSsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasDsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasDsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasCsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasZsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZsymm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasChemm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasChemm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasZhemm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param M: Number of rows in matrix A
	:param N: Number of columns in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZhemm(order, side, uplo, M, N, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasCherk(order, uplo, transA, N, K, alpha, A, offa, lda, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCherk(order, uplo, transA, N, K, alpha, A, offa, lda, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasZherk(order, uplo, transA, N, K, alpha, A, offa, lda, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param transA: How matrix A is to be transposed
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZherk(order, uplo, transA, N, K, alpha, A, offa, lda, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasCher2k(order, uplo, trans, N, K, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCher2k(order, uplo, trans, N, K, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasZher2k(order, uplo, trans, N, K, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList):
	"""	:param order: Row/column order
	:param N: Number of columns in matrix B
	:param K: Number of columns in matrix A and rows in matrix B
	:param C: Buffer object storing matrix C
	:param commandQueues: List or tuple containing pyopencl.CommandQueue instances
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasZher2k(order, uplo, trans, N, K, alpha, A, offa, lda, B, offb, ldb, beta, C, offc, ldc, commandQueues, eventWaitList)

def clblasMatrixSizeInfo(order, rows, columns, elemsize, padding):
	"""	:param order: Row/column order
	"""
    return pyclblas_swig.clblasMatrixSizeInfo(order, rows, columns, elemsize, padding)

def clblasCreateMatrix(context, order, rows, columns, elemsize, padding):
	"""	:param order: Row/column order
	"""
    return pyclblas_swig.clblasCreateMatrix(context, order, rows, columns, elemsize, padding)

def clblasCreateMatrixWithLd(context, order, rows, columns, elemsize, ld):
	"""	:param order: Row/column order
	"""
    return pyclblas_swig.clblasCreateMatrixWithLd(context, order, rows, columns, elemsize, ld)

def clblasCreateMatrixFromHost(context, order, rows, columns, elemsize, ld, host, off_host, ld_host, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCreateMatrixFromHost(context, order, rows, columns, elemsize, ld, host, off_host, ld_host, command_queue, eventWaitList)

def clblasWriteSubMatrix(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasWriteSubMatrix(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList)

def clblasWriteSubMatrixAsync(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList, event):
	"""	:param order: Row/column order
	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasWriteSubMatrixAsync(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList, event)

def clblasReadSubMatrix(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasReadSubMatrix(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList)

def clblasReadSubMatrixAsync(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList, event):
	"""	:param order: Row/column order
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasReadSubMatrixAsync(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList, event)

def clblasCopySubMatrix(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCopySubMatrix(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList)

def clblasCopySubMatrixAsync(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList, event):
	"""	:param order: Row/column order
	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCopySubMatrixAsync(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, B, offB, ldB, nrB, ncB, xB, yB, nx, ny, command_queue, eventWaitList, event)

def clblasWriteVector(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList):
	"""	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasWriteVector(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList)

def clblasWriteVectorAsync(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList):
	"""	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasWriteVectorAsync(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList)

def clblasReadVector(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList):
	"""	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasReadVector(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList)

def clblasReadVectorAsync(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList):
	"""	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasReadVectorAsync(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList)

def clblasCopyVector(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList):
	"""	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCopyVector(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList)

def clblasCopyVectorAsync(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList):
	"""	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCopyVectorAsync(nb_elem, element_size, A, offA, B, offB, command_queue, eventWaitList)

def clblasWriteMatrix(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasWriteMatrix(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList)

def clblasWriteMatrixAsync(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasWriteMatrixAsync(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList)

def clblasReadMatrix(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasReadMatrix(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList)

def clblasReadMatrixAsync(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasReadMatrixAsync(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList)

def clblasCopyMatrix(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCopyMatrix(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList)

def clblasCopyMatrixAsync(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param B: Buffer object storing matrix B
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasCopyMatrixAsync(order, sx, sy, element_size, A, offA, ldA, B, offB, ldB, command_queue, eventWaitList)

def clblasFillVector(nb_elem, element_size, A, offA, host, command_queue, eventWaitList):
	"""	:param A: Buffer object storing matrix A
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasFillVector(nb_elem, element_size, A, offA, host, command_queue, eventWaitList)

def clblasFillVectorAsync(nb_elem, element_size, A, offA, pattern, command_queue, eventWaitList, event):
	"""	:param A: Buffer object storing matrix A
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasFillVectorAsync(nb_elem, element_size, A, offA, pattern, command_queue, eventWaitList, event)

def clblasFillMatrix(order, element_size, A, offA, ldA, nrA, ncA, pattern, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param A: Buffer object storing matrix A
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasFillMatrix(order, element_size, A, offA, ldA, nrA, ncA, pattern, command_queue, eventWaitList)

def clblasFillSubMatrix(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, nx, ny, pattern, command_queue, eventWaitList):
	"""	:param order: Row/column order
	:param A: Buffer object storing matrix A
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasFillSubMatrix(order, element_size, A, offA, ldA, nrA, ncA, xA, yA, nx, ny, pattern, command_queue, eventWaitList)

def clblasFillSubMatrixAsync(order, element_size, A, offA, ldA, sxA, syA, xA, yA, nx, ny, host, command_queue, eventWaitList, event):
	"""	:param order: Row/column order
	:param A: Buffer object storing matrix A
	:param eventWaitList: List or tuple containing pyopencl.Event instances
	"""
    return pyclblas_swig.clblasFillSubMatrixAsync(order, element_size, A, offA, ldA, sxA, syA, xA, yA, nx, ny, host, command_queue, eventWaitList, event)

