class Solution {
	public:
	int maxProduct(vector<int> &arr) {
		
		int n = arr.size();
		
		int leftProduct = 1;
		int rightProduct = 1;
		
		int maxProduct = arr[0];
		
		for (int i = 0; i < n; i++)
			{
			leftProduct *= arr[i];
			rightProduct *= arr[n - i - 1];
			
			maxProduct = max({maxProduct, leftProduct, rightProduct});
			
			if (leftProduct == 0)
				leftProduct = 1;
			if (rightProduct == 0)
				rightProduct = 1;
		}
		
		return maxProduct ;
	}
};
