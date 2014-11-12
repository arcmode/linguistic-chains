import ling_chains
import unittest


class TestLingChains(unittest.TestCase):

    def setUp(self):
        self.words = ['a',
                      'at',
                      'bat',
                      'be',
                      'bee',
                      'sat',
                      'sati',
                      'satin',
                      'starting',
                      'statin',
                      'stating']
        self.graph = {
            'a':       set(['at']),
            'at':      set(['bat', 'sat']),
            'be':      set(['bee']),
            'sat':     set(['sati']),
            'sati':    set(['satin']),
            'satin':   set(['statin']),
            'statin':  set(['stating']),
            'stating': set(['starting'])
        }

    def test_make_graph(self):
        graph = ling_chains.make_graph(self.words)
        self.assertItemsEqual(graph.viewitems(), self.graph.viewitems())

    def test_compute_paths(self):
        expected_paths = [
            ['at', 'bat'],
            ['at', 'sat', 'sati', 'satin', 'statin', 'stating', 'starting']
        ]
        paths = ling_chains.compute_paths(self.graph, ['at'])
        self.assertItemsEqual(paths, expected_paths)

    def test_compute_all_paths(self):
        expected_paths = [
            ['a', 'at', 'bat'],
            ['a', 'at', 'sat', 'sati', 'satin',
             'statin', 'stating', 'starting'],
            ['at', 'bat'],
            ['at', 'sat', 'sati', 'satin', 'statin', 'stating', 'starting'],
            ['be', 'bee'],
            ['sat', 'sati', 'satin', 'statin', 'stating', 'starting'],
            ['sati', 'satin', 'statin', 'stating', 'starting'],
            ['satin', 'statin', 'stating', 'starting'],
            ['statin', 'stating', 'starting'],
            ['stating', 'starting']
        ]
        paths = ling_chains.compute_all_paths(self.graph)
        self.assertItemsEqual(paths, expected_paths)

    def test_get_longest(self):
        all_paths = [
            ['a', 'at', 'bat'],
            ['a', 'at', 'sat', 'sati', 'satin',
             'statin', 'stating', 'starting'],
            ['at', 'bat'],
            ['at', 'sat', 'sati', 'satin', 'statin', 'stating', 'starting'],
            ['be', 'bee'],
            ['sat', 'sati', 'satin', 'statin', 'stating', 'starting'],
            ['sati', 'satin', 'statin', 'stating', 'starting'],
            ['satin', 'statin', 'stating', 'starting'],
            ['statin', 'stating', 'starting'],
            ['stating', 'starting']
        ]
        expected_paths = [
            ['a', 'at', 'sat', 'sati', 'satin',
             'statin', 'stating', 'starting']
        ]
        longest_paths = ling_chains.get_longest(all_paths)
        self.assertItemsEqual(longest_paths, expected_paths)

    def test_make_report(self):
        paths = [
            ['a', 'at', 'sat', 'sati', 'satin',
             'statin', 'stating', 'starting']
        ]
        expected_report = [
            'a => at => sat => sati => satin => statin => stating => starting'
        ]
        report = ling_chains.make_report(paths)
        self.assertItemsEqual(report, expected_report)


if __name__ == '__main__':
    unittest.main()
