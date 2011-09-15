#compile time options
#OPTS += -DDEBUG_IO #define for some debuggin I/O - none implemented so far
OPTS += -DDEBUG -DDEBUG_LEVEL=0 #leave undefined for no debugging - 0,1, and 2 give progressively more output to stderr
#OPTS += -DTEST_CODE #define to run some basic test code
#OPTS += -DCOMPUTE_SIGMAM #set to compute sigmam for a list of masses in a file

#select your computer
COMP="orange"
#COMP="mandor-icc"
#COMP="mandor-gcc"

#edit/add to match your machine
ifeq ($(COMP),"orange")
CC          = mpicc
OPTIMIZE    = -Wall -O3 -wd2259 -wd981
GSLI        =  -I/afs/slac.stanford.edu/g/ki/software/gsl/include 
GSLL        =  -L/afs/slac.stanford.edu/g/ki/software/gsl/lib
FFTWI       =  -I/afs/slac.stanford.edu/g/ki/software/fftw/3.2.2/include
FFTWL       =  -L/afs/slac.stanford.edu/g/ki/software/fftw/3.2.2/lib 
EXTRACFLAGS =
EXTRACLIB   =  -lgsl -lgslcblas -lfftw3 -lfftw3f
endif

ifeq ($(COMP),"mandor-icc")
CC          =  icc 
OPTIMIZE    =  -g -O3
GSLI        =  -I/home/beckermr/include
GSLL        =  -L/home/beckermr/lib -lgsl -lgslcblas
FFTWI       =  -I/home/beckermr/include
FFTWL       =  -L/home/beckermr/lib -lfftw3 -lfftw3f
FITSI       =  -I/home/beckermr/include
FITSL       =  -L/home/beckermr/lib -lcfitsio
EXTRACFLAGS =  -Wall -wd981 #-wd1419 -wd810
EXTRACLIB   =  
endif

ifeq ($(COMP),"mandor-gcc")
CC          =  gcc
OPTIMIZE    =  -pg -g #-Werror
GSLI        =  -I/home/beckermr/include
GSLL        =  -L/home/beckermr/lib -lgsl -lgslcblas
FFTWI       =  -I/home/beckermr/include
FFTWL       =  -L/home/beckermr/lib -lfftw3 -lfftw3f
FITSI       =  -I/home/beckermr/include
FITSL       =  -L/home/beckermr/lib -lcfitsio
EXTRACFLAGS =  -ansi -std=c99 -pedantic -Wall -W -Wmissing-prototypes -Wstrict-prototypes -Wconversion -Wshadow -Wpointer-arith -Wcast-qual -Wcast-align \
	-Wwrite-strings -Wnested-externs -fshort-enums -fno-common -Dinline= 
EXTRACLIB   =  
endif

#set it all up
CLINK=$(CC)
CFLAGS=$(OPTIMIZE) $(GSLI) $(FFTWI) $(FITSI) $(EXTRACFLAGS) $(OPTS)
CLIB=$(EXTRACLIB) $(GSLL) $(FFTWL) $(FITSL) $(GSLL) -lm

ifneq (TEST_CODE,$(findstring TEST_CODE,$(CFLAGS)))
TESTCODE=
else
TESTCODE=test_code.o
endif

OBJS = $(TESTCODE) distances.o linear_powspec.o transfer_function.o \
	growth_function.o hubble.o peakheight.o mass_bias_functions.o \
	linear_corrfunc.o fftlog.o utils.o nonlinear_powspec.o nonlinear_corrfunc.o

EXEC = computecosmo
TEST =
all: $(EXEC)
test: $(TEST) clean

OBJS1=$(OBJS) main.o
$(EXEC): $(OBJS1)
	$(CLINK) $(CFLAGS) -o $@ $(OBJS1) $(CLIB)

$(OBJS1): cosmocalc.h Makefile

.PHONY : clean
clean: 
	rm -f *.o

.PHONY : spotless
spotless: 
	rm -f *.o $(EXEC) $(TEST)
