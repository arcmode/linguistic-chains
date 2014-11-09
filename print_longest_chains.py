#!/usr/bin/python
# -*- coding: utf-8 -*-

# example usage: ./linguistic_chains.py real_dict.txt


def print_longest_chains(dict_path):
    import ling_chains
    lines = []
    with open(dict_path) as dictionary:
        lines = sorted([line.rstrip('\n').lower()
                        for line in dictionary if line.strip('')], key=lambda x: len(x))
    graph = ling_chains.make_graph(lines)
    paths = ling_chains.compute_all_paths(graph)
    longest_paths = ling_chains.get_longest(paths)
    report = ling_chains.make_report(longest_paths)
    for datum in report:
        print datum

# todo: validate args
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print_longest_chains(sys.argv[1])
