class Solution {
	public:
	vector<vector<int>> mergeOverlap(vector<vector<int>> & arr) {
		
		sort(arr.begin(), arr.end());
		
		vector<vector<int>> result;
		
		for (auto &interval : arr)
			{
			int n = result.size();
			
			if (result.empty() || result[n - 1][1] < interval[0])
				result.push_back({interval[0], interval[1]});
			else
				result[n - 1][1] = max(result[n - 1][1], interval[1]);
		}
		return result;
		
	}
};
