#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Linguistic Chains analysis runner.

This module shows a solution to the homework problem.

Examples:
    Run the homework solution:

        $ python measure_time.py input/unix_words.txt
"""


def print_longest_chains(dict_path):
    import ling_chains
    lines = []
    with open(dict_path) as dictionary:
        lines = [line.rstrip('\n').rstrip('\r').lower()
                 for line in dictionary if line.strip('')]
    graph = ling_chains.make_graph(lines)
    paths = ling_chains.compute_all_paths(graph)
    longest_paths = ling_chains.get_longest(paths)
    report = ling_chains.make_report(
        [list(reversed(path)) for path in longest_paths])
    for datum in report:
        print datum

# todo: validate args
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print_longest_chains(sys.argv[1])
