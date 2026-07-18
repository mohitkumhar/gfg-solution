class Solution {
	public:
	int find_pivot(int left, int right, vector<int> &nums)
	{
		
		int pivot = nums[left];
		int pivot_idx = left;

		while (left <= right)
			{
			if (nums[left] > pivot && nums[right] < pivot) {
				swap(nums[left], nums[right]);
				left++;
				right--;
			}
			if (left <= right && nums[left] <= pivot)
				left++;
			if (left <= right && nums[right] >= pivot)
				right--;
		}

		swap(nums[pivot_idx], nums[right]);
		return right;
	}

	int kthSmallest(vector<int> &arr, int k) {
		int left = 0;
		int right = arr.size() - 1;

		while (left <= right)
			{
			int pivot = find_pivot(left, right, arr);
			
			if (pivot == k - 1)
				return arr[pivot];
			
			if (pivot > k - 1)
				right = pivot - 1;
			
			if (pivot < k - 1)
				left = pivot + 1;
		}
	return 0;
	}
};
