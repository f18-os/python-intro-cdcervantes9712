#! /usr/bin/env python3

import os, sys, time, re

pid = os.getpid()	# get and remember pid

os.write(1, ("Shell Initializing...\n").encode())

exitChek = False

while True:
    rc = os.fork()

    if rc < 0:
        os.write(2, ("Fork failed, returning %d\n" % rc).encode())
        sys.exit()

    elif rc == 0:
        os.write(1, ("$ ").encode())
        input = os.read(0, 512)
        input = userInput[:-1]

        args = re.split(" ", input.decode())

        if args[-1] == "exit":
            print(args[-1])
            exitChek = True
            break
            sys.exit()

        print(args[-1])

        for dir in re.split(":", os.environ['PATH']):	# try each directory in path
            program = "%s/%s" % (dir, args[0])
            try:
                os.execve(program, args, os.environ)	# try to exec program
            except FileNotFoundError:	# ...expected
                pass			# ...fail quietly

        os.write(2, ("Error: could not exec \n").encode())
	sys.exit(1)	# terminate with error

    else:	# parent (forked ok)
        childPidCode = os.wait()
        if exitChek:
            sys.exit()
	os.write(1, ("Terminated with exit code %d, Goodbye\n" % childPidCode).encode())
	
