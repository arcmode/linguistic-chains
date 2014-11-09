#!/usr/bin/python

# -*- coding: utf-8 -*-

# Linguistic Chains

# Write a program (Java or Python) that finds the word from which one can
# remove the most letters, one at a time, such that each resulting word is
# itself a valid word. For example, you can remove seven letters from
# "starting":

# starting => stating => statin => satin => sati => sat => at => a

# assuming your dictionary is:

# a
# at
# bat
# be
# bee
# sat
# sati
# satin
# starting
# statin
# stating

# The program must take the path to a dictionary as input. The dictionary
# will contain words, one per line. The program must output the longest
# chains which can be created from the words in the dictionary. The format
# must be as above with one space between each word and the following "=>"
# and one space after the "=>". If there are multiple words that produce
# equal length chains, then print each chain on a line by itself.

# Your program must work with large dictionaries with more than a hundred
# thousand words.

# What is the complexity of your program?

# example: ./linguistic_chains.py dictionary.txt

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
    # todo: transactions

    @staticmethod
    def build_graph(lines):
        graph = dict()
        groups = [set(group)
                  for key, group in itertools.groupby(lines, keyfunc)]
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
    def compute_paths(graph):
        for from_node, to_nodes in graph.viewitems():
            LinguisticChains.traverse(graph, [from_node], to_nodes)

    @staticmethod
    def traverse(graph, from_path = [], to_nodes = []):
        # todo: caching
        paths = []
        for node in to_nodes:
            path = from_path + [node]
            if node in graph:
                LinguisticChains.traverse(graph, path, graph[node])
            else:
                paths.append(path)
        print paths


# todo: validate args
if __name__ == '__main__' and len(sys.argv) == 2:
    dictionary_path = sys.argv[1]
    lines = []

    with open(dictionary_path) as dictionary:
        keyfunc = lambda x: len(x)
        lines = sorted([line.rstrip('\n').lower()
                        for line in dictionary if line.strip('')], key=keyfunc)

    graph = LinguisticChains.build_graph(lines)
    paths = LinguisticChains.compute_paths(graph)
