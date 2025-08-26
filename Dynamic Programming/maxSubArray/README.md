<h2><a href="https://leetcode.com/problems/maximum-subarray">53. Maximum Subarray</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code>, find the <span data-keyword="subarray-nonempty">subarray</span> with the largest sum, and return <em>its sum</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [1] has the largest sum 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>
<pre>
Position 0: number = 1
- No previous sum, so current sum = 1
- Best so far = 1

Position 1: number = -3  
- Previous sum was 1
- Continue: 1 + (-3) = -2
- Start fresh: -3
- Choose: max(-2, -3) = -2
- Best so far = max(1, -2) = 1

Position 2: number = 2
- Previous sum was -2
- Continue: -2 + 2 = 0  
- Start fresh: 2
- Choose: max(0, 2) = 2 ← Start fresh is better!
- Best so far = max(1, 2) = 2

Position 3: number = 1
- Previous sum was 2
- Continue: 2 + 1 = 3
- Start fresh: 1
- Choose: max(3, 1) = 3 ← Continue is better!
- Best so far = max(2, 3) = 3

Position 4: number = -1
- Previous sum was 3  
- Continue: 3 + (-1) = 2
- Start fresh: -1
- Choose: max(2, -1) = 2 ← Continue is better!
- Best so far = max(3, 2) = 3

Final answer: 3
</pre>
