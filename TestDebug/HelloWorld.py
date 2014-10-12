__author__ = 'Simon'

import sys
sys.path.append('pycharm-debug-py3k.egg')
import pydevd
pydevd.settrace('192.168.13.100', port=51200, stdoutToServer=True, stderrToServer=True)

print "Hello, World!"
a = 50
b = 12
c = a+b
d = c + 1+a
print "Debug"
pydevd.stoptrace()