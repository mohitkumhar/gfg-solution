<h2><a href="https://www.geeksforgeeks.org/problems/possible-paths--141628/1">Possible Paths in a Tree</a></h2><h3>Hard</h3><hr><p><span style="font-size: 18px;">Given a weighted tree with <strong>n</strong> nodes and n - 1 edges, where each edge is represented as [u, v, w] indicating an edge between nodes u and v with weight w.</span></p>
<p><span style="font-size: 18px;">You are also given an array <strong>queries[]</strong>, where each queries[i] contains a single integer x.</span></p>
<p><span style="font-size: 18px;">For each query x, find the number of distinct paths in the tree such that the maximum edge weight on the path is less than or equal to x.</span></p>
<p><span style="font-size: 18px;">Return an array containing the number of valid paths for each query.</span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> A path from node u to node v and the path from node v to node u are considered the same path. A path must contain at least one edge, so a path from a node to itself is not considered.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> </span><span style="font-size: 18px;"><span style="font-size: 18px;">n = 3, edges[][] = [[1, 2, 1], [2, 3, 4]], queries[] = [3]
</span><strong style="font-size: 18px;">Output:</strong><span style="font-size: 18px;"> [1]
</span><strong style="font-size: 18px;">Explanation:</strong><span style="font-size: 18px;">
For x = 3, only the edge [1, 2, 1] has weight less than or equal to 3.
Therefore, the only valid path is: 1 -&gt; 2
The path 1 -&gt; 3 contains an edge of weight 4, so it is not valid.
Hence, the answer is 1.</span></span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> </span><span style="font-size: 18px;"><span style="font-size: 18px;">n = 7, edges[][] = [[1, 2, 3], [2, 3, 1], [2, 4, 9], [3, 6, 7], [3, 5, 8], [5, 7, 4]], queries[] = [1, 3, 5]
</span><strong style="font-size: 18px;">Output:</strong><span style="font-size: 18px;"> [1, 3, 4]
</span><strong style="font-size: 18px;">Explanation:</strong><span style="font-size: 18px;"> </span></span><span style="font-size: 18px;">For x = 1, only the edge [2, 3, 1] satisfies the condition. <br>Therefore, the only valid path is 2 -&gt; 3, giving an answer of 1.
For x = 3, the edges [2, 3, 1] and [1, 2, 3] can be used. <br>They form three valid paths: 1 -&gt; 2, 2 -&gt; 3, and 1 -&gt; 3. 
For x = 5, the edges with weights 1, 3, and 4 can be used. <br>They form four valid paths: 1 -&gt; 2, 2 -&gt; 3, 1 -&gt; 3, and 5 -&gt; 7.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>2 ≤ n ≤ 10<sup>4<br></sup>1 ≤ q ≤ 10<sup>4</sup><sup><br></sup></span><span style="font-size: 18px;">1 </span><span style="font-size: 18px;">≤ edges[i][0], edges[i][1]&nbsp;</span><span style="font-size: 18px;">≤ n<br></span><span style="font-size: 18px;">edges[i][0] != edges[i][1]<br></span><span style="font-size: 18px;">0 </span><span style="font-size: 18px;">≤ </span><span style="font-size: 18px;">edges[i][2] </span><span style="font-size: 18px;">≤ 10<sup>5</sup><br>0&nbsp;≤&nbsp;queries[i] ≤ 10<sup>5</sup><br></span></p>