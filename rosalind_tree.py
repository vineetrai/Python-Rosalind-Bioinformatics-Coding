'''
A simple, undirected graph on n nodes has e edges, where e <= (n choose 2) = n(n-1)/2.
If the graph has no cycles, then e <= n-1, and the graph consists of tree(s).
If e = n - 1, then the graph is a single connected component (1 tree)

If we are given the number of nodes (n) and the number of edges (e), then we add b
edges such that e + b = n-1.

Therefore, b = n-1 + e

Suppose the graph has k connected components. Then k-1 edges need to be added
to fully connect the tree. Proof by induction on k:

    Trivial case: k = 0, no graph exists
    Trivial case: k = 1, b = 0 and no edges need to be added
    If k = 2: We add a single edge to fully connect the graph, so b = 1
    If k = 3: We add two edges to fully connect the graph, so b = 2
    Assume for k = x, we add x-1 edges to fully connect the graph, so b = x-1
    If k = x+1: Take previous case and notice there is only 1 more connected component,
    so only 1 more edge should be added. b = x-1 + 1 => b = x => b = k-1
'''

f = open('rosalind_tree.txt', 'r')
n = int(f.readline())
e = 0
for line in f:
    e += 1
f.close()

print(n-1-e)
