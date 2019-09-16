CFLAGS = -Wall -m32 -g -fno-stack-protector -Wno-unused-function -mpreferred-stack-boundary=2 -fno-PIC
LDFLAGS = -no-pie -m32 -zexecstack

.PHONY: all clean

all: vuln

vuln: vuln.o

clean:
	-rm -f *~
	-rm -f peda-session*.txt
	-rm -f vuln.o
	-rm -f vuln
