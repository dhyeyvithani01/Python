import sys

from cs50.saying import hello
from cs50.saying import goodbye

if len(sys.argv)==3:
    hello(sys.argv[1])

if len(sys.argv)==3:
    goodbye(sys.argv[2])