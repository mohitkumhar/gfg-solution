<h2><a href="https://www.geeksforgeeks.org/problems/capacity-to-ship-packages-within-d-days/1">Capacity To Ship Packages Within D Days</a></h2><h3>Medium</h3><hr><p><span style="font-size: 14pt;">Given <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">arr[]</code> of weights, find the <strong>minimum boat capacity</strong> to ship all weights within <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.4rem] px-1 py-px text-[0.9rem]">d</code> days, loading <strong>in order</strong> without exceeding capacity on any day.<br></span><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1, 2, 1], d = 2
<strong>Output: </strong>3
<strong>Explanation: </strong>We can ship with boat capacity 3 in 2 days.
Day 1- 1,2
Day 2- 1</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [9, 8, 10], d = 3
<strong>Output: </strong>10</span>
<span style="font-size: 18px;"><strong>Explanation: </strong>We can ship with boat capacity 10 in 3 days.
Day 1- 9
Day 2- 8
Day 3- 10</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ d ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>5</sup></span></p>