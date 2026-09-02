<h2><a href="https://www.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1">Serialize and Deserialize a Binary Tree</a></h2><h3>Hard</h3><hr><p><span style="font-size: 14pt;">Given the <strong>root</strong> of a binary tree. You have to perform Serialization and Deserialization. Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions:</span></p>
<ul>
<li><span style="font-size: 14pt;"><strong>serialize() :</strong> stores the tree into an array&nbsp;and returns the array.</span></li>
<li><span style="font-size: 14pt;"><strong>deSerialize() :</strong>&nbsp;deserializes the array to the tree and returns the root of the tree.</span></li>
</ul>
<p><span style="font-size: 14pt;"><strong>Note:&nbsp;</strong>Multiple nodes can have the same data and the node values are<strong>&nbsp;</strong>always&nbsp;positive integers. Your code will be correct if the tree returned by&nbsp;deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the level order traversal of the tree returned by deSerialize(serialize(input_tree)).</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>root = [1, 2, 3] &nbsp; &nbsp; &nbsp; </span><br><span style="font-size: 14pt;"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/908076/Web/Other/blobid1_1754980863.webp" width="245" height="151">
<strong>Output: </strong>[1, 2, 3]
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> root = [10, 20, 30, 40, 60, N, N] <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/908076/Web/Other/blobid0_1754980083.webp" width="249" height="198">
<strong>Output: </strong>[10, 20, 30, 40, 60]</span></pre>
