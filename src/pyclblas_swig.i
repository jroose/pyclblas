 /* example.i */
 %module pyclblas_swig
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
 PyObject* clblasException_class;
 cl_int cl_error;

 %}

typedef float cl_float;
typedef double cl_double;
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
    clblasException_class = PyErr_NewExceptionWithDoc("pyclblas.clblasException", "Exception corresponding to clblasStatus. Has attributes message and number.", PyExc_RuntimeError, NULL);

    clblasSetup();
%}

%{
PyObject* shutdown(void) {
    clblasTeardown();
    Py_DECREF(pocl_event_class);
    Py_DECREF(pocl_queue_class);
    Py_DECREF(pocl_event_fromptr);
    Py_DECREF(pocl_module);

    Py_DECREF(numpy_ndarray_class);
    Py_DECREF(numpy_module);

    Py_DECREF(clblasException_class);

    return Py_None;
}
%}

PyObject* shutdown();

%{
void handle_cl_error(cl_int stat, char* errmsg) {
    char descno[32];
    descno[31] = '\0';
    snprintf(descno, 31, "%d", stat);

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
    descno[31] = '\0';
    snprintf(descno, 31, "%d", stat);

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
    snprintf(e_desc, 1023, "%s", desc);
    strncpy(errmsg, e_desc, 1024);
}
%}

%{
void clblasExceptionRaise(clblasStatus stat) {
    char errmsg[1024];
    handle_error(stat, errmsg);
    PyObject* ret = PyObject_CallObject(clblasException_class, NULL);
    PyObject *decr, *decr2;
    PyObject_SetAttrString(ret, "message", decr=PyString_FromString(errmsg));
    Py_DECREF(decr);
    PyObject_SetAttrString(ret, "args", decr2 = PyTuple_Pack(1, decr = PyString_FromString(errmsg)));
    Py_DECREF(decr);
    Py_DECREF(decr2);
    PyObject_SetAttrString(ret, "number", decr=PyLong_FromLong(stat));
    Py_DECREF(decr);
    SWIG_Python_SetErrorObj(clblasException_class, ret);
}
%}

%typemap(in) (void *) {
    if(PyObject_IsInstance($input, numpy_ndarray_class))
    {
        PyObject *decr, *decr2;
        $1 = ((void *) PyLong_AsVoidPtr(decr2=PyObject_GetAttrString(decr=PyObject_GetAttrString($input, "ctypes"), "data")));
        Py_DECREF(decr);
        Py_DECREF(decr2);
    }else
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '$type': should be a numpy.ndarray");
}

%typemap(in) (const void *) {
    if(PyObject_IsInstance($input, numpy_ndarray_class)) {
        PyObject *decr, *decr2;
        $1 = ((void *) PyLong_AsVoidPtr(decr=PyObject_GetAttrString(decr2=PyObject_GetAttrString($input, "ctypes"), "data")));
        Py_DECREF(decr);
        Py_DECREF(decr2);
    }else
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '$type': should be a numpy.ndarray");
}

%typemap(in, numinputs=0) (cl_int *err) {
    $1 = NULL;
}

%typemap(in) cl_context {
    PyObject* decr;
    $1 = ((cl_context) PyLong_AsVoidPtr(decr=PyObject_GetAttrString($input, "int_ptr")));
    Py_DECREF(decr);
}

%typemap(in) cl_command_queue {
    PyObject* decr;
    $1 = ((cl_command_queue) PyLong_AsVoidPtr(decr=PyObject_GetAttrString($input, "int_ptr")));
    Py_DECREF(decr);
}

%typemap(in) cl_mem {
    PyObject* decr;
    $1 = ((cl_mem) PyLong_AsVoidPtr(decr=PyObject_GetAttrString($input, "int_ptr")));
    Py_DECREF(decr);
}

%typemap(in) const cl_mem {
    PyObject* decr;
    $1 = ((const cl_mem) PyLong_AsVoidPtr(decr=PyObject_GetAttrString($input, "int_ptr")));
    Py_DECREF(decr);
}

%typemap(in) (cl_uint numCommandQueues, cl_command_queue*) {
    cl_command_queue* queues;
    
    int it_cq;
    if(PyTuple_Check($input)) {
        $1 = PyTuple_Size($input);
        assert($1 < 128); //Events output can only return 128 events
        if($1 > 0) {
            queues = (cl_command_queue*) calloc(sizeof(cl_command_queue), $1);
            for(it_cq=0; it_cq < PyTuple_Size($input); it_cq++)
            {
                PyObject* q = PyTuple_GetItem($input, it_cq);
                if(!PyObject_IsInstance(q, pocl_queue_class))
                    SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
                PyObject* decr;
                queues[it_cq] = ((cl_command_queue) PyLong_AsVoidPtr(decr=PyObject_GetAttrString(q, "int_ptr")));
                Py_DECREF(decr);
            }
            $2 = queues;
        }else{
            $2 = NULL;
        }
    }else if(PyList_Check($input)) {
        $1 = PyList_Size($input);
        assert($1 < 128); //Events output can only return 128 events
        if($1 > 0) {
            queues = (cl_command_queue*) calloc(sizeof(cl_command_queue), $1);
            for(it_cq=0; it_cq < PyList_Size($input); it_cq++)
            {
                PyObject* q = PyList_GetItem($input, it_cq);
                if(!PyObject_IsInstance(q, pocl_queue_class))
                    SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
                PyObject* decr;
                queues[it_cq] = ((cl_command_queue) PyLong_AsVoidPtr(decr=PyObject_GetAttrString(q, "int_ptr")));
                Py_DECREF(decr);
            }
            $2 = queues;
        }else{
            $2 = NULL;
        }
    }else if(PyObject_IsInstance($input, pocl_queue_class)) {
        PyObject* decr;
        queues = (cl_command_queue*) calloc(sizeof(cl_command_queue), 1);
        queues[0] = ((cl_command_queue) PyLong_AsVoidPtr(decr=PyObject_GetAttrString($input, "int_ptr")));
        Py_DECREF(decr);
        $1 = 1;
        $2 = queues;
    }else{
        $1 = 0;
        $2 = NULL;
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
    }
}


%typemap(freearg) (cl_uint numCommandQueues, cl_command_queue*) {
    if($2 != NULL)
        free($2);
}

%typemap(in) (cl_uint numEventsInWaitList, const cl_event* eventWaitList) {
    cl_event* events;
    PyObject* decr;
    
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
                events[it_cq] = ((cl_event) PyLong_AsVoidPtr(decr=PyObject_GetAttrString(e, "int_ptr")));
                Py_DECREF(decr);
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
                events[it_cq] = ((cl_event) PyLong_AsVoidPtr(decr=PyObject_GetAttrString(e, "int_ptr")));
                Py_DECREF(decr);
            }
            $2 = events;
        }else{
            $2 = NULL;
        }
    }else if(PyObject_IsInstance($input, pocl_event_class)) {
        events = (cl_event*) calloc(sizeof(cl_event), 1);
        events[0] = ((cl_event) PyLong_AsVoidPtr(decr=PyObject_GetAttrString($input, "int_ptr")));
        Py_DECREF(decr);
        $1 = 1;
        $2 = events;
    }else if($input == Py_None) {
        $1 = 0;
        $2 = NULL;
    }else{
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "'");
    }
}

%typemap(freearg) (cl_uint numEventsInWaitList, const cl_event* eventWaitList) {
    if($2 != NULL)
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

//Events output can return a maximum of 128 events
%typemap(in, numinputs=0) (cl_event* events) {
    $1 = (cl_event*) calloc(sizeof(cl_event), 128);
}

%typemap(argout) (cl_event* events) {
    int it_cq;

    for(it_cq = 0; it_cq < 128; it_cq++)
        if($1[it_cq] == NULL)
            break;

    $result = PyTuple_New(it_cq);
    for(it_cq = 0; it_cq < PyTuple_Size($result); it_cq++)
    {
        PyObject* decr;
        PyObject* nevent = PyObject_CallFunction(pocl_event_fromptr, "O", decr=PyLong_FromVoidPtr($1[it_cq]));
        Py_DECREF(decr);
        PyTuple_SET_ITEM($result, it_cq, nevent);
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
    }else if(PyInt_Check($input)) {
        ret.x = PyInt_AsLong($input);
        ret.y = 0.0f;
    }else if(PyLong_Check($input)) {
        ret.x = PyLong_AsLongLong($input);
        ret.y = 0.0f;
    }else if(PyList_Check($input)) {
        if(PyList_Size($input) == 2) {
            PyObject* x = PyList_GetItem($input,0);
            PyObject* y = PyList_GetItem($input,1);
            if(PyFloat_Check(x))
                ret.x = PyFloat_AsDouble(x);
            else if(PyInt_Check(x))
                ret.x = PyInt_AsLong(x);
            else if(PyLong_Check(x))
                ret.x = PyLong_AsLongLong(x);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': List input must contain floats or ints");

            if(PyFloat_Check(y))
                ret.y = PyFloat_AsDouble(y);
            else if(PyInt_Check(y))
                ret.y = PyInt_AsLong(y);
            else if(PyLong_Check(y))
                ret.y = PyLong_AsLongLong(y);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': List input must contain floats or ints");
        }else if(PyList_Size($input) == 1) {
            PyObject* x = PyList_GetItem($input,0);

            if(PyFloat_Check(x))
                ret.x = PyFloat_AsDouble(x);
            else if(PyInt_Check(x))
                ret.x = PyInt_AsLong(x);
            else if(PyLong_Check(x))
                ret.x = PyLong_AsLongLong(x);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': List input must contain floats or ints");

            ret.y = 0.0f;
        }else
            SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': List input must have at least 1, and at most 2 elements");
    }else if(PyTuple_Check($input)) {
        if(PyTuple_Size($input) == 2) {
            PyObject* x = PyTuple_GetItem($input,0);
            PyObject* y = PyTuple_GetItem($input,1);
            if(PyFloat_Check(x))
                ret.x = PyFloat_AsDouble(x);
            else if(PyInt_Check(x))
                ret.x = PyInt_AsLong(x);
            else if(PyLong_Check(x))
                ret.x = PyLong_AsLongLong(x);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Tuple input must contain floats or ints");

            if(PyFloat_Check(y))
                ret.y = PyFloat_AsDouble(y);
            else if(PyInt_Check(y))
                ret.y = PyInt_AsLong(y);
            else if(PyLong_Check(y))
                ret.y = PyLong_AsLongLong(y);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Tuple input must contain floats or ints");
        }else if(PyTuple_Size($input) == 1) {
            PyObject* x = PyTuple_GetItem($input,0);

            if(PyFloat_Check(x))
                ret.x = PyFloat_AsDouble(x);
            else if(PyInt_Check(x))
                ret.x = PyInt_AsLong(x);
            else if(PyLong_Check(x))
                ret.x = PyLong_AsLongLong(x);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Tuple input must contain floats or ints");

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
        ret.y = 0.0f;
    }else if(PyInt_Check($input)) {
        ret.x = PyInt_AsLong($input);
        ret.y = 0.0f;
    }else if(PyLong_Check($input)) {
        ret.x = PyLong_AsLongLong($input);
        ret.y = 0.0f;
    }else if(PyList_Check($input)) {
        if(PyList_Size($input) == 2) {
            PyObject* x = PyList_GetItem($input,0);
            PyObject* y = PyList_GetItem($input,1);
            if(PyFloat_Check(x))
                ret.x = PyFloat_AsDouble(x);
            else if(PyInt_Check(x))
                ret.x = PyInt_AsLong(x);
            else if(PyLong_Check(x))
                ret.x = PyLong_AsLongLong(x);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': List input must contain floats or ints");

            if(PyFloat_Check(y))
                ret.y = PyFloat_AsDouble(y);
            else if(PyInt_Check(y))
                ret.y = PyInt_AsLong(y);
            else if(PyLong_Check(y))
                ret.y = PyLong_AsLongLong(y);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': List input must contain floats or ints");
        }else if(PyList_Size($input) == 1) {
            PyObject* x = PyList_GetItem($input,0);

            if(PyFloat_Check(x))
                ret.x = PyFloat_AsDouble(x);
            else if(PyInt_Check(x))
                ret.x = PyInt_AsLong(x);
            else if(PyLong_Check(x))
                ret.x = PyLong_AsLongLong(x);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': List input must contain floats or ints");

            ret.y = 0.0f;
        }else
            SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': List input must have at least 1, and at most 2 elements");
    }else if(PyTuple_Check($input)) {
        if(PyTuple_Size($input) == 2) {
            PyObject* x = PyTuple_GetItem($input,0);
            PyObject* y = PyTuple_GetItem($input,1);
            if(PyFloat_Check(x))
                ret.x = PyFloat_AsDouble(x);
            else if(PyInt_Check(x))
                ret.x = PyInt_AsLong(x);
            else if(PyLong_Check(x))
                ret.x = PyLong_AsLongLong(x);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Tuple input must contain floats or ints");

            if(PyFloat_Check(y))
                ret.y = PyFloat_AsDouble(y);
            else if(PyInt_Check(y))
                ret.y = PyInt_AsLong(y);
            else if(PyLong_Check(y))
                ret.y = PyLong_AsLongLong(y);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Tuple input must contain floats or ints");
        }else if(PyTuple_Size($input) == 1) {
            PyObject* x = PyTuple_GetItem($input,0);

            if(PyFloat_Check(x))
                ret.x = PyFloat_AsDouble(x);
            else if(PyInt_Check(x))
                ret.x = PyInt_AsLong(x);
            else if(PyLong_Check(x))
                ret.x = PyLong_AsLongLong(x);
            else
                SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Tuple input must contain floats or ints");

            ret.y = 0.0f;
        }else
            SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Tuple input must have at least 1, and at most 2 elements");
    }else
        SWIG_exception_fail(SWIG_TypeError, "in method '" "$symname" "', argument $argnum of type '" "$type" "': Input should be int, float, complex, or tuple (of 1 or 2 numbers)");
    $1 = ret;
}

%typemap(out) (clblasStatus) {
    if($1 != 0) {
        clblasExceptionRaise((clblasStatus)$1);
        SWIG_fail;
    }

    $result = Py_None;
}

%typemap(in, numinputs=0) (cl_uint *major, cl_uint *minor, cl_uint *patch) {
    $1 = (cl_uint*) calloc(sizeof(cl_uint), 3);
    $2 = &($1[1]);
    $3 = &($1[2]);
}

%typemap(argout) (cl_uint *major, cl_uint *minor, cl_uint *patch) {
    char version_buffer[128];
    size_t nchars = snprintf(version_buffer, 127, "%u.%u.%u", *$1, *$2, *$3);
    version_buffer[nchars] = '\0';
    $result = PyString_FromString(version_buffer);
}

%typemap(freearg) (cl_uint *major, cl_uint *minor, cl_uint *patch) {
    free($1);
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
 
%include "clBLAS.h"
