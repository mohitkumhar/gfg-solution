<h2><a href="https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1">Spirally Traversing a Matrix</a></h2><h3>Medium</h3><hr><p><span style="font-size: 14pt;">Given a rectangular matrix <strong>mat[][]</strong> of size <strong>n x m</strong>, and return a 1D array<strong> </strong>containing all its elements in <strong>spiral </strong>order.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
<strong>Output</strong>: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
<strong>Explanation</strong>: <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/701264/Web/Other/blobid1_1734498654.png" width="456" height="228"><br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: mat[][] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
<strong>Output</strong>: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
<strong>Explanation</strong>: Applying same technique as shown above.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]
<strong>Output</strong>: [32, 44, 27, 23, 62, 50, 28, 54]
<strong>Explanation</strong>: Applying same technique as shown above, output will be [32, 44, 27, 23, 62, 50, 28, 54].</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ n, m ≤1000<br>0 ≤ mat[i][j] ≤100</span></p>