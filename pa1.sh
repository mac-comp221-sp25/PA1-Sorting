#! /bin/bash

# Leave the line corresponding to the language you used uncommented
# This makes testing your sorts in the commandline 
# the same regardless of the language you use.
#
# Test with a line like:
# ./pa1.sh --ints 4 7 -12 6 -3 5 --alg bubble
#
# You should handle sorts named...
# merge
# bubble
# qslomuto
# qshaore
#
# and return sorted integers separated by newlines. i.e.
# -12
# -3
# 4
# 5
# 6
# 7
# If the argument --time is provided, it should print ONLY the time taken to sort the input, in milliseconds.


# If using python
python3 python/pa1.py "$@" 

# If using java
java -cp java/build/classes/java/main/ pa1_template.pa1 "$@"

# If using c
c/pa1 "$@"
