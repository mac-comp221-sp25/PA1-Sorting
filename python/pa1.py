import argparse
import numpy as np

# Use the argument parser library to collect commandline argument in args
parser = argparse.ArgumentParser()
parser.add_argument("--ints", type=int, nargs='+')
parser.add_argument("--alg", type=str)
parser.add_argument("--time", action="store_true")
args = parser.parse_args()

# And just print out the args
if __name__ == "__main__":
    print(args.alg)
    A = np.array(args.ints) # Use this, not the built-in python lists!
    for i in A:
        print(i)
    print(args.time)
