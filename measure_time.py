#!/usr/bin/python
# -*- coding: utf-8 -*-

# example usage: `SAMPLE=0.6 ./measure_time.py input/unix_words.txt`


def print_longest_chains(dict_path):
    import ling_chains
    import random
    import os
    lines = []
    with open(dict_path) as dictionary:
        lines = sorted([line.rstrip('\n').rstrip('\r').lower()
                        for line in dictionary
                        if line.strip('') and random.random() > 1.0 - float(os.environ.get('SAMPLE', 1.0))],
                        key=lambda x: len(x))
    graph = ling_chains.make_graph(lines)
    paths = ling_chains.compute_all_paths(graph)
    longest_paths = ling_chains.get_longest(paths)
    report = ling_chains.make_report([list(reversed(path)) for path in longest_paths])
    for datum in report:
        print datum
    print('Sample size: {}'.format(len(lines)))

# todo: validate args
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        import time
        start = time.clock()
        print_longest_chains(sys.argv[1])
        elapsed = (time.clock() - start)
        print "Elapsed time: {}".format(elapsed)
