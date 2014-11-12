
### Important files

* `ling_chains.py`: code for solving the given problem
* `ling_chains_test.py`: unit tests
* `print_longest_chain.py`: executable with the solution

### How to test the solution

If you want to run the unit tests run `python ling_chains_test.py -v`

In order to run the code against the test example input run `./print_longest_chains.py input/dictionary.txt`

if you want to run the code against a real world input then run `./print_longest_chains.py input/unix_words.txt`

### Algorythm

#### Building the graph

1.  Group words by length
2.  For each pair of groups like (`one_letters`, `two_letters`)
3.  For each word in the group of larger words
4.  For each possible match (variations of the same word with one less character)
5.  If the possible match is present in the group of shorter words
6.  Append match as an edge to the graph

#### Computing the paths

1.  For each edge (word => wordy)
2.  Compute paths traversing all edges
3.  Sort paths by length (desc)
4.  Pick longest paths

### Time complexity

#### Building the graph
`O(l n)` where `n` is the number of words and `l` is the average length of the words having more than one letter

#### Computing the paths
`O(m^2)` where `m` is the number of nodes in the graph (proportional to `n^2`). In the expected case (english word list found in unix systems at `/usr/share/dict/words`) the proportionality constant is in the order of `1e-06`.

#### Finally
The time complexity of the solution is given by `O((l n) + (k n^2)` where `k` is in the order of `1e-12` and `l` in the order of `1e1`. This is polynomial time, but as you can see the quadratic component is greatly amortized. See `./bench/time.png`
