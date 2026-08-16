class Solution {
	public:
	bool isPossible(long long maxPage, vector<int> &nums, int m)
	{
		long long currPage = 0;
		int studentCount = 1;
		
		for (int num : nums)
			{
			if ((currPage + num) > maxPage)
				{
				studentCount++;
				currPage = num;
			}
			else
				currPage += num;
			
			if (studentCount > m)
				return false;
		}
		return true;
	}
	
	int findPages(vector<int> &nums, int m) {
		// code here
		if (m > nums.size())
			return - 1;

		
		long long left = *max_element(nums.begin(), nums.end());
		long long right = accumulate(nums.begin(), nums.end(), 0LL);
		
		while (left < right)
			{
			long long mid = left + (right - left) / 2;
			
			if (isPossible(mid, nums, m))
				right = mid;
			else
				left = mid + 1;
		}
		return left;
	}
};
