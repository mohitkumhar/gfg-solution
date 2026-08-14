class Solution {
	public:
	int nthRoot(int n, int m) {
		
		if (m == 0)
			return 0;
		
		int left = 1;
		int right = m;
		
		while (left <= right)
			{
			int mid = left + (right - left) / 2;
			
			long long product = 1;
			for (int i = 0; i < n; ++i)
				product *= mid;
			
			if (m == product)
				return mid;
			else if (product > m)
				right = mid - 1;
			else
				left = mid + 1;
		}
		return - 1;
		
	}
};
