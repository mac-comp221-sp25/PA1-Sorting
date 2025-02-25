import subprocess
import random
import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Generate an array of random, bounded ints
def random_array(n, lower_bound=-100, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for i in range(n)]

# The choices of n/algorithm
ns = [10, 100, 200, 500, 800, 1000] #2000, 5000, 10000, 20000, 50000]
algs = ["bubble", "merge", "qslomuto", "qshoare"]

# number of samples to take per n/algorithm. 
num_reps = 10

# Sample runtimes
data = {"n":[], "alg":[], "rep":[], "ms":[]}
for alg in algs:
    for n in ns:
        for rep in range(num_reps):
            A = random_array(n)
            cmd = ["./pa1.sh", "--ints"] + [str(a) for a in A] + ["--alg", alg, "--time"]
            out = subprocess.run(cmd, capture_output=True)


            data["n"].append(n)
            data["alg"].append(alg)
            data["rep"].append(rep)
            try:
                data["ms"].append(float(out.stdout))
            except ValueError:
                print("Output formatted incorrectly. Only print a float when --time is provided.")
                data["ms"].append(None)

        print(alg, n)


# Save sampled times to csv
df = pandas.DataFrame(data)
df.to_csv("sampled-times.csv")

# Generate plot
plot = sns.lineplot(x="n", y="ms",
                   hue="alg",
                   data=df)

plot.get_figure().savefig("plot.pdf")

