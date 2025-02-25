# Programming Assignment 1 - COMP221

Your goal is to implement up to 4 sorting algorithms in either C, Java, or Python from (roughly) scratch. We will then time how fast each sorting algorithm sorts to determine whether our optimized sorts are actually any better than naive sorts.

To receive full credit (100pts), you will need to implement Bubblesort (50pts), Mergesort (25pts), Quicksort w/ Lomuto Partitions (20pts), and Quicksort w/ the Hoare Partition (5pts). I recommend strategizing about how much of the assignment to complete; In many ways, the Hoare partition quicksort implementation is nearly a bonus problem, as doing the rest of the assignment correctly will net you a 95%! 

### Project Specifications 

Your solution will be graded on **correctness** (does the algorithm actually sort, and is it the sort that it claims to be). However, to be tested, you will need to make sure your code accepts the correct command-line arguments and outputs the proper output, up to the exact formatting. There are two configurations you should be familiar with, outlined in the following sections.

#### Sorting Mode

Given an input that looks like the following

```bash
./pa1.sh --ints 1 4 -5 10 --alg bubble
```

Your code should output

```bash
-5
1
4
10
``` 
That is, when given only the --ints and --alg arguments, which specify the integers to sort and the algorithm to sort with, you should output the integers, one-per-line, in sorted order.

You should accept any integers as arguments to ints and accept the following labels for the sorting algorithms: bubble (for bubblesort), merge (for mergesort), qslomuto (for quicksort with the lomuto partition), and qshoare (for quicksort with the hoare partition). 

#### Timing Mode

Given input that looks like the following

```bash
./pa1.sh --ints 1 4 -5 10 --alg bubble --time
```

Your code should output something like

```bash
0.012
```

indicating that sorting the 4 elements took approximately 0.012ms (or 12 millionths of a second). You should ensure that the data your code sends to stdout (the standard output) can be parsed as a float. Format your output such that you return the number of milliseconds with 3 places past the decimal point preserved. This will ensure the output is compatible with any post-processing. 

**Failing to return outputs that match these requirements will cause you to lose a significant number of points**. If any of these instructions are unclear, please ask for clarifcation as early as possible.


#### Notes:

- Familiarize yourself with what tools are available for measuring time in the language of your choice (`system.nanotime()` in Java, or the `time` package in Python, or `clock()` in c). Make sure you understand what units time is measured in, and know how to convert those units to milliseconds before printing output. 

- Look to the QuickSort activity to see pseudocode for the Hoare Partitioning Scheme, which is the only thing we didn't see in class.

- If you choose to code in python, note that since there isn't a first-party array implementation, you must use the array implementation from numpy. **This is the only 3rd-party library you are allowed to use**. 

- The provided starter code provides sample code for interacting with command-line arguments, if you haven't seen code like this before. You should modify this code as necessary to match the project specification above.

- The provided starter code also provides pa1.sh, a bash file that simplifies grading by providing a single way to run your code regardless of what language it's in. Be sure to open the file and read the instructions in the file to understand how it should function, and how to edit the script. **Failure to do this may result in the loss of points!**

- Note that the pa1.sh file DOES NOT compile your c or java code for you. Make sure you setup/modify the provided build system (Make or Gradle) to compile your sorting code in a place where pa1.sh can find it. Feel free to modify pa1.sh as needed to do so.

- Github actions have been set up to autorun code to sample the runtime of your sorting algorithms for various choices of n and then plot those results. You can also run this manually using the plotting code in the sampling/ folder. **Don't modify this script**, but feel free to use it to verify your output is properly formatted.

- If anything is unclear, or you think you've found a typo, please let me know as soon as you can!
