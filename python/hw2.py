import argparse

# Use the argument parser library to collect commandline argument in args
parser = argparse.ArgumentParser()
parser.add_argument("--ints", type=int, nargs='+')
parser.add_argument("--alg", type=str)
args = parser.parse_args()

# And just print out the args
if __name__ == "__main__":
    print(args.alg)
    for i in args.ints:
        print(i)
