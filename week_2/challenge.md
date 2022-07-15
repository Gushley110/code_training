# Flipping the matrix

> Source [Flipping the Matrix | Hackerrank](https://www.hackerrank.com/challenges/flipping-the-matrix/problem#:~:text=Sean%20invented%20a%20game%20involving,left%20quadrant%20of%20the%20matrix.)

## Description

Sean invented a game involving a `2n x 2n` matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the `n x n` submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for  matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

### **Example 1**:
~~~python
matrix  =   [[1,2],
            [3,4]]
~~~
~~~python
1 2
3 4
~~~
it is `2x2` and we want to maximize the top left quadrant, a `1x1`matrix. Reverse row 1.
~~~python
1 2
4 3
~~~
And now reverse column 0.
~~~python
4 2
1 3
~~~
The maximal sum is 4.

### **Function Description**:
Complete the flippingMatrix function in the editor below.

flippingMatrix has the following parameters:

`int matrix[2n][2n]: a 2-dimensional array of integers`

**Returns**

`int: the maximum sum possible.`

**Input Format**

The first line contains an integer , the number of queries.

The next `q` sets of lines are in the following format:

The first line of each query contains an integer, `n`.
Each of the next `2n` lines contains `2n` space-separated integers `matrix[i][j]` in row `i` of the matrix.

**Constraints:**

`1 <= q <= 16`

`1 <= n <= 128`

`0 <= matrix[i][j] <= 4096, where 0 <= i,j < 2n`

**Sample Input**

~~~
STDIN           Function
-----           --------
1               q = 1
2               n = 2
112 42 83 119   matrix = [[112, 42, 83, 119], [56, 125, 56, 49], \
56 125 56 49              [15, 78, 101, 43], [62, 98, 114, 108]]
15 78 101 43
62 98 114 108
~~~

**Sample Output**

~~~
414
~~~