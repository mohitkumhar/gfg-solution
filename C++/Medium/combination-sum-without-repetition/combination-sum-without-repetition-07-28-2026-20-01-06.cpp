class Solution {
	public:
	
	void backtrack(int i, int curr_sum, vector<int> &curr_comb, vector<vector<int>> &result, vector<int> &arr, int target) {
		if (curr_sum == target) {
			result.push_back(curr_comb);
			return;
		}
		
		if (i >= arr.size() || curr_sum > target)
			return ;
		
		for (int j = i; j < arr.size(); j++) {
			if (j > i && arr[j] == arr[j - 1])
				continue;
			
			curr_sum += arr[j];
			curr_comb.push_back(arr[j]);
			
			backtrack(j + 1, curr_sum, curr_comb, result, arr, target);
			
			curr_comb.pop_back();
			curr_sum -= arr[j];
		}
		
	}
	
	vector<vector<int>> uniqueCombinations(vector<int> &arr, int target) {
		
		int n = arr.size();
		
		vector<vector<int>> result;
		vector<int> curr_comb;
		
		sort(arr.begin(), arr.end());
		
		backtrack(0, 0, curr_comb, result, arr, target);
		
		return result;
		
	}
};
