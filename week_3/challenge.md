# Flipping the matrix

> Source [Floyd City of blinding lights | Hackerrank](https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights/problem)

## Description

Given a directed weighted graph where weight indicates distance, for each query, determine the length of the shortest path between nodes. There may be many queries, so efficiency counts.

For example, your graph consists of  `5` nodes as in the following:

![](images/graph_1.png)

A few queries are from node `4` to node `3`, node `2` to node `5`, and node `5` to node `3`.


1. There are two paths from `4` to `3`:

- `4 -> 1 -> 2 -> 3` at a distance of `4 + 5 + 1 = 10`
- `4 -> 1 -> 5 -> 3` at a distance of `4 + 3 + 2 = 9`

    In this case we choose path .
2. There is no path from `2` to `5`, so we return `-1`.

3. There is one path from `5` to `3`:

- `5 -> 3` at a distance of `2`.


**Input Format**

The first line has two integers `n` and `m`, the number of nodes and the number of edges in the graph.
Each of the next `m` lines contains three space-separated integers ***u***, ***v*** and ***w*** and , the two nodes between which the directed edge `u -> v` exists, and `w`, the length of the edge.
The next line contains a single integer `q`, the number of queries.
Each of the next `q` lines contains two space-separated integers `a` and `b`, denoting the start and end nodes for traversal.

**Constraints:**

`2 <= n <= 400`

`1 <= m <= nx(n-1) / 2`

`1 <= q <= 10⁵`

`1 <= u,v <= n`

`1 <= w <= 350`

The distance from a node to itself is always `0` and it is always reachable from itself.

**If there are edges between the same pair of nodes with different weights, the last one (most recent) is to be considered as the only edge between them.**

**Output Format**

Print `q` lines, each containing a single integer specifying the shortest distance for the query.

If the destination node is not reachable, return `-1`.

**Sample Input**

~~~
STDIN   Function
-----   --------
4 5     n = 4, m = 5
1 2 5   u = 1, v = 2, w = 5
1 4 24  u = 1, v =4, w = 24 ...
2 4 6
3 4 4
3 2 7
3       q = 3
1 2     query 0: from 1 to 2
3 1     query 1: from 3 to 1
1 4     query 2: from 1 to 4
~~~

**Sample Output**

~~~
5
-1
11
~~~

**Explanation**

The graph given in the test case is:

![](images/graph_2.png)

The shortest paths for the 3 queries are :

- `1 -> 2`: The direct path is shortest with weight 5
- `-1`: There is no way of reaching node 1 from node 3
- `1 -> 2 -> 4`: The indirect path is shortest with weight (5+6) = 11 units. The direct path is longer with 24 units length.
