# Programming Assignment 1 - COMP221

Your goal is to implement up to 4 sorting algorithms in either C, Java, or Python from (roughly) scratch. We will then time how fast each sorting algorithm sorts to determine whether our optimized sorts are actually any better than naive sorts.

To receive full credit (100pts), you will need to implement Bubblesort (50pts), Mergesort (25pts), Quicksort w/ Lomuto Partitions (20pts), and Quicksort w/ the Hoare Partition (5pts). I recommend strategizing about how much of the assignment to complete; In many ways, the Hoare partition quicksort implementation is a bonus problem, as doing the rest of the assignment correctly will net you a 95% --- An A! 

### Project Specifications 

Your solution will be graded on **correctness** (does the algorithm actually sort, and is it the sort that it claims to be). However, to be tested, you will need to make sure your code accepts the correct command-line arguments and outputs the proper output, up to the exact formatting. There are two modes your solution should handle, both of which are outlined in the following sections.

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

You should accept any integers as arguments to ints and accept the following labels for the sorting algorithms: `bubble` (for bubblesort), `merge` (for mergesort), `qslomuto` (for quicksort with the lomuto partition scheme), and `qshoare` (for quicksort with the hoare partition scheme). 

#### Timing Mode

Given input that looks like the following

```bash
./pa1.sh --ints 1 4 -5 10 --alg bubble --time
```

Your code should output something like

```bash
0.012
```

indicating that sorting the 4 elements took approximately 0.012ms (or 12 millionths of a second). 

Format your output such that you return the number of milliseconds sorting took, rounding to 3 places past the decimal point. This will ensure the output is compatible with any post-processing. Include no extraneous text --- if it cannot be parsed as a float, your output cannot be post-processing by the plotting script.

**Failing to return outputs that match these requirements will cause you to lose a significant number of points**. If any of these instructions are unclear, please ask for clarification as early as possible.


#### Notes:

- Familiarize yourself with what tools are available for measuring time in the language of your choice (`system.nanotime()` in Java, or the `time` package in Python, or `clock()` in c). Make sure you understand what units time is measured in, and know how to convert those units to milliseconds before printing output. 

- Look to the QuickSort activity to see pseudocode for the Hoare Partitioning Scheme, which is the only thing we didn't see in class.

- If you choose to code in python, note that since there isn't a first-party array implementation, you must use the array implementation from `numpy`, as the starter code does. **This is the only 3rd-party library you are allowed to use**. 

- The provided starter code provides sample code for interacting with command-line arguments, in case you haven't seen code like this before. You should modify this code as necessary to match the project specification above.

- The provided starter code also provides pa1.sh, a bash file that simplifies grading by providing a single way to run your code regardless of what language it's in. Be sure to open the file and read the instructions in the file to understand how it should function, and how to edit the script so it selects the language you chose to use. **Failure to do this may result in the loss of points!**

- Note that the pa1.sh file DOES NOT compile your c or java code for you. Make sure you setup/modify the provided build system (Make or Gradle) to compile your sorting code in a place where pa1.sh can find it. You should feel free to modify pa1.sh as needed to do so, but be wary that it should *not* print any extraneous output! You may use the (currently empty) setup.sh to indicate how you would like your code to be built.

- Github actions have been set up to autorun code to sample the runtime of your sorting algorithms for various choices of n and then plot those results. You can also run this manually using the plotting code in the sampling/ folder. **Don't modify this script**, but feel free to use it to verify your output is properly formatted.

- If anything is unclear, or you think you've found a typo, please let me know as soon as you can!

#### Tips for Java

##### Modifying pa1.sh

The standard way to run Java code in the command-line is, as one might expect, with the `java` command. What it always wants passed in is the name of the main class to run. If you're running it from a directory that doesn't contain all of your compiled `.class` files, it will also want a *classpath*, which tells you where those classes are! This is specified by the `-cp` option. So the standard call to `java` for us will look like

```bash
java -cp [PATH TO .CLASS FILES] [NAME OF MAIN CLASS]
```
where you substitute for the things in brackets. Given the structure I've given you in the Java project, `pa1_template.pa1` is the name of the package/class our code is in, so we have to find the path where the `pa1_template` folder resides.

This is the line that should be in your `pa1.sh` file if you're using Java!

##### Compiling Java Code

Your typical method for compiling Java code is probably either (1) just hitting compile & run in VSCode or (2) Using Gradle Build. The way things are set-up in VSCode, these may result in different locations where your code ends up! By default, running `gradle build` will put things in the `java/build/classes/java/main/` folder, and VSCode places it in `java/bin/main/` 

If you want to have the plot autogeneration go easily, my recommendation is to compile using gradle, and uncomment the lines in the ./setup.sh file in this repository to build using gradle for you. That way, you can compile your code via the commandline by running `./setup.sh`, and then run your code using something like `./pa1.sh --ints 1 2 3 --alg bubble --time`. This means you should have the classpath in `pa1.sh` refer to the gradle build path, which you can manually verify after using `setup.sh`

