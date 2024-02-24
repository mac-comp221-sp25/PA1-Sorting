#! /bin/bash

# Uncomment the line corresponding to the language you used
# This makes testing your sorts in the commandline 
# the same regardless of the language you use.
#
# Test with a line like:
# ./hw2.sh --ints 4 7 -12 6 -3 5 --alg bubblesort
#
# You should handle sorts named...
# mergesort
# bubblesort
# quicksortlomuto
# quicksorthaore
#
# and return sorted integers separated by newlines. i.e.
# -12
# -3
# 4
# 5
# 6
# 7


# If using python
python python/hw2.py "$@" 

# If using java
java -cp java/bin/main hw2_template.hw2 "$@"

# If using c
c/hw2 "$@"
