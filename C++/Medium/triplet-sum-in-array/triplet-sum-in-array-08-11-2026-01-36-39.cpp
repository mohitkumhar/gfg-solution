class Solution {
	public:
	bool hasTripletSum(vector<int> &arr, int target) {
		// Code Here
		
		int n = arr.size();
		vector<vector<int>> result;
		
		sort(arr.begin(), arr.end());
		
		for (int k = 0; k < n - 2; k++)
			{
			if (k > 0 && arr[k] == arr[k - 1])
				continue;
			
			int low = k + 1;
			int high = n - 1;
			
			while (low < high)
				{
				int currSum = arr[k] + arr[low] + arr[high];
				
				if (currSum == target)
					{
					result.push_back({arr[k], arr[low], arr[high]});
					
					while (low < high && arr[low] == arr[low + 1])
						low++;
					while (low < high && arr[high] == arr[high - 1])
						high--;
					
					low++;
					high--;
				}
				
				else if (currSum > target)
					high--;
				else
					low++;
			}
		}
		
		if (result.size() > 0)
			return true;
		return false;
	}
};
