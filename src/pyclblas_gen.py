#!/usr/bin/env python

import sys
import re

re_parsedecl = re.compile(r"^(\w+) (\w+)\((.*)\);$")
re_parseparam = re.compile(r"^(.*?)(\w+)$")

def splitparam(p):
    m = re_parseparam.match(p)
    if m:
        return (m.group(1).strip(), m.group(2))
    else:
        print >>sys.stderr, "Failed to parse parameter", p
        return None

def compare_param(x, y):
    if x[0] and y[0] and (x[0] != y[0]):
        return False
    elif x[1] and y[1] and (x[1] != y[1]):
        return False
    else:
        return True

merge_params = (
    (
        ("","numEventsInWaitList"),
        ("","eventWaitList"),
        "eventWaitList"
    ),
    (
        ("", "numCommandQueues"),
        ("", "commandQueues"),
        "commandQueues"
    ),
)

remove_params = (
    ("cl_event *", "events"),
    ("cl_int *", "err"),
    ("size_t *", "fullsize"),
    ("size_t *", "ld"),
)

params_description = (
    (("clblasOrder", "order"),  "Row/column order"),
    (("clblasTranspose", "transA"),  "How matrix A is to be transposed"),
    (("clblasTranspose", "transB"),  "How matrix B is to be transposed"),
    (("size_t", "M"),  "Number of rows in matrix A"),
    (("size_t", "K"),  "Number of columns in matrix A and rows in matrix B"),
    (("size_t", "N"),  "Number of columns in matrix B"),
    (("cl_mem", "A"),  "Buffer object storing matrix A"),
    (("cl_mem", "B"),  "Buffer object storing matrix B"),
    (("cl_mem", "C"),  "Buffer object storing matrix C"),
    (("", "commandQueues"), "List or tuple containing pyopencl.CommandQueue instances"),
    (("", "eventWaitList"), "List or tuple containing pyopencl.Event instances"),
)

print "import pyclblas_swig"
print ""
print """
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
"""

with open(sys.argv[1],'r') as fin:
    for line in fin:
        match = re_parsedecl.match(line)
        rettype = match.group(1)
        name = match.group(2)
        params = [splitparam(x.strip()) for x in match.group(3).split(",") if x]

        for cp in remove_params:
            compares = list(compare_param(cp, p) for p in params)
            if any(compares):
                params.pop(compares.index(True))

        for rule in merge_params:
            check_params = rule[:-1]
            result = rule[-1]

            bad = False
            idx = []
            for cp in check_params:
                compares = list(compare_param(cp, p) for p in params)
                if not any(compares):
                    bad = True
                    break
                else:
                    idx.append(compares.index(True))

            if not bad:
                idx.sort(reverse=True)
                for i in idx:
                    params.pop(i)
                
                params.insert(idx[-1], ("", result))

        docstring = ""
        for p in params:
            for cp, desc in params_description:
                if compare_param(cp, p):
                    docstring += "\t:param %s: %s\n" % (cp[1], desc)

        if docstring:
            docstring = '\t"""' + docstring + '\t"""\n'
            

        s_params = ", ".join(x[1] for x in params)
        print "def %s(%s):\n%s    return pyclblas_swig.%s(%s)\n" % (name, s_params, docstring, name, s_params)


