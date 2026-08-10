class Solution {
	public:
	vector<vector<int>> fourSum(vector<int> &arr, int target) {
		
		int n = arr.size();
		sort(arr.begin(), arr.end());
		
		vector<vector<int>> result;
		
		for (int i = 0; i < n - 3; i++)
			{
			if (i > 0 && arr[i] == arr[i - 1])
				continue;
			
			for (int j = i + 1; j < n - 2; j++)
				{
				if (j > i + 1 and arr[j] == arr[j - 1])
					continue;
				
				int low = j + 1;
				int high = n - 1;
				
				while (low < high)
					{
					int currSum = arr[i] + arr[j] + arr[low] + arr[high];
					
					if (currSum == target)
						{
						result.push_back({arr[i], arr[j], arr[low], arr[high]});
						
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
		}
		return result;
		
	}
};
