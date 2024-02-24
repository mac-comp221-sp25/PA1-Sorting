#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char *argv[]) {
    int *ints;
    int num_ints = 0;
    char *alg;

    // Argument parsing
    int i = 1;
    while (i < argc) {
        // Grab all of the integers into ints
        if(strcmp(argv[i], "--ints") == 0) {
            i++;
            int start = i;
            while ((i < argc) && strcmp(argv[i], "--alg")) {
                i++;
            }
            num_ints = i - start;
            ints = malloc(sizeof(int) * (num_ints)); // Please free this eventually!
            for (int j = 0; j < num_ints; j++) {
                ints[j] = atoi(argv[start + j]);
            }
        }
        // Grab the algorithm name
        else if(strcmp(argv[i], "--alg") == 0) {
            i++;
            alg = argv[i];
            i++;   
        } 
        else {
            i++;
        }
    }

    // Our commandline arguments are here! Print them
    printf("%s\n", alg);
    for (int i = 0; i < num_ints; i++) {
        printf("%i\n", ints[i]);
    } 

    if (num_ints > 0) free(ints); // This is where ints is eventually free'd
}
