#!/usr/bin/python

# -*- coding: utf-8 -*-

# example usage: ./linguistic_chains.py real_dict.txt

import sys
import difflib
import itertools


def pairwise(iterable):
    # http://docs.python.org/library/itertools.html#recipes
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)


class LinguisticChains:

    @staticmethod
    def make_graph(lines):
        graph = dict()
        groups = [set(group)
                  for key, group in itertools.groupby(lines, lambda x: len(x))]
        for shorter, larger in pairwise(groups):
            comparison_range = xrange(0, len(list(larger)[0]))
            for large in larger:
                for idx in comparison_range:
                    possible_match = large[:idx] + large[(idx + 1):]
                    if possible_match in shorter:
                        if possible_match in graph:
                            graph[possible_match].add(large)
                        else:
                            graph[possible_match] = set([large])
        return graph

    @staticmethod
    def compute_all_paths(graph):
        all_paths = []
        for from_node, to_nodes in graph.viewitems():
            all_paths += LinguisticChains.compute_paths(
                graph, [from_node], to_nodes, [])
        return all_paths

    @staticmethod
    def compute_paths(graph, from_path=[], to_nodes=[], accum_paths=[]):
        # todo: caching
        for node in to_nodes:
            path = from_path + [node]
            if node in graph:
                LinguisticChains.compute_paths(
                    graph, path, graph[node], accum_paths)
            else:
                accum_paths.append(path)
        return accum_paths

    @staticmethod
    def get_longest(paths):
        sorted_paths = sorted(paths, key=lambda x: -len(x))
        longest_paths = []
        longest_paths_length = len(sorted_paths[0])
        for path in sorted_paths:
            if len(path) < longest_paths_length:
                break
            longest_paths.append(path)
        return longest_paths

    @staticmethod
    def report(paths):
        report = []
        for path in paths:
            report.append(" => ".join(path))
        return report

    @staticmethod
    def print_longest_chains(dict_path):
        lines = []
        with open(dict_path) as dictionary:
            lines = sorted([line.rstrip('\n').lower()
                            for line in dictionary if line.strip('')], key=lambda x: len(x))
        graph = LinguisticChains.make_graph(lines)
        paths = LinguisticChains.compute_all_paths(graph)
        longest_paths = LinguisticChains.get_longest(paths)
        report = LinguisticChains.report(longest_paths)
        for datum in report:
            print datum

# todo: validate args
if __name__ == '__main__' and len(sys.argv) == 2:
    LinguisticChains.print_longest_chains(sys.argv[1])
