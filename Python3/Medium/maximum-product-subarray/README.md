<h2><a href="https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1">Maximum Product Subarray</a></h2><h3>Medium</h3><hr><p><span style="font-size: 18px;">Given an array&nbsp;<strong>arr[]</strong>&nbsp;that contains positive and negative integers (may contain 0 as well). Find the&nbsp;<strong>maximum</strong>&nbsp;product that we can get in a subarray of&nbsp;<strong>arr[]</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> It is guaranteed that the answer fits in a 32-bit integer.</span></p>
<p><span style="font-size: 18px;"><strong>Examples<br></strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [-2, 6, -3, -10, 0, 2]
<strong>Output:</strong> 180
<strong>Explanation:</strong> The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [-1, -3, -10, 0, 6]
<strong>Output:</strong> 30
<strong>Explanation:</strong> The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [2, 3, 4] <br><strong>Output:</strong> 24 <br><strong>Explanation:</strong> For an array with all positive elements, the result is product of all elements. </span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br>-100 ≤ arr[i] ≤ 100</span></p>