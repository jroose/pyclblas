 /* example.i */
 %module pyclblas
 %{
 /* Put header files here or function declarations like below */
#include <clBLAS.h>
#include <assert.h>
#include <CL/cl.h>
 PyObject* numpy_module;
 PyObject* numpy_ndarray_class;
 PyObject* pocl_module;
 PyObject* pocl_event_class;
 PyObject* pocl_queue_class;
 PyObject* pocl_event_fromptr;
 cl_int cl_error;

 %}

typedef float cl_float;
typedef uint32_t cl_uint;
typedef cl_double2 DoubleComplex;
typedef cl_float2 FloatComplex;

 %init %{
    pocl_module = PyImport_ImportModule("pyopencl");
    assert(pocl_module != NULL);
    pocl_event_class = PyObject_GetAttrString(pocl_module, "Event");
    pocl_queue_class = PyObject_GetAttrString(pocl_module, "CommandQueue");
    pocl_event_fromptr = PyObject_GetAttrString(pocl_event_class, "from_int_ptr");

    numpy_module = PyImport_ImportModule("numpy");
    assert(numpy_module != NULL);
    numpy_ndarray_class = PyObject_GetAttrString(numpy_module, "ndarray");

    clblasSetup();
 %}

%{
void handle_cl_error(clblasStatus stat, char* errmsg) {
    char descno[32];
    descno[32] = '\0';
    snprintf(descno, 1023, "%d", stat);

    const char* desc = descno;
    if(stat==CL_DEVICE_NOT_FOUND) desc="CL_DEVICE_NOT_FOUND";
    else if(stat==CL_DEVICE_NOT_AVAILABLE) desc="CL_DEVICE_NOT_AVAILABLE";
    else if(stat==CL_COMPILER_NOT_AVAILABLE) desc="CL_COMPILER_NOT_AVAILABLE";
    else if(stat==CL_MEM_OBJECT_ALLOCATION_FAILURE) desc="CL_MEM_OBJECT_ALLOCATION_FAILURE";
    else if(stat==CL_OUT_OF_RESOURCES) desc="CL_OUT_OF_RESOURCES";
    else if(stat==CL_OUT_OF_HOST_MEMORY) desc="CL_OUT_OF_HOST_MEMORY";
    else if(stat==CL_PROFILING_INFO_NOT_AVAILABLE) desc="CL_PROFILING_INFO_NOT_AVAILABLE";
    else if(stat==CL_MEM_COPY_OVERLAP) desc="CL_MEM_COPY_OVERLAP";
    else if(stat==CL_IMAGE_FORMAT_MISMATCH) desc="CL_IMAGE_FORMAT_MISMATCH";
    else if(stat==CL_IMAGE_FORMAT_NOT_SUPPORTED) desc="CL_IMAGE_FORMAT_NOT_SUPPORTED";
    else if(stat==CL_BUILD_PROGRAM_FAILURE) desc="CL_BUILD_PROGRAM_FAILURE";
    else if(stat==CL_MAP_FAILURE) desc="CL_MAP_FAILURE";
    else if(stat==CL_MISALIGNED_SUB_BUFFER_OFFSET) desc="CL_MISALIGNED_SUB_BUFFER_OFFSET";
    else if(stat==CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST) desc="CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST";
    else if(stat==CL_COMPILE_PROGRAM_FAILURE) desc="CL_COMPILE_PROGRAM_FAILURE";
    else if(stat==CL_LINKER_NOT_AVAILABLE) desc="CL_LINKER_NOT_AVAILABLE";
    else if(stat==CL_LINK_PROGRAM_FAILURE) desc="CL_LINK_PROGRAM_FAILURE";
    else if(stat==CL_DEVICE_PARTITION_FAILED) desc="CL_DEVICE_PARTITION_FAILED";
    else if(stat==CL_KERNEL_ARG_INFO_NOT_AVAILABLE) desc="CL_KERNEL_ARG_INFO_NOT_AVAILABLE";

    else if(stat==CL_INVALID_VALUE) desc="CL_INVALID_VALUE";
    else if(stat==CL_INVALID_DEVICE_TYPE) desc="CL_INVALID_DEVICE_TYPE";
    else if(stat==CL_INVALID_PLATFORM) desc="CL_INVALID_PLATFORM";
    else if(stat==CL_INVALID_DEVICE) desc="CL_INVALID_DEVICE";
    else if(stat==CL_INVALID_CONTEXT) desc="CL_INVALID_CONTEXT";
    else if(stat==CL_INVALID_QUEUE_PROPERTIES) desc="CL_INVALID_QUEUE_PROPERTIES";
    else if(stat==CL_INVALID_COMMAND_QUEUE) desc="CL_INVALID_COMMAND_QUEUE";
    else if(stat==CL_INVALID_HOST_PTR) desc="CL_INVALID_HOST_PTR";
    else if(stat==CL_INVALID_MEM_OBJECT) desc="CL_INVALID_MEM_OBJECT";
    else if(stat==CL_INVALID_IMAGE_FORMAT_DESCRIPTOR) desc="CL_INVALID_IMAGE_FORMAT_DESCRIPTOR";
    else if(stat==CL_INVALID_IMAGE_SIZE) desc="CL_INVALID_IMAGE_SIZE";
    else if(stat==CL_INVALID_SAMPLER) desc="CL_INVALID_SAMPLER";
    else if(stat==CL_INVALID_BINARY) desc="CL_INVALID_BINARY";
    else if(stat==CL_INVALID_BUILD_OPTIONS) desc="CL_INVALID_BUILD_OPTIONS";
    else if(stat==CL_INVALID_PROGRAM) desc="CL_INVALID_PROGRAM";
    else if(stat==CL_INVALID_PROGRAM_EXECUTABLE) desc="CL_INVALID_PROGRAM_EXECUTABLE";
    else if(stat==CL_INVALID_KERNEL_NAME) desc="CL_INVALID_KERNEL_NAME";
    else if(stat==CL_INVALID_KERNEL_DEFINITION) desc="CL_INVALID_KERNEL_DEFINITION";
    else if(stat==CL_INVALID_KERNEL) desc="CL_INVALID_KERNEL";
    else if(stat==CL_INVALID_ARG_INDEX) desc="CL_INVALID_ARG_INDEX";
    else if(stat==CL_INVALID_ARG_VALUE) desc="CL_INVALID_ARG_VALUE";
    else if(stat==CL_INVALID_ARG_SIZE) desc="CL_INVALID_ARG_SIZE";
    else if(stat==CL_INVALID_KERNEL_ARGS) desc="CL_INVALID_KERNEL_ARGS";
    else if(stat==CL_INVALID_WORK_DIMENSION) desc="CL_INVALID_WORK_DIMENSION";
    else if(stat==CL_INVALID_WORK_GROUP_SIZE) desc="CL_INVALID_WORK_GROUP_SIZE";
    else if(stat==CL_INVALID_WORK_ITEM_SIZE) desc="CL_INVALID_WORK_ITEM_SIZE";
    else if(stat==CL_INVALID_GLOBAL_OFFSET) desc="CL_INVALID_GLOBAL_OFFSET";
    else if(stat==CL_INVALID_EVENT_WAIT_LIST) desc="CL_INVALID_EVENT_WAIT_LIST";
    else if(stat==CL_INVALID_EVENT) desc="CL_INVALID_EVENT";
    else if(stat==CL_INVALID_OPERATION) desc="CL_INVALID_OPERATION";
    else if(stat==CL_INVALID_GL_OBJECT) desc="CL_INVALID_GL_OBJECT";
    else if(stat==CL_INVALID_BUFFER_SIZE) desc="CL_INVALID_BUFFER_SIZE";
    else if(stat==CL_INVALID_MIP_LEVEL) desc="CL_INVALID_MIP_LEVEL";
    else if(stat==CL_INVALID_GLOBAL_WORK_SIZE) desc="CL_INVALID_GLOBAL_WORK_SIZE";
    else if(stat==CL_INVALID_PROPERTY) desc="CL_INVALID_PROPERTY";
    else if(stat==CL_INVALID_IMAGE_DESCRIPTOR) desc="CL_INVALID_IMAGE_DESCRIPTOR";
    else if(stat==CL_INVALID_COMPILER_OPTIONS) desc="CL_INVALID_COMPILER_OPTIONS";
    else if(stat==CL_INVALID_LINKER_OPTIONS) desc="CL_INVALID_LINKER_OPTIONS";
    else if(stat==CL_INVALID_DEVICE_PARTITION_COUNT) desc="CL_INVALID_DEVICE_PARTITION_COUNT";

    char e_desc[1024];
    e_desc[1023] = '\0';
    snprintf(e_desc, 1023, "method '$symname' returned error code '%s'\n", desc);
    strncpy(errmsg, e_desc, 1024);
}

void handle_error(clblasStatus stat, char* errmsg) {
    char descno[32];
    descno[32] = '\0';
    snprintf(descno, 1023, "%d", stat);

    const char* desc = descno;

    if(stat == clblasNotImplemented)
        desc="clblasNotImplemented: Functionality is not implemented";
    else if(stat == clblasNotInitialized)
        desc="clblasNotInitialized: clblas library is not initialized yet";
    else if(stat == clblasInvalidMatA)
        desc="clblasInvalidMatA: Matrix A is not a valid memory object";
    else if(stat == clblasInvalidMatB)
        desc="clblasInvalidMatB: Matrix B is not a valid memory object";
    else if(stat == clblasInvalidMatC)
        desc="clblasInvalidMatC: Matrix C is not a valid memory object";
    else if(stat == clblasInvalidVecX)
        desc="clblasInvalidVecX: Vector X is not a valid memory object";
    else if(stat == clblasInvalidVecY)
        desc="clblasInvalidVecY: Vector Y is not a valid memory object";
    else if(stat == clblasInvalidDim)
        desc="clblasInvalidDim: An input dimension (M,N,K) is invalid";
    else if(stat == clblasInvalidLeadDimA)
        desc="clblasInvalidLeadDimA: Leading dimension A must not be less than the size of the first dimension";
    else if(stat == clblasInvalidLeadDimB)
        desc="clblasInvalidLeadDimB: Leading dimension B must not be less than the size of the second dimension";
    else if(stat == clblasInvalidLeadDimC)
        desc="clblasInvalidLeadDimC: Leading dimension C must not be less than the size of the third dimension";
    else if(stat == clblasInvalidIncX)
        desc="clblasInvalidIncX: The increment for a vector X must not be 0";
    else if(stat == clblasInvalidIncY)
        desc="clblasInvalidIncY: The increment for a vector Y must not be 0";
    else if(stat == clblasInsufficientMemMatA)
        desc="clblasInsufficientMemMatA: The memory object for Matrix A is too small";
    else if(stat == clblasInsufficientMemMatB)
        desc="clblasInsufficientMemMatB: The memory object for Matrix B is too small";
    else if(stat == clblasInsufficientMemMatC)
        desc="clblasInsufficientMemMatC: The memory object for Matrix C is too small";
    else if(stat == clblasInsufficientMemVecX)
        desc="clblasInsufficientMemVecX: The memory object for Vector X is too small";
    else if(stat == clblasInsufficientMemVecY)
        desc="clblasInsufficientMemVecY: The memory object for Vector Y is too small ";

    char e_desc[1024];
    e_desc[1023] = '\0';
    snprintf(e_desc, 1023, "method '$symname' returned error code '%s'\n", desc);
    strncpy(errmsg, e_desc, 1024);
}
%}

%typemap(in) (void *) {
    if(PyObject_IsInstance($input, numpy_ndarray_class))
        $1 = ((void *) PyLong_AsVoidPtr(PyObject_GetAttrString(PyObject_GetAttrString($input, "ctypes"), "data")));
    else
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '$type': should be a numpy.ndarray");
}

%typemap(in) (const void *) {
    if(PyObject_IsInstance($input, numpy_ndarray_class))
        $1 = ((void *) PyLong_AsVoidPtr(PyObject_GetAttrString(PyObject_GetAttrString($input, "ctypes"), "data")));
    else
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '$type': should be a numpy.ndarray");
}

%typemap(in, numinputs=0) (cl_int *err) {
    $1 = NULL;
}

%typemap(in) cl_context {
    $1 = ((cl_context) PyLong_AsVoidPtr(PyObject_GetAttrString($input, "int_ptr")));
}

%typemap(in) cl_command_queue {
    $1 = ((cl_command_queue) PyLong_AsVoidPtr(PyObject_GetAttrString($input, "int_ptr")));
}

%typemap(in) cl_mem {
    $1 = ((cl_mem) PyLong_AsVoidPtr(PyObject_GetAttrString($input, "int_ptr")));
}

%typemap(in) const cl_mem {
    $1 = ((const cl_mem) PyLong_AsVoidPtr(PyObject_GetAttrString($input, "int_ptr")));
}

%typemap(in) (cl_uint numCommandQueues, cl_command_queue*) {
    cl_command_queue* queues;
    
    int it_cq;
    if(PyTuple_Check($input)) {
        $1 = PyTuple_Size($input);
        assert($1 < 32);
        if($1 > 0) {
            queues = (cl_command_queue*) calloc(sizeof(cl_command_queue), $1);
            for(it_cq=0; it_cq < PyTuple_Size($input); it_cq++)
            {
                PyObject* q = PyTuple_GetItem($input, it_cq);
                if(!PyObject_IsInstance(q, pocl_queue_class))
                    SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
                queues[it_cq] = ((cl_command_queue) PyLong_AsVoidPtr(PyObject_GetAttrString(q, "int_ptr")));
            }
            $2 = queues;
        }else{
            $2 = NULL;
        }
    }else if(PyList_Check($input)) {
        $1 = PyList_Size($input);
        assert($1 < 32);
        if($1 > 0) {
            queues = (cl_command_queue*) calloc(sizeof(cl_command_queue), $1);
            for(it_cq=0; it_cq < PyList_Size($input); it_cq++)
            {
                PyObject* q = PyList_GetItem($input, it_cq);
                if(!PyObject_IsInstance(q, pocl_queue_class))
                    SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
                queues[it_cq] = ((cl_command_queue) PyLong_AsVoidPtr(PyObject_GetAttrString(q, "int_ptr")));
            }
            $2 = queues;
        }else{
            $2 = NULL;
        }
    }else{
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
    }
}


%typemap(freearg) (cl_uint numCommandQueues, cl_command_queue*) {
    free($2);
}

%typemap(in) (cl_uint numEventsInWaitList, const cl_event* eventWaitList) {
    cl_event* events;
    
    int it_cq;
    if(PyTuple_Check($input)) {
        $1 = PyTuple_Size($input);
        if($1 > 0) {
            events = (cl_event*) calloc(sizeof(cl_event), $1);
            for(it_cq=0; it_cq < PyTuple_Size($input); it_cq++)
            {
                PyObject* e = PyTuple_GetItem($input, it_cq);
                if(!PyObject_IsInstance(e, pocl_event_class))
                    SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
                events[it_cq] = ((cl_event) PyLong_AsVoidPtr(PyObject_GetAttrString(e, "int_ptr")));
            }
            $2 = events;
        }else{
            $2 = NULL;
        }
    }else if(PyList_Check($input)) {
        $1 = PyList_Size($input);
        if($1 > 0) {
            events = (cl_event*) calloc(sizeof(cl_event), $1);
            for(it_cq=0; it_cq < PyList_Size($input); it_cq++)
            {
                PyObject* e = PyList_GetItem($input, it_cq);
                if(!PyObject_IsInstance(e, pocl_event_class))
                    SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
                events[it_cq] = ((cl_event) PyLong_AsVoidPtr(PyObject_GetAttrString(e, "int_ptr")));
            }
            $2 = events;
        }else{
            $2 = NULL;
        }
    }else{
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
    }
}

%typemap(freearg) (cl_uint numEventsInWaitList, const cl_event* eventWaitList) {
    free($2);
}

%typemap(arginit) (cl_event* events) {
    $1 = NULL;
}

%typemap(arginit) (const cl_event* eventWaitList) {
    $1 = NULL;
}

%typemap(arginit) (cl_command_queue*) {
    $1 = NULL;
}


//Ignore the following inputs/features
%typemap(in, numinputs=0) (size_t *ld) {
    $1 = NULL;
}
%typemap(in, numinputs=0) (size_t *fullsize) {
    $1 = NULL;
}

%typemap(in, numinputs=0) (cl_event* events) {
    $1 = (cl_event*) calloc(sizeof(cl_event), 32);
}

%typemap(argout) (cl_event* events) {
    int it_cq;

    for(it_cq = 0; it_cq < 32; it_cq++)
        if($1[it_cq] == NULL)
            break;

    if(it_cq > 1) {
        $result = PyTuple_New(it_cq);
        for(it_cq = 0; it_cq < PyTuple_Size($result); it_cq++)
        {
            PyObject* nevent = PyObject_CallFunction(pocl_event_fromptr, "O", PyLong_FromVoidPtr($1[it_cq]));
            PyTuple_SET_ITEM($result, it_cq, nevent);
        }
    }else if(it_cq == 1) {
        $result = PyObject_CallFunction(pocl_event_fromptr, "O", PyLong_FromVoidPtr($1[0]));
    }else if(it_cq == 0) {
        $result = Py_None;
    }
    free($1);
}

%typemap(in) (cl_float2) {
    cl_float2 ret;
    if(PyComplex_Check($input)) {
        ret.x = PyComplex_RealAsDouble($input);
        ret.y = PyComplex_ImagAsDouble($input);
    }else if(PyFloat_Check($input)) {
        ret.x = PyFloat_AsDouble($input);
        ret.y = 0.0f;
    }else if(PyLong_Check($input)) {
        ret.x = PyLong_AsLongLong($input);
        ret.y = 0.0f;
    }else if(PyTuple_Check($input)) {
        if(PyTuple_Size($input) == 2) {
            PyObject* x = PyTuple_GetItem($input,0);
            PyObject* y = PyTuple_GetItem($input,1);
            ret.x = PyFloat_AsDouble(x);
            ret.y = PyFloat_AsDouble(y);
        }else if(PyTuple_Size($input) == 1) {
            PyObject* x = PyTuple_GetItem($input,0);
            ret.x = PyFloat_AsDouble(x);
            ret.y = 0.0f;
        }else
            SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Tuple input must have at least 1, and at most 2 elements");
    }else
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Input should be int, float, complex, or tuple (of 1 or 2 numbers)");
    $1 = ret;
}

%typemap(in) (cl_double2) {
    cl_double2 ret;
    if(PyComplex_Check($input)) {
        ret.x = PyComplex_RealAsDouble($input);
        ret.y = PyComplex_ImagAsDouble($input);
    }else if(PyFloat_Check($input)) {
        ret.x = PyFloat_AsDouble($input);
        ret.y = 0.0;
    }else if(PyLong_Check($input)) {
        ret.x = PyLong_AsLongLong($input);
        ret.y = 0.0;
    }else if(PyTuple_Check($input)) {
        if(PyTuple_Size($input) == 2) {
            PyObject* x = PyTuple_GetItem($input,0);
            PyObject* y = PyTuple_GetItem($input,1);
            ret.x = PyFloat_AsDouble(x);
            ret.y = PyFloat_AsDouble(y);
        }else if(PyTuple_Size($input) == 1) {
            PyObject* x = PyTuple_GetItem($input,0);
            ret.x = PyFloat_AsDouble(x);
            ret.y = 0.0;
        }else
            SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Tuple input must have at least 1, and at most 2 elements");
    }else
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Input should be int, float, complex, or tuple (of 1 or 2 numbers)");
    $1 = ret;
}


%typemap(out) (clblasStatus) {
    if($1 != 0) {
        char errmsg[1024];
        handle_error($1, errmsg);
        SWIG_exception_fail(SWIG_RuntimeError, errmsg);
    }

    $result = Py_None;
}

%exception clblasCreateMatrix {
    cl_int err;
    cl_int* arg9 = &err; /*HACK to get around SWIG's argout/out conflicts https://github.com/swig/swig/issues/684 */
    $action
    if(err != 0) {
        char errmsg[1024];
        handle_cl_error(err, errmsg);
        SWIG_exception_fail(SWIG_RuntimeError, errmsg);
    }
}

%exception clblasCreateMatrixWithLd {
    cl_int err;
    cl_int* arg8 = &err; /*HACK to get around SWIG's argout/out conflicts https://github.com/swig/swig/issues/684 */
    $action
    if(err != 0) {
        char errmsg[1024];
        handle_cl_error(err, errmsg);
        SWIG_exception_fail(SWIG_RuntimeError, errmsg);
    }
}

%exception  clblasCreateMatrixFromHost {
    cl_int err;
    cl_int* arg13 = &err; /*HACK to get around SWIG's argout/out conflicts https://github.com/swig/swig/issues/684 */
    $action
    if(err != 0) {
        char errmsg[1024];
        handle_cl_error(err, errmsg);
        SWIG_exception_fail(SWIG_RuntimeError, errmsg);
    }

}

/*
clblasStatus clblasSgemm(
    clblasOrder order, 
    clblasTranspose transA, 
    clblasTranspose transB, 
    size_t M, size_t N, size_t K, 
    cl_float alpha, 
    const cl_mem A, size_t offA, size_t lda, 
    const cl_mem B, size_t offB, size_t ldb, 
    cl_float beta, cl_mem C, size_t offC, size_t ldc, 
    cl_uint numCommandQueues, cl_command_queue *commandQueues, 
    cl_uint numEventsInWaitList, const cl_event *eventWaitList, 
    cl_event *events
);
  fprintf(stderr, "(%d,%d,%d\n%lu,%lu,%lu,\n%f,\n%p,%lu,%lu,\n%p,%lu,%lu,\n%f,%p,%lu,%lu,\n%u,%p,\n%u,%p\n,%p\n)",
            arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15,arg16,arg17,arg18,arg19,arg20,(cl_event const *)arg21,arg22
  );
*/
 
%include <clBLAS.h>
