all: _pyclblas.so

clean:
	rm -f pyclblas.py  pyclblas.pyc  _pyclblas.so  pyclblas_wrap.c  pyclblas_wrap.o

_pyclblas.so: pyclblas_wrap.o
	$(LD) -shared $^ -o "$@" -lclBLAS

pyclblas_wrap.o: pyclblas_wrap.c
	$(CC) $^ -I/usr/include/python2.7 -c -fPIC -o "$@" -g

pyclblas_wrap.c: pyclblas.i
	swig -python $^
