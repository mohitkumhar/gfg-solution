<h2><a href="https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1">Distinct Permutations of a String</a></h2><h3>Medium</h3><hr><p><span style="font-size: 18.6667px;">Given a string <strong>s</strong>, which may contain duplicate characters, your task is to generate and return an array of all <strong>unique </strong>permutations of the string. You can return your answer in <strong>any </strong>order.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "ABC"
<strong>Output: </strong>["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
<strong>Explanation: </strong>Given string ABC has 6 unique permutations.
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "ABSG"
<strong>Output: </strong>["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
<strong>Explanation: </strong>Given string ABSG has 24 unique permutations.
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s =<strong> </strong>"AAA"
<strong>Output: </strong>["AAA"]<br></span><strong style="font-size: 14pt; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Explanation: </strong><span style="font-family: -apple-system, system-ui, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif;"><span style="font-size: 18.6667px;">No other unique permutations can be formed as all the characters are same.</span></span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 &lt;= s.size() &lt;= 9<br>s contains only Uppercase english alphabets</span></p>