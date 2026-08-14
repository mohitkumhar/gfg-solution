class Solution {
	public:
	
	int first(vector<int> &nums, int target)
	{
		
		int n = nums.size();
		int ans = -1;
		
		int left = 0;
		int right = n - 1;
		
		while (left <= right)
			{
			int mid = left + (right - left) / 2;
			
			if (nums[mid] == target)
				{
				ans = mid;
				right = mid - 1;
			}
			else if (nums[mid] > target)
				right = mid - 1;
			else
				left = mid + 1;
		}
		return ans;
	}
	
	int second(vector<int> nums, int target)
	{
		int n = nums.size();
		int ans = -1;
		
		int left = 0;
		int right = n - 1;
		
		while (left <= right)
			{
			int mid = left + (right - left) / 2;
			
			if (nums[mid] == target)
				{
				ans = mid;
				left = mid + 1;
			}
			else if (nums[mid] > target)
				right = mid - 1;
			else
				left = mid + 1;
		}
		return ans;
	}
	
	vector<int> find(vector<int>& arr, int x) {
		return {first(arr, x), second(arr, x)};
	}
};
