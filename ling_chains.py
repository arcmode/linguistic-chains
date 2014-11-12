#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools


def pairwise(iterable):
    # http://docs.python.org/library/itertools.html#recipes
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)


def make_graph(lines):
    graph = dict()
    keyfunc = lambda x: len(x)
    groups = [set(group)
              for key, group in itertools.groupby(sorted(lines, key=keyfunc), keyfunc)]
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


def compute_all_paths(graph):
    all_paths = []
    for node in graph.keys():
        all_paths += compute_paths(graph, [node])
    return all_paths


def compute_paths(graph, from_path=[], accum_paths=None):
    # todo: memoize
    if accum_paths == None:
        accum_paths = []
    through_nodes = graph[from_path[-1]]
    for node in through_nodes:
        path = from_path + [node]
        if node in graph:
            compute_paths(graph, path, accum_paths)
        else:
            accum_paths.append(path)
    return accum_paths


def get_longest(paths):
    sorted_paths = sorted(paths, key=lambda x: -len(x))
    longest_paths = []
    longest_paths_length = len(sorted_paths[0])
    for path in sorted_paths:
        if len(path) < longest_paths_length:
            break
        longest_paths.append(path)
    return longest_paths


def make_report(paths):
    report = []
    for path in paths:
        report.append(" => ".join(path))
    return report
