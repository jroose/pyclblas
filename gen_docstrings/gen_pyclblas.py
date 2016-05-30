#!/usr/bin/env python

import bs4 as bs
import re
import sys
import urllib2
from urlparse import urlparse, urljoin
from os.path import dirname, basename, exists

fin = urllib2.urlopen(sys.argv[1])
data = bs.BeautifulSoup(fin.read(), 'lxml')
fin.close()

parts = urlparse(sys.argv[1])

def prettify(x):
    if isinstance(x, str) or isinstance(x, bs.NavigableString):
        return x.strip()
    else:
        return x.prettify().replace("\n"," ").strip().replace("  "," ").replace("  "," ").replace("  "," ")

def cleanup(x):
    x = str(x)
    x = x.strip().replace("\n", " ")
    x = x.replace("\\leftarrow", "|larr|")
    x = x.replace("\\(", "(")
    x = x.replace("\\)", ")")
    x = x.replace("\\alpha", "|alpha|")
    x = x.replace("\\beta", "|beta|")
    x = x.replace("\\overline", "conj")
    x = x.replace("\\conjg", "conj")
    x = x.replace("^T","\\ :sup:`T`\\ ")
    x = x.replace("^H","\\ :sup:`H`\\ ")
    x = x.replace("^{-1}","\\ :sup:`-1`\\ ")
    x = re.sub(r"  +", " ", x)
    x = x.replace(" ,", ",")
    x = x.replace(" .", ".")
    x = re.sub(r"<b>\s*(.*?)\s*</b>", r"**\1**", x)
    x = re.sub(r"<p>\s*(.*?)\s*</p>", r"\1", x)
    x = re.sub(r"<ul>\s*(.*?)\s*</ul>", r"\1\n\n", x)
    x = re.sub(r"<li>\s*(.*?)\s*</li>", r"\n\n* \1", x)
    x = re.sub("<br ?/>"," ", x)
    return x

class P:
    def __init__(self, ptype, pname="", pdir="", pdesc=""):
        self.ptype = ptype.strip()
        self.pname = pname.strip()
        self.pdir = pdir.strip()
        self.pdesc = pdesc.strip().replace(" .",".")
        self.pdesc = cleanup(re.sub(r"For (a )?detailed description, see.*", "", self.pdesc))

    @classmethod
    def fromdesc(cls, pdir, pname, pdesc):
        return P("", pname, pdir.lstrip("[").rstrip("]"), pdesc)

    def __eq__(self, other):
        if self.ptype != other.ptype:
            return False

        if self.pname and other.pname and (self.pname != other.pname):
            return False

        if self.pdir and other.pdir and (self.pdir != other.pdir):
            return False

        return True

    def __str__(self):
        return "[%s],%s,%s,%s" % (self.pdir, self.ptype, self.pname, self.pdesc)

    def __repr__(self):
        return "P([%s] %s %s)" % (self.pdir, self.ptype, self.pname)
    

AlterDesc = (
    ((P("cl_context"),),"pyopencl.Context", ""),
    ((P("cl_command_queue"),),"pyopencl.CommandQueue", ""),
    ((P("cl_mem"),),"pyopencl.Buffer", ""),
    ((P("const cl_mem"),),"pyopencl.Buffer", ""),
    ((P("cl_uint", "numCommandQueues"), P("cl_command_queue *")),"pyopencl.CommandQueue", "A list, tuple, or single instance of pyopencl.CommandQueue. Must not be None."),
    ((P("cl_uint", "numEventsInWaitList"), P("const cl_event *")), "pyopencl.Event", "A list, tuple, or single instance of pyopencl.Event. May be None."),
    ((P("cl_float2"),), "complex", ""),
    ((P("cl_double2"),), "complex", ""),
    ((P("FloatComplex"),), "complex", ""),
    ((P("DoubleComplex"),), "complex", ""),
    ((P("size_t"),), "int", ""),
    ((P("cl_uint"),), "int", ""),
    ((P("cl_int"),), "int", ""),
    ((P("cl_double"),), "float", ""),
    ((P("double"),), "float", ""),
    ((P("cl_float"),), "float", ""),
)

ArgsRemoved = (
    (P("cl_event *", "events"),),
    (P("cl_uint *", "major"), P("cl_uint *", "minor"), P("cl_uint *", "patch")),
)

ArgsReturned = (
    ((P("cl_event *", "events"),), (P("pyopencl.Event", "events", pdesc="A tuple of pyopencl.Event instances, one for each commandQueue supplied."),)),
    ((P("cl_uint *", "major"), P("cl_uint *", "minor"), P("cl_uint *", "patch")), (P("str", "version", pdesc="Version string as %s.%s.%s % (major, minor, patch)"),)),
)

print """
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

""".strip()
print


all_types = set()
for atag in data.findAll('a',{'class':'el'}):    
    page_name = atag['href']
    page_url = urljoin(sys.argv[1], atag['href'])

    if 'TYPES' in page_url.upper(): continue

    #if 'GEMM' not in page_url.upper(): continue

    #print atag['href']
    if not exists(atag['href']):
        assert(0)
        atag_fin = urllib2.urlopen(page_url)
        page_data = bs.BeautifulSoup(atag_fin.read(), 'lxml')
        atag_fin.close()
        with open(atag['href'],'wb') as fout:
            fout.write(page_data.prettify())
    else:
        with open(atag['href'],'rb') as fin:
            page_data = bs.BeautifulSoup(fin.read(), 'lxml')

    #print page_url
    content = page_data.findAll('div', {'class':'contents'})[0]
    for divs in content.findAll('div', {'class':'memitem'}):
        tds = divs.findAll('td', {'class':'memname'})
        fname = tds[0].contents[-1].strip().split()[-1]
        anchor = divs.previous_sibling.previous_sibling
        args = []
        returns = []
        fdesc = []
        anchor = page_url + "#" + anchor['id']
        #print fname, anchor
        for t_param_name in divs.findAll('td', {'class':'paramdir'}):
            args.append(P.fromdesc(*[" ".join(prettify(c) for c in x.contents) for x in t_param_name.parent.findAll('td')]))

        t_memdoc = divs.findAll("div", {"class":"memdoc"})[0]
        for t_subdoc in t_memdoc.contents:
            if isinstance(t_subdoc, bs.element.Tag) and 'class' in t_subdoc.attrs and "params" in t_subdoc['class']: break
            if isinstance(t_subdoc, bs.element.Tag) and 'class' in t_subdoc.attrs and "return" in t_subdoc['class']: break
            if isinstance(t_subdoc, bs.element.Tag) and 'class' in t_subdoc.attrs and "note" in t_subdoc['class']: break
            if isinstance(t_subdoc, bs.element.Tag) and "Examples" in t_subdoc.get_text(): break
            fdesc.append(prettify(t_subdoc))
        fdesc = cleanup(" ".join(fdesc))
        #print fdesc


        it_arg = 0
        for t_param_type in divs.findAll('td', {'class':'paramtype'}):
            t_param_name = t_param_type.parent.findAll('td', {'class':'paramname'})[0]
            ptype = t_param_type.get_text().replace(",","").strip()
            pname = t_param_name.get_text().replace(",","").strip()
            if pname == "" and ptype == "void": continue

            try:
                assert(args[it_arg].pname == pname)
            except:
                print args[it_arg], pname
                raise
            args[it_arg].ptype = ptype
            it_arg += 1

        for argslist, ntype, ndesc in AlterDesc:
            find = [x for x in args if x in argslist]
            if len(find) == len(argslist):
                pos = args.index(find[0])
                for f in find:
                    args.remove(f)
                narg = P(ntype, find[-1].pname, find[-1].pdir, find[-1].pdesc.strip().rstrip(".") + ".  " + ndesc)
                args.insert(pos, narg)

            if len(find) > 1 and len(argslist) == 1:
                for f in find:
                    pos = args.index(f)
                    args.remove(f)
                    narg = P(ntype, f.pname, f.pdir, f.pdesc.strip().rstrip(".") + ".  " + ndesc)
                    args.insert(pos, narg)

        for repargs, ret in ArgsReturned:
            find = [x for x in args if x in repargs]
            if tuple(find) == tuple(repargs):
                for f in find:
                    args.remove(f)

                for retval in ret:
                    returns.append(retval)
        
        for kill in ArgsRemoved:
            find = [x for x in args if x in kill]
            if len(find) == len(kill):
                for f in find:
                    args.remove(f)

        for a in args:
            all_types.add(a.ptype)

        all_args = ", ".join([a.pname for a in args])
        print "def %s(%s):" % (fname, all_args)
        print '    """',
        print "wraps: `%s <%s>`_" % (fname, anchor)
        print
        print "%s" % fdesc
        print
        for arg in args:
            print ":param %s: %s" % (arg.pname, arg.pdesc)
            print ":type %s: %s [%s]" % (arg.pname, arg.ptype, arg.pdir)    
        for ret in returns:
            print ":return: %s" % (ret.pdesc)
            #print ":rtype: %s" % (ret.ptype)
        print
        print '"""'
        print "    return pyclblas_swig.%s(%s)" % (fname, all_args)
        print
