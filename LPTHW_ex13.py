# %%
# -*- coding: utf-8 -*-
# Exercise 13: Parameters, Unpacking, Variables
#from sys import argv
import sys

def main(argv):
    print("the script has %d argement."%(len(argv)-1))
    script, first, second, third = argv
    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)
    print("Your third variable is:", third)

if __name__ == "__main__":
    main(sys.argv)


# %%



