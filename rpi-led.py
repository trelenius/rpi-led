__author__ = 'Simon'
import sys
sys.path.append('pycharm-debug-py3k.egg')

import pydevd
debugServerIP = '192.168.13.100'
debugServerPort = 51200
pydevd.settrace(debugServerIP, port=debugServerPort, stdoutToServer=True, stderrToServer=True)