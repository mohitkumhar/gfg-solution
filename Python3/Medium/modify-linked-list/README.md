<h2><a href="https://www.geeksforgeeks.org/problems/modify-linked-list-1-0546/1">Modify Linked List</a></h2><h3>Medium</h3><hr><p><span style="font-size: 14pt;">Given the head of a singly linked list, modify the list as follows:</span></p>
<ul>
<li><span style="font-size: 14pt;">Pair the first node with the last node, the second node with the second last node, and so on.</span></li>
<li><span style="font-size: 14pt;">For each node in the first half, replace its value with (value of its paired node minus its current value).</span></li>
<li><span style="font-size: 14pt;">Replace the values of the nodes in the second half with the original values of the corresponding first-half nodes.</span></li>
<li><span style="font-size: 14pt;">If the linked list has an odd number of nodes, the middle node remains unchanged.</span></li>
</ul>
<p><span style="font-size: 14pt;">Return the head of the modified linked list.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>10 -&gt; 4 -&gt; 5 -&gt; 3 -&gt; 6
<strong>Output: </strong>-4 -&gt; -1 -&gt; 5 -&gt; 4 -&gt; 10<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/715242/Web/Other/blobid0_1723399856.png" width="400" height="130"><br><strong>Explanation:<br></strong>The linked list has an odd number of nodes, so the middle node (5) remains unchanged.
Pair (10, 6): Update the first node to 6 - 10 = -4, and the last node becomes the original value of the first node, 10.
Pair (4, 3): Update the second node to 3 - 4 = -1, and the second last node becomes the original value of the second node, 4.
</span></pre>
<pre><span style="font-size: 12pt;"><span style="font-size: 14pt;"><strong>Input: </strong>2 -&gt; 9 -&gt; 8 -&gt; 12 -&gt; 7 -&gt; 10
<strong>Output: </strong>8 -&gt; -2 -&gt; 4 -&gt; 8 -&gt; 9 -&gt; 2<br><strong>Explanation:<br></strong>The linked list has an even number of nodes.
Pair (2, 10): Update the first node to 10 - 2 = 8, and the last node becomes 2.
Pair (9, 7): Update the second node to 7 - 9 = -2, and the second last node becomes 9.
Pair (8, 12): Update the third node to 12 - 8 = 4, and the third last node becomes 8.</span></span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ size of linked list&nbsp;≤ 10<sup>6</sup><sup><br></sup>-10<sup>5 </sup>≤ data of nodes&nbsp;≤&nbsp;10<sup>6</sup></span></p>