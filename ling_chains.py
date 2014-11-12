# -*- coding: utf-8 -*-
"""Linguistic Chains analysis.

This module provides functions for the study of "linguistic chains" as described
in the homework.
"""

import itertools


def pairwise(iterable):
    # http://docs.python.org/library/itertools.html#recipes
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)


def make_graph(strings):
    """This function makes a graph description from a list of strings.

    The graph is described as a python dictionary holding the nodes as keys
    and is treated like a directed graph.

    The edges are inferred from the situation where a given string (node) can be
    reproduced by substracting a single character from another string (node)

    Args:
        strings (list of str): A list of strings.

    Returns:
      dict: A graph representation of the list of strings.

    Example:
        ```
            >>> make_graph(['a', 'ab', 'abc'])
            // give us a graph described by
            // a => ab => abc
            // in a form like the following dict
            { 'a': set(['ab']), 'ab': set(['abc']) }
        ```
    """
    graph = dict()
    keyfunc = lambda x: len(x)
    groups = [set(group)
              for key, group in itertools.groupby(sorted(strings, key=keyfunc),
                                                  keyfunc)]
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
    """This function computes all the paths in a graph created by calling
    `make_graph`.

    The graph is traversed as a list of tree walks where the keys of the graph
    are treated as roots of the trees. All trees are fully walked (don't
    try it with circular data). All returned paths begin at one of the roots.

    Args:
        graph (dict): A graph created by calling make_graph.

    Returns:
      list: The walked paths.

    Example:
        ```
            >>> compute_all_paths({ 'a': set(['ab']), 'ab': set(['abc']) })
            // give us the following paths
            // [['a', 'ab', 'abc'], ['ab', 'abc']]
        ```
    """
    all_paths = []
    for node in graph.keys():
        all_paths += compute_paths(graph, [node])
    return all_paths


def compute_paths(graph, from_path=[], accum_paths=None):
    """This function computes all the paths, starting from the "leaf node"
    (last item) in the `from_path` parameter, in a graph created by calling
    `make_graph`.

    The graph is traversed using a tree walk where the root of the tree is the
    "leaf node" mentioned above. All possible paths stating at the root are
    fully walked (don't try it with circular data).

    To do:
        Add memoization

    Args:
        graph (dict): A graph created by calling make_graph.
        from_path (list): A path to start with.
        accum_paths (list): An accumulator for the walked paths.

    Returns:
      accum_paths: The walked paths.

    Example:
        ```
            >>> compute_paths({ 'a': set(['ab']), 'ab': set(['abc']) }, ['ab'])
            // give us the following result
            // [['ab', 'abc']]
        ```
    """
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
    """This function gives the longest paths in the input.

    The input list of paths is sorted by lenght (desc) and then iterated
    until all the longest paths are collected.

    Args:
        paths (list): A list with paths.

    Returns:
      longet_paths: The longest paths from the input.

    Example:
        ```
            >>> get_longest([['a', 'ab', 'abc'], ['ab', 'abc']])
            // give us the following result
            // [['a', 'ab', 'abc']]
        ```
    """
    sorted_paths = sorted(paths, key=lambda x: -len(x))
    longest_paths = []
    longest_paths_length = len(sorted_paths[0])
    for path in sorted_paths:
        if len(path) < longest_paths_length:
            break
        longest_paths.append(path)
    return longest_paths


def make_report(paths):
    """This function makes a report from a list of paths.

    The paths are represented as strings with the form "start => middle => end".

    Args:
        paths (list): A list with paths.

    Returns:
      report: A list with the paths described by strings with arrows.

    Example:
        ```
            >>> make_report([['a', 'ab', 'abc'], ['ab', 'abc']])
            // give us the following result
            // ['a => ab => abc', 'ab => abc']
        ```
    """
    return [" => ".join(path) for path in paths]
