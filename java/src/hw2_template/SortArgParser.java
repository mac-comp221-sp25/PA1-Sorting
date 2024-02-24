package hw2_template;

/*
 * SortArgParser parses command line arguments --ints and --alg
 * into the appropriate instance variables to facilitate commandline
 * sorting inputs
 */
public class SortArgParser {
    private int[] ints;
    private String alg;

    /**
     * Constructor
     * @param args commandline arguments
     */
    public SortArgParser(String[] args) {
        int i = 0;
        while (i < args.length) {
            if (args[i].equals("--alg")) {
                i++;
                alg = args[i];
                i++;
            }
            else if (args[i].equals("--ints")) {
                i++;
                int start = i;
                while ((i < args.length)) {
                    try {
                        Integer.parseInt(args[i]);
                        i++;
                    } catch (Exception e) {
                        break;
                    }
                }
                ints = new int[i-start];
                for (int j = 0; j < ints.length; j++) {
                    ints[j] = Integer.parseInt(args[j + start]);
                }
            }
            else {
                i++;
            }
        }
    }

    /**
     * Returns the integers to sort.
     * @return An array of the integers you should sort.
     */
    public int[] getInts() {
        return ints;
    }

    /**
     * returns the sorting algorithm you should use.
     * @return A string representing the algorithm you should sort with.
     */
    public String getAlg() {
        return alg;
    }
}
