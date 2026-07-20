class Solution {
	public:
	int findSmallerKValues(int val, int n, vector<vector<int>> mat)
	{
		int i = n - 1;
		int j = 0;
		int count = 0;
		
		while (i >= 0 && j < n)
			{
			if (mat[i][j] <= val)
				{
				count += i + 1;
				j++;
			}
			else
				i--;
		}
		return count;
	}
	
	int kthSmallest(vector<vector<int>> &mat, int k) {
		int n = mat.size();
		
		// smallest value in matrix
		int left = mat[0][0];
		
		// largest value in matrix
		int right = mat[n - 1][n - 1];
		
		while (left < right)
			{
			int mid = left + (right - left) / 2;
			
			int smallerKValues = findSmallerKValues(mid, n, mat);
			
			if (smallerKValues >= k)
				right = mid;
			
			else
				left = mid + 1;
		}
		return left;
	}
};
