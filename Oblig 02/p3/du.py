import sys
from collections import defaultdict

def read_lookup_table(file_path):
    lookup_table = {}
    with open(file_path, "r") as f:
        for line in f.readlines():
            x, fx = line.strip().split("->")
            lookup_table[x] = fx
    return lookup_table

def xor_binary(a,b):
    return "".join(["0" if a[i] == b[i] else "1" for i in range(len(a))])

def compute_differential_uniformity(lookup_table):
    n = len(next(iter(lookup_table.keys())))  # Remove the extra parentheses
    delta_counts = defaultdict(int)

    for x1 in lookup_table:
        for x2 in lookup_table:
            if x1 != x2:
                delta_x = xor_binary(x1, x2)
                delta_fx = xor_binary(lookup_table[x1], lookup_table[x2])
                delta_counts[(delta_x, delta_fx)] += 1

    return max(delta_counts.values())


def main(file_path):
    lookup_table = read_lookup_table(file_path)
    differential_uniformity = compute_differential_uniformity(lookup_table)
    print(differential_uniformity)

if __name__ == '__main__':
    file_path = sys.argv[1]
    main(file_path)