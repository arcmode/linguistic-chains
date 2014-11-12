#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Linguistic Chains analysis benchmarks.

This module runs the solution to the homework problem printing the execution
time and input size.

Examples:
    Benchmark the solution against subsets of the input with arbitrary sizing

        // each line in the input file has a probability of being filtered
        // equal to the environment var "SAMPLE"
        $ SAMPLE=0.3 ./measure_time.py input/unix_words.txt
        // Sample size: 70796 lines
        // Elapsed time: 0.739316 [s]
        $ SAMPLE=0.6 ./measure_time.py input/unix_words.txt
        //Sample size: 141871 lines
        //Elapsed time: 1.235725 [s]
        $ SAMPLE=1 ./measure_time.py input/unix_words.txt
        // Sample size: 212317 lines
        // Elapsed time: 1.987616 [s]
"""


def print_longest_chains(dict_path):
    import ling_chains
    import random
    import os
    lines = []
    threshold = 1.0 - float(os.environ.get('SAMPLE', 1.0))
    with open(dict_path) as dictionary:
        lines = [line.rstrip('\n').rstrip('\r').lower()
                 for line in dictionary
                 if line.strip('') and random.random() > threshold]
    graph = ling_chains.make_graph(lines)
    paths = ling_chains.compute_all_paths(graph)
    longest_paths = ling_chains.get_longest(paths)
    report = ling_chains.make_report(
        [list(reversed(path)) for path in longest_paths])
    for datum in report:
        print datum
    print('Sample size: {} lines'.format(len(lines)))

# todo: validate args
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        import time
        start = time.clock()
        print_longest_chains(sys.argv[1])
        elapsed = (time.clock() - start)
        print "Elapsed time: {} [s]".format(elapsed)
