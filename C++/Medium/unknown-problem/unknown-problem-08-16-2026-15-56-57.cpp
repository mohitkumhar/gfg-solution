class Solution {
	public:
	
	bool isPossible(int minDist, vector<int> &arr, int k)
	{
		int prevDist = arr[0];
		int currCow = 1;
		
		for (int num : arr)
			{
			int currDist = num - prevDist;
			if (currDist >= minDist)
				{
				prevDist = num;
				currCow++;
			}
			if (currCow >= k)
				return true;
		}
		return false;
	}
	int aggressiveCows(vector<int> &nums, int k) {
		
		sort(nums.begin(), nums.end());
		int n = nums.size();
		
		int left = 0;
		int right = nums[n - 1];
		
		while (left <= right)
			{
			int mid = left + (right - left) / 2;
			
			if (isPossible(mid, nums, k))
				left = mid + 1;
			else
				right = mid - 1;
		}
		return right;
		
	}
};
